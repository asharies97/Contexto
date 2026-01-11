from openai import OpenAI
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv
import os

load_dotenv()
client=OpenAI()
EMBED_MODEL=os.getenv("EMBED_MODEL")
EMBED_DIM=os.getenv("VECTOR_DB_DIM")

splitter=SentenceSplitter(chunk_size=os.getenv('CHUNK_SIZE'),chunk_overlap=os.getenv('CHUNK_OVERLAP') )

def load_and_chunk_pdf(path:str):
    docs=PDFReader().load_data(file=path)
    texts=[d.text for d in docs if getattr(d,"text",None)]
    chunks=[]
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks

def embed_texts(texts:list[str])->list[list[float]]:
    response=client.embeddings.create(
        model=EMBED_MODEL,
        input=texts
    )
    return [ item.embedding for item in response.data]
