from abc import *
from typing import Dict, List, Any, Union

class Session(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, source_paths: Union[List[str], str], **kwargs) -> None:
        pass

    @abstractmethod
    def log_parameters(self, params: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def log_metric(self, val_name: str, value: Any) -> None:
        pass