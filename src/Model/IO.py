"""

A module for defining the structure
of the input and output, and enforce
conformation

"""

import torch
from typing import Optional


class TensorPackage:
    """
    A dataclass consisting of a collection
    of associated parameters.
    """
    def __init__(self,
                 content: torch.Tensor,
                 flags: Optional[torch.Tensor],
                 lexical: Optional[torch.Tensor]
                 ):
        self.content = content
        self.flags = flags
        self.lexical = lexical



class TensorPackager:
    """
    Must be setup to create packets which
    can later be passed into a model.

    Displays information about the model to other entities,
    and used for initialization
    """
    def __init__(self,
                 d_model,
                 lexical_tensor: bool = False,
                 flags: Optional[int] = None,
                 ):
        self.d_model = d_model
        self.lexical_tensor = lexical_tensor
        self.flags = flags

    def __call__(self,
                 content: torch.Tensor,
                 lexical: Optional[torch.Tensor] = None,
                 flags: Optional[torch.Tensor] = None,
                 )->TensorPackage:





