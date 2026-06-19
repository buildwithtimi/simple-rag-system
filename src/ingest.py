import os
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_chunk_git_book(directory_path):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )
    
    chunks = []
    metadatas = []
    ids = []
    chunk_counter = 0
    
    # Convert string path to a robust Path object
    base_dir = Path(directory_path)
    print(f"Scanning directory safely: {base_dir.resolve()}")
    
    # rglob("*.asc") searches through all nested subfolders recursively for .asc files
    for file_path in sorted(base_dir.rglob("*.asc")):
        print(f"📖 Reading file: {file_path.name}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        file_chunks = text_splitter.split_text(content)
        
        for index, chunk in enumerate(file_chunks):
            chunks.append(chunk)
            ids.append(f"id_{chunk_counter}")
            metadatas.append({
                "file_path": str(file_path.relative_to(base_dir)),
                "source": file_path.name,
                "chunk_index": index
            })
            chunk_counter += 1
            
    return chunks, metadatas, ids

