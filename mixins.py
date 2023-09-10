from typing import Sequence, List
from random import choice


def is_sublist(sublist, list):
    return all(item in list for item in sublist)


def is_subsequence(subsequence: Sequence[str], sequence: Sequence[str]) -> bool:
    if len(subsequence) == 0 or len(sequence) == 0 or len(subsequence) > len(sequence):
        return False

    for i in range(len(subsequence)):
        if subsequence[i] != sequence[i]:
            return False

    return True


def get_error_message() -> str:
    options: List[str] = [
        "I'm so lost, I feel like a penguin in the Sahara.",
        "I'm as confused as a cat at a dog show.",
        "I'm about as useful as a screen door on a submarine.",
        "I'm as clueless as a goldfish with short-term memory loss.",
        "I'm as lost as a needle in a haystack.",
        "I'm like a squirrel on an espresso binge—lots of energy, no idea where I'm going.",
        "I'm as uncertain as a chameleon in a bag of Skittles.",
        "I'm like a GPS without batteries—no direction at all!"
    ]

    return choice(options)