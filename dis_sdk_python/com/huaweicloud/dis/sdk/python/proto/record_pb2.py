# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: record.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from dis_sdk_python.dependency.google.protobuf import descriptor as _descriptor
from dis_sdk_python.dependency.google.protobuf import message as _message
from dis_sdk_python.dependency.google.protobuf import reflection as _reflection
from dis_sdk_python.dependency.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='record.proto',
  package='',
  syntax='proto2',
  serialized_options=_b('\n&com.huaweicloud.dis-sdk-resources-demo1.iface.api.protobufB\007Message'),
  serialized_pb=_b('\n\x0crecord.proto\"Q\n\x11PutRecordsRequest\x12\x12\n\nstreamName\x18\x01 \x02(\t\x12(\n\x07records\x18\x02 \x03(\x0b\x32\x17.PutRecordsRequestEntry\"\xb8\x01\n\x16PutRecordsRequestEntry\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x17\n\x0f\x65xplicitHashKey\x18\x04 \x01(\t\x12\x14\n\x0cpartitionKey\x18\x05 \x01(\t\x12\x13\n\x0bpartitionId\x18\x06 \x01(\t\x12\x39\n\x0c\x65xtendedInfo\x18\x07 \x01(\x0b\x32#.PutRecordsRequestEntryExtendedInfo\x12\x11\n\ttimestamp\x18\x1d \x01(\x03\"u\n\"PutRecordsRequestEntryExtendedInfo\x12\x10\n\x08\x66ileName\x18\x08 \x02(\t\x12\x15\n\rdeliverDataId\x18\t \x02(\t\x12\x16\n\x07\x65ndFlag\x18\n \x01(\x08:\x05\x66\x61lse\x12\x0e\n\x06seqNum\x18\x0b \x02(\x03\"V\n\x10PutRecordsResult\x12\x19\n\x11\x66\x61iledRecordCount\x18\x15 \x02(\x05\x12\'\n\x07records\x18\x16 \x03(\x0b\x32\x16.PutRecordsResultEntry\"i\n\x15PutRecordsResultEntry\x12\x0f\n\x07shardId\x18\x17 \x01(\t\x12\x16\n\x0esequenceNumber\x18\x18 \x01(\t\x12\x11\n\terrorCode\x18\x19 \x01(\t\x12\x14\n\x0c\x65rrorMessage\x18\x1a \x01(\t\"9\n\x11GetRecordsRequest\x12\x15\n\rshardIterator\x18\x0c \x02(\t\x12\r\n\x05limit\x18\r \x01(\x05\"G\n\x10GetRecordsResult\x12\x19\n\x11nextShardIterator\x18\x0e \x02(\t\x12\x18\n\x07records\x18\x10 \x03(\x0b\x32\x07.Record\"n\n\x06Record\x12\x14\n\x0cpartitionKey\x18\x11 \x01(\t\x12\x16\n\x0esequenceNumber\x18\x12 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x13 \x01(\x0c\x12\x11\n\ttimestamp\x18\x1b \x01(\x03\x12\x15\n\rtimestampType\x18\x1c \x01(\tB1\n&com.huaweicloud.dis-sdk-resources-demo1.iface.api.protobufB\x07Message')
)




_PUTRECORDSREQUEST = _descriptor.Descriptor(
  name='PutRecordsRequest',
  full_name='PutRecordsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='streamName', full_name='PutRecordsRequest.streamName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='PutRecordsRequest.records', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=97,
)


_PUTRECORDSREQUESTENTRY = _descriptor.Descriptor(
  name='PutRecordsRequestEntry',
  full_name='PutRecordsRequestEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='PutRecordsRequestEntry.data', index=0,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='explicitHashKey', full_name='PutRecordsRequestEntry.explicitHashKey', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partitionKey', full_name='PutRecordsRequestEntry.partitionKey', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partitionId', full_name='PutRecordsRequestEntry.partitionId', index=3,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extendedInfo', full_name='PutRecordsRequestEntry.extendedInfo', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='PutRecordsRequestEntry.timestamp', index=5,
      number=29, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=284,
)


_PUTRECORDSREQUESTENTRYEXTENDEDINFO = _descriptor.Descriptor(
  name='PutRecordsRequestEntryExtendedInfo',
  full_name='PutRecordsRequestEntryExtendedInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileName', full_name='PutRecordsRequestEntryExtendedInfo.fileName', index=0,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deliverDataId', full_name='PutRecordsRequestEntryExtendedInfo.deliverDataId', index=1,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endFlag', full_name='PutRecordsRequestEntryExtendedInfo.endFlag', index=2,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seqNum', full_name='PutRecordsRequestEntryExtendedInfo.seqNum', index=3,
      number=11, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=403,
)


_PUTRECORDSRESULT = _descriptor.Descriptor(
  name='PutRecordsResult',
  full_name='PutRecordsResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='failedRecordCount', full_name='PutRecordsResult.failedRecordCount', index=0,
      number=21, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='PutRecordsResult.records', index=1,
      number=22, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=405,
  serialized_end=491,
)


_PUTRECORDSRESULTENTRY = _descriptor.Descriptor(
  name='PutRecordsResultEntry',
  full_name='PutRecordsResultEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shardId', full_name='PutRecordsResultEntry.shardId', index=0,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequenceNumber', full_name='PutRecordsResultEntry.sequenceNumber', index=1,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorCode', full_name='PutRecordsResultEntry.errorCode', index=2,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorMessage', full_name='PutRecordsResultEntry.errorMessage', index=3,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=598,
)


