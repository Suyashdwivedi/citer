from lib.citoid import get_citoid_dict


def test_url():
    assert get_citoid_dict(
        'https://books.google.com/ngrams/graph?content=countermeasure&year_start=1740&year_end=1760&corpus=en-2019&smoothing=3',
        True,
    ) == {
        'cite_type': 'web',
        'language': 'en',
        'title': 'Google Books Ngram Viewer',
        'website': 'books.google.com',
    }
