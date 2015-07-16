def write_object_to_file(out_file, obj):
  serialized = base64.encodestring(zlib.compress(cPickle.dumps(obj, -1), 9)) 
  try:
    f = open(out_file, 'w')
    f.write(serialized)
  except OSError as e:
    print 'Failed to write object to file.'
    raise
