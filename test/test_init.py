import tempfile
import os
import shutil

from nose.tools import with_setup

from pygit import init
from pygit import utils
from pygit import globalVars

class TestInit():
  def setup(self):
    self.root_temp_dir = tempfile.mkdtemp()

  def teardown(self):
    shutil.rmtree(self.root_temp_dir)

  @with_setup(setup, teardown)
  def test_init(self):
    os.chdir(self.root_temp_dir)
    init.init()
    os.chdir('.pygit')

    # Read index object
    index_object = utils.read_object_from_file(globalVars.index_file_name)
    assert isinstance(index_object, set) == True

  @with_setup(setup, teardown)
  def test_check_init_existing_dir(self):
    os.chdir(self.root_temp_dir)
    init.init()

    try:
      init.init()
    except init.RepoExistsException:
      assert True
