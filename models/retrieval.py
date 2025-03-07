import chromadb
from config import Config

def retrieve_msa_clause(query):
    client = chromadb.PersistentClient(path=Config.VECTOR_DB_PATH)
    collection = client.get_collection(name="msa_clauses")
    results = collection.query(query_texts=[query], n_results=1)
    return results["documents"][0] if results["documents"] else None
