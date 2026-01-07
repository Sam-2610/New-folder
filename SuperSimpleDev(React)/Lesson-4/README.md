# React Basics - Exercises 4a to 4i

This repository contains solutions to exercises 4a through 4i from the React Basics course using the SuperSimpleDev CDN version of React. Each section includes a description of the exercise and the key code functionalities.

---

## ✅ 4a. Basic React Component

**Goal**: Create a simple React component that renders some JSX.

```jsx
function App() {
  return <p>Hello, world!</p>;
}
```

---

## ✅ 4b. Click Counter with useState

**Goal**: Create a counter that increases when a button is clicked.

```jsx
function App() {
  const [count, setCount] = React.useState(0);

  return <button onClick={() => setCount(count + 1)}>Count: {count}</button>;
}
```

---

## ✅ 4c. Disable Button on Click

**Goal**: Add a "Confirm" button that becomes disabled after clicking.

```jsx
function App() {
  const [isConfirmed, setIsConfirmed] = React.useState(false);

  return (
    <button disabled={isConfirmed} onClick={() => setIsConfirmed(true)}>
      {isConfirmed ? "Confirmed" : "Confirm"}
    </button>
  );
}
```

---

## ✅ 4d. Dark Mode Toggle

**Goal**: Create a button that toggles dark/light mode.

```jsx
function App() {
  const [isDarkMode, setIsDarkMode] = React.useState(false);

  return (
    <div className={isDarkMode ? "dark-mode" : "light-mode"}>
      <button onClick={() => setIsDarkMode(!isDarkMode)}>
        {isDarkMode ? "Light Mode" : "Dark Mode"}
      </button>
    </div>
  );
}
```

---

## ✅ 4e. Password Toggle (Show/Hide)

**Goal**: Add a button to show/hide the password field.

```jsx
function App() {
  const [isPasswordVisible, setIsPasswordVisible] = React.useState(false);

  return (
    <div>
      <input
        type={isPasswordVisible ? "text" : "password"}
        placeholder="Enter Password"
      />
      <button onClick={() => setIsPasswordVisible(!isPasswordVisible)}>
        {isPasswordVisible ? "Hide" : "Show"}
      </button>
    </div>
  );
}
```

---

## ✅ 4f. Clock App using useEffect and dayjs

**Goal**: Display current time that updates every second.

```jsx
function App() {
  const [time, setTime] = React.useState(dayjs().format("HH:mm:ss"));

  React.useEffect(() => {
    const intervalId = setInterval(() => {
      setTime(dayjs().format("HH:mm:ss"));
    }, 1000);

    return () => clearInterval(intervalId); // Cleanup
  }, []);

  return <p>Current time: {time}</p>;
}
```

---

## ✅ 4g. Dependency Array Demo

**Goal**: Demonstrate the impact of the dependency array in `useEffect`.

```jsx
React.useEffect(() => {
  setInterval(() => {
    console.log("run code");
    setTime(dayjs().format("HH:mm:ss"));
  }, 1000);
}, []); // Removing this causes multiple intervals
```

---

## ✅ 4h. Counter with Reset and Auto Click

**Goal**: Create a counter with:

- Increment button
- Reset button (sets count to 0)
- Auto Click button (clicks every second)

```jsx
function App() {
  const [count, setCount] = React.useState(0);
  const buttonRef = React.useRef(null);
  const intervalRef = React.useRef(null);

  function handleClick() {
    setCount((prev) => prev + 1);
  }

  function handleReset() {
    setCount(0);
    clearInterval(intervalRef.current);
    intervalRef.current = null;
  }

  function handleAutoClick() {
    if (!intervalRef.current) {
      intervalRef.current = setInterval(() => {
        if (buttonRef.current) {
          buttonRef.current.click();
        }
      }, 1000);
    }
  }

  return (
    <div>
      <button ref={buttonRef} onClick={handleClick}>
        Count: {count}
      </button>
      <button onClick={handleReset}>Reset</button>
      <button onClick={handleAutoClick}>Auto Click</button>
    </div>
  );
}
```

---

## ✅ 4i. Styled Counter App

**Goal**: Style the app from 4h.

```css
body {
  margin: 0;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: rgb(222, 222, 222);
}

button {
  background-color: rgb(25, 135, 84);
  color: white;
  padding: 10px;
  border: none;
  margin-right: 10px;
  cursor: pointer;
}
```

Wrap the buttons in a div with class `container`:

```jsx
<div className="container">
  <button ref={buttonRef} onClick={handleClick}>
    Count: {count}
  </button>
  <button onClick={handleReset}>Reset</button>
  <button onClick={handleAutoClick}>Auto Click</button>
</div>
```

---

## ✅ Summary

You’ve completed exercises from 4a to 4i covering:

- Basic React usage
- State management with `useState`
- Effects with `useEffect`
- Element references with `useRef`
- Conditional rendering and event handling
- Interval logic and cleanup
- Responsive design using Flexbox

## 👨‍💻 Author

Satyam Sagar

## 📅 Date Completed: August 8, 2025
