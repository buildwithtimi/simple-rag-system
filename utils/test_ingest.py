# test_ingest.py
from src.ingest import load_and_chunk_git_book

def verify_ingestion():
    # 1. Point to your local git markdown folder
    book_directory = "./data/pro-git-book"
    
    print("⏳ Running ingestion and chunking parser...")
    chunks, metadatas, ids = load_and_chunk_git_book(book_directory)
    print("✅ Ingestion complete!\n")
    
    # 2. Structural Assertions (The Core Health Check)
    print("--- 🛠️ METRIC CHECK ---")
    print(f"Total chunks generated: {len(chunks)}")
    print(f"Total metadata records: {len(metadatas)}")
    print(f"Total unique IDs written: {len(ids)}")
    
    # Verify that arrays are symmetrical
    if len(chunks) == len(metadatas) == len(ids):
        print("📊 Array Alignment: PERFECT (All data arrays match in size).")
    else:
        print("❌ Array Alignment: ERROR (Mismatch between chunks, metadata, or IDs).")
        return

    # 3. Visual Content Sample (The Reality Check)
    print("\n--- 👁️ DATA SAMPLE CHECK (Chunk #0) ---")
    print(f"Identifier: {ids[0]}")
    print(f"Metadata:   {metadatas[0]}")
    print(f"Chunk Size: {len(chunks[0])} characters")
    print("\n--- Raw Text Fragment Preview ---")
    print(chunks[0][:300]) # Print first 300 characters of the first chunk
    print("---------------------------------\n")

if __name__ == "__main__":
    verify_ingestion()