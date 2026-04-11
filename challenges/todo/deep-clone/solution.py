from typing import Any


def deep_clone(value: Any, _seen: dict = None) -> Any:
    """
    Produce a deep clone of `value`.

    Handles:
    - Primitives (int, float, str, bool, None, bytes) — returned as-is
    - list  — cloned recursively
    - dict  — cloned recursively (keys and values)
    - set   — cloned recursively
    - tuple — cloned recursively (returns a new tuple)
    - Circular references — must not recurse infinitely; mirror the same structure

    Out of scope (return as-is): functions, modules, custom class instances
    without __dict__, etc.

    :param value:  the value to clone
    :param _seen:  internal dict mapping id(obj) -> clone, for cycle detection
    :return: deep copy of value

    TODO: implement recursive cloning with cycle detection
    """
    pass
