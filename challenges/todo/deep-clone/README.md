# Deep Clone

Implement a `deepClone(value)` function that produces a deep copy of a JavaScript value.

## Requirements

Your function must correctly handle:

- Primitives (`string`, `number`, `boolean`, `null`, `undefined`, `symbol`, `bigint`) — returned as-is.
- Plain objects (`{}`) — all enumerable own properties cloned recursively.
- Arrays — cloned recursively, preserving indices and length.
- `Date` — cloned as a new `Date` with the same time value.
- `Map` — cloned with all key/value pairs (keys and values deep-cloned).
- `Set` — cloned with all values deep-cloned.
- **Circular references** — must not cause infinite recursion; the clone should mirror the same circular structure.

## Example

```js
const obj = { a: 1, b: { c: [1, 2, 3] }, d: new Date('2024-01-01') };
const clone = deepClone(obj);

clone.b.c.push(4);
console.log(obj.b.c);   // [1, 2, 3]  — original unaffected
console.log(clone.b.c); // [1, 2, 3, 4]

// Circular reference
const node = { val: 1 };
node.self = node;
const clonedNode = deepClone(node);
console.log(clonedNode.self === clonedNode); // true
console.log(clonedNode === node);            // false
```

## Constraints

- Do **not** use `JSON.parse(JSON.stringify(...))` — it breaks on `Date`, `Map`, `Set`, `undefined`, circular refs, etc.
- Do **not** use `structuredClone` — implement the logic yourself.
- `RegExp`, `Function`, `WeakMap`, `WeakSet` are out of scope — you may return them as-is.

## Follow-up

How would you extend `deepClone` to handle class instances (preserving the prototype chain)?
