// Copyright 2018 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include <memory>

#include "include/v8-inspector.h"
#include "include/v8-local-handle.h"
#include "include/v8-primitive.h"
#include "src/inspector/string-util.h"
#include "src/inspector/v8-inspector-impl.h"
#include "test/cctest/cctest.h"

using v8_inspector::String16;
using v8_inspector::StringBuffer;
using v8_inspector::StringView;
using v8_inspector::toString16;
using v8_inspector::toStringView;
using v8_inspector::V8ContextInfo;
using v8_inspector::V8Inspector;
using v8_inspector::V8InspectorSession;

namespace {

class NoopChannel : public V8Inspector::Channel {
 public:
  ~NoopChannel() override = default;
  void sendResponse(int callId,
                    std::unique_ptr<StringBuffer> message) override {}
  void sendNotification(std::unique_ptr<StringBuffer> message) override {}
  void flushProtocolNotifications() override {}
};

void WrapOnInterrupt(v8::Isolate* isolate, void* data) {
  const char* object_group = "";
  StringView object_group_view(reinterpret_cast<const uint8_t*>(object_group),
                               strlen(object_group));
  reinterpret_cast<V8InspectorSession*>(data)->wrapObject(
      isolate->GetCurrentContext(), v8::Null(isolate), object_group_view,
      false);
}

}  // namespace

TEST(WrapInsideWrapOnInterrupt) {
  LocalContext env;
  v8::Isolate* isolate = env->GetIsolate();
  v8::HandleScope handle_scope(isolate);

  v8_inspector::V8InspectorClient default_client;
  std::unique_ptr<V8Inspector> inspector =
      V8Inspector::create(isolate, &default_client);
  const char* name = "";
  StringView name_view(reinterpret_cast<const uint8_t*>(name), strlen(name));
  V8ContextInfo context_info(env.local(), 1, name_view);
  inspector->contextCreated(context_info);

  NoopChannel channel;
  const char* state = "{}";
  StringView state_view(reinterpret_cast<const uint8_t*>(state), strlen(state));
  std::unique_ptr<V8InspectorSession> session = inspector->connect(
      1, &channel, state_view, v8_inspector::V8Inspector::kFullyTrusted);

  const char* object_group = "";
  StringView object_group_view(reinterpret_cast<const uint8_t*>(object_group),
                               strlen(object_group));
  isolate->RequestInterrupt(&WrapOnInterrupt, session.get());
  session->wrapObject(env.local(), v8::Null(isolate), object_group_view, false);
}

TEST(BinaryFromBase64) {
  auto checkBinary = [](const v8_inspector::protocol::Binary& binary,
                        const std::vector<uint8_t>& values) {
    std::vector<uint8_t> binary_vector(binary.data(),
                                       binary.data() + binary.size());
    CHECK_EQ(binary_vector, values);
  };

  {
    bool success;
    auto binary = v8_inspector::protocol::Binary::fromBase64("", &success);
    CHECK(success);
    checkBinary(binary, {});
  }
  {
    bool success;
    auto binary = v8_inspector::protocol::Binary::fromBase64("YQ==", &success);
    CHECK(success);
    checkBinary(binary, {'a'});
  }
  {
    bool success;
    auto binary = v8_inspector::protocol::Binary::fromBase64("YWI=", &success);
    CHECK(success);
    checkBinary(binary, {'a', 'b'});
  }
  {
    bool success;
    auto binary = v8_inspector::protocol::Binary::fromBase64("YWJj", &success);
    CHECK(success);
    checkBinary(binary, {'a', 'b', 'c'});
  }
  {
    bool success;
    // Wrong input length:
    auto binary = v8_inspector::protocol::Binary::fromBase64("Y", &success);
    CHECK(!success);
  }
  {
    bool success;
    // Invalid space:
    auto binary = v8_inspector::protocol::Binary::fromBase64("=AAA", &success);
    CHECK(!success);
  }
  {
    bool success;
    // Invalid space in a non-final block of four:
    auto binary =
        v8_inspector::protocol::Binary::fromBase64("AAA=AAAA", &success);
    CHECK(!success);
  }
  {
    bool success;
    // Invalid invalid space in second to last position:
    auto binary = v8_inspector::protocol::Binary::fromBase64("AA=A", &success);
    CHECK(!success);
  }
  {
    bool success;
    // Invalid character:
    auto binary = v8_inspector::protocol::Binary::fromBase64(" ", &success);
    CHECK(!success);
  }
}

TEST(BinaryToBase64) {
  uint8_t input[] = {'a', 'b', 'c'};
  {
    auto binary = v8_inspector::protocol::Binary::fromSpan(input, 0);
    v8_inspector::protocol::String base64 = binary.toBase64();
    CHECK_EQ(base64.utf8(), "");
  }
  {
    auto binary = v8_inspector::protocol::Binary::fromSpan(input, 1);
    v8_inspector::protocol::String base64 = binary.toBase64();
    CHECK_EQ(base64.utf8(), "YQ==");
  }
  {
    auto binary = v8_inspector::protocol::Binary::fromSpan(input, 2);
    v8_inspector::protocol::String base64 = binary.toBase64();
    CHECK_EQ(base64.utf8(), "YWI=");
  }
  {
    auto binary = v8_inspector::protocol::Binary::fromSpan(input, 3);
    v8_inspector::protocol::String base64 = binary.toBase64();
    CHECK_EQ(base64.utf8(), "YWJj");
  }
}

