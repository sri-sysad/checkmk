# Stubs for kubernetes.client.models.v2beta2_metric_target (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V2beta2MetricTarget:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    average_utilization: Any = ...
    average_value: Any = ...
    type: Any = ...
    value: Any = ...
    def __init__(self, average_utilization: Optional[Any] = ..., average_value: Optional[Any] = ..., type: Optional[Any] = ..., value: Optional[Any] = ...) -> None: ...
    @property
    def average_utilization(self): ...
    @average_utilization.setter
    def average_utilization(self, average_utilization: Any) -> None: ...
    @property
    def average_value(self): ...
    @average_value.setter
    def average_value(self, average_value: Any) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type: Any) -> None: ...
    @property
    def value(self): ...
    @value.setter
    def value(self, value: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...