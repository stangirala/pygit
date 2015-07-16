import sys
import errn

def compute_string_hash(unhashed_string):
  # Simply return the same string for now.
  return unhashed_string

def pygit_add(filename):
  ''' Main method to add files to the current index. '''

  # Load index from file, add file and write back to disk.
  # TODO Figure out how a git repo is identified. I assume it's recursive search. This allows
  # for submodules. Test if git repo would fail here for such a search.
  try:
  index_dict = read_object_from_file.read_object_from_file('.pygit/index_file')
  temp_index_dict = read_object_from_file.read_object_from_file('.pygit/temp_index_file')
  except OSError as e:
    if e.errno == errno.ENOENT:
      print 'Failed to read index. Broke repo.'
      sys.exit(-1)
  if compute_string_hash(filename) in index_dict:
    # compute diff and do other magic.
  else:
    temp_index_dict.add





