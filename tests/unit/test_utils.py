#testing read_yaml function

from importlib.resources import read_binary
import pytest
from deepclassifier.utils import read_yaml
from pathlib import Path
from box import ConfigBox
from ensure.main import EnsureError

#let us take dummy yaml files created inside data folder.
class Test_read_yaml:
    yaml_files = [
        "tests/data/empty.yaml",
        "tests/data/demo.yaml"
    ]


# the empty file should raise ValueError
    def test_read_yaml_empty(self):
        with pytest.raises(ValueError):
            read_yaml(Path(self.yaml_files[0]))

 #the response should be a configbox instance type. We use assert to check that.
    def test_read_yaml_return_type(self):
        response= read_yaml(Path(self.yaml_files[-1]))
        assert isinstance(response, ConfigBox)     

#if user makes the mistake of passing the file which is not of Path type

 
    @pytest.mark.parametrize("path_to_yaml", yaml_files) #to pass multiple files by parametrizing: first argument is string, next is list to pass
    def test_read_yaml_bad_type(self, path_to_yaml):
        with pytest.raises(EnsureError): #should raise ensure error if path not passes in the Path format
            read_yaml(path_to_yaml)

