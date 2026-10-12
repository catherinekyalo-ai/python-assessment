import pythonAssessment as p

ARTICLE = "The cat sat on the mat. The cat slept!\n\nIs the dog here? No.\n\n\nThe end.\n"


def test_count_specific_word():
    assert p.count_specific_word(ARTICLE, "the") == 5
    assert p.count_specific_word(ARTICLE, "zebra") == 0


def test_most_common_word():
    assert p.identify_most_common_word(ARTICLE) == "the"
    assert p.identify_most_common_word("") is None


def test_average_word_length():
    assert round(p.calculate_average_word_length(ARTICLE), 2) == 3.00
    assert p.calculate_average_word_length("") == 0


def test_paragraphs():
    assert p.count_paragraphs(ARTICLE) == 3
    assert p.count_paragraphs("") == 1


def test_sentences():
    assert p.count_sentences(ARTICLE) == 5
