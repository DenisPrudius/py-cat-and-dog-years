from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "both_zero",
        "both_just_below_threshold",
        "both_exactly_15",
        "both_just_under_24",
        "both_exactly_24",
        "both_under_28",
        "cat_28_dog_28",
        "both_100",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: int) -> None:
    assert get_human_age(cat_age, dog_age) == result
