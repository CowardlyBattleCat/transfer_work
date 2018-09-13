
from coll_loop_functions import(
    fizz_buzz_sum,
    make_triangle,
    word_sentence_paragraph_count,
    )

import pytest


def test_fizz_buzz_sum():
    assert fizz_buzz_sum([3, 6, 5, 15, -4]) == 29
    assert fizz_buzz_sum([3, 6, 5, 15, -4, 7], True) == 3
    assert fizz_buzz_sum([-5, 0, 2, -5, 2]) == -10
    assert fizz_buzz_sum([-5, 0, 2, -3, 3, 15 -5, 2], True) == 4




def test_make_triangle():
    assert make_triangle(1) == [[1]]
    assert make_triangle(2) == [[1], [2, 3]]
    assert make_triangle(3) == [[1], [2, 3], [4, 5, 6]]
    assert make_triangle(4) == [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]




def test_word_sentence_paragraph_count():
    assert word_sentence_paragraph_count(0) == 1
    assert word_sentence_paragraph_count(5) == 120
    with pytest.raises(TypeError):
        word_sentence_paragraph_count('string')
