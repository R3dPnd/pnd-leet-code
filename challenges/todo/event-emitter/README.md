# Event Emitter

Implement a simplified `EventEmitter` class similar to Node.js's built-in `EventEmitter`.

## Requirements

Your class must support the following methods:

- `on(event, listener)` — Register a listener for an event. Multiple listeners can be registered for the same event.
- `off(event, listener)` — Remove a specific listener from an event.
- `emit(event, ...args)` — Call all listeners registered for the event, passing `...args` to each. Returns `true` if any listeners were called, `false` otherwise.
- `once(event, listener)` — Register a listener that fires **at most once**, then automatically removes itself.

## Example

```js
const emitter = new EventEmitter();

const greet = (name) => console.log(`Hello, ${name}!`);
emitter.on('greet', greet);
emitter.emit('greet', 'Alice'); // Hello, Alice!
emitter.emit('greet', 'Bob');   // Hello, Bob!

emitter.off('greet', greet);
emitter.emit('greet', 'Charlie'); // (no output) returns false

const logOnce = () => console.log('fired once');
emitter.once('ping', logOnce);
emitter.emit('ping'); // fired once
emitter.emit('ping'); // (no output)
```

## Constraints

- Event names are strings.
- The same listener function may be registered multiple times; `off` should only remove one occurrence per call.
- `emit` on an event with no listeners should return `false`.

## Follow-up

How would you add a `removeAllListeners(event?)` method that clears all listeners for a given event, or all listeners across all events if no argument is provided?
