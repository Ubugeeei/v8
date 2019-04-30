// Copyright 2014 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef V8_MACHINE_TYPE_H_
#define V8_MACHINE_TYPE_H_

#include <iosfwd>

#include "src/base/bits.h"
#include "src/globals.h"

namespace v8 {
namespace internal {

enum class MachineRepresentation : uint8_t {
  kNone,
  kBit,
  kWord8,
  kWord16,
  kWord32,
  kWord64,
  kTaggedSigned,
  kTaggedPointer,
  kTagged,
  kCompressedSigned,
  kCompressedPointer,
  kCompressed,
  // FP representations must be last, and in order of increasing size.
  kFloat32,
  kFloat64,
  kSimd128,
  kFirstFPRepresentation = kFloat32,
  kLastRepresentation = kSimd128
};

bool IsSubtype(MachineRepresentation rep1, MachineRepresentation rep2);

static_assert(static_cast<int>(MachineRepresentation::kLastRepresentation) <
                  kIntSize * kBitsPerByte,
              "Bit masks of MachineRepresentation should fit in an int");

V8_EXPORT_PRIVATE const char* MachineReprToString(MachineRepresentation);

enum class MachineSemantic : uint8_t {
  kNone,
  kBool,
  kInt32,
  kUint32,
  kInt64,
  kUint64,
  kNumber,
  kAny
};

V8_EXPORT_PRIVATE inline int ElementSizeLog2Of(MachineRepresentation rep);

V8_EXPORT_PRIVATE inline int ElementSizeInBytes(MachineRepresentation rep);

class MachineType {
 public:
  constexpr MachineType()
      : representation_(MachineRepresentation::kNone),
        semantic_(MachineSemantic::kNone) {}
  constexpr MachineType(MachineRepresentation representation,
                        MachineSemantic semantic)
      : representation_(representation), semantic_(semantic) {}

  constexpr bool operator==(MachineType other) const {
    return representation() == other.representation() &&
           semantic() == other.semantic();
  }

  constexpr bool operator!=(MachineType other) const {
    return !(*this == other);
  }

  constexpr MachineRepresentation representation() const {
    return representation_;
  }
  constexpr MachineSemantic semantic() const { return semantic_; }

  constexpr bool IsNone() const {
    return representation() == MachineRepresentation::kNone;
  }

