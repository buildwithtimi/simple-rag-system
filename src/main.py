import os
import sys
from dotenv import load_dotenv
from src.database import get_chroma_collection, query_vector_db
from src.generator import generate_answer

def main():
    # Load environment variables from .env file
    load_dotenv()
    print("🤖 Initializing Simple Git RAG Engine...")
    
    # 1. Connect to our existing on-disk persistent vector database
    try:
        collection = get_chroma_collection()
        # Quick health check to see if database has items
        count = collection.count()
        if count == 0:
            print("❌ Database is empty! Please re-run your seeding script first.")
            sys.exit(1)
        print(f"✅ Vector Database Connected! ({count} text chunks ready on disk)")
    except Exception as e:
        print(f"❌ Could not connect to ChromaDB: {e}")
        sys.exit(1)
        
    print("\n💡 System ready. Ask any Git questions! (Type 'exit' to quit)")
    print("=" * 60)
    
    # 2. Boot up the real-time Interactive Loop
    while True:
        try:
            user_query = input("\n📝 Ask Git: ").strip()
            
            if not user_query:
                continue
            if user_query.lower() in ['exit', 'quit']:
                print("👋 Exiting RAG application. Happy coding!")
                break
                
            # Step A: Retrieve semantic chunks from ChromaDB
            documents, metadatas = query_vector_db(collection, user_query, num_results=3)
            
            # Step B: Pass query and chunks to LLM for final synthesis
            print("🧠 Synthesizing answer based on Pro Git data...")
            final_answer = generate_answer(user_query, documents)
            
            # Step C: Print the grounded answer
            print("\n🤖 ANSWER:")
            print(final_answer)
            print("=" * 60)
            
        except KeyboardInterrupt:
            print("\n👋 Exiting safely.")
            break

if __name__ == "__main__":
    main()