from random import randrange


def main():
    determiners_singular = ["the", "one"]
    determiners_plural = ["some", "many"]
    nouns = ["child", "girl", "dog", "rabbit"]
    verbs_past = ["talked", "laughed", "ran", "drank"]
    verbs_present = ["talks", "laughs", "runs", "drinks"]
    verbs_future = ["will talk", "will laugh", "will run", "will drink"]
    preposition = ["for", "above", "off", "at", "on", "about"]

    sentence_template = "{d1} {n1} {v} {p} {d2} {n2}."

    # A. Singular nouns in past tense
    d1_idx = randrange(0, len(determiners_singular))
    n1_idx = randrange(0, len(nouns))
    v_idx = randrange(0, len(verbs_past))
    p_idx = randrange(0, len(preposition))
    d2_idx = randrange(0, len(determiners_singular))
    n2_idx = randrange(0, len(nouns))

    print(
        sentence_template.format(
            d1=determiners_singular[d1_idx].capitalize(),
            n1=nouns[n1_idx],
            v=verbs_past[v_idx],
            p=preposition[p_idx],
            d2=determiners_singular[d2_idx],
            n2=nouns[n2_idx],
        )
    )

    # B. Singular nouns in present tense
    d1_idx = randrange(0, len(determiners_singular))
    n1_idx = randrange(0, len(nouns))
    v_idx = randrange(0, len(verbs_present))
    p_idx = randrange(0, len(preposition))
    d2_idx = randrange(0, len(determiners_singular))
    n2_idx = randrange(0, len(nouns))

    print(
        sentence_template.format(
            d1=determiners_singular[d1_idx].capitalize(),
            n1=nouns[n1_idx],
            v=verbs_present[v_idx],
            p=preposition[p_idx],
            d2=determiners_singular[d2_idx],
            n2=nouns[n2_idx],
        )
    )

    # C. Singular nouns in future tense
    d1_idx = randrange(0, len(determiners_singular))
    n1_idx = randrange(0, len(nouns))
    v_idx = randrange(0, len(verbs_future))
    p_idx = randrange(0, len(preposition))
    d2_idx = randrange(0, len(determiners_singular))
    n2_idx = randrange(0, len(nouns))

    print(
        sentence_template.format(
            d1=determiners_singular[d1_idx].capitalize(),
            n1=nouns[n1_idx],
            v=verbs_future[v_idx],
            p=preposition[p_idx],
            d2=determiners_singular[d2_idx],
            n2=nouns[n2_idx],
        )
    )

    # D. Plural nouns in past tense
    d1_idx = randrange(0, len(determiners_plural))
    n1_idx = randrange(0, len(nouns))
    v_idx = randrange(0, len(verbs_past))
    p_idx = randrange(0, len(preposition))
    d2_idx = randrange(0, len(determiners_singular))
    n2_idx = randrange(0, len(nouns))

    print(
        sentence_template.format(
            d1=determiners_plural[d1_idx].capitalize(),
            n1=nouns[n1_idx] + ("ren" if n1_idx == 0 else "s"),
            v=verbs_past[v_idx],
            p=preposition[p_idx],
            d2=determiners_plural[d2_idx],
            n2=nouns[n2_idx] + ("ren" if n2_idx == 0 else "s"),
        )
    )

    # E. Plural nouns in present tense
    d1_idx = randrange(0, len(determiners_plural))
    n1_idx = randrange(0, len(nouns))
    v_idx = randrange(0, len(verbs_present))
    p_idx = randrange(0, len(preposition))
    d2_idx = randrange(0, len(determiners_plural))
    n2_idx = randrange(0, len(nouns))

    print(
        sentence_template.format(
            d1=determiners_plural[d1_idx].capitalize(),
            n1=nouns[n1_idx] + ("ren" if n1_idx == 0 else "s"),
            v=verbs_present[v_idx],
            p=preposition[p_idx],
            d2=determiners_plural[d2_idx],
            n2=nouns[n2_idx] + ("ren" if n2_idx == 0 else "s"),
        )
    )

    # F. Plural nouns in future tense
    d1_idx = randrange(0, len(determiners_plural))
    n1_idx = randrange(0, len(nouns))
    v_idx = randrange(0, len(verbs_future))
    p_idx = randrange(0, len(preposition))
    d2_idx = randrange(0, len(determiners_plural))
    n2_idx = randrange(0, len(nouns))

    print(
        sentence_template.format(
            d1=determiners_plural[d1_idx].capitalize(),
            n1=nouns[n1_idx] + ("ren" if n1_idx == 0 else "s"),
            v=verbs_future[v_idx],
            p=preposition[p_idx],
            d2=determiners_plural[d2_idx],
            n2=nouns[n2_idx] + ("ren" if n2_idx == 0 else "s"),
        )
    )


if __name__ == "__main__":
    main()
