from dataclasses import dataclass, field
from typing import Callable, Optional

import dash
from dash.dependencies import Input, Output, State


@dataclass
class SimpleDashCallback:
    func: Callable
    output: list[Output]
    input: list[Input]
    state: Optional[list[State]] = None

    _output: Output | list[Output] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._output = self.output
        if isinstance(self.output, list) and len(self.output) == 1:
            (self._output,) = self.output

    def register(self, app: dash.Dash) -> None:
        if self.state is not None:
            app.callback(self._output, self.input, self.state)(self.func)
        else:
            app.callback(self._output, self.input)(self.func)
