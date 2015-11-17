import tempfile
import os
import sys
import shutil
import platform

from nose.tools import with_setup

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

def create_and_return_temporary_folder_space_for_tests():
  if platform.system() == 'Darwin':
    return '/private' + tempfile.mkdtemp()

class TestFindPygitRepo:
  def setup(self):
    self.root_temp_dir = create_and_return_temporary_folder_space_for_tests()

    os.makedirs(self.root_temp_dir + '/one/two/three')
    os.makedirs(self.root_temp_dir + '/zero/minus_one/minus_two')
    os.makedirs(self.root_temp_dir + '/zero/i')
    os.makedirs(self.root_temp_dir + '/zero/reals')

    self.pygit_repo_path = self.root_temp_dir + '/one/'
    os.mkdir(self.pygit_repo_path + '.pygit')

  def teardown(self):
    shutil.rmtree(self.root_temp_dir)

  @with_setup(setup, teardown)
  def test_find_existing_pygit_repo(self):
    os.chdir(self.root_temp_dir + '/one/two/three')
    discovered_pygit_repo_path = utils.find_pygit_repo()
    assert os.path.abspath(discovered_pygit_repo_path) == os.path.abspath(self.pygit_repo_path)

    os.chdir(self.root_temp_dir + '/one')
    discovered_pygit_repo_path = utils.find_pygit_repo()
    assert os.path.abspath(discovered_pygit_repo_path) == os.path.abspath(self.pygit_repo_path)

  @with_setup(setup, teardown)
  def test_find_non_existing_pygit_repo(self):
    try:
      os.chdir(self.root_temp_dir + '/zero/minus_one')
      pygit_repo_path = utils.find_pygit_repo()
    except utils.RepoNotFoundException:
      assert True
