import pytest
from ANSWERS.president import President

def test_invalid_term_raises_error():
    for term in -1, 47:
        with pytest.raises(ValueError):
            _ = President(term)


