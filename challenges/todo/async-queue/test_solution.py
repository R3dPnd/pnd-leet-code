import unittest
import threading
import time
from solution import AsyncQueue


class TestAsyncQueue(unittest.TestCase):

    def test_runs_single_task(self):
        q = AsyncQueue(2)
        result = q.add(lambda: 42)
        self.assertEqual(result, 42)

    def test_runs_all_tasks(self):
        q = AsyncQueue(2)
        results = []
        lock = threading.Lock()

        threads = []
        for i in range(5):
            val = i
            def submit(v=val):
                r = q.add(lambda x=v: x * 2)
                with lock:
                    results.append(r)
            t = threading.Thread(target=submit)
            threads.append(t)

        for t in threads:
            t.start()
        for t in threads:
            t.join()

        self.assertEqual(sorted(results), [0, 2, 4, 6, 8])

    def test_concurrency_limit_is_respected(self):
        concurrency = 2
        q = AsyncQueue(concurrency)
        active = [0]
        peak = [0]
        lock = threading.Lock()

        def task():
            with lock:
                active[0] += 1
                peak[0] = max(peak[0], active[0])
            time.sleep(0.05)
            with lock:
                active[0] -= 1

        threads = [threading.Thread(target=q.add, args=(task,)) for _ in range(6)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        self.assertLessEqual(peak[0], concurrency)

    def test_returns_task_result(self):
        q = AsyncQueue(3)
        result = q.add(lambda: "hello")
        self.assertEqual(result, "hello")

    def test_propagates_exception(self):
        q = AsyncQueue(2)
        with self.assertRaises(ValueError):
            q.add(lambda: (_ for _ in ()).throw(ValueError("boom")))

    def test_failed_task_does_not_block_queue(self):
        q = AsyncQueue(1)
        results = []

        def bad_task():
            raise RuntimeError("fail")

        def good_task():
            return "ok"

        try:
            q.add(bad_task)
        except RuntimeError:
            pass

        results.append(q.add(good_task))
        self.assertEqual(results, ["ok"])


if __name__ == "__main__":
    unittest.main()
