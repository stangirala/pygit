import tempfile
import os
import sys
import shutil

from pygit import utils
from pygit import globalVars

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

  os.remove(file_path)

def test_find_pygit_repo():
  root_temp_dir = create_dir_structure_and_pygit_repos()

  # Quirk of os.path.abspath('./') that I haven't figured out yet.
  os.chdir(root_temp_dir)
  root_temp_dir = os.path.abspath('./')

  test_pygit_repo_path = root_temp_dir + '/one/'
  os.mkdir(test_pygit_repo_path + '.pygit')

  os.chdir(root_temp_dir + '/one/two/three')
  pygit_repo_path = utils.find_pygit_repo()
  assert os.path.abspath(pygit_repo_path) == os.path.abspath(test_pygit_repo_path)

  try:
    os.chdir(root_temp_dir + '/zero/minus_one')
    pygit_repo_path = utils.find_pygit_repo()
  except utils.RepoNotFoundException:
    assert True

  shutil.rmtree(root_temp_dir)

def create_dir_structure_and_pygit_repos():
  root_temp_dir = tempfile.mkdtemp()

  os.makedirs(root_temp_dir + '/one/two/three')
  os.makedirs(root_temp_dir + '/zero/minus_one/minus_two')
  os.makedirs(root_temp_dir + '/zero/i')
  os.makedirs(root_temp_dir + '/zero/reals')

  return root_temp_dir
