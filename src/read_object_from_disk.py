def read_object_from_file(read_file):
  try:
    f = open(read_file, 'r')
    return cPickle.loads(zlib.decompress(base64.b64decode(read_file)))
  except OSError:
    print 'Failed to read object from file -- ', read_file
    raise
