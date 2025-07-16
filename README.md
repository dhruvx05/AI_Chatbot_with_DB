# 🧠 Local AI Chatbot with LangChain and SQLite

This is a conversational AI chatbot that uses **LangChain** with **Ollama** for generating responses and **SQLite** for storing conversation history.  
It allows users to interact with the bot, view past conversations, and manage the stored data — all locally and offline.

---

## ✨ Features

- 🤖 AI-powered chatbot using the **Ollama Phi** model (or any other local LLM via Ollama)
- 🗂️ Conversation history is saved in a local **SQLite** database
- 🔍 Options to **view** or **delete** previous conversations
- 🔒 Fully local and private — no cloud or internet required

---

## ⚙️ Prerequisites

Before running the project, make sure you have the following installed:

1. **Python 3.8 or higher**  
   👉 [Download Python](https://www.python.org/downloads/)

2. **Ollama (Local LLM Runtime)**  
   👉 Download and install Ollama from [https://ollama.com](https://ollama.com)  
   After installation, pull the model you'd like to use (e.g., Phi):
   ```bash
   ollama pull phi
   
---

💬 Chatbot Commands
Once the chatbot is running:

🗣️ Type your message and press Enter to chat with the AI

📜 Type history → View stored conversation history

🧹 Type clear → Delete all saved chat history

❌ Type exit → Quit the chatbot

All conversations are stored in chat_history.db (SQLite) in the project folder.
