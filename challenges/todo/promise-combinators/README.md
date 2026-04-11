# Promise Combinators

Re-implement three core Promise combinators **from scratch** without using their built-in versions.

## Requirements

### 1. `myPromiseAll(promises)`
Resolves with an array of all resolved values (in input order) when **all** promises resolve.  
Rejects immediately with the first rejection reason if **any** promise rejects.

### 2. `myPromiseRace(promises)`
Resolves or rejects with the value/reason of whichever promise **settles first**.

### 3. `myPromiseAllSettled(promises)`
Always resolves with an array of result objects — one per input promise — in the form:
- `{ status: 'fulfilled', value: <value> }`
- `{ status: 'rejected', reason: <reason> }`

## Example

```js
myPromiseAll([
  Promise.resolve(1),
  Promise.resolve(2),
  Promise.resolve(3),
]).then(console.log); // [1, 2, 3]

myPromiseAll([
  Promise.resolve(1),
  Promise.reject('oops'),
]).catch(console.error); // 'oops'

myPromiseRace([
  new Promise((res) => setTimeout(() => res('slow'), 100)),
  new Promise((res) => setTimeout(() => res('fast'), 10)),
]).then(console.log); // 'fast'

myPromiseAllSettled([
  Promise.resolve(42),
  Promise.reject('bad'),
]).then(console.log);
// [
//   { status: 'fulfilled', value: 42 },
//   { status: 'rejected', reason: 'bad' }
// ]
```

## Constraints

- You may use `new Promise(...)`, `.then()`, and `.catch()` — but not `Promise.all`, `Promise.race`, or `Promise.allSettled`.
- Input arrays may be empty; handle that edge case.
- Non-Promise values in the array should be treated as already-resolved promises.

## Follow-up

How would you implement `myPromiseAny` — which resolves with the first fulfilled value and rejects only if **all** promises reject?
