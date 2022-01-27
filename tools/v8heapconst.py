# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  96: "SHARED_STRING_TYPE",
  101: "SHARED_THIN_STRING_TYPE",
  104: "SHARED_ONE_BYTE_STRING_TYPE",
  109: "SHARED_THIN_ONE_BYTE_STRING_TYPE",
  128: "SYMBOL_TYPE",
  129: "BIG_INT_BASE_TYPE",
  130: "HEAP_NUMBER_TYPE",
  131: "ODDBALL_TYPE",
  132: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  133: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  134: "CALLABLE_TASK_TYPE",
  135: "CALLBACK_TASK_TYPE",
  136: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  137: "LOAD_HANDLER_TYPE",
  138: "STORE_HANDLER_TYPE",
  139: "FUNCTION_TEMPLATE_INFO_TYPE",
  140: "OBJECT_TEMPLATE_INFO_TYPE",
  141: "ACCESS_CHECK_INFO_TYPE",
  142: "ACCESSOR_INFO_TYPE",
  143: "ACCESSOR_PAIR_TYPE",
  144: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  145: "ALLOCATION_MEMENTO_TYPE",
  146: "ALLOCATION_SITE_TYPE",
  147: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  148: "ASM_WASM_DATA_TYPE",
  149: "ASYNC_GENERATOR_REQUEST_TYPE",
  150: "BREAK_POINT_TYPE",
  151: "BREAK_POINT_INFO_TYPE",
  152: "CACHED_TEMPLATE_OBJECT_TYPE",
  153: "CALL_HANDLER_INFO_TYPE",
  154: "CALL_SITE_INFO_TYPE",
  155: "CLASS_POSITIONS_TYPE",
  156: "DEBUG_INFO_TYPE",
  157: "ENUM_CACHE_TYPE",
  158: "ERROR_STACK_DATA_TYPE",
  159: "FEEDBACK_CELL_TYPE",
  160: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  161: "INTERCEPTOR_INFO_TYPE",
  162: "INTERPRETER_DATA_TYPE",
  163: "MODULE_REQUEST_TYPE",
  164: "PROMISE_CAPABILITY_TYPE",
  165: "PROMISE_REACTION_TYPE",
  166: "PROPERTY_DESCRIPTOR_OBJECT_TYPE",
  167: "PROTOTYPE_INFO_TYPE",
  168: "REG_EXP_BOILERPLATE_DESCRIPTION_TYPE",
  169: "SCRIPT_TYPE",
  170: "SCRIPT_OR_MODULE_TYPE",
  171: "SOURCE_TEXT_MODULE_INFO_ENTRY_TYPE",
  172: "STACK_FRAME_INFO_TYPE",
  173: "TEMPLATE_OBJECT_DESCRIPTION_TYPE",
  174: "TUPLE2_TYPE",
  175: "WASM_CONTINUATION_OBJECT_TYPE",
  176: "WASM_EXCEPTION_TAG_TYPE",
  177: "WASM_INDIRECT_FUNCTION_TABLE_TYPE",
  178: "FIXED_ARRAY_TYPE",
  179: "HASH_TABLE_TYPE",
  180: "EPHEMERON_HASH_TABLE_TYPE",
  181: "GLOBAL_DICTIONARY_TYPE",
  182: "NAME_DICTIONARY_TYPE",
  183: "NAME_TO_INDEX_HASH_TABLE_TYPE",
  184: "NUMBER_DICTIONARY_TYPE",
  185: "ORDERED_HASH_MAP_TYPE",
  186: "ORDERED_HASH_SET_TYPE",
  187: "ORDERED_NAME_DICTIONARY_TYPE",
  188: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  189: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  190: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  191: "SCRIPT_CONTEXT_TABLE_TYPE",
  192: "BYTE_ARRAY_TYPE",
  193: "BYTECODE_ARRAY_TYPE",
  194: "FIXED_DOUBLE_ARRAY_TYPE",
  195: "INTERNAL_CLASS_WITH_SMI_ELEMENTS_TYPE",
  196: "SLOPPY_ARGUMENTS_ELEMENTS_TYPE",
  197: "TURBOFAN_BITSET_TYPE_TYPE",
  198: "TURBOFAN_HEAP_CONSTANT_TYPE_TYPE",
  199: "TURBOFAN_OTHER_NUMBER_CONSTANT_TYPE_TYPE",
  200: "TURBOFAN_RANGE_TYPE_TYPE",
  201: "TURBOFAN_UNION_TYPE_TYPE",
  202: "ABSTRACT_INTERNAL_CLASS_SUBCLASS1_TYPE",
  203: "ABSTRACT_INTERNAL_CLASS_SUBCLASS2_TYPE",
  204: "FOREIGN_TYPE",
  205: "WASM_INTERNAL_FUNCTION_TYPE",
  206: "WASM_TYPE_INFO_TYPE",
  207: "AWAIT_CONTEXT_TYPE",
  208: "BLOCK_CONTEXT_TYPE",
  209: "CATCH_CONTEXT_TYPE",
  210: "DEBUG_EVALUATE_CONTEXT_TYPE",
  211: "EVAL_CONTEXT_TYPE",
  212: "FUNCTION_CONTEXT_TYPE",
  213: "MODULE_CONTEXT_TYPE",
  214: "NATIVE_CONTEXT_TYPE",
  215: "SCRIPT_CONTEXT_TYPE",
  216: "WITH_CONTEXT_TYPE",
  217: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  218: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_AND_JOB_TYPE",
  219: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  220: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_WITH_JOB_TYPE",
  221: "WASM_FUNCTION_DATA_TYPE",
  222: "WASM_CAPI_FUNCTION_DATA_TYPE",
  223: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  224: "WASM_JS_FUNCTION_DATA_TYPE",
  225: "EXPORTED_SUB_CLASS_BASE_TYPE",
  226: "EXPORTED_SUB_CLASS_TYPE",
  227: "EXPORTED_SUB_CLASS2_TYPE",
  228: "SMALL_ORDERED_HASH_MAP_TYPE",
  229: "SMALL_ORDERED_HASH_SET_TYPE",
  230: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  231: "DESCRIPTOR_ARRAY_TYPE",
  232: "STRONG_DESCRIPTOR_ARRAY_TYPE",
  233: "SOURCE_TEXT_MODULE_TYPE",
  234: "SYNTHETIC_MODULE_TYPE",
  235: "WEAK_FIXED_ARRAY_TYPE",
  236: "TRANSITION_ARRAY_TYPE",
  237: "CELL_TYPE",
  238: "CODE_TYPE",
  239: "CODE_DATA_CONTAINER_TYPE",
  240: "COVERAGE_INFO_TYPE",
  241: "EMBEDDER_DATA_ARRAY_TYPE",
  242: "FEEDBACK_METADATA_TYPE",
  243: "FEEDBACK_VECTOR_TYPE",
  244: "FILLER_TYPE",
  245: "FREE_SPACE_TYPE",
  246: "INTERNAL_CLASS_TYPE",
  247: "INTERNAL_CLASS_WITH_STRUCT_ELEMENTS_TYPE",
  248: "MAP_TYPE",
  249: "MEGA_DOM_HANDLER_TYPE",
  250: "ON_HEAP_BASIC_BLOCK_PROFILER_DATA_TYPE",
  251: "PREPARSE_DATA_TYPE",
  252: "PROPERTY_ARRAY_TYPE",
  253: "PROPERTY_CELL_TYPE",
  254: "SCOPE_INFO_TYPE",
  255: "SHARED_FUNCTION_INFO_TYPE",
  256: "SMI_BOX_TYPE",
  257: "SMI_PAIR_TYPE",
  258: "SORT_STATE_TYPE",
  259: "SWISS_NAME_DICTIONARY_TYPE",
  260: "WASM_API_FUNCTION_REF_TYPE",
  261: "WASM_ON_FULFILLED_DATA_TYPE",
  262: "WEAK_ARRAY_LIST_TYPE",
  263: "WEAK_CELL_TYPE",
  264: "WASM_ARRAY_TYPE",
  265: "WASM_STRUCT_TYPE",
  266: "JS_PROXY_TYPE",
  1057: "JS_OBJECT_TYPE",
  267: "JS_GLOBAL_OBJECT_TYPE",
  268: "JS_GLOBAL_PROXY_TYPE",
  269: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_PRIMITIVE_WRAPPER_TYPE",
  1058: "JS_API_OBJECT_TYPE",
  2058: "JS_LAST_DUMMY_API_OBJECT_TYPE",
  2059: "JS_BOUND_FUNCTION_TYPE",
  2060: "JS_FUNCTION_TYPE",
  2061: "BIGINT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2062: "BIGUINT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2063: "FLOAT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2064: "FLOAT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2065: "INT16_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2066: "INT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2067: "INT8_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2068: "UINT16_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2069: "UINT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2070: "UINT8_CLAMPED_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2071: "UINT8_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2072: "JS_ARRAY_CONSTRUCTOR_TYPE",
  2073: "JS_PROMISE_CONSTRUCTOR_TYPE",
  2074: "JS_REG_EXP_CONSTRUCTOR_TYPE",
  2075: "JS_CLASS_CONSTRUCTOR_TYPE",
  2076: "JS_ARRAY_ITERATOR_PROTOTYPE_TYPE",
  2077: "JS_ITERATOR_PROTOTYPE_TYPE",
  2078: "JS_MAP_ITERATOR_PROTOTYPE_TYPE",
  2079: "JS_OBJECT_PROTOTYPE_TYPE",
  2080: "JS_PROMISE_PROTOTYPE_TYPE",
  2081: "JS_REG_EXP_PROTOTYPE_TYPE",
  2082: "JS_SET_ITERATOR_PROTOTYPE_TYPE",
  2083: "JS_SET_PROTOTYPE_TYPE",
  2084: "JS_STRING_ITERATOR_PROTOTYPE_TYPE",
  2085: "JS_TYPED_ARRAY_PROTOTYPE_TYPE",
  2086: "JS_MAP_KEY_ITERATOR_TYPE",
  2087: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  2088: "JS_MAP_VALUE_ITERATOR_TYPE",
  2089: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  2090: "JS_SET_VALUE_ITERATOR_TYPE",
  2091: "JS_GENERATOR_OBJECT_TYPE",
  2092: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  2093: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  2094: "JS_DATA_VIEW_TYPE",
  2095: "JS_TYPED_ARRAY_TYPE",
  2096: "JS_MAP_TYPE",
  2097: "JS_SET_TYPE",
  2098: "JS_WEAK_MAP_TYPE",
  2099: "JS_WEAK_SET_TYPE",
  2100: "JS_ARGUMENTS_OBJECT_TYPE",
  2101: "JS_ARRAY_TYPE",
  2102: "JS_ARRAY_BUFFER_TYPE",
  2103: "JS_ARRAY_ITERATOR_TYPE",
  2104: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  2105: "JS_COLLATOR_TYPE",
  2106: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  2107: "JS_DATE_TYPE",
  2108: "JS_DATE_TIME_FORMAT_TYPE",
  2109: "JS_DISPLAY_NAMES_TYPE",
  2110: "JS_ERROR_TYPE",
  2111: "JS_FINALIZATION_REGISTRY_TYPE",
  2112: "JS_LIST_FORMAT_TYPE",
  2113: "JS_LOCALE_TYPE",
  2114: "JS_MESSAGE_OBJECT_TYPE",
  2115: "JS_NUMBER_FORMAT_TYPE",
  2116: "JS_PLURAL_RULES_TYPE",
  2117: "JS_PROMISE_TYPE",
  2118: "JS_REG_EXP_TYPE",
  2119: "JS_REG_EXP_STRING_ITERATOR_TYPE",
  2120: "JS_RELATIVE_TIME_FORMAT_TYPE",
  2121: "JS_SEGMENT_ITERATOR_TYPE",
  2122: "JS_SEGMENTER_TYPE",
  2123: "JS_SEGMENTS_TYPE",
  2124: "JS_SHADOW_REALM_TYPE",
  2125: "JS_STRING_ITERATOR_TYPE",
  2126: "JS_TEMPORAL_CALENDAR_TYPE",
  2127: "JS_TEMPORAL_DURATION_TYPE",
  2128: "JS_TEMPORAL_INSTANT_TYPE",
  2129: "JS_TEMPORAL_PLAIN_DATE_TYPE",
  2130: "JS_TEMPORAL_PLAIN_DATE_TIME_TYPE",
  2131: "JS_TEMPORAL_PLAIN_MONTH_DAY_TYPE",
  2132: "JS_TEMPORAL_PLAIN_TIME_TYPE",
  2133: "JS_TEMPORAL_PLAIN_YEAR_MONTH_TYPE",
  2134: "JS_TEMPORAL_TIME_ZONE_TYPE",
  2135: "JS_TEMPORAL_ZONED_DATE_TIME_TYPE",
  2136: "JS_V8_BREAK_ITERATOR_TYPE",
  2137: "JS_WEAK_REF_TYPE",
  2138: "WASM_GLOBAL_OBJECT_TYPE",
  2139: "WASM_INSTANCE_OBJECT_TYPE",
  2140: "WASM_MEMORY_OBJECT_TYPE",
  2141: "WASM_MODULE_OBJECT_TYPE",
  2142: "WASM_SUSPENDER_OBJECT_TYPE",
  2143: "WASM_TABLE_OBJECT_TYPE",
  2144: "WASM_TAG_OBJECT_TYPE",
  2145: "WASM_VALUE_OBJECT_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("read_only_space", 0x02149): (248, "MetaMap"),
  ("read_only_space", 0x02171): (131, "NullMap"),
  ("read_only_space", 0x02199): (232, "StrongDescriptorArrayMap"),
  ("read_only_space", 0x021c1): (262, "WeakArrayListMap"),
  ("read_only_space", 0x02205): (157, "EnumCacheMap"),
  ("read_only_space", 0x02239): (178, "FixedArrayMap"),
  ("read_only_space", 0x02285): (8, "OneByteInternalizedStringMap"),
  ("read_only_space", 0x022d1): (245, "FreeSpaceMap"),
  ("read_only_space", 0x022f9): (244, "OnePointerFillerMap"),
  ("read_only_space", 0x02321): (244, "TwoPointerFillerMap"),
  ("read_only_space", 0x02349): (131, "UninitializedMap"),
  ("read_only_space", 0x023c1): (131, "UndefinedMap"),
  ("read_only_space", 0x02405): (130, "HeapNumberMap"),
  ("read_only_space", 0x02439): (131, "TheHoleMap"),
  ("read_only_space", 0x02499): (131, "BooleanMap"),
  ("read_only_space", 0x0253d): (192, "ByteArrayMap"),
  ("read_only_space", 0x02565): (178, "FixedCOWArrayMap"),
  ("read_only_space", 0x0258d): (179, "HashTableMap"),
  ("read_only_space", 0x025b5): (128, "SymbolMap"),
  ("read_only_space", 0x025dd): (40, "OneByteStringMap"),
  ("read_only_space", 0x02605): (254, "ScopeInfoMap"),
  ("read_only_space", 0x0262d): (255, "SharedFunctionInfoMap"),
  ("read_only_space", 0x02655): (238, "CodeMap"),
  ("read_only_space", 0x0267d): (237, "CellMap"),
  ("read_only_space", 0x026a5): (253, "GlobalPropertyCellMap"),
  ("read_only_space", 0x026cd): (204, "ForeignMap"),
  ("read_only_space", 0x026f5): (236, "TransitionArrayMap"),
  ("read_only_space", 0x0271d): (45, "ThinOneByteStringMap"),
  ("read_only_space", 0x02745): (243, "FeedbackVectorMap"),
  ("read_only_space", 0x0277d): (131, "ArgumentsMarkerMap"),
  ("read_only_space", 0x027dd): (131, "ExceptionMap"),
  ("read_only_space", 0x02839): (131, "TerminationExceptionMap"),
  ("read_only_space", 0x028a1): (131, "OptimizedOutMap"),
  ("read_only_space", 0x02901): (131, "StaleRegisterMap"),
  ("read_only_space", 0x02961): (191, "ScriptContextTableMap"),
  ("read_only_space", 0x02989): (189, "ClosureFeedbackCellArrayMap"),
  ("read_only_space", 0x029b1): (242, "FeedbackMetadataArrayMap"),
  ("read_only_space", 0x029d9): (178, "ArrayListMap"),
  ("read_only_space", 0x02a01): (129, "BigIntMap"),
  ("read_only_space", 0x02a29): (190, "ObjectBoilerplateDescriptionMap"),
  ("read_only_space", 0x02a51): (193, "BytecodeArrayMap"),
  ("read_only_space", 0x02a79): (239, "CodeDataContainerMap"),
  ("read_only_space", 0x02aa1): (240, "CoverageInfoMap"),
  ("read_only_space", 0x02ac9): (194, "FixedDoubleArrayMap"),
  ("read_only_space", 0x02af1): (181, "GlobalDictionaryMap"),
  ("read_only_space", 0x02b19): (159, "ManyClosuresCellMap"),
  ("read_only_space", 0x02b41): (249, "MegaDomHandlerMap"),
  ("read_only_space", 0x02b69): (178, "ModuleInfoMap"),
  ("read_only_space", 0x02b91): (182, "NameDictionaryMap"),
  ("read_only_space", 0x02bb9): (159, "NoClosuresCellMap"),
  ("read_only_space", 0x02be1): (184, "NumberDictionaryMap"),
  ("read_only_space", 0x02c09): (159, "OneClosureCellMap"),
  ("read_only_space", 0x02c31): (185, "OrderedHashMapMap"),
  ("read_only_space", 0x02c59): (186, "OrderedHashSetMap"),
  ("read_only_space", 0x02c81): (183, "NameToIndexHashTableMap"),
  ("read_only_space", 0x02ca9): (187, "OrderedNameDictionaryMap"),
  ("read_only_space", 0x02cd1): (251, "PreparseDataMap"),
  ("read_only_space", 0x02cf9): (252, "PropertyArrayMap"),
  ("read_only_space", 0x02d21): (153, "SideEffectCallHandlerInfoMap"),
  ("read_only_space", 0x02d49): (153, "SideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x02d71): (153, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x02d99): (188, "SimpleNumberDictionaryMap"),
  ("read_only_space", 0x02dc1): (228, "SmallOrderedHashMapMap"),
  ("read_only_space", 0x02de9): (229, "SmallOrderedHashSetMap"),
  ("read_only_space", 0x02e11): (230, "SmallOrderedNameDictionaryMap"),
  ("read_only_space", 0x02e39): (233, "SourceTextModuleMap"),
  ("read_only_space", 0x02e61): (259, "SwissNameDictionaryMap"),
  ("read_only_space", 0x02e89): (234, "SyntheticModuleMap"),
  ("read_only_space", 0x02eb1): (260, "WasmApiFunctionRefMap"),
  ("read_only_space", 0x02ed9): (222, "WasmCapiFunctionDataMap"),
  ("read_only_space", 0x02f01): (223, "WasmExportedFunctionDataMap"),
  ("read_only_space", 0x02f29): (205, "WasmInternalFunctionMap"),
  ("read_only_space", 0x02f51): (224, "WasmJSFunctionDataMap"),
  ("read_only_space", 0x02f79): (261, "WasmOnFulfilledDataMap"),
  ("read_only_space", 0x02fa1): (206, "WasmTypeInfoMap"),
  ("read_only_space", 0x02fc9): (235, "WeakFixedArrayMap"),
  ("read_only_space", 0x02ff1): (180, "EphemeronHashTableMap"),
  ("read_only_space", 0x03019): (241, "EmbedderDataArrayMap"),
  ("read_only_space", 0x03041): (263, "WeakCellMap"),
  ("read_only_space", 0x03069): (32, "StringMap"),
  ("read_only_space", 0x03091): (41, "ConsOneByteStringMap"),
  ("read_only_space", 0x030b9): (33, "ConsStringMap"),
  ("read_only_space", 0x030e1): (37, "ThinStringMap"),
  ("read_only_space", 0x03109): (35, "SlicedStringMap"),
  ("read_only_space", 0x03131): (43, "SlicedOneByteStringMap"),
  ("read_only_space", 0x03159): (34, "ExternalStringMap"),
  ("read_only_space", 0x03181): (42, "ExternalOneByteStringMap"),
  ("read_only_space", 0x031a9): (50, "UncachedExternalStringMap"),
  ("read_only_space", 0x031d1): (0, "InternalizedStringMap"),
  ("read_only_space", 0x031f9): (2, "ExternalInternalizedStringMap"),
  ("read_only_space", 0x03221): (10, "ExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x03249): (18, "UncachedExternalInternalizedStringMap"),
  ("read_only_space", 0x03271): (26, "UncachedExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x03299): (58, "UncachedExternalOneByteStringMap"),
  ("read_only_space", 0x032c1): (104, "SharedOneByteStringMap"),
  ("read_only_space", 0x032e9): (96, "SharedStringMap"),
  ("read_only_space", 0x03311): (109, "SharedThinOneByteStringMap"),
  ("read_only_space", 0x03339): (101, "SharedThinStringMap"),
  ("read_only_space", 0x03361): (96, "TwoByteSeqStringMigrationSentinelMap"),
  ("read_only_space", 0x03389): (104, "OneByteSeqStringMigrationSentinelMap"),
  ("read_only_space", 0x033b1): (131, "SelfReferenceMarkerMap"),
  ("read_only_space", 0x033d9): (131, "BasicBlockCountersMarkerMap"),
  ("read_only_space", 0x0341d): (147, "ArrayBoilerplateDescriptionMap"),
  ("read_only_space", 0x0351d): (161, "InterceptorInfoMap"),
  ("read_only_space", 0x05e25): (132, "PromiseFulfillReactionJobTaskMap"),
  ("read_only_space", 0x05e4d): (133, "PromiseRejectReactionJobTaskMap"),
  ("read_only_space", 0x05e75): (134, "CallableTaskMap"),
  ("read_only_space", 0x05e9d): (135, "CallbackTaskMap"),
  ("read_only_space", 0x05ec5): (136, "PromiseResolveThenableJobTaskMap"),
  ("read_only_space", 0x05eed): (139, "FunctionTemplateInfoMap"),
  ("read_only_space", 0x05f15): (140, "ObjectTemplateInfoMap"),
  ("read_only_space", 0x05f3d): (141, "AccessCheckInfoMap"),
  ("read_only_space", 0x05f65): (142, "AccessorInfoMap"),
  ("read_only_space", 0x05f8d): (143, "AccessorPairMap"),
  ("read_only_space", 0x05fb5): (144, "AliasedArgumentsEntryMap"),
  ("read_only_space", 0x05fdd): (145, "AllocationMementoMap"),
  ("read_only_space", 0x06005): (148, "AsmWasmDataMap"),
  ("read_only_space", 0x0602d): (149, "AsyncGeneratorRequestMap"),
  ("read_only_space", 0x06055): (150, "BreakPointMap"),
  ("read_only_space", 0x0607d): (151, "BreakPointInfoMap"),
  ("read_only_space", 0x060a5): (152, "CachedTemplateObjectMap"),
  ("read_only_space", 0x060cd): (154, "CallSiteInfoMap"),
  ("read_only_space", 0x060f5): (155, "ClassPositionsMap"),
  ("read_only_space", 0x0611d): (156, "DebugInfoMap"),
  ("read_only_space", 0x06145): (158, "ErrorStackDataMap"),
  ("read_only_space", 0x0616d): (160, "FunctionTemplateRareDataMap"),
  ("read_only_space", 0x06195): (162, "InterpreterDataMap"),
  ("read_only_space", 0x061bd): (163, "ModuleRequestMap"),
  ("read_only_space", 0x061e5): (164, "PromiseCapabilityMap"),
  ("read_only_space", 0x0620d): (165, "PromiseReactionMap"),
  ("read_only_space", 0x06235): (166, "PropertyDescriptorObjectMap"),
  ("read_only_space", 0x0625d): (167, "PrototypeInfoMap"),
  ("read_only_space", 0x06285): (168, "RegExpBoilerplateDescriptionMap"),
  ("read_only_space", 0x062ad): (169, "ScriptMap"),
  ("read_only_space", 0x062d5): (170, "ScriptOrModuleMap"),
  ("read_only_space", 0x062fd): (171, "SourceTextModuleInfoEntryMap"),
  ("read_only_space", 0x06325): (172, "StackFrameInfoMap"),
  ("read_only_space", 0x0634d): (173, "TemplateObjectDescriptionMap"),
  ("read_only_space", 0x06375): (174, "Tuple2Map"),
  ("read_only_space", 0x0639d): (175, "WasmContinuationObjectMap"),
  ("read_only_space", 0x063c5): (176, "WasmExceptionTagMap"),
  ("read_only_space", 0x063ed): (177, "WasmIndirectFunctionTableMap"),
  ("read_only_space", 0x06415): (196, "SloppyArgumentsElementsMap"),
  ("read_only_space", 0x0643d): (231, "DescriptorArrayMap"),
  ("read_only_space", 0x06465): (219, "UncompiledDataWithoutPreparseDataMap"),
  ("read_only_space", 0x0648d): (217, "UncompiledDataWithPreparseDataMap"),
  ("read_only_space", 0x064b5): (220, "UncompiledDataWithoutPreparseDataWithJobMap"),
  ("read_only_space", 0x064dd): (218, "UncompiledDataWithPreparseDataAndJobMap"),
  ("read_only_space", 0x06505): (250, "OnHeapBasicBlockProfilerDataMap"),
  ("read_only_space", 0x0652d): (197, "TurbofanBitsetTypeMap"),
  ("read_only_space", 0x06555): (201, "TurbofanUnionTypeMap"),
  ("read_only_space", 0x0657d): (200, "TurbofanRangeTypeMap"),
  ("read_only_space", 0x065a5): (198, "TurbofanHeapConstantTypeMap"),
  ("read_only_space", 0x065cd): (199, "TurbofanOtherNumberConstantTypeMap"),
  ("read_only_space", 0x065f5): (246, "InternalClassMap"),
  ("read_only_space", 0x0661d): (257, "SmiPairMap"),
  ("read_only_space", 0x06645): (256, "SmiBoxMap"),
  ("read_only_space", 0x0666d): (225, "ExportedSubClassBaseMap"),
  ("read_only_space", 0x06695): (226, "ExportedSubClassMap"),
  ("read_only_space", 0x066bd): (202, "AbstractInternalClassSubclass1Map"),
  ("read_only_space", 0x066e5): (203, "AbstractInternalClassSubclass2Map"),
  ("read_only_space", 0x0670d): (195, "InternalClassWithSmiElementsMap"),
  ("read_only_space", 0x06735): (247, "InternalClassWithStructElementsMap"),
  ("read_only_space", 0x0675d): (227, "ExportedSubClass2Map"),
  ("read_only_space", 0x06785): (258, "SortStateMap"),
  ("read_only_space", 0x067ad): (146, "AllocationSiteWithWeakNextMap"),
  ("read_only_space", 0x067d5): (146, "AllocationSiteWithoutWeakNextMap"),
  ("read_only_space", 0x067fd): (137, "LoadHandler1Map"),
  ("read_only_space", 0x06825): (137, "LoadHandler2Map"),
  ("read_only_space", 0x0684d): (137, "LoadHandler3Map"),
  ("read_only_space", 0x06875): (138, "StoreHandler0Map"),
  ("read_only_space", 0x0689d): (138, "StoreHandler1Map"),
  ("read_only_space", 0x068c5): (138, "StoreHandler2Map"),
  ("read_only_space", 0x068ed): (138, "StoreHandler3Map"),
  ("map_space", 0x02149): (1057, "ExternalMap"),
  ("map_space", 0x02171): (2114, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x021e9): "EmptyWeakArrayList",
  ("read_only_space", 0x021f5): "EmptyDescriptorArray",
  ("read_only_space", 0x0222d): "EmptyEnumCache",
  ("read_only_space", 0x02261): "EmptyFixedArray",
  ("read_only_space", 0x02269): "NullValue",
  ("read_only_space", 0x02371): "UninitializedValue",
  ("read_only_space", 0x023e9): "UndefinedValue",
  ("read_only_space", 0x0242d): "NanValue",
  ("read_only_space", 0x02461): "TheHoleValue",
  ("read_only_space", 0x0248d): "HoleNanValue",
  ("read_only_space", 0x024c1): "TrueValue",
  ("read_only_space", 0x02501): "FalseValue",
  ("read_only_space", 0x02531): "empty_string",
  ("read_only_space", 0x0276d): "EmptyScopeInfo",
  ("read_only_space", 0x027a5): "ArgumentsMarker",
  ("read_only_space", 0x02805): "Exception",
  ("read_only_space", 0x02861): "TerminationException",
  ("read_only_space", 0x028c9): "OptimizedOut",
  ("read_only_space", 0x02929): "StaleRegister",
  ("read_only_space", 0x03401): "EmptyPropertyArray",
  ("read_only_space", 0x03409): "EmptyByteArray",
  ("read_only_space", 0x03411): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x03445): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x03451): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x03459): "EmptySlowElementDictionary",
  ("read_only_space", 0x0347d): "EmptyOrderedHashMap",
  ("read_only_space", 0x03491): "EmptyOrderedHashSet",
  ("read_only_space", 0x034a5): "EmptyFeedbackMetadata",
  ("read_only_space", 0x034b1): "EmptyPropertyDictionary",
  ("read_only_space", 0x034d9): "EmptyOrderedPropertyDictionary",
  ("read_only_space", 0x034f1): "EmptySwissPropertyDictionary",
  ("read_only_space", 0x03545): "NoOpInterceptorInfo",
  ("read_only_space", 0x0356d): "EmptyWeakFixedArray",
  ("read_only_space", 0x03575): "InfinityValue",
  ("read_only_space", 0x03581): "MinusZeroValue",
  ("read_only_space", 0x0358d): "MinusInfinityValue",
  ("read_only_space", 0x03599): "SelfReferenceMarker",
  ("read_only_space", 0x035d9): "BasicBlockCountersMarker",
  ("read_only_space", 0x0361d): "OffHeapTrampolineRelocationInfo",
  ("read_only_space", 0x03629): "GlobalThisBindingScopeInfo",
  ("read_only_space", 0x03659): "EmptyFunctionScopeInfo",
  ("read_only_space", 0x0367d): "NativeScopeInfo",
  ("read_only_space", 0x03695): "HashSeed",
  ("old_space", 0x04241): "ArgumentsIteratorAccessor",
  ("old_space", 0x04285): "ArrayLengthAccessor",
  ("old_space", 0x042c9): "BoundFunctionLengthAccessor",
  ("old_space", 0x0430d): "BoundFunctionNameAccessor",
  ("old_space", 0x04351): "ErrorStackAccessor",
  ("old_space", 0x04395): "FunctionArgumentsAccessor",
  ("old_space", 0x043d9): "FunctionCallerAccessor",
  ("old_space", 0x0441d): "FunctionNameAccessor",
  ("old_space", 0x04461): "FunctionLengthAccessor",
  ("old_space", 0x044a5): "FunctionPrototypeAccessor",
  ("old_space", 0x044e9): "StringLengthAccessor",
  ("old_space", 0x0452d): "InvalidPrototypeValidityCell",
  ("old_space", 0x04535): "EmptyScript",
  ("old_space", 0x04575): "ManyClosuresCell",
  ("old_space", 0x04581): "ArrayConstructorProtector",
  ("old_space", 0x04595): "NoElementsProtector",
  ("old_space", 0x045a9): "MegaDOMProtector",
  ("old_space", 0x045bd): "IsConcatSpreadableProtector",
  ("old_space", 0x045d1): "ArraySpeciesProtector",
  ("old_space", 0x045e5): "TypedArraySpeciesProtector",
  ("old_space", 0x045f9): "PromiseSpeciesProtector",
  ("old_space", 0x0460d): "RegExpSpeciesProtector",
  ("old_space", 0x04621): "StringLengthProtector",
  ("old_space", 0x04635): "ArrayIteratorProtector",
  ("old_space", 0x04649): "ArrayBufferDetachingProtector",
  ("old_space", 0x0465d): "PromiseHookProtector",
  ("old_space", 0x04671): "PromiseResolveProtector",
  ("old_space", 0x04685): "MapIteratorProtector",
  ("old_space", 0x04699): "PromiseThenProtector",
  ("old_space", 0x046ad): "SetIteratorProtector",
  ("old_space", 0x046c1): "StringIteratorProtector",
  ("old_space", 0x046d5): "SingleCharacterStringCache",
  ("old_space", 0x04add): "StringSplitCache",
  ("old_space", 0x04ee5): "RegExpMultipleCache",
  ("old_space", 0x052ed): "BuiltinsConstantsTable",
  ("old_space", 0x05715): "AsyncFunctionAwaitRejectSharedFun",
  ("old_space", 0x05739): "AsyncFunctionAwaitResolveSharedFun",
  ("old_space", 0x0575d): "AsyncGeneratorAwaitRejectSharedFun",
  ("old_space", 0x05781): "AsyncGeneratorAwaitResolveSharedFun",
  ("old_space", 0x057a5): "AsyncGeneratorYieldResolveSharedFun",
  ("old_space", 0x057c9): "AsyncGeneratorReturnResolveSharedFun",
  ("old_space", 0x057ed): "AsyncGeneratorReturnClosedRejectSharedFun",
  ("old_space", 0x05811): "AsyncGeneratorReturnClosedResolveSharedFun",
  ("old_space", 0x05835): "AsyncIteratorValueUnwrapSharedFun",
  ("old_space", 0x05859): "PromiseAllResolveElementSharedFun",
  ("old_space", 0x0587d): "PromiseAllSettledResolveElementSharedFun",
  ("old_space", 0x058a1): "PromiseAllSettledRejectElementSharedFun",
  ("old_space", 0x058c5): "PromiseAnyRejectElementSharedFun",
  ("old_space", 0x058e9): "PromiseCapabilityDefaultRejectSharedFun",
  ("old_space", 0x0590d): "PromiseCapabilityDefaultResolveSharedFun",
  ("old_space", 0x05931): "PromiseCatchFinallySharedFun",
  ("old_space", 0x05955): "PromiseGetCapabilitiesExecutorSharedFun",
  ("old_space", 0x05979): "PromiseThenFinallySharedFun",
  ("old_space", 0x0599d): "PromiseThrowerFinallySharedFun",
  ("old_space", 0x059c1): "PromiseValueThunkFinallySharedFun",
  ("old_space", 0x059e5): "ProxyRevokeSharedFun",
}

# Lower 32 bits of first page addresses for various heap spaces.
HEAP_FIRST_PAGES = {
  0x000c0000: "old_space",
  0x00100000: "map_space",
  0x00000000: "read_only_space",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "WASM",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "STACK_SWITCH",
  "WASM_DEBUG_BREAK",
  "C_WASM_ENTRY",
  "WASM_EXIT",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "BASELINE",
  "OPTIMIZED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
