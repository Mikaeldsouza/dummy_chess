from typing import List, Tuple, Union

from pandas.core.series import Series

from Gui import Gui
from mixins import is_subsequence, is_sublist
import re
from random import choice


class Oracle:

    def __init__(self, matches: Series) -> None:

        self.cache: Tuple[Tuple[str]] = self.cache_notation_arrays(matches=matches)

    def cache_notation_arrays(self, matches: Series) -> Tuple[Tuple[str]]:
        _cache: List[Tuple[str]] = []

        match: str
        for match in matches:
            _cache.append(self.get_notation_array(notation_text=match))

        return tuple(_cache)

    def predict(self, context: List[str], vagueness: int = 0) -> Union[str, None]:
        possible_next_moves: Series = Series(self.get_next_move_of_similar_matches(matches=self.cache,
                                                                                   partial_match=context,
                                                                                   vagueness=vagueness))
        if len(possible_next_moves) == 0:
            return None

        mode: Series = possible_next_moves.mode()

        if len(mode) == 0:
            return None

        return choice(mode)

    @staticmethod
    def get_next_move_of_similar_matches(matches: Tuple[Tuple[str]], partial_match: List[str], vagueness: int = 0) -> \
            Tuple[str]:
        _next_moves: List[str] = []
        index = len(partial_match)

        match: Tuple[str]
        for match in matches:

            if len(match) < index + 1:
                continue
            if vagueness > 0:
                if is_sublist(partial_match[-vagueness:], match):
                    _next_moves.append(match[index])
            else:
                if is_subsequence(subsequence=partial_match, sequence=match):
                    _next_moves.append(match[index])

        return tuple(_next_moves)

    @classmethod
    def get_notation_array(cls, notation_text) -> Tuple[str]:
        return tuple(cls.normalize_notation_text(text=notation_text).split(' '))

    @staticmethod
    def normalize_notation_text(text: str) -> str:
        return re.sub(r'\d+\.', '', text).replace('  ', ' ').strip()

    def get_result_force(self, last_move: str, update: Gui) -> Union[str, None]:
        matches: Tuple[Tuple[str]] = self.cache
        match: Tuple[str]

        for match in matches:

            if last_move in match:
                if len(match) == match.index(last_move) + 1:
                    continue
                move: str = match[match.index(last_move) + 1]

                try:
                    update.update(move)
                    return move
                except:
                    continue
