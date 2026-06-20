import os
from google import genai
from google.genai import types

def generate_answer(user_query, retrieved_chunks):
    """Combines text chunks into a secure context template and asks Gemini to synthesize the answer."""
    
    # 1. Initialize the client.
    # It will automatically check your system environment or .env for GEMINI_API_KEY
    client = genai.Client()
    
    # 2. Flatten your vector chunks into a single text block
    context_block = "\n---\n".join(retrieved_chunks)
    
    # 3. Formulate the precise system guidelines
    system_instruction = (
        "You are a precise, elite technical assistant specializing exclusively in Git version control.\n"
        "Your knowledge base comes entirely from the provided fragments of the Pro Git book below.\n\n"
        f"--- START OF PRO GIT BOOK CONTEXT ---\n{context_block}\n--- END OF CONTEXT ---\n\n"
        "CRITICAL INSTRUCTIONS:\n"
        "1. Answer the user's question using ONLY the facts and commands found in the context above.\n"
        "2. If the context does not contain enough information to answer definitively, say exactly:\n"
        "   'I am sorry, but the provided text does not contain that information.'\n"
        "3. Do not make up information, do not assume, and do not use outside general knowledge."
    )
    
    # 4. Request generation using the lightning-fast gemini-2.5-flash model
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_query,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.0  # Forces factual consistency
            )
        )
        return response.text
    except Exception as e:
        return f"❌ Gemini API Error: {str(e)}\nEnsure your GEMINI_API_KEY is correctly loaded."