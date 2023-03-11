from sentences import (
    tenses,
    determiners_singular,
    determiners_plural,
    nouns_singular,
    nouns_plural,
    verbs_past,
    verbs_present_singular,
    verbs_present_plural,
    verbs_future,
    prepositions,
    get_determiner,
    get_noun,
    get_verb,
    get_preposition,
    get_prepositional_phrase,
)
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in determiners_singular

    # 2. Test the plural determiners.

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in determiners_plural


def test_get_noun():
    for _ in range(4):
        noun = get_noun(1)

        assert noun in nouns_singular


def test_get_verb():
    for _ in range(4):
        verb = get_verb(1, tenses[0])

        assert verb in verbs_past


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
