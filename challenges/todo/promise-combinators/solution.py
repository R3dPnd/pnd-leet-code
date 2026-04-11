"""
Python equivalent of Promise combinators using concurrent.futures.
The Node.js Promise API maps to Python's Future/coroutine model.
We use threading to simulate concurrent async tasks.
"""
from typing import List, Any, Dict
from concurrent.futures import Future, ThreadPoolExecutor, FIRST_COMPLETED, wait
import threading


def my_promise_all(futures: List[Future]) -> List[Any]:
    """
    Block until ALL futures resolve and return results in input order.
    Raises the first exception encountered if any future fails.

    TODO: implement this without using concurrent.futures helpers like
    as_completed — manually track completions and propagate errors.
    """
    pass


def my_promise_race(futures: List[Future]) -> Any:
    """
    Block until the FIRST future settles and return its result (or raise its exception).

    TODO: implement this without using concurrent.futures.wait(FIRST_COMPLETED).
    """
    pass


def my_promise_all_settled(futures: List[Future]) -> List[Dict]:
    """
    Block until ALL futures settle.
    Always returns a list of dicts:
      {'status': 'fulfilled', 'value': <value>}
      {'status': 'rejected', 'reason': <exception>}

    TODO: implement this without raising — capture errors as 'rejected' entries.
    """
    pass
