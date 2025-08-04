# Top 10 React Interview Questions

This guide covers the most commonly asked React interview questions with detailed explanations and code examples.

## 1. What is React and what are its key features?

**Answer:** React is a JavaScript library for building user interfaces, particularly single-page applications. It's used for handling the view layer and can be used for developing both web and mobile applications.

**Key Features:**
- **Virtual DOM**: React creates a virtual representation of the UI in memory
- **Component-Based**: UI is broken down into reusable components
- **Unidirectional Data Flow**: Data flows from parent to child components
- **JSX**: JavaScript syntax extension that allows HTML-like code in JavaScript
- **Declarative**: You describe what you want, React handles the DOM updates

```jsx
// Example of a simple React component
import React from 'react';

function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}

export default Welcome;
```

## 2. What is JSX and how does it work?

**Answer:** JSX (JavaScript XML) is a syntax extension for JavaScript that allows you to write HTML-like code in JavaScript files.

**Key Points:**
- JSX is transpiled to `React.createElement()` calls
- It must have a single parent element (or use React.Fragment)
- You can embed JavaScript expressions using curly braces `{}`
- JSX prevents XSS attacks by escaping content

```jsx
// JSX Example
const element = (
  <div>
    <h1>Hello, {user.name}!</h1>
    <p>You are {user.age} years old</p>
  </div>
);

// Transpiles to:
const element = React.createElement(
  'div',
  null,
  React.createElement('h1', null, 'Hello, ', user.name, '!'),
  React.createElement('p', null, 'You are ', user.age, ' years old')
);
```

## 3. What are React Components and what are the different types?

**Answer:** React components are reusable pieces of UI that can accept props and return React elements.

**Types of Components:**

### Functional Components (Recommended)
```jsx
// Modern functional component with hooks
import React, { useState, useEffect } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Count: ${count}`;
  }, [count]);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

### Class Components (Legacy)
```jsx
import React, { Component } from 'react';

class Counter extends Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }

  componentDidMount() {
    document.title = `Count: ${this.state.count}`;
  }

  componentDidUpdate() {
    document.title = `Count: ${this.state.count}`;
  }

  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={() => this.setState({ count: this.state.count + 1 })}>
          Increment
        </button>
      </div>
    );
  }
}
```

## 4. What are Props and State in React?

**Answer:** Props and State are two fundamental concepts in React for managing data.

### Props (Properties)
- Read-only data passed from parent to child
- Cannot be modified by the child component
- Used for configuration and data passing

```jsx
// Parent component
function Parent() {
  return <Child name="John" age={25} />;
}

// Child component
function Child(props) {
  return (
    <div>
      <p>Name: {props.name}</p>
      <p>Age: {props.age}</p>
    </div>
  );
}
```

### State
- Internal data managed by the component
- Can be modified using setState (class) or state setters (hooks)
- Triggers re-renders when changed

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');

  return (
    <div>
      <input 
        value={name} 
        onChange={(e) => setName(e.target.value)} 
        placeholder="Enter name"
      />
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

## 5. What are React Hooks and what are the most commonly used ones?

**Answer:** Hooks are functions that allow you to use state and other React features in functional components.

### useState
```jsx
import React, { useState } from 'react';

function Example() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');

  return (
    <div>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

### useEffect
```jsx
import React, { useState, useEffect } from 'react';

function Example() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // ComponentDidMount equivalent
    fetchData();
    
    // ComponentWillUnmount equivalent
    return () => {
      // Cleanup function
    };
  }, []); // Empty dependency array = run only once

  useEffect(() => {
    // Runs when data changes
    if (data) {
      setLoading(false);
    }
  }, [data]);

  const fetchData = async () => {
    const response = await fetch('/api/data');
    const result = await response.json();
    setData(result);
  };

  if (loading) return <div>Loading...</div>;
  return <div>{JSON.stringify(data)}</div>;
}
```

### useContext
```jsx
import React, { createContext, useContext, useState } from 'react';

const ThemeContext = createContext();

function App() {
  const [theme, setTheme] = useState('light');

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <Header />
      <Main />
    </ThemeContext.Provider>
  );
}

function Header() {
  const { theme, setTheme } = useContext(ThemeContext);
  
  return (
    <header>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme
      </button>
    </header>
  );
}
```

## 6. What is the Virtual DOM and how does it work?

**Answer:** The Virtual DOM is a lightweight copy of the actual DOM that React uses to optimize rendering performance.

**How it works:**
1. When state changes, React creates a new Virtual DOM tree
2. React compares the new Virtual DOM with the previous one (diffing)
3. React calculates the minimum number of changes needed
4. React updates only the changed parts of the actual DOM

**Benefits:**
- Faster than direct DOM manipulation
- Cross-platform compatibility
- Batch updates for better performance

```jsx
// Example showing Virtual DOM optimization
function TodoList() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'Learn React', completed: false },
    { id: 2, text: 'Build an app', completed: false }
  ]);

  const toggleTodo = (id) => {
    setTodos(todos.map(todo => 
      todo.id === id 
        ? { ...todo, completed: !todo.completed }
        : todo
    ));
  };

  return (
    <ul>
      {todos.map(todo => (
        <li 
          key={todo.id}
          onClick={() => toggleTodo(todo.id)}
          style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}
        >
          {todo.text}
        </li>
      ))}
    </ul>
  );
}
```

## 7. What is the difference between controlled and uncontrolled components?

**Answer:** The difference lies in how form data is managed.

### Controlled Components
- Form data is handled by React state
- React controls the component's behavior
- More predictable and testable

```jsx
import React, { useState } from 'react';

function ControlledForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Name:', name, 'Email:', email);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Name"
      />
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```

### Uncontrolled Components
- Form data is handled by the DOM itself
- Use refs to access form values
- Less code but less control

```jsx
import React, { useRef } from 'react';

function UncontrolledForm() {
  const nameRef = useRef();
  const emailRef = useRef();

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Name:', nameRef.current.value);
    console.log('Email:', emailRef.current.value);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        ref={nameRef}
        placeholder="Name"
      />
      <input
        type="email"
        ref={emailRef}
        placeholder="Email"
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```

## 8. What are React Keys and why are they important?

**Answer:** Keys are special string attributes that help React identify which items have changed, been added, or been removed in lists.

**Why they're important:**
- Help React identify unique elements
- Improve performance by avoiding unnecessary re-renders
- Prevent bugs when items are reordered

```jsx
// Good: Using unique keys
function TodoList() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'Learn React' },
    { id: 2, text: 'Build an app' },
    { id: 3, text: 'Deploy to production' }
  ]);

  return (
    <ul>
      {todos.map(todo => (
        <li key={todo.id}>{todo.text}</li>
      ))}
    </ul>
  );
}

// Bad: Using array index as key
function BadTodoList() {
  const [todos, setTodos] = useState([
    { text: 'Learn React' },
    { text: 'Build an app' },
    { text: 'Deploy to production' }
  ]);

  return (
    <ul>
      {todos.map((todo, index) => (
        <li key={index}>{todo.text}</li> // ❌ Don't use index as key
      ))}
    </ul>
  );
}
```

## 9. What is React Context and when should you use it?

**Answer:** Context provides a way to pass data through the component tree without having to pass props down manually at every level.

**When to use Context:**
- Global state management (theme, user authentication, language)
- Avoiding prop drilling
- Sharing data between components that are not directly related

```jsx
import React, { createContext, useContext, useState } from 'react';

// Create context
const UserContext = createContext();
const ThemeContext = createContext();

function App() {
  const [user, setUser] = useState({ name: 'John', isLoggedIn: true });
  const [theme, setTheme] = useState('light');

  return (
    <UserContext.Provider value={{ user, setUser }}>
      <ThemeContext.Provider value={{ theme, setTheme }}>
        <Header />
        <Main />
        <Footer />
      </ThemeContext.Provider>
    </UserContext.Provider>
  );
}

function Header() {
  const { user } = useContext(UserContext);
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <header style={{ background: theme === 'light' ? '#fff' : '#333' }}>
      <h1>Welcome, {user.name}!</h1>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme
      </button>
    </header>
  );
}

function Main() {
  const { user } = useContext(UserContext);
  
  return (
    <main>
      {user.isLoggedIn ? (
        <p>You are logged in as {user.name}</p>
      ) : (
        <p>Please log in</p>
      )}
    </main>
  );
}

function Footer() {
  const { theme } = useContext(ThemeContext);
  
  return (
    <footer style={{ background: theme === 'light' ? '#f0f0f0' : '#222' }}>
      <p>Footer content</p>
    </footer>
  );
}
```

## 10. What are React Lifecycle Methods and how do they compare to Hooks?

**Answer:** Lifecycle methods are functions that get called at different stages of a component's life. With hooks, we use useEffect to achieve similar functionality.

### Class Component Lifecycle
```jsx
import React, { Component } from 'react';

class LifecycleExample extends Component {
  constructor(props) {
    super(props);
    this.state = { data: null };
  }

  componentDidMount() {
    // Called after component is mounted
    this.fetchData();
  }

  componentDidUpdate(prevProps, prevState) {
    // Called after component updates
    if (prevProps.id !== this.props.id) {
      this.fetchData();
    }
  }

  componentWillUnmount() {
    // Called before component unmounts
    this.cancelRequest();
  }

  render() {
    return <div>{this.state.data}</div>;
  }
}
```

### Functional Component with Hooks
```jsx
import React, { useState, useEffect } from 'react';

function LifecycleExample({ id }) {
  const [data, setData] = useState(null);

  useEffect(() => {
    // componentDidMount equivalent
    fetchData();
    
    // componentWillUnmount equivalent
    return () => {
      cancelRequest();
    };
  }, []); // Empty dependency array = run only once

  useEffect(() => {
    // componentDidUpdate equivalent
    if (id) {
      fetchData();
    }
  }, [id]); // Run when id changes

  const fetchData = async () => {
    // Fetch data logic
  };

  const cancelRequest = () => {
    // Cleanup logic
  };

  return <div>{data}</div>;
}
```

## Additional Tips for React Interviews

1. **Practice coding challenges** - Be ready to write components on a whiteboard
2. **Understand performance optimization** - Know about React.memo, useMemo, useCallback
3. **Learn about testing** - Jest, React Testing Library
4. **Know about routing** - React Router
5. **Understand state management** - Redux, Zustand, or Context API
6. **Be familiar with modern React patterns** - Custom hooks, compound components
7. **Know about error boundaries** - How to handle errors gracefully
8. **Understand code splitting** - React.lazy, Suspense
9. **Be aware of React 18 features** - Concurrent features, automatic batching
10. **Practice explaining concepts** - Be able to explain React concepts in simple terms

## Resources for Further Learning

- [React Official Documentation](https://react.dev/)
- [React Hooks Documentation](https://react.dev/reference/react)
- [React Patterns](https://reactpatterns.com/)
- [React Interview Questions on GitHub](https://github.com/sudheerj/reactjs-interview-questions)
