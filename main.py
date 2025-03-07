from fastapi import FastAPI, HTTPException
from models.retrieval import retrieve_msa_clause
from models.generator import generate_sow

app = FastAPI()

@app.get("/ping")
def health_check():
    return {"status": "OK"}

@app.get("/retrieve")
def get_msa_clause(query: str):
    result = retrieve_msa_clause(query)
    if not result:
        raise HTTPException(status_code=404, detail="Clause not found")
    return {"clause": result}

@app.get("/generate")
def get_sow():
    sow_text = generate_sow()
    return {"sow": sow_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
