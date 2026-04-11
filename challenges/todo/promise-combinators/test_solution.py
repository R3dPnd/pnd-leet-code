import unittest
import threading
import time
from concurrent.futures import Future
from solution import my_promise_all, my_promise_race, my_promise_all_settled


def resolved(value, delay=0) -> Future:
    """Helper: returns a Future that resolves with value after delay seconds."""
    f = Future()
    def _resolve():
        if delay:
            time.sleep(delay)
        f.set_result(value)
    threading.Thread(target=_resolve, daemon=True).start()
    return f


def rejected(exc, delay=0) -> Future:
    """Helper: returns a Future that raises exc after delay seconds."""
    f = Future()
    def _reject():
        if delay:
            time.sleep(delay)
        f.set_exception(exc)
    threading.Thread(target=_reject, daemon=True).start()
    return f


class TestMyPromiseAll(unittest.TestCase):

    def test_all_resolve(self):
        result = my_promise_all([resolved(1), resolved(2), resolved(3)])
        self.assertEqual(result, [1, 2, 3])

    def test_preserves_order(self):
        result = my_promise_all([resolved(1, 0.05), resolved(2, 0.01), resolved(3, 0.02)])
        self.assertEqual(result, [1, 2, 3])

    def test_rejects_on_first_error(self):
        with self.assertRaises(ValueError):
            my_promise_all([resolved(1), rejected(ValueError("oops")), resolved(3)])

    def test_empty_list(self):
        self.assertEqual(my_promise_all([]), [])


class TestMyPromiseRace(unittest.TestCase):

    def test_returns_fastest(self):
        result = my_promise_race([resolved("slow", 0.1), resolved("fast", 0.01)])
        self.assertEqual(result, "fast")

    def test_raises_if_fastest_rejects(self):
        with self.assertRaises(RuntimeError):
            my_promise_race([rejected(RuntimeError("first"), 0.01), resolved("late", 0.1)])

    def test_single_future(self):
        self.assertEqual(my_promise_race([resolved(99)]), 99)


class TestMyPromiseAllSettled(unittest.TestCase):

    def test_all_fulfilled(self):
        result = my_promise_all_settled([resolved(1), resolved(2)])
        self.assertEqual(result, [
            {"status": "fulfilled", "value": 1},
            {"status": "fulfilled", "value": 2},
        ])

    def test_mixed_results(self):
        err = ValueError("bad")
        result = my_promise_all_settled([resolved(42), rejected(err)])
        self.assertEqual(result[0], {"status": "fulfilled", "value": 42})
        self.assertEqual(result[1]["status"], "rejected")
        self.assertIs(result[1]["reason"], err)

    def test_all_rejected(self):
        e1, e2 = RuntimeError("a"), RuntimeError("b")
        result = my_promise_all_settled([rejected(e1), rejected(e2)])
        self.assertEqual(result[0]["status"], "rejected")
        self.assertEqual(result[1]["status"], "rejected")

    def test_empty_list(self):
        self.assertEqual(my_promise_all_settled([]), [])

    def test_never_raises(self):
        # should not raise even if all futures fail
        try:
            my_promise_all_settled([rejected(Exception("x")) for _ in range(3)])
        except Exception:
            self.fail("my_promise_all_settled should not raise")


if __name__ == "__main__":
    unittest.main()
