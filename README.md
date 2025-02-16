# 🍸 Cocktail Chat Application

This is a Python-based chat application that integrates with a LLM to create a Retrieval-Augmented Generation (RAG) system using a vector database. The application allows users to ask questions about cocktails and get recommendations based on their preferences.

## 🛠️ Prerequisites

- **Python 3.12** 🐍
- **Poetry** (for dependency management) ⚙️
- **Hugging Face API token** 💻
- **Make** (optional) 🧰

## 🚀 Installation

### 1. Clone the repository
Start by cloning the repository:

```bash
git clone https://github.com/dxrrkwm/CocktailChat.git
cd CocktailChat
```

## 2. 📄 Fill in the environment variables
Copy the .env.sample file to .env and fill in the HUGGINGFACE_API_TOKEN with your Hugging Face API token:
   ```bash
   cp .env.sample .env
   ```
## 3. ⚙️ Installing dependencies
   ```bash
   make deps
   ```
   or
   ```bash
   poetry install
   ```
-------------------
## 4. 🧨 Running the application
   ```bash
   make run
   ```
   or
   ```bash
   uvicorn main:app --reload
   ```
## 5. 🐾 Try it out
The application will be running at http://127.0.0.1:8000/static/index.html
