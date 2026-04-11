# Middleware Pipeline

Implement a `compose` function that chains Express-style middleware functions into a single executable pipeline.

## Background

In Express/Koa, middleware functions have the signature `(ctx, next) => void|Promise`. Each middleware can:
1. Do work **before** calling `next()` (pre-processing).
2. `await next()` to pass control to the next middleware.
3. Do work **after** `next()` resolves (post-processing).
4. Skip `next()` to short-circuit the chain.

## Requirements

```js
const pipeline = compose([fn1, fn2, fn3]);
await pipeline(ctx);
```

- `compose(middlewares)` — takes an array of middleware functions and returns a single function.
- The returned function accepts a `ctx` object and an optional `next` (default: no-op).
- Middleware must be called in order.
- Each middleware receives `(ctx, next)` where `next()` calls the following middleware.
- Should support both sync and async middleware.
- Calling `next()` more than once in a single middleware should throw an error.

## Example

```js
const log = async (ctx, next) => {
  console.log('before', ctx.url);
  await next();
  console.log('after', ctx.status);
};

const setStatus = async (ctx, next) => {
  ctx.status = 200;
  await next();
};

const pipeline = compose([log, setStatus]);

const ctx = { url: '/hello', status: null };
await pipeline(ctx);
// before /hello
// after 200
```

## Constraints

- Works with any number of middleware (including zero — just call the final `next`).
- Properly propagates errors thrown inside middleware.
- Async and sync middleware may be mixed freely.

## Follow-up

How would you implement a `Router` on top of `compose` that matches `ctx.method` + `ctx.path` and only runs matched middleware?
