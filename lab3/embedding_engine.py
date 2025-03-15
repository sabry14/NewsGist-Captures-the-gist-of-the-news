from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


class EmbeddingEngine:
    def __init__(self):
        self.model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_db = None

    def generate_embeddings(self, articles):
        """Generates vector embeddings and stores them in FAISS."""
        texts = [article["content"] or article["description"] for article in articles if article.get("content")]

        if not texts:
            print("No valid articles found for embedding.")
            return

        embeddings = self.model.embed_documents(texts)

        self.vector_db = FAISS.from_texts(texts, self.model)
