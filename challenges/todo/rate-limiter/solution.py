import time


class RateLimiter:
    def __init__(self, capacity: float, refill_rate: float):
        """
        :param capacity:    maximum tokens the bucket can hold
        :param refill_rate: tokens added per second (can be fractional)

        TODO: initialize bucket state and timestamp tracking
        """
        pass

    def consume(self, tokens: float = 1) -> bool:
        """
        Attempt to consume `tokens` from the bucket.
        Lazily refills based on elapsed time since the last call.

        Returns True if there were enough tokens, False otherwise.

        TODO: implement lazy refill + consume logic
        """
        pass
