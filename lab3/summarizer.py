from langchain.chains.summarize import load_summarize_chain
from langchain.llms import HuggingFacePipeline
from langchain_community.llms import HuggingFaceHub
from langchain_core.documents import Document
from transformers import pipeline


class Summarizer:
    def __init__(self):
        """Initialize LangChain summarization chains using different models."""

        # Load Hugging Face models for summarization
        self.brief_model = pipeline("summarization", model="google/pegasus-xsum")
        self.detailed_model = pipeline("summarization", model="allenai/led-large-16384")

        # Wrap models with LangChain
        self.brief_llm = HuggingFacePipeline(pipeline=self.brief_model)
        self.detailed_llm = HuggingFacePipeline(pipeline=self.detailed_model)

        # Load LangChain summarization chains
        self.brief_chain = load_summarize_chain(self.brief_llm, chain_type="map_reduce")
        self.detailed_chain = load_summarize_chain(self.detailed_llm, chain_type="refine")

    def summarize(self, text, summary_type="brief"):
        """Summarizes text using LangChain summarization chains."""
        if not text or len(text.split()) < 10:
            return "Input text is too short for summarization."

        doc = [Document(page_content=text)]

        try:
            if summary_type == "brief":
                return self.brief_chain.invoke(doc)
            else:
                return self.detailed_chain.invoke(doc)
        except Exception as e:
            return f"Summarization failed: {str(e)}"