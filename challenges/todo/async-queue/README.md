# Async Queue with Concurrency Limit

Implement an `AsyncQueue` class that runs async tasks with a **maximum concurrency limit**.

## Requirements

```js
const queue = new AsyncQueue(concurrency);
queue.add(asyncTask); // returns a Promise that resolves with the task's result
```

- `concurrency` — maximum number of tasks that may run **simultaneously**.
- `add(task)` — accepts a zero-argument async function (or a function returning a Promise). Returns a Promise that resolves/rejects with the task's result/error.
- Tasks beyond the concurrency limit are **queued** and start automatically as running tasks finish.
- The queue should handle task rejections without crashing — other pending tasks must still run.

## Example

```js
const delay = (ms, val) => new Promise((res) => setTimeout(() => res(val), ms));

const queue = new AsyncQueue(2); // max 2 concurrent

queue.add(() => delay(100, 'a')).then(console.log); // 'a'
queue.add(() => delay(50,  'b')).then(console.log); // 'b'
queue.add(() => delay(10,  'c')).then(console.log); // 'c'  (starts after 'b' finishes)
queue.add(() => delay(10,  'd')).then(console.log); // 'd'  (starts after 'a' finishes)

// Output order: b, c, a, d  (b and a start immediately; b finishes first, c starts; etc.)
```

## Constraints

- `concurrency` is a positive integer.
- Tasks are started in FIFO order as slots become available.
- A rejected task should not affect other tasks.

## Follow-up

Add a `drain()` method that returns a Promise resolving when all currently queued and running tasks have completed.
