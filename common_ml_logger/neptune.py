from neptune import new as neptune
from neptune.new.run import Run
from typing import Dict, List, Any, Union

from common_ml_logger.session import Session
from common_ml_logger import *

class NeptuneSession(Session):
    nep_ex: Run

    def __init__(self, source_paths: Union[List[str], str], **kwargs) -> None:
        self.nep_ex = neptune.init(source_files=source_paths, **kwargs)
    
    def log_parameters(self, params: Dict[str, Any]) -> None:
        self.nep_ex["parameters"] = params
    
    def log_metric(self, val_name: str, value: Any) -> None:
        self.nep_ex[val_name].log(value)