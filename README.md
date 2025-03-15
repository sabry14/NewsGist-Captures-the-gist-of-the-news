# 📰 News Summarization App  

This is a Python-based news summarization tool that retrieves news articles, processes embeddings, and summarizes content using different summarization models.  

## 🚀 Features  
- **Retrieve News**: Fetch news articles based on a given topic.  
- **Summarization**: Generate brief or detailed summaries of news articles.  
- **User Preferences**: Store and retrieve previously searched topics.  
- **Search History**: Keep track of searched topics for easy access.  
- **Embeddings**: Generate embeddings for retrieved news articles.  

---

## 📂 Project Structure  

```
📦 News Summarization App  
├── 📄 main.py                  # Main script to run the application  
├── 📄 news_retriever.py        # Handles fetching news articles  
├── 📄 embedding_engine.py      # Generates embeddings for news articles  
├── 📄 summarizer.py            # Summarizes articles using NLP models  
├── 📄 user_manager.py          # Manages user preferences and search history  
├── 📄 config.py                # Configuration settings  
├── 📄 requirements.txt         # List of dependencies  
└── 📂 __pycache__/             # Cached Python files  
```

---

## 🛠 Installation  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/news-summarization-app.git
   cd news-summarization-app
   ```

2. **Create a Virtual Environment (Optional but Recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚡ Usage  

Run the application using:  

```bash
python main.py
```

### 📌 Options in the App  
1️⃣ **Search for News**: Enter a topic to fetch and summarize related articles.  
2️⃣ **View Saved Topics**: Check previously searched topics.  
3️⃣ **View Search History**: See past search queries.  
4️⃣ **Exit**: Quit the application.  

---

## 🧠 How It Works  

1. **News Retrieval (`news_retriever.py`)**  
   - Fetches news articles based on the user’s input.  

2. **Embedding Generation (`embedding_engine.py`)**  
   - Converts news articles into embeddings for future use.  

3. **Summarization (`summarizer.py`)**  
   - Uses NLP models to summarize news in **brief** or **detailed** format.  

4. **User Management (`user_manager.py`)**  
   - Stores user preferences and search history.  

---

## 📜 License  
This project is licensed under the MIT License.  
