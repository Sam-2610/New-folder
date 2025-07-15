# 🗃️ Simple Kanban Board

A minimal yet functional **Kanban Board** built using **HTML**, **CSS**, and **Vanilla JavaScript**. Tasks can be dragged and dropped across columns like **To Do**, **In Progress**, and **Done**—making it a great starting point for learning about the **Drag and Drop API**.

---

## 🔍 Features

- ✅ Drag-and-drop task cards across columns
- 💻 Fully responsive layout (mobile-friendly)
- 🎨 Clean, modern interface with smooth hover animations
- 🚀 Beginner-friendly and easy to extend

---

## 💡 How It Works

- **Each card** is made draggable using `draggable="true"`.
- **When a drag starts**, the card's ID is saved via `dataTransfer`.
- **Drop zones (columns)** listen for `dragover`, `dragenter`, `dragleave`, and `drop` events.
- On **drop**, the dragged card is appended to the target list.
- The **`.over`** class gives visual feedback while hovering over a drop zone.

---

## 📦 Tech Stack

- HTML5
- CSS3 (Flexbox, Media Queries)
- JavaScript (Drag and Drop API)

---

## 🧑‍💻 Author

**Satyam Sagar**  

