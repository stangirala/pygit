import os
import errno
import write_object_to_file

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

  try:
    write_object_to_file.write_object_to_file({})
  except OSError as e:
    if e.errno == errno.ENOENT:
      print 'Failed to create repo.'

  os.chdir('../')

if __name__ == '__main__':
  pygitinit()

