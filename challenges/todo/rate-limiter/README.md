# Token Bucket Rate Limiter

Implement a `RateLimiter` class using the **token bucket** algorithm.

## Background

A token bucket holds up to `capacity` tokens. Tokens are added at a fixed `refillRate` (tokens per second). Each call to `consume(tokens)` removes that many tokens. If there aren't enough tokens available, the request is rejected.

## Requirements

```js
const limiter = new RateLimiter({ capacity, refillRate });
limiter.consume(tokens);  // returns true if allowed, false if rate-limited
```

- `capacity` — maximum tokens the bucket can hold.
- `refillRate` — tokens added per second (can be fractional, e.g. `0.5` = one token every 2 s).
- `consume(tokens = 1)` — attempts to consume `tokens` from the bucket. Returns `true` if successful, `false` if there are not enough tokens.
- Tokens should refill **lazily** (calculated on each `consume` call based on elapsed time), not via `setInterval`.
- The bucket should never exceed `capacity`.

## Example

```js
const limiter = new RateLimiter({ capacity: 3, refillRate: 1 }); // 1 token/sec, max 3

console.log(limiter.consume()); // true  (2 tokens left)
console.log(limiter.consume()); // true  (1 token left)
console.log(limiter.consume()); // true  (0 tokens left)
console.log(limiter.consume()); // false (empty)

// wait 1 second...
// 1 token refilled
console.log(limiter.consume()); // true
```

## Constraints

- Use `Date.now()` (or `performance.now()`) to track elapsed time — do **not** use `setInterval`.
- Tokens are real numbers internally; `consume` checks if `currentTokens >= requested`.
- Requesting more tokens than `capacity` should always return `false`.

## Follow-up

How would you extend this to a **sliding window** rate limiter that tracks request counts over a rolling time window instead?
