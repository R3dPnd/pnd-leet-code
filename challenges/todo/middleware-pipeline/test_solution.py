import unittest
from solution import compose


class TestMiddlewarePipeline(unittest.TestCase):

    def test_single_middleware_runs(self):
        order = []

        def mw(ctx, next):
            order.append("mw")
            next()

        pipeline = compose([mw])
        pipeline({})
        self.assertEqual(order, ["mw"])

    def test_middleware_runs_in_order(self):
        order = []

        def mw1(ctx, next):
            order.append(1)
            next()

        def mw2(ctx, next):
            order.append(2)
            next()

        def mw3(ctx, next):
            order.append(3)
            next()

        compose([mw1, mw2, mw3])({})
        self.assertEqual(order, [1, 2, 3])

    def test_pre_and_post_processing(self):
        order = []

        def mw1(ctx, next):
            order.append("before-1")
            next()
            order.append("after-1")

        def mw2(ctx, next):
            order.append("before-2")
            next()
            order.append("after-2")

        compose([mw1, mw2])({})
        self.assertEqual(order, ["before-1", "before-2", "after-2", "after-1"])

    def test_ctx_is_shared(self):
        def mw1(ctx, next):
            ctx["a"] = 1
            next()

        def mw2(ctx, next):
            ctx["b"] = ctx["a"] + 1
            next()

        ctx = {}
        compose([mw1, mw2])(ctx)
        self.assertEqual(ctx, {"a": 1, "b": 2})

    def test_short_circuit_skips_rest(self):
        order = []

        def mw1(ctx, next):
            order.append(1)
            # intentionally does NOT call next()

        def mw2(ctx, next):
            order.append(2)
            next()

        compose([mw1, mw2])({})
        self.assertEqual(order, [1])

    def test_empty_pipeline(self):
        pipeline = compose([])
        pipeline({})  # should not raise

    def test_calling_next_twice_raises(self):
        def bad_mw(ctx, next):
            next()
            next()  # second call should raise

        with self.assertRaises(RuntimeError):
            compose([bad_mw])({})

    def test_error_propagates(self):
        def mw(ctx, next):
            raise ValueError("middleware error")

        with self.assertRaises(ValueError):
            compose([mw])({})

    def test_outer_next_called_at_end(self):
        called = []

        def mw(ctx, next):
            next()

        def final_next():
            called.append("final")

        compose([mw])({}, final_next)
        self.assertEqual(called, ["final"])


if __name__ == "__main__":
    unittest.main()
