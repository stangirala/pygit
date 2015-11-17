import tempfile
import os
import sys
import shutil

from nose.tools import with_setup

from pygit import utils
from pygit import globalVars
from pygit import add
from pygit import init

class TestAdd:
  def setup(self):
    self.root_temp_dir = tempfile.mkdtemp()

    os.makedirs(self.root_temp_dir + '/one/two/three')
    os.makedirs(self.root_temp_dir + '/zero/minus_one/minus_two')
    os.makedirs(self.root_temp_dir + '/zero/i')
    os.makedirs(self.root_temp_dir + '/zero/reals')

    pygit_repo_path = self.root_temp_dir + '/one/'
    os.chdir(pygit_repo_path)

    init.init()

  def teardown(self):
    shutil.rmtree(self.root_temp_dir)

  @with_setup(setup, teardown)
  def test_add_for_non_existing_pygit_repo(self):
    os.chdir(self.root_temp_dir + '/zero')

    # Not using utime.
    temp_file_name = 'temp_touch.file'
    f = open('temp_touch.file', 'a')
    f.close()

    try:
      add.add(temp_file_name)
    except SystemExit as e:
      assert e.code == 41

  @with_setup(setup, teardown)
  def test_add_for_non_existant_file(self):
    os.chdir(self.root_temp_dir + '/one')
    temp_file_name = 'temp_touch.file'
    try:
      add.add(temp_file_name)
    except SystemExit as e:
      assert e.code == 43

  @with_setup(setup, teardown)
  def test_add_happy_state(self):
    os.chdir(self.root_temp_dir + '/one')
    os.chdir('.pygit')

    index_set = utils.read_object_from_file(globalVars.index_file_name)
    assert len(index_set) == 0

    os.chdir('../')
    f = open('temp_touch.file', 'a')
    f.close()
    temp_file_name = 'temp_touch.file'
    add.add(temp_file_name)

    os.chdir('.pygit')
    index_set = utils.read_object_from_file(globalVars.index_file_name)

    assert len(index_set) == 1
    assert temp_file_name in index_set

  @with_setup(setup, teardown)
  def test_add(self):
    pygit_repo_path = self.root_temp_dir + '/one/'

    os.chdir(self.root_temp_dir + '/one/two/three')
    pygit_repo_path = utils.find_pygit_repo()
    assert os.path.abspath(pygit_repo_path) == os.path.abspath(pygit_repo_path)

    os.chdir(self.root_temp_dir + '/one')
    pygit_repo_path = utils.find_pygit_repo()
    assert os.path.abspath(pygit_repo_path) == os.path.abspath(pygit_repo_path)

    try:
      os.chdir(self.root_temp_dir + '/zero/minus_one')
      pygit_repo_path = utils.find_pygit_repo()
    except utils.RepoNotFoundException:
      assert True
