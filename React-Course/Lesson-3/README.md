# ⚛️ React Basics Practice (Tasks 3a–3f)

This project contains a sequence of exercises (3a–3f) designed to help me learn and practice the core concepts of React, such as JSX, state management, component structure, and state lifting.

Each task builds on the previous one to gradually introduce key ideas in React.

---

## 📚 Table of Contents

- [3a - Button Click Console Log](#3a---button-click-console-log)
- [3b - Counter with useState](#3b---counter-with-usestate)
- [3c - Conditional Text Rendering](#3c---conditional-text-rendering)
- [3d - Reusable Counter Component](#3d---reusable-counter-component)
- [3e - Synchronized Counters (Lifting State Up)](#3e---synchronized-counters-lifting-state-up)
- [3f - Refactoring Counter into Separate Component](#3f---refactoring-counter-into-separate-component)
- [Technologies Used](#technologies-used)
- [What I Learned](#what-i-learned)
- [Next Steps](#next-steps)
- [Author](#author)

---

## ✅ 3a - Button Click Console Log

- Created a button with text: `Clicked 0 times`.
- When the button is clicked, it logs `"Clicked!"` to the console.
- Practiced:
  - JSX rendering
  - Handling basic `onClick` events

---

## ✅ 3b - Counter with useState

- Used `React.useState()` to create a `count` state.
- Displayed the count value dynamically inside the button.
- Incremented the count when the button was clicked.
- Practiced:
  - React state initialization and updating
  - Updating the UI using state

---

## ✅ 3c - Conditional Text Rendering

- Improved the button text to use proper singular/plural grammar:
  - `Clicked 1 time`
  - `Clicked 2 times`
- Used conditional JSX logic:
  ```jsx
  {
    count === 1 ? "Clicked 1 time" : `Clicked ${count} times`;
  }
  ```

## ✅ 3d - Reusable Counter Component

- Created a Counter component.

- Rendered two instances of the Counter component inside the App.

- Each counter had its own separate state.

Practiced:

- Component reusability

- Understanding state isolation per component instance

## ✅ 3e - Synchronized Counters (Lifting State Up)

- Moved the state from individual Counter components to a parent App component.

- Passed count and setCount as props to both Counter components.

- Now, both counters share the same state and stay synchronized.

Practiced:

- Lifting state up

- State sharing across components using props

## ✅ 3f - Refactoring Counter into Separate Component

- Refactored the counter button into its own functional Counter component.

- The App component only manages state and renders two Counter components.

- Encouraged clean code structure and component separation.

Practiced:

- Component decomposition

- Prop drilling and modular React structure

## 🛠️ Technologies Used

- HTML5

- React (via CDN)

- ReactDOM (via CDN)

- Babel (in-browser) for JSX support

## 👨‍💻 Author

Satyam Sagar

\_ 📅 Date Completed: August 7, 2025