TEST(BinaryBase64RoundTrip) {
  std::array<uint8_t, 256> values;
  for (uint16_t b = 0x0; b <= 0xFF; ++b) values[b] = b;
  auto binary =
      v8_inspector::protocol::Binary::fromSpan(values.data(), values.size());
  v8_inspector::protocol::String base64 = binary.toBase64();
  bool success = false;
  auto roundtrip_binary =
      v8_inspector::protocol::Binary::fromBase64(base64, &success);
  CHECK(success);
  CHECK_EQ(values.size(), roundtrip_binary.size());
  for (size_t i = 0; i < values.size(); ++i) {
    CHECK_EQ(values[i], roundtrip_binary.data()[i]);
  }
}

TEST(NoInterruptOnGetAssociatedData) {
  LocalContext env;
  v8::Isolate* isolate = env->GetIsolate();
  v8::HandleScope handle_scope(isolate);

  v8_inspector::V8InspectorClient default_client;
  std::unique_ptr<v8_inspector::V8InspectorImpl> inspector(
      new v8_inspector::V8InspectorImpl(isolate, &default_client));

  v8::Local<v8::Context> context = env->GetIsolate()->GetCurrentContext();
  v8::Local<v8::Value> error = v8::Exception::Error(v8_str("custom error"));
  v8::Local<v8::Name> key = v8_str("key");
  v8::Local<v8::Value> value = v8_str("value");
  inspector->associateExceptionData(context, error, key, value);

  struct InterruptRecorder {
    static void handler(v8::Isolate* isolate, void* data) {
      reinterpret_cast<InterruptRecorder*>(data)->WasInvoked = true;
    }

    bool WasInvoked = false;
  } recorder;

  isolate->RequestInterrupt(&InterruptRecorder::handler, &recorder);

  v8::Local<v8::Object> data =
      inspector->getAssociatedExceptionData(error).ToLocalChecked();
  CHECK(!recorder.WasInvoked);

  CHECK_EQ(data->Get(context, key).ToLocalChecked(), value);

  CompileRun("0");
  CHECK(recorder.WasInvoked);
}

TEST(NoConsoleAPIForUntrustedClient) {
  LocalContext env;
  v8::Isolate* isolate = env->GetIsolate();
  v8::HandleScope handle_scope(isolate);

  v8_inspector::V8InspectorClient default_client;
  std::unique_ptr<V8Inspector> inspector =
      V8Inspector::create(isolate, &default_client);
  V8ContextInfo context_info(env.local(), 1, toStringView(""));
  inspector->contextCreated(context_info);

  class TestChannel : public V8Inspector::Channel {
   public:
    ~TestChannel() override = default;
    void sendResponse(int callId,
                      std::unique_ptr<StringBuffer> message) override {
      CHECK_EQ(callId, 1);
      CHECK_NE(toString16(message->string()).find(expected_response_matcher_),
               String16::kNotFound);
    }
    void sendNotification(std::unique_ptr<StringBuffer> message) override {}
    void flushProtocolNotifications() override {}
    v8_inspector::String16 expected_response_matcher_;
  };

  TestChannel channel;
  const char kCommand[] = R"({
    "id": 1,
    "method": "Runtime.evaluate",
    "params": {
      "expression": "$0 || 42",
      "contextId": 1,
      "includeCommandLineAPI": true
    }
  })";
  std::unique_ptr<V8InspectorSession> trusted_session =
      inspector->connect(1, &channel, toStringView("{}"),
                         v8_inspector::V8Inspector::kFullyTrusted);
  channel.expected_response_matcher_ = R"("value":42)";
  trusted_session->dispatchProtocolMessage(toStringView(kCommand));

  std::unique_ptr<V8InspectorSession> untrusted_session = inspector->connect(
      1, &channel, toStringView("{}"), v8_inspector::V8Inspector::kUntrusted);
  channel.expected_response_matcher_ = R"("className":"ReferenceError")";
  untrusted_session->dispatchProtocolMessage(toStringView(kCommand));
}

TEST(ApiCreatedTasksAreCleanedUp) {
  i::FLAG_experimental_async_stack_tagging_api = true;
  LocalContext env;
  v8::Isolate* isolate = env->GetIsolate();
  v8::HandleScope handle_scope(isolate);

  v8_inspector::V8InspectorClient default_client;
  std::unique_ptr<v8_inspector::V8InspectorImpl> inspector =
      std::make_unique<v8_inspector::V8InspectorImpl>(isolate, &default_client);
  V8ContextInfo context_info(env.local(), 1, toStringView(""));
  inspector->contextCreated(context_info);

  // Trigger V8Console creation.
  v8_inspector::V8Console* console = inspector->console();
  CHECK(console);

  {
    v8::HandleScope handle_scope(isolate);
    v8::MaybeLocal<v8::Value> result = CompileRun(env.local(), R"(
      globalThis['task'] = console.createTask('Task');
    )");
    CHECK(!result.IsEmpty());

    // Run GC and check that the task is still here.
    CcTest::CollectAllGarbage();
    CHECK_EQ(console->AllConsoleTasksForTest().size(), 1);
  }

  // Get rid of the task on the context, run GC and check we no longer have
  // the TaskInfo in the inspector.
  env->Global()->Delete(env.local(), v8_str("task")).Check();
  CcTest::CollectAllGarbage();
  CHECK_EQ(console->AllConsoleTasksForTest().size(), 0);
}
