
from tensorboardX import SummaryWriter
from typing import Dict, List, Any, Union
from os.path import isfile, basename

from common_ml_logger.session import Session
from common_ml_logger import *

class TensorboardSession(Session):
    writer: SummaryWriter

    def __init__(self, source_paths: Union[List[str], str], **kwargs) -> None:
        self.writer = SummaryWriter()
        source_md = []
        for path in source_paths:
            if isfile(path):
                fs = open(path, mode="r")
                source_md.append(f"* {basename(path)}\n\n\"\"\"python")
                source_md.append(fs.read())
                source_md.append("\"\"\"\n\n")
                fs.close()
            else:
                print(f"CometSession: Warning, No such file - {path}")
        self.writer.add_text("Source codes", "\n".join(source_md))
    
    def log_parameters(self, params: Dict[str, Any]) -> None:
        self.writer.add_hparams(params)
    
    def log_metric(self, val_name: str, value: Any) -> None:
        self.writer.add_scalar(val_name, value)