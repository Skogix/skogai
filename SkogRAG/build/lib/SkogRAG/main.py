# Import necessary modules
import os
import sys
import os.path
from .hello import hello

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import argparse  # For parsing command-line arguments
from llama_index.core import (  # Importing components for handling vector store index
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

def main():
    """
    Main function to run the SkogRAG project.
    It initializes the data directory, checks for existing storage,
    and processes a query using a vector store index.
    """
    # Set up argument parser for command-line options
    parser = argparse.ArgumentParser(description="Run SkogRAG with a specified data directory.")
    parser.add_argument('--data', type=str, default='./data', help='The path to the data directory (default: ./data)')
    parser.add_argument('query', type=str, nargs='?', default='What year is the story about?', help='The query question')
    args = parser.parse_args()

    data_dir = args.data  # Directory containing data files
    query_question = args.query
    # Check if storage already exists
    PERSIST_DIR = "./storage"
    if not os.path.exists(data_dir):  # Validate data directory existence
        raise ValueError(f"Data directory not found: {os.path.abspath(data_dir)}. Please create the directory and add files to it.")
    if not os.path.exists(PERSIST_DIR):  # If no storage, create index from documents
        if not os.listdir(data_dir):
            raise ValueError(f"No files found in {data_dir}. Please add files to the directory and try again.")
        documents = SimpleDirectoryReader(data_dir).load_data()
        index = VectorStoreIndex.from_documents(documents)
        # Store index for later use
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # Load the existing index from storage
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)

    # Query the index with the provided question
    query_engine = index.as_query_engine()
    response = query_engine.query(query_question)
    print(response)  # Output the response to the query

if __name__ == "__main__":  # Entry point for the script
    main()
