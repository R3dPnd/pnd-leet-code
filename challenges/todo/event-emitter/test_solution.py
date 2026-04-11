import unittest
from solution import EventEmitter


class TestEventEmitter(unittest.TestCase):

    def test_on_and_emit_basic(self):
        emitter = EventEmitter()
        results = []
        emitter.on("data", lambda x: results.append(x))
        emitter.emit("data", 42)
        self.assertEqual(results, [42])

    def test_emit_calls_multiple_listeners(self):
        emitter = EventEmitter()
        results = []
        emitter.on("msg", lambda: results.append("a"))
        emitter.on("msg", lambda: results.append("b"))
        emitter.emit("msg")
        self.assertEqual(sorted(results), ["a", "b"])

    def test_emit_returns_true_when_listeners_exist(self):
        emitter = EventEmitter()
        emitter.on("x", lambda: None)
        self.assertTrue(emitter.emit("x"))

    def test_emit_returns_false_when_no_listeners(self):
        emitter = EventEmitter()
        self.assertFalse(emitter.emit("nonexistent"))

    def test_off_removes_listener(self):
        emitter = EventEmitter()
        results = []
        fn = lambda: results.append(1)
        emitter.on("click", fn)
        emitter.off("click", fn)
        emitter.emit("click")
        self.assertEqual(results, [])

    def test_off_removes_only_one_occurrence(self):
        emitter = EventEmitter()
        results = []
        fn = lambda: results.append(1)
        emitter.on("click", fn)
        emitter.on("click", fn)  # registered twice
        emitter.off("click", fn)  # remove one
        emitter.emit("click")
        self.assertEqual(results, [1])  # still fires once

    def test_once_fires_only_one_time(self):
        emitter = EventEmitter()
        results = []
        emitter.once("ping", lambda: results.append("fired"))
        emitter.emit("ping")
        emitter.emit("ping")
        emitter.emit("ping")
        self.assertEqual(results, ["fired"])

    def test_once_passes_args(self):
        emitter = EventEmitter()
        results = []
        emitter.once("data", lambda x, y: results.append((x, y)))
        emitter.emit("data", 1, 2)
        self.assertEqual(results, [(1, 2)])

    def test_emit_passes_multiple_args(self):
        emitter = EventEmitter()
        received = []
        emitter.on("event", lambda a, b, c: received.append((a, b, c)))
        emitter.emit("event", "x", "y", "z")
        self.assertEqual(received, [("x", "y", "z")])

    def test_different_events_are_isolated(self):
        emitter = EventEmitter()
        results = []
        emitter.on("a", lambda: results.append("a"))
        emitter.emit("b")
        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
