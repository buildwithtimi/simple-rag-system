# src/main.py
from src.ingest import load_and_chunk_git_book
from src.database import get_chroma_collection, seed_vector_db

def main():
    # 1. Parse and chunk the Asciidoc files
    book_dir = "./data/pro-git-book"
    chunks, metadatas, ids = load_and_chunk_git_book(book_dir)
    
    # 2. Connect to ChromaDB
    collection = get_chroma_collection()
    
    # 3. Seed the database
    seed_vector_db(collection, chunks, metadatas, ids)

if __name__ == "__main__":
    main()