from vertexai.preview import rag
from vertexai.preview.generative_models import GenerativeModel, Tool
import os
import vertexai

# Create a RAG Corpus, Import Files, and Generate a response

# TODO(developer): Update these lines with actual values
display_name = "test_corpus"
paths = ["https://drive.google.com/file/d/123", "gs://my_bucket/my_files_dir"]  # Supports Google Cloud Storage and Google Drive Links

# Initialize Vertex AI API once per session
vertexai.init(project=os.environ.get("GOOGLE_PROJECT_ID"), location="us-central1")

# Create RagCorpus
# Configure embedding model, for example "text-embedding-004".
embedding_model_config = rag.EmbeddingModelConfig(
    publisher_model="publishers/google/models/text-embedding-004"
)

rag_corpus = rag.create_corpus(
    display_name=display_name,
    embedding_model_config=embedding_model_config,
)

# Import Files to the RagCorpus
rag.import_files(
    rag_corpus.name,
    paths,
    chunk_size=512,  # Optional
    chunk_overlap=100,  # Optional
    max_embedding_requests_per_min=900,  # Optional
)

# Direct context retrieval
response = rag.retrieval_query(
    rag_resources=[
        rag.RagResource(
            rag_corpus=rag_corpus.name,
            # Optional: supply IDs from `rag.list_files()`.
            # rag_file_ids=["rag-file-1", "rag-file-2", ...],
        )
    ],
    text="What is RAG and why it is helpful?",
    similarity_top_k=10,  # Optional
    vector_distance_threshold=0.5,  # Optional
)
print(response)

# Enhance generation
# Create a RAG retrieval tool
rag_retrieval_tool = Tool.from_retrieval(
    retrieval=rag.Retrieval(
        source=rag.VertexRagStore(
            rag_resources=[
                rag.RagResource(
                    rag_corpus=rag_corpus.name,  # Currently only 1 corpus is allowed.
                    # Optional: supply IDs from `rag.list_files()`.
                    # rag_file_ids=["rag-file-1", "rag-file-2", ...],
                )
            ],
            similarity_top_k=3,  # Optional
            vector_distance_threshold=0.5,  # Optional
        ),
    )
)
# Create a gemini-pro model instance
rag_model = GenerativeModel(
    model_name="gemini-1.5-flash-001", tools=[rag_retrieval_tool]
)

# Generate response
response = rag_model.generate_content("What is RAG and why it is helpful?")
print(response.text)
# Example response:
#   RAG stands for Retrieval-Augmented Generation.
#   It's a technique used in AI to enhance the quality of responses
# ...