  constexpr bool IsSigned() const {
    return semantic() == MachineSemantic::kInt32 ||
           semantic() == MachineSemantic::kInt64;
  }
  constexpr bool IsUnsigned() const {
    return semantic() == MachineSemantic::kUint32 ||
           semantic() == MachineSemantic::kUint64;
  }
  constexpr bool IsTagged() const {
    return representation() == MachineRepresentation::kTaggedPointer ||
           representation() == MachineRepresentation::kTaggedSigned ||
           representation() == MachineRepresentation::kTagged;
  }
  constexpr bool IsTaggedSigned() const {
    return representation() == MachineRepresentation::kTaggedSigned;
  }
  constexpr bool IsTaggedPointer() const {
    return representation() == MachineRepresentation::kTaggedPointer;
  }
  constexpr bool IsCompressed() const {
    return representation() == MachineRepresentation::kCompressedPointer ||
           representation() == MachineRepresentation::kCompressedSigned ||
           representation() == MachineRepresentation::kCompressed;
  }
  constexpr bool IsCompressedSigned() const {
    return representation() == MachineRepresentation::kCompressedSigned;
  }
  constexpr bool IsCompressedPointer() const {
    return representation() == MachineRepresentation::kCompressedPointer;
  }
  constexpr static MachineRepresentation PointerRepresentation() {
    return (kSystemPointerSize == 4) ? MachineRepresentation::kWord32
                                     : MachineRepresentation::kWord64;
  }
  constexpr static MachineType UintPtr() {
    return (kSystemPointerSize == 4) ? Uint32() : Uint64();
  }
  constexpr static MachineType IntPtr() {
    return (kSystemPointerSize == 4) ? Int32() : Int64();
  }
  constexpr static MachineType Int8() {
    return MachineType(MachineRepresentation::kWord8, MachineSemantic::kInt32);
  }
  constexpr static MachineType Uint8() {
    return MachineType(MachineRepresentation::kWord8, MachineSemantic::kUint32);
  }
  constexpr static MachineType Int16() {
    return MachineType(MachineRepresentation::kWord16, MachineSemantic::kInt32);
  }
  constexpr static MachineType Uint16() {
    return MachineType(MachineRepresentation::kWord16,
                       MachineSemantic::kUint32);
  }
  constexpr static MachineType Int32() {
    return MachineType(MachineRepresentation::kWord32, MachineSemantic::kInt32);
  }
  constexpr static MachineType Uint32() {
    return MachineType(MachineRepresentation::kWord32,
                       MachineSemantic::kUint32);
  }
  constexpr static MachineType Int64() {
    return MachineType(MachineRepresentation::kWord64, MachineSemantic::kInt64);
  }
  constexpr static MachineType Uint64() {
    return MachineType(MachineRepresentation::kWord64,
                       MachineSemantic::kUint64);
  }
  constexpr static MachineType Float32() {
    return MachineType(MachineRepresentation::kFloat32,
                       MachineSemantic::kNumber);
  }
  constexpr static MachineType Float64() {
    return MachineType(MachineRepresentation::kFloat64,
                       MachineSemantic::kNumber);
  }
  constexpr static MachineType Simd128() {
    return MachineType(MachineRepresentation::kSimd128, MachineSemantic::kNone);
  }
  constexpr static MachineType Pointer() {
    return MachineType(PointerRepresentation(), MachineSemantic::kNone);
  }
  constexpr static MachineType TaggedPointer() {
    return MachineType(MachineRepresentation::kTaggedPointer,
                       MachineSemantic::kAny);
  }
  constexpr static MachineType TaggedSigned() {
    return MachineType(MachineRepresentation::kTaggedSigned,
                       MachineSemantic::kInt32);
  }
  constexpr static MachineType AnyTagged() {
    return MachineType(MachineRepresentation::kTagged, MachineSemantic::kAny);
  }
  constexpr static MachineType CompressedSigned() {
    return MachineType(MachineRepresentation::kCompressedSigned,
                       MachineSemantic::kInt32);
  }
  constexpr static MachineType CompressedPointer() {
    return MachineType(MachineRepresentation::kCompressedPointer,
                       MachineSemantic::kAny);
  }
  constexpr static MachineType AnyCompressed() {
    return MachineType(MachineRepresentation::kCompressed,
                       MachineSemantic::kAny);
  }
  constexpr static MachineType Bool() {
    return MachineType(MachineRepresentation::kBit, MachineSemantic::kBool);
  }
  constexpr static MachineType TaggedBool() {
    return MachineType(MachineRepresentation::kTagged, MachineSemantic::kBool);
  }
  constexpr static MachineType CompressedBool() {
    return MachineType(MachineRepresentation::kCompressed,
                       MachineSemantic::kBool);
  }
  constexpr static MachineType None() {
    return MachineType(MachineRepresentation::kNone, MachineSemantic::kNone);
  }

  // These naked representations should eventually go away.
  constexpr static MachineType RepWord8() {
    return MachineType(MachineRepresentation::kWord8, MachineSemantic::kNone);
  }
  constexpr static MachineType RepWord16() {
    return MachineType(MachineRepresentation::kWord16, MachineSemantic::kNone);
  }
  constexpr static MachineType RepWord32() {
    return MachineType(MachineRepresentation::kWord32, MachineSemantic::kNone);
  }
  constexpr static MachineType RepWord64() {
    return MachineType(MachineRepresentation::kWord64, MachineSemantic::kNone);
  }
  constexpr static MachineType RepFloat32() {
    return MachineType(MachineRepresentation::kFloat32, MachineSemantic::kNone);
  }
  constexpr static MachineType RepFloat64() {
    return MachineType(MachineRepresentation::kFloat64, MachineSemantic::kNone);
  }
  constexpr static MachineType RepSimd128() {
    return MachineType(MachineRepresentation::kSimd128, MachineSemantic::kNone);
  }
  constexpr static MachineType RepTagged() {
    return MachineType(MachineRepresentation::kTagged, MachineSemantic::kNone);
  }
  constexpr static MachineType RepCompressed() {
    return MachineType(MachineRepresentation::kCompressed,
                       MachineSemantic::kNone);
  }
  constexpr static MachineType RepBit() {
    return MachineType(MachineRepresentation::kBit, MachineSemantic::kNone);
  }

