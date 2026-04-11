import unittest
import time
from solution import RateLimiter


class TestRateLimiter(unittest.TestCase):

    def test_allows_up_to_capacity(self):
        limiter = RateLimiter(capacity=3, refill_rate=0)  # no refill
        self.assertTrue(limiter.consume())
        self.assertTrue(limiter.consume())
        self.assertTrue(limiter.consume())

    def test_rejects_when_empty(self):
        limiter = RateLimiter(capacity=2, refill_rate=0)
        limiter.consume()
        limiter.consume()
        self.assertFalse(limiter.consume())

    def test_refills_over_time(self):
        limiter = RateLimiter(capacity=1, refill_rate=100)  # 100 tokens/sec
        limiter.consume()  # empty
        time.sleep(0.02)   # ~2 tokens refilled
        self.assertTrue(limiter.consume())

    def test_bucket_does_not_exceed_capacity(self):
        limiter = RateLimiter(capacity=2, refill_rate=1000)
        time.sleep(0.05)  # would add 50 tokens if uncapped
        # should only have 2
        self.assertTrue(limiter.consume())
        self.assertTrue(limiter.consume())
        self.assertFalse(limiter.consume())

    def test_requesting_more_than_capacity_always_fails(self):
        limiter = RateLimiter(capacity=3, refill_rate=1000)
        self.assertFalse(limiter.consume(10))

    def test_partial_refill(self):
        limiter = RateLimiter(capacity=10, refill_rate=10)  # 10 tokens/sec
        for _ in range(10):
            limiter.consume()  # drain
        self.assertFalse(limiter.consume())
        time.sleep(0.15)  # ~1.5 tokens refilled
        self.assertTrue(limiter.consume())   # 1 token available
        self.assertFalse(limiter.consume())  # second one fails

    def test_consume_fractional_tokens(self):
        limiter = RateLimiter(capacity=1.5, refill_rate=0)
        self.assertTrue(limiter.consume(1.5))
        self.assertFalse(limiter.consume(0.1))

    def test_returns_bool(self):
        limiter = RateLimiter(capacity=1, refill_rate=0)
        result = limiter.consume()
        self.assertIsInstance(result, bool)


if __name__ == "__main__":
    unittest.main()
