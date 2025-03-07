from models.generator import generate_sow

def test_generate_sow():
    assert "mocked" in generate_sow()
