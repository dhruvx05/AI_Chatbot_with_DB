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
   [Download Python](https://www.python.org/downloads/)

2. **Ollama (Local LLM Runtime)**  
   Install Ollama from [https://ollama.com](https://ollama.com)  
   Then pull the Phi model:
   ```bash
   ollama pull phi
