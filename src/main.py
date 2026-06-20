# src/main.py
from src.database import get_chroma_collection, query_vector_db

def main():
    # 1. Connect to the existing local database on disk
    collection = get_chroma_collection()
    
    # 2. Define a highly targeted technical query
    test_query = "How do I undo a commit that hasn't been pushed yet?"
    
    # 3. Execute the search
    documents, metadatas = query_vector_db(collection, test_query)
    
    # 4. Print the results to verify relevance
    print(f"\n🎯 Found {len(documents)} relevant matches:\n")
    for index, (doc, meta) in enumerate(zip(documents, metadatas)):
        print(f"--- MATCH #{index + 1} (Source: {meta['source']}) ---")
        print(doc[:400]) # Show the first 400 characters of the text chunk
        print("-" * 40, "\n")

if __name__ == "__main__":
    main()