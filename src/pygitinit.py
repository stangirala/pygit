import os
import errno

def write_object_to_file(out_file, obj):
  serialized = base64.encodestring(zlib.compress(cPickle.dumps(obj, -1), 9))
  try:
    f = open(out_file, 'w')
    f.write(serialized)
  except OSError as e:
    if e.errno == errno.ENOINT:
      print 'Broken repo. Please reinitialize.'

def pygitinit():
  ''' Create empty repo and other tracking data. '''
  try:
    os.mkdir('.pygit')
  except OSError as e:
    if e.errno == errno.EEXIST:
      print 'File exists. Analyzing pygit repo.'
      # Do nothing for now.
      pass
  os.chdir('.pygit')

  index_dict = {}
  write_object_to_file({})

  os.chdir('../')

if __name__ == '__main__':
  pygitinit()

