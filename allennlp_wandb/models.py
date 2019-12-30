import torch
from typing import Dict

class TensorBoardLoggable(object):
    def get_scalars_to_log(self) -> Dict[str, torch.Tensor]:
        raise NotImplementedError

    def get_histograms_to_log(self) -> Dict[str, torch.Tensor]:
        raise NotImplementedError


