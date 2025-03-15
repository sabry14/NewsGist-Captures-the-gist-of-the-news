from news_retriever import Retriever
from embedding_engine import EmbeddingEngine
from summarizer import Summarizer
from user_manager import UserManager

def main():
    retriever = Retriever()
    embedder = EmbeddingEngine()
    summarizer = Summarizer()
    user_manager = UserManager()

    while True:
        print("\n--- News Summarization App ---")
        print("1. Search for news")
        print("2. View saved topics")
        print("3. View search history")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            topic = input("Enter topic: ")
            user_manager.add_search_history(topic)
            user_manager.add_preference(topic)

            articles = retriever.fetch_articles(topic)
            if not articles:
                print("No articles found.")
                continue

            embedder.generate_embeddings(articles)

            for i, article in enumerate(articles):
                print(f"\n[{i+1}] {article['title']}")
                print(f"Source: {article['source']['name']}")
                print(f"URL: {article['url']}\n")

            summary_type = input("Choose summary type (brief/detailed): ").strip().lower()
            summaries = [summarizer.summarize(a["content"], summary_type) for a in articles if a["content"]]

            for i, summary in enumerate(summaries):
                print(f"\nSummary {i+1}: {summary}")

        elif choice == "2":
            print("\nSaved Topics:", user_manager.data["preferences"])

        elif choice == "3":
            print("\nSearch History:", [h["topic"] for h in user_manager.data["history"]])

        elif choice == "4":
            print("Exiting application.")
            break

if __name__ == "__main__":
    main()
