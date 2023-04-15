from typing import Callable, List, NamedTuple, Set
from ..input.type import Video
from ..output.type import Features
from ...core import Id, Stream, Image

class FlowItem(NamedTuple):
    id: Id

FlowStream = Stream[FlowItem]

FlowStage = Callable[[FlowStream], FlowStream]

FlowEnter = Callable[[Video], FlowStream]
FlowInternal = List[FlowStage]
FlowExit = Callable[[FlowStream], Features]

class Flow(NamedTuple):
    enter: FlowEnter
    internal: FlowInternal
    exit: FlowExit

    def process(self, input: Video) -> Features:
        data = self.enter(input)
        for stage in self.internal:
            data = stage(data)
        data = self.exit(data)
        return data