  // These methods return compressed representations when the compressed
  // pointer flag is enabled. Otherwise, they returned the corresponding tagged
  // one.
  constexpr static MachineRepresentation RepCompressedTagged() {
#ifdef V8_COMPRESS_POINTERS
    return MachineRepresentation::kCompressed;
#else
    return MachineRepresentation::kTagged;
#endif
  }
  constexpr static MachineRepresentation RepCompressedTaggedSigned() {
#ifdef V8_COMPRESS_POINTERS
    return MachineRepresentation::kCompressedSigned;
#else
    return MachineRepresentation::kTaggedSigned;
#endif
  }
  constexpr static MachineRepresentation RepCompressedTaggedPointer() {
#ifdef V8_COMPRESS_POINTERS
    return MachineRepresentation::kCompressedPointer;
#else
    return MachineRepresentation::kTaggedPointer;
#endif
  }

  constexpr static MachineType TypeCompressedTagged() {
#ifdef V8_COMPRESS_POINTERS
    return MachineType::AnyCompressed();
#else
    return MachineType::AnyTagged();
#endif
  }
  constexpr static MachineType TypeCompressedTaggedSigned() {
#ifdef V8_COMPRESS_POINTERS
    return MachineType::CompressedSigned();
#else
    return MachineType::TaggedSigned();
#endif
  }
  constexpr static MachineType TypeCompressedTaggedPointer() {
#ifdef V8_COMPRESS_POINTERS
    return MachineType::CompressedPointer();
#else
    return MachineType::TaggedPointer();
#endif
  }

  constexpr bool IsCompressedTagged() const {
#ifdef V8_COMPRESS_POINTERS
    return IsCompressed();
#else
    return IsTagged();
#endif
  }

  constexpr bool IsCompressedTaggedSigned() const {
#ifdef V8_COMPRESS_POINTERS
    return IsCompressedSigned();
#else
    return IsTaggedSigned();
#endif
  }

  constexpr bool IsCompressedTaggedPointer() const {
#ifdef V8_COMPRESS_POINTERS
    return IsCompressedPointer();
#else
    return IsTaggedPointer();
#endif
  }

  static MachineType TypeForRepresentation(const MachineRepresentation& rep,
                                           bool isSigned = true) {
    switch (rep) {
      case MachineRepresentation::kNone:
        return MachineType::None();
      case MachineRepresentation::kBit:
        return MachineType::Bool();
      case MachineRepresentation::kWord8:
        return isSigned ? MachineType::Int8() : MachineType::Uint8();
      case MachineRepresentation::kWord16:
        return isSigned ? MachineType::Int16() : MachineType::Uint16();
      case MachineRepresentation::kWord32:
        return isSigned ? MachineType::Int32() : MachineType::Uint32();
      case MachineRepresentation::kWord64:
        return isSigned ? MachineType::Int64() : MachineType::Uint64();
      case MachineRepresentation::kFloat32:
        return MachineType::Float32();
      case MachineRepresentation::kFloat64:
        return MachineType::Float64();
      case MachineRepresentation::kSimd128:
        return MachineType::Simd128();
      case MachineRepresentation::kTagged:
        return MachineType::AnyTagged();
      case MachineRepresentation::kTaggedSigned:
        return MachineType::TaggedSigned();
      case MachineRepresentation::kTaggedPointer:
        return MachineType::TaggedPointer();
      case MachineRepresentation::kCompressed:
        return MachineType::AnyCompressed();
      case MachineRepresentation::kCompressedPointer:
        return MachineType::CompressedPointer();
      case MachineRepresentation::kCompressedSigned:
        return MachineType::CompressedSigned();
      default:
        UNREACHABLE();
    }
  }

