# React Basics Practice

This repository contains a collection of beginner-friendly **React exercises** to practice rendering components, handling props, and basic JSX usage.  
All examples use the `react.js`, `react-dom.js`, and `babel.js` setup from **SuperSimpleDev** for quick learning without installing dependencies.

---

## 1️⃣ Exercise 1 — Simple Button & Paragraph

**Goal:** Render a paragraph and a button to the page.

**Code:**

```jsx
function App() {
  return (
    <>
      <p>Hello, React!</p>
      <button>Click Me</button>
    </>
  );
}
const container = document.querySelector(".js-container");
ReactDOM.createRoot(container).render(<App />);
```

Key Concepts:

- JSX syntax.

- Rendering elements inside a fragment (<> </>).

- Using ReactDOM.createRoot().

---

## 2️⃣ Exercise 2 — E-commerce Product (Socks Example)

**Goal:** Display product details and an "Add to Cart" button.

**Output:**

Cotton Socks
Price: $10.90
[ Add to Cart ]

**Code:**

```jsx
function App() {
  return (
    <>
      <p>Cotton Socks</p>
      <p>Price: $10.90</p>
      <button>Add to Cart</button>
    </>
  );
}
const container = document.querySelector(".js-container");
ReactDOM.createRoot(container).render(<App />);
```



Key Concepts:

- Static text rendering.

- Component grouping with fragments.

- Simple UI structure for product display.

---

## 3️⃣ Exercise 3 — Personalized Greeting

**Goal:** Render a personalized greeting message.

**Code:**

```jsx
function App() {
  const name = "John";
  return (
    <>
      <h1>Hello, {name}!</h1>
      <p>Welcome to React practice.</p>
    </>
  );
}
const container = document.querySelector(".js-container");
ReactDOM.createRoot(container).render(<App />);
```


Key Concepts:

- JavaScript expression embedding inside JSX ({}).

- Dynamic rendering based on variables.

---

## 4️⃣ Exercise 4 — Props Usage

**Goal:** Create a component that accepts title and price as props.

**Code:**

```jsx
function Product(props) {
  return (
    <>
      <p>{props.title}</p>
      <p>Price: ${props.price}</p>
      <button>Add to Cart</button>
    </>
  );
}

function App() {
  return <Product title="Cotton Socks" price="10.90" />;
}

const container = document.querySelector(".js-container");
ReactDOM.createRoot(container).render(<App />);
```

Key Concepts:

- Passing props to components.

- Reusable components.

---


## 🎯 Learning Outcomes

- Understanding JSX structure.

- Using fragments to group elements.

- Embedding JavaScript in JSX.

- Passing and rendering props.

- Structuring UI components.

---

## 👨‍💻 Author

Satyam Sagar

## 📅 Date Completed: August 6, 2025




`````
