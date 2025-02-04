from twttr import shorten

def test_assert():
    assert shorten("twitter") == "twttr"
    assert shorten("gotcuk") == "gtck"

def test_capital():
    assert shorten("TWITTER") == "TWTTR"
