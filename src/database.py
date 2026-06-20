import chromadb
from chromadb.utils import embedding_functions

def get_chroma_collection(db_path="./chroma_db", collection_name="pro_git_book"):
    """Initializes a persistent local Chroma client and returns the collection."""
    # Create or connect to the local database directory on disk
    client = chromadb.PersistentClient(path=db_path)
    
    # Explicitly define the default local embedding function
    # This runs completely locally on your CPU for free
    default_ef = embedding_functions.DefaultEmbeddingFunction()
    
    # Get or create the collection with the embedding function attached
    collection = client.get_or_create_collection(
        name=collection_name, 
        embedding_function=default_ef
    )
    return collection

def seed_vector_db(collection, chunks, metadatas, ids):
    """Batches and inserts text chunks, metadata, and IDs into ChromaDB."""
    print(f"🚀 Seeding ChromaDB with {len(chunks)} chunks...")
    
    # ChromaDB has a maximum batch limit per insertion (typically 4166 items)
    # Since we have 1,313 chunks, we can safely add them in one go, 
    # but chunking the ingestion into smaller batches is safer practice.
    batch_size = 100
    for i in range(0, len(chunks), batch_size):
        end_idx = i + batch_size
        
        collection.add(
            documents=chunks[i:end_idx],
            metadatas=metadatas[i:end_idx],
            ids=ids[i:end_idx]
        )
        print(f"📦 Indexed chunks {i} to {min(end_idx, len(chunks))}...")
        
    print("✅ Vector database seeding complete and saved to disk!")