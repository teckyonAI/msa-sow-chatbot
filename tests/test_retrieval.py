from models.retrieval import retrieve_msa_clause

def test_retrieve_msa():
    assert retrieve_msa_clause("payment terms") is not None
