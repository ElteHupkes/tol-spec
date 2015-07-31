# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model_inserted.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


from pygazebo.msg import model_pb2, time_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='model_inserted.proto',
  package='revolve.msgs',
  serialized_pb='\n\x14model_inserted.proto\x12\x0crevolve.msgs\x1a\x0bmodel.proto\x1a\ntime.proto\"S\n\rModelInserted\x12\x1f\n\x04time\x18\x01 \x02(\x0b\x32\x11.gazebo.msgs.Time\x12!\n\x05model\x18\x02 \x02(\x0b\x32\x12.gazebo.msgs.Model')




_MODELINSERTED = _descriptor.Descriptor(
  name='ModelInserted',
  full_name='revolve.msgs.ModelInserted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='revolve.msgs.ModelInserted.time', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model', full_name='revolve.msgs.ModelInserted.model', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=63,
  serialized_end=146,
)

_MODELINSERTED.fields_by_name['time'].message_type = time_pb2._TIME
_MODELINSERTED.fields_by_name['model'].message_type = model_pb2._MODEL
DESCRIPTOR.message_types_by_name['ModelInserted'] = _MODELINSERTED

class ModelInserted(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODELINSERTED

  # @@protoc_insertion_point(class_scope:revolve.msgs.ModelInserted)


# @@protoc_insertion_point(module_scope)
