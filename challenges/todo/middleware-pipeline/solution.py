from typing import Callable, List, Any


def compose(middlewares: List[Callable]) -> Callable:
    """
    Compose a list of middleware functions into a single callable pipeline.

    Each middleware has the signature:
        def middleware(ctx: dict, next: Callable) -> None

    Calling next() passes control to the following middleware.
    Calling next() more than once in a single middleware should raise RuntimeError.

    :param middlewares: list of middleware callables
    :return: a function (ctx, next=None) -> None that runs the full pipeline

    TODO: implement the composition logic
    """
    pass
