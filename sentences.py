import random

tenses = ["past", "present", "future"]

determiners_singular = ["a", "one", "the"]
determiners_plural = ["some", "many", "the"]

nouns_singular = [
    "bird",
    "boy",
    "car",
    "cat",
    "child",
    "dog",
    "girl",
    "man",
    "rabbit",
    "woman",
]
nouns_plural = [
    "birds",
    "boys",
    "cars",
    "cats",
    "children",
    "dogs",
    "girls",
    "men",
    "rabbits",
    "women",
]

verbs_past = [
    "drank",
    "ate",
    "grew",
    "laughed",
    "thought",
    "ran",
    "slept",
    "talked",
    "walked",
    "wrote",
]
verbs_present_singular = [
    "drinks",
    "eats",
    "grows",
    "laughs",
    "thinks",
    "runs",
    "sleeps",
    "talks",
    "walks",
    "writes",
]
verbs_present_plural = [
    "drink",
    "eat",
    "grow",
    "laugh",
    "think",
    "run",
    "sleep",
    "talk",
    "walk",
    "write",
]
verbs_future = [
    "will drink",
    "will eat",
    "will grow",
    "will laugh",
    "will think",
    "will run",
    "will sleep",
    "will talk",
    "will walk",
    "will write",
]

prepositions = [
    "about",
    "above",
    "across",
    "after",
    "along",
    "around",
    "at",
    "before",
    "behind",
    "below",
    "beyond",
    "by",
    "despite",
    "except",
    "for",
    "from",
    "in",
    "into",
    "near",
    "of",
    "off",
    "on",
    "onto",
    "out",
    "over",
    "past",
    "to",
    "under",
    "with",
    "without",
]


def get_determiner(quantity):
    if quantity == 1:
        return random.choice(determiners_singular)
    else:
        return random.choice(determiners_plural)


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        return random.choice(nouns_singular)
    else:
        return random.choice(nouns_plural)


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb."""

    if tense == "past":
        return random.choice(verbs_past)
    if tense == "present":
        if quantity == 1:
            return random.choice(verbs_present_singular)
        else:
            return random.choice(verbs_present_plural)
    if tense == "future":
        return random.choice(verbs_future)
    return ""


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """

    return random.choice(prepositions)


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    return "{} {} {}".format(
        get_preposition(), get_determiner(quantity), get_noun(quantity)
    )


def main():
    # Write the main function and any other functions that you think are necessary
    # for your program to generate and print six sentences with these characteristics:

    """Quantity	Verb Tense
    a.	single	past
    b.	single	present
    c.	single	future
    d.	plural	past
    e.	plural	present
    f.	plural	future"""

    sentence_template = "{} {} {} {}."

    quantity = 1

    # a.	single	past
    print(
        sentence_template.format(
            get_determiner(quantity).capitalize(),
            get_noun(quantity),
            get_verb(quantity, tenses[0]),
            get_prepositional_phrase(quantity),
        )
    )

    # b.	single	present
    print(
        sentence_template.format(
            get_determiner(quantity).capitalize(),
            get_noun(quantity),
            get_verb(quantity, tenses[1]),
            get_prepositional_phrase(quantity),
        )
    )

    # c.	single	future
    print(
        sentence_template.format(
            get_determiner(quantity).capitalize(),
            get_noun(quantity),
            get_verb(quantity, tenses[2]),
            get_prepositional_phrase(quantity),
        )
    )

    quantity = 0

    # d.	plural	past
    tense = "past"
    print(
        sentence_template.format(
            get_determiner(quantity).capitalize(),
            get_noun(quantity),
            get_verb(quantity, tenses[0]),
            get_prepositional_phrase(quantity),
        )
    )

    # e.	plural	present
    tense = "present"
    print(
        sentence_template.format(
            get_determiner(quantity).capitalize(),
            get_noun(quantity),
            get_verb(quantity, tenses[1]),
            get_prepositional_phrase(quantity),
        )
    )

    # f.	plural	future
    tense = "future"
    print(
        sentence_template.format(
            get_determiner(quantity).capitalize(),
            get_noun(quantity),
            get_verb(quantity, tenses[2]),
            get_prepositional_phrase(quantity),
        )
    )


if __name__ == "__main__":
    main()
