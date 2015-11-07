import tempfile
import os
import shutil

from pygit import init
from pygit import utils
from pygit import globalVars

def test_init():
  root_temp_dir = tempfile.mkdtemp()
  os.chdir(root_temp_dir)
  init.init()
  os.chdir('.pygit')

  # Read index object
  index_object = utils.read_object_from_file(globalVars.index_file_name)
  assert isinstance(index_object, set) == True

  shutil.rmtree(root_temp_dir)

def test_check_init_existing_dir():
  root_temp_dir = tempfile.mkdtemp()
  os.chdir(root_temp_dir)
  init.init()

  try:
    init.init()
  except init.RepoExistsException:
    assert True

  shutil.rmtree(root_temp_dir)
