import os
import sys
import zlib
import base64
import cPickle

import globalVars

def find_pygit_repo():
  current_dir = os.path.abspath('./')
  count = 0
  root_path = os.path.abspath(globalVars.root)
  while current_dir != globalVars.root:
    if count == 10:
      sys.exit(-1)
    else:
      count += 1
    current_dir_ls = os.listdir(current_dir)
    if '.pygit' in current_dir_ls:
        return os.path.abspath(current_dir)

    current_dir += '/../'
    current_dir = os.path.abspath(current_dir)

  return ''

def read_object_from_file(file_name):
  try:
    with open(file_name, 'r') as fp:
      decoded_file_string = base64.b64decode(fp.read())
      uncompressed_pickled_object = zlib.decompress(decoded_file_string)
      unpickled_object = cPickle.loads(uncompressed_pickled_object)

      return unpickled_object
  except OSError:
    sys.stderr.write('Failed to read object from file -- ' + file_name + '\n')
    raise

def write_object_to_file(file_name, obj):
  pickled_object = cPickle.dumps(obj, -1)
  compressed_object_string = zlib.compress(pickled_object, 9)
  encoded_file_string = base64.encodestring(compressed_object_string)
  try:
    with open(file_name, 'w') as fp:
      fp.write(encoded_file_string)
  except OSError:
    sys.stderr.write('Failed to write object to file -- ' + file_name + '\n')
    raise

def compute_string_hash(unhashed_string):
  ''' Simply return the same string for now. '''
  return unhashed_string

def write_error_message_and_exit(message):
  sys.stderr.write('Error: ' + message + '\n')
  sys.exit(-1)
