import tempfile
import os
import shutil
from mock import patch

from pygit import utils
from pygit import globalVars

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

  os.remove(file_path)

def create_dir_structure_and_pygit_repos():
  root_temp_dir = tempfile.mkdtemp()

  os.makedirs(root_temp_dir + '/one/two/three')
  os.makedirs(root_temp_dir + '/zero/minus_one/minus_two')
  os.makedirs(root_temp_dir + '/zero/i')
  os.makedirs(root_temp_dir + '/zero/reals')

  return root_temp_dir

@patch('pygit.globalVars.root')
def test_find_pygit_repo(mock_root):
  root_temp_dir = create_dir_structure_and_pygit_repos()

  # Quirk of os.path.abspath('./') that I haven't figured out yet.
  os.chdir(root_temp_dir)
  root_temp_dir = os.path.abspath('./')

  test_pygit_repo_path = root_temp_dir + '/one/'
  os.mkdir(test_pygit_repo_path + '.pygit')

  mock_root.return_value = root_temp_dir

  os.chdir(root_temp_dir + '/one/two/three')
  pygit_repo_path = utils.find_pygit_repo()
  assert os.path.abspath(pygit_repo_path) == os.path.abspath(test_pygit_repo_path)

  os.chdir(root_temp_dir + '/zero/minus_one')
  pygit_repo_path = utils.find_pygit_repo()
  assert os.path.abspath(pygit_repo_path) == ''

  shutil.rmtree(root_temp_dir)
