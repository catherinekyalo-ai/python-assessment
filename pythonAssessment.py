"""Text analysis of a news article: word counts, averages, paragraphs, sentences."""

import re
import sys
from collections import Counter

ARTICLE_PATH = "article.txt"

WORD_PATTERN = re.compile(r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)*")
NON_ALNUM_PATTERN = re.compile(r"[^A-Za-z0-9]")
PARAGRAPH_SPLIT_PATTERN = re.compile(r"\n\s*\n")
SENTENCE_SPLIT_PATTERN = re.compile(r"[.!?]+(?=\s|$)")


def read_article(path):
    """Return the contents of the text file at `path` as a string."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def extract_words(text):
    """Return a list of lowercase words, excluding punctuation."""
    return WORD_PATTERN.findall(text.lower().replace("\u2019", "'"))


def count_specific_word(text, search_word):
    """Return how many times `search_word` appears in `text` (case-insensitive)."""
    cleaned = search_word.strip().strip(".,!?;:\"").lower()
    count = 0
    for word in extract_words(text):
        if word == cleaned:
            count += 1
    return count


def identify_most_common_word(text):
    """Return the most common word in `text`, or None if there are no words."""
    words = extract_words(text)
    if not words:
        return None
    return Counter(words).most_common(1)[0][0]


def calculate_average_word_length(text):
    """Return the average word length, ignoring punctuation. Empty text gives 0."""
    words = extract_words(text)
    if not words:
        return 0
    total_letters = 0
    index = 0
    while index < len(words):
        total_letters += len(NON_ALNUM_PATTERN.sub("", words[index]))
        index += 1
    return total_letters / len(words)


def count_paragraphs(text):
    """Return the number of paragraphs (blocks separated by empty lines).

    An empty string counts as 1 paragraph.
    """
    stripped = text.strip()
    if not stripped:
        return 1
    return len([p for p in PARAGRAPH_SPLIT_PATTERN.split(stripped) if p.strip()])


def count_sentences(text):
    """Return the number of sentences. An empty string counts as 1."""
    if not text.strip():
        return 1
    count = 0
    for sentence in SENTENCE_SPLIT_PATTERN.split(text):
        if sentence.strip():
            count += 1
    return count


def main():
    """Read the article, run every analysis, and print the results."""
    try:
        article = read_article(ARTICLE_PATH)
    except FileNotFoundError:
        print(f"Error: '{ARTICLE_PATH}' not found. Place it in this folder and try again.")
        sys.exit(1)

    search_word = input("Enter the word you want to count: ").strip()

    print("\n--- Article Analysis ---")
    if search_word:
        count = count_specific_word(article, search_word)
        print(f"Occurrences of '{search_word}': {count}")
    else:
        print("No search word entered, skipping word count.")

    print(f"Most common word: {identify_most_common_word(article)}")
    print(f"Average word length: {calculate_average_word_length(article):.2f}")
    print(f"Number of paragraphs: {count_paragraphs(article)}")
    print(f"Number of sentences: {count_sentences(article)}")


if __name__ == "__main__":
    main()
