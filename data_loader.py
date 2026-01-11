from openai import OpenAI
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv
import os
load_dotenv()

# Gemini uses different model names for embeddings
EMBED_MODEL = os.getenv("EMBED_MODEL")
EMBED_DIM=os.getenv("VECTOR_DB_DIM")

def getAIClient(model:str):
    if model=="GEMINI":
        return OpenAI(
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url=os.getenv("BASEURL")
        )
    else :
        return OpenAI()

client=getAIClient(os.getenv("AIPROVIDER"))
splitter=SentenceSplitter(chunk_size=os.getenv('CHUNK_SIZE'),chunk_overlap=os.getenv('CHUNK_OVERLAP') )

def load_and_chunk_pdf(path:str):
    docs=PDFReader().load_data(file=path)
    texts=[d.text for d in docs if getattr(d,"text",None)]
    chunks=[]
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks


def embed_texts(texts: list[str]) -> list[list[float]]:
    all_embeddings = []

    # Process in chunks of 100 to satisfy Google's strict limit
    for i in range(0, len(texts), 100):
        batch = texts[i:i + 100]
        response = client.embeddings.create(
            model="gemini-embedding-001",
            input=batch
        )
        all_embeddings.extend([record.embedding for record in response.data])

    return all_embeddings
