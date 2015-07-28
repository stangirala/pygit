import tempfile

from pygit import utils

def set_up():
  pass

def tear_down():
  pass

def test_compute_string_hash():
  unhashed_string = 'asdljf'
  hashed_string = utils.compute_string_hash(unhashed_string)

  assert unhashed_string == hashed_string

def test_read_and_write_object_from_file():
  _, file_path = tempfile.mkstemp()
  temp_list = [1, 2, 'aksjdhf']
  utils.write_object_to_file(file_path, temp_list)
  temp_list_from_disk = utils.read_object_from_file(file_path)

  assert all([i == j for (i, j) in zip(temp_list_from_disk, temp_list)]) == True
