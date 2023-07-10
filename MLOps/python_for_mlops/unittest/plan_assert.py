"""
Run 
pytest this_file.py
"""

def test_long_dictionaries():
    result = {'key': 'value', 'lastname': 'book'}
    expected = {'key': 'value', 'lastname': 'book'}
    assert result == expected

def test_long_dictionaries():
    result = ['this', 'is', 'A', 'test']
    expected = ['this', 'is', 'a', 'test']
    assert result == expected
