from typing import Callable, Any


class EventEmitter:
    def __init__(self):
        # TODO: initialize storage for listeners
        pass

    def on(self, event: str, listener: Callable) -> None:
        # TODO: register listener for event
        pass

    def off(self, event: str, listener: Callable) -> None:
        # TODO: remove one occurrence of listener from event
        pass

    def emit(self, event: str, *args: Any) -> bool:
        # TODO: call all listeners for event with args
        # return True if any listeners were called, False otherwise
        pass

    def once(self, event: str, listener: Callable) -> None:
        # TODO: register listener that fires at most once, then removes itself
        pass