  bool LessThanOrEqualPointerSize() {
    return ElementSizeLog2Of(this->representation()) <= kSystemPointerSizeLog2;
  }

 private:
  MachineRepresentation representation_;
  MachineSemantic semantic_;
};

V8_INLINE size_t hash_value(MachineRepresentation rep) {
  return static_cast<size_t>(rep);
}

V8_INLINE size_t hash_value(MachineType type) {
  return static_cast<size_t>(type.representation()) +
         static_cast<size_t>(type.semantic()) * 16;
}

V8_EXPORT_PRIVATE std::ostream& operator<<(std::ostream& os,
                                           MachineRepresentation rep);
std::ostream& operator<<(std::ostream& os, MachineSemantic type);
V8_EXPORT_PRIVATE std::ostream& operator<<(std::ostream& os, MachineType type);

inline bool IsFloatingPoint(MachineRepresentation rep) {
  return rep >= MachineRepresentation::kFirstFPRepresentation;
}

inline bool CanBeTaggedPointer(MachineRepresentation rep) {
  return rep == MachineRepresentation::kTagged ||
         rep == MachineRepresentation::kTaggedPointer;
}

inline bool CanBeTaggedSigned(MachineRepresentation rep) {
  return rep == MachineRepresentation::kTagged ||
         rep == MachineRepresentation::kTaggedSigned;
}

inline bool IsAnyTagged(MachineRepresentation rep) {
  return CanBeTaggedPointer(rep) || rep == MachineRepresentation::kTaggedSigned;
}

inline bool CanBeCompressedPointer(MachineRepresentation rep) {
  return rep == MachineRepresentation::kCompressed ||
         rep == MachineRepresentation::kCompressedPointer;
}

inline bool CanBeTaggedOrCompressedPointer(MachineRepresentation rep) {
  return CanBeTaggedPointer(rep) || CanBeCompressedPointer(rep);
}

inline bool CanBeCompressedSigned(MachineRepresentation rep) {
  return rep == MachineRepresentation::kCompressed ||
         rep == MachineRepresentation::kCompressedSigned;
}

inline bool IsAnyCompressed(MachineRepresentation rep) {
  return CanBeCompressedPointer(rep) ||
         rep == MachineRepresentation::kCompressedSigned;
}

// TODO(solanes): remove '|| IsAnyTagged(rep)' when all the representation
// changes are in place
inline bool IsAnyCompressedTagged(MachineRepresentation rep) {
#ifdef V8_COMPRESS_POINTERS
  return IsAnyCompressed(rep) || IsAnyTagged(rep);
#else
  return IsAnyTagged(rep);
#endif
}

// Gets the log2 of the element size in bytes of the machine type.
V8_EXPORT_PRIVATE inline int ElementSizeLog2Of(MachineRepresentation rep) {
  switch (rep) {
    case MachineRepresentation::kBit:
    case MachineRepresentation::kWord8:
      return 0;
    case MachineRepresentation::kWord16:
      return 1;
    case MachineRepresentation::kWord32:
    case MachineRepresentation::kFloat32:
      return 2;
    case MachineRepresentation::kWord64:
    case MachineRepresentation::kFloat64:
      return 3;
    case MachineRepresentation::kSimd128:
      return 4;
    case MachineRepresentation::kTaggedSigned:
    case MachineRepresentation::kTaggedPointer:
    case MachineRepresentation::kTagged:
    case MachineRepresentation::kCompressedSigned:
    case MachineRepresentation::kCompressedPointer:
    case MachineRepresentation::kCompressed:
      return kTaggedSizeLog2;
    default:
      break;
  }
  UNREACHABLE();
}

V8_EXPORT_PRIVATE inline int ElementSizeInBytes(MachineRepresentation rep) {
  return 1 << ElementSizeLog2Of(rep);
}

// Converts representation to bit for representation masks.
V8_EXPORT_PRIVATE inline constexpr int RepresentationBit(
    MachineRepresentation rep) {
  return 1 << static_cast<int>(rep);
}

}  // namespace internal
}  // namespace v8

#endif  // V8_MACHINE_TYPE_H_