_GETRECORDSREQUEST = _descriptor.Descriptor(
  name='GetRecordsRequest',
  full_name='GetRecordsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shardIterator', full_name='GetRecordsRequest.shardIterator', index=0,
      number=12, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='GetRecordsRequest.limit', index=1,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=600,
  serialized_end=657,
)


_GETRECORDSRESULT = _descriptor.Descriptor(
  name='GetRecordsResult',
  full_name='GetRecordsResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nextShardIterator', full_name='GetRecordsResult.nextShardIterator', index=0,
      number=14, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='GetRecordsResult.records', index=1,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=659,
  serialized_end=730,
)


_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partitionKey', full_name='Record.partitionKey', index=0,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequenceNumber', full_name='Record.sequenceNumber', index=1,
      number=18, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='Record.data', index=2,
      number=19, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Record.timestamp', index=3,
      number=27, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestampType', full_name='Record.timestampType', index=4,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=732,
  serialized_end=842,
)

_PUTRECORDSREQUEST.fields_by_name['records'].message_type = _PUTRECORDSREQUESTENTRY
_PUTRECORDSREQUESTENTRY.fields_by_name['extendedInfo'].message_type = _PUTRECORDSREQUESTENTRYEXTENDEDINFO
_PUTRECORDSRESULT.fields_by_name['records'].message_type = _PUTRECORDSRESULTENTRY
_GETRECORDSRESULT.fields_by_name['records'].message_type = _RECORD
DESCRIPTOR.message_types_by_name['PutRecordsRequest'] = _PUTRECORDSREQUEST
DESCRIPTOR.message_types_by_name['PutRecordsRequestEntry'] = _PUTRECORDSREQUESTENTRY
DESCRIPTOR.message_types_by_name['PutRecordsRequestEntryExtendedInfo'] = _PUTRECORDSREQUESTENTRYEXTENDEDINFO
DESCRIPTOR.message_types_by_name['PutRecordsResult'] = _PUTRECORDSRESULT
DESCRIPTOR.message_types_by_name['PutRecordsResultEntry'] = _PUTRECORDSRESULTENTRY
DESCRIPTOR.message_types_by_name['GetRecordsRequest'] = _GETRECORDSREQUEST
DESCRIPTOR.message_types_by_name['GetRecordsResult'] = _GETRECORDSRESULT
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PutRecordsRequest = _reflection.GeneratedProtocolMessageType('PutRecordsRequest', (_message.Message,), dict(
  DESCRIPTOR = _PUTRECORDSREQUEST,
  __module__ = 'record_pb2'
  # @@protoc_insertion_point(class_scope:PutRecordsRequest)
  ))
_sym_db.RegisterMessage(PutRecordsRequest)

PutRecordsRequestEntry = _reflection.GeneratedProtocolMessageType('PutRecordsRequestEntry', (_message.Message,), dict(
  DESCRIPTOR = _PUTRECORDSREQUESTENTRY,
  __module__ = 'record_pb2'
  # @@protoc_insertion_point(class_scope:PutRecordsRequestEntry)
  ))
_sym_db.RegisterMessage(PutRecordsRequestEntry)

PutRecordsRequestEntryExtendedInfo = _reflection.GeneratedProtocolMessageType('PutRecordsRequestEntryExtendedInfo', (_message.Message,), dict(
  DESCRIPTOR = _PUTRECORDSREQUESTENTRYEXTENDEDINFO,
  __module__ = 'record_pb2'
  # @@protoc_insertion_point(class_scope:PutRecordsRequestEntryExtendedInfo)
  ))
_sym_db.RegisterMessage(PutRecordsRequestEntryExtendedInfo)

PutRecordsResult = _reflection.GeneratedProtocolMessageType('PutRecordsResult', (_message.Message,), dict(
  DESCRIPTOR = _PUTRECORDSRESULT,
  __module__ = 'record_pb2'
  # @@protoc_insertion_point(class_scope:PutRecordsResult)
  ))
_sym_db.RegisterMessage(PutRecordsResult)

PutRecordsResultEntry = _reflection.GeneratedProtocolMessageType('PutRecordsResultEntry', (_message.Message,), dict(
  DESCRIPTOR = _PUTRECORDSRESULTENTRY,
  __module__ = 'record_pb2'
  # @@protoc_insertion_point(class_scope:PutRecordsResultEntry)
  ))
_sym_db.RegisterMessage(PutRecordsResultEntry)

GetRecordsRequest = _reflection.GeneratedProtocolMessageType('GetRecordsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETRECORDSREQUEST,
  __module__ = 'record_pb2'
  # @@protoc_insertion_point(class_scope:GetRecordsRequest)
  ))
_sym_db.RegisterMessage(GetRecordsRequest)

GetRecordsResult = _reflection.GeneratedProtocolMessageType('GetRecordsResult', (_message.Message,), dict(
  DESCRIPTOR = _GETRECORDSRESULT,
  __module__ = 'record_pb2'
  # @@protoc_insertion_point(class_scope:GetRecordsResult)
  ))
_sym_db.RegisterMessage(GetRecordsResult)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), dict(
  DESCRIPTOR = _RECORD,
  __module__ = 'record_pb2'
  # @@protoc_insertion_point(class_scope:Record)
  ))
_sym_db.RegisterMessage(Record)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)