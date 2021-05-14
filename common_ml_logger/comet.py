from comet_ml import Experiment
from typing import Dict, List, Any, Union
from os.path import isfile, basename

from common_ml_logger.session import Session
from common_ml_logger import *

class CometSession(Session):
    com_ex: Experiment

    def __init__(self, source_paths: Union[List[str], str], **kwargs) -> None:
        self.com_ex = Experiment(**kwargs)
        for path in source_paths:
            if isfile(path):
                fs = open(path, mode="r")
                self.com_ex.log_code(code_name=basename(path), code=fs)
                fs.close()
            else:
                print(f"CometSession: Warning, No such file - {path}")
    
    def log_parameters(self, params: Dict[str, Any]) -> None:
        self.com_ex.log_parameters(params)
    
    def log_metric(self, val_name: str, value: Any) -> None:
        self.com_ex.log_metric(val_name, value)
