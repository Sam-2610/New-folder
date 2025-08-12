import { useState } from 'react'
import './App.css'

 function ChatInput({ chatMessages, setChatMessages }) {
        const [inputValue, setInputValue] = React.useState("");

      function saveInput(event) {
        setInputValue(event.target.value);
      }

      function handleSend() {
        if (inputValue.trim() === "") return;

          // Add user's message
          const userMessage = {
            message: inputValue,
            sender: "user",
            id: crypto.randomUUID(),
          };

          const updatedMessages = [...chatMessages, userMessage];
          setChatMessages(updatedMessages);

          // Get bot response
          const botResponse = ChatBot.getResponse(inputValue);

          const botMessage = {
            message: botResponse,
            sender: "robot",
            id: crypto.randomUUID(),
          };

          setChatMessages((prev) => [...prev, botMessage]);
          setInputValue("");
        }

        return (
          <>
            <input
              type="text"
              placeholder="Type your message here..."
              size="30"
              onChange={saveInput}
              value={inputValue}
            />
            <button onClick={handleSend}>Send</button>
          </>
        );
      }

      function ChatMessage({ message, sender }) {
        return (
          <div>
            {sender === "robot" && <img src="robot.png" width="50" />}
            <span>{message}</span>
            {sender === "user" && <img src="user.png" width="50" />}
          </div>
        );
      }


function App() {
  const [chatMessages, setChatMessages] = useState([
    {
      message: "Hello Chatbot",
      sender: "user",
      id: crypto.randomUUID(),
    },
    {
      message: "Hello! How can I help you?",
      sender: "robot",
      id: crypto.randomUUID(),
    },
  ]);

    return (
      <>
        <ChatInput
          chatMessages={chatMessages}
          setChatMessages={setChatMessages}
        />
        {chatMessages.map((msg) => (
          <ChatMessage
            key={msg.id}
            message={msg.message}
            sender={msg.sender}
          />
        ))}
      </>
        );
}

export default App
