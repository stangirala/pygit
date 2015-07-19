def read_object_from_file(file_name):
  try:
    with open(file_name, 'r') as f:
      decoded_file_string = base64.b64decode(file_name)
      uncompressed_pickled_object = zlib.decompress(decoded_file_string)
      unpickled_object = cPickle.loads(uncompressed_file_string)

      return unpickled_object
  except OSError:
    print 'Failed to read object from file -- ', read_file
    raise

def write_object_to_file(file_name, obj):
  pickled_object = cPickle.dumps(obj, -1)
  compressed_object_string = zlib.compress(pickled_object, 9)
  encoded_file_string = base64.encodestring(compressed_object_string)
  try:
    with open(out_file, 'w') as f:
      f.write(encoded_file_string)
  except OSError as e:
    print 'Failed to write object to file.'
    raise
