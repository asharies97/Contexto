🧠 Contexto: PDF-to-Insight RAG Engine
Contexto is a high-performance, event-driven RAG (Retrieval-Augmented Generation) application built to transform static PDF documents into interactive, searchable knowledge bases. Leveraging LlamaIndex for orchestration and Inngest for reliable, asynchronous processing, Contexto provides a robust pipeline for high-fidelity document understanding.

🚀 Key Features
Event-Driven Ingestion: Uses Inngest to handle long-running PDF parsing and embedding tasks without timeouts or server crashes.

Dual LLM Support: Seamlessly integrates with Google Gemini for state-of-the-art reasoning and OpenAI (optional) for legacy compatibility.

High-Fidelity Parsing: Powered by LlamaIndex to handle complex PDF structures, ensuring tables and metadata are preserved.

Semantic Search: Implements high-dimensional vector search to find exact context matches beyond simple keyword lookups.

3072-Dim Embeddings: Optimized for Qdrant or local vector stores using gemini-embedding-001.

🏗️ The Architecture
Contexto follows a standard but optimized RAG lifecycle:

Ingestion: A user uploads a PDF. Inngest triggers a background job to handle the heavy lifting.

Chunking & Embedding: LlamaIndex splits the document into semantic nodes. These nodes are converted into 3072-dimensional vectors via Gemini.

Storage: Vectors are stored in a dedicated collection (defaulting to Qdrant).

Retrieval: When a query arrives, we calculate the Cosine Similarity between the query vector and the document chunks.

Generation: The top-$K$ most relevant chunks are injected into a prompt, and Gemini 2.0/2.5 generates a grounded, accurate answer.

🚦 Getting Started
1. Environment Configuration
Create a .env file in the root directory and provide your API keys:
  # Provide at least one
  GEMINI_API_KEY=your_gemini_api_key
  OPENAI_API_KEY=your_openai_api_key

2. Launch the Stack
Start the application and its dependencies (Qdrant, Inngest Dev Server, and the App) using Docker:

Bash
  docker-compose up -d

3. Monitor Workflows
Once the containers are running, you can monitor your document processing runs, retries, and step-by-step logs at:

👉 http://localhost:8288/runs
