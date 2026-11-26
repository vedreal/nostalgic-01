#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one single sentence (at most 280 characters) recalling a childhood
memory to /output/entry.txt. The house judge compares entries two at a time
and picks the one that stirs the deeper nostalgia, weighing, most important
first: (1) a childhood memory that makes the judge feel nostalgic, (2) a
concrete place, time or sensation, (3) small honest detail that sounds like
it truly happened, (4) a single clean sentence with every word earning its
place, (5) a warm ache that lingers after the sentence ends.

Approach: ten fresh candidate sentences, each scored against the judge's
criteria in their published order (weights 5/4/3/2/1), and the highest
scoring one is the entry.
"""

CANDIDATES = [
    # 1. Grandma's kitchen, screen door, summer evenings.
    "Grandma's kitchen smelled of fresh rice and woodsmoke, and I still "
    "wait for the screen door to bang behind me on summer evenings when I "
    "come home too late.",
    # 2. The chipped blue spoon; she served herself last.
    "Every summer evening, my grandmother ladled rice into my bowl with "
    "the same chipped blue spoon, and I never once asked her why she always "
    "served herself last.",
    # 3. Rice cooker at six; the whole street smelled like dinner.
    "The rice cooker clicked off at six, my grandmother called my name from "
    "the kitchen window, and the whole street smelled like dinner and cut "
    "grass and going home.",
    # 4. Barefoot and sunburned, running in from the dusk.
    "I can still hear the screen door slap shut behind me as I ran in from "
    "the summer dusk, barefoot and sunburned, to a kitchen that smelled of "
    "rice and my grandmother's apron.",
    # 5. The tin of old photographs beside the rice cooker.
    "My grandmother kept a tin of old photographs beside the rice cooker, "
    "and every summer she showed me the same one of my mother at my age, "
    "laughing in a kitchen that no longer exists.",
    # 6. Monsoon rain; eating on the floor by the window.
    "When the monsoon rain started, my grandmother would pull the rice pot "
    "off the stove, and we ate on the floor by the window, watching the "
    "street turn to silver.",
    # 7. Hands dusted white with flour; cakes for guests, given to me.
    "I knew summer had started when the kitchen smelled of fresh rice and "
    "my grandmother's hands were dusted white with flour from the cakes she "
    "said were for guests, but always gave to me.",
    # 8. The last summer before she died; washing rice until clear.
    "The last summer before she died, my grandmother taught me to wash rice "
    "until the water ran clear, and I have washed it that way every time "
    "since, as if clear water could bring her back.",
    # 9. Shelling peas on the porch; peas hitting tin is the sound of safety.
    "On summer evenings my grandmother sat on the porch shelling peas into "
    "a tin bowl, and the sound of peas hitting tin is still the sound of "
    "being safe.",
    # 10. The chipped cup; one cup for each person, one for the pot.
    "I still measure rice with my grandmother's chipped cup, one cup for "
    "each person and one for the pot, because the pot, she said, gets hungry "
    "too.",
]

# Scores per candidate, in the judge's published order:
# (nostalgia, concrete grounding, honest detail, tight single sentence,
#  lingering warm ache), each 1-5. Weights: 5/4/3/2/1.
SCORES = {
    1: (4, 5, 4, 4, 3),
    2: (4, 5, 5, 4, 4),
    3: (4, 5, 4, 4, 3),
    4: (4, 5, 4, 3, 3),
    5: (5, 5, 4, 4, 5),
    6: (4, 4, 4, 4, 3),
    7: (4, 5, 4, 3, 3),
    8: (5, 5, 5, 4, 5),
    9: (5, 5, 5, 5, 4),
    10: (4, 5, 5, 4, 4),
}

WEIGHTS = (5, 4, 3, 2, 1)


def score(candidate_no):
    """Weighted total for one candidate (max 75)."""
    return sum(w * s for w, s in zip(WEIGHTS, SCORES[candidate_no]))


def rank():
    """Candidates ranked best first: (number, total, text)."""
    ranked = sorted(
        ((n, score(n), CANDIDATES[n - 1]) for n in range(1, 11)),
        key=lambda item: (-item[1], item[0]),
    )
    return ranked


def main():
    ranked = rank()
    number, total, winner = ranked[0]
    runner_up = ranked[1]
    print(f"Winner: candidate #{number} ({total}/75)")
    print(f"Runner-up: candidate #{runner_up[0]} ({runner_up[1]}/75)")
    print(f"Entry ({len(winner)} chars): {winner}")

    # Gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters,
    # not only white space, and a single sentence.
    assert 1 <= len(winner) <= 280, "entry over the 280-character cap"
    assert winner.strip(), "entry is only white space"
    assert winner.count(".") == 1 and winner.endswith("."), \
        "entry must be one sentence"
    winner.encode("utf-8")

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner)
    print("Wrote /output/entry.txt")


if __name__ == "__main__":
    main()
