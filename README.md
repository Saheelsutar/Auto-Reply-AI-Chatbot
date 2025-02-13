# Auto Reply AI Chatbot

AI-powered virtual assistant designed to automate interactions with a chat application. It analyzes chat history and generates humorous, roast-style responses using Google's **Gemini 1.5 Flash API**.

## Features

### 🔄 Automated Chat Interaction
- Uses `pyautogui` to perform mouse and keyboard operations, interacting with the chat application without manual intervention.

### 📜 Chat History Analysis
- Copies chat history from the chat application and analyzes it to determine if the last message was sent by a specific user (e.g., **"Aryan Suryavanshi"**).

### 🤣 Humorous Response Generation
- Integrates with **Gemini 1.5 Flash API** to generate funny, roast-style responses based on the analyzed chat history.

### 📋 Clipboard Operations
- Utilizes `pyperclip` to copy and paste text, facilitating the retrieval and insertion of chat messages.
- Uses `pyautogui` to interact with the chat application seamlessly.
