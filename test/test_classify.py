import pytest
from contextlib import contextmanager
from src.classify import classify, InvalidData

def test_non_int_arguments():
	with pytest.raises(InvalidData):
		obj = classify()
		obj.get_classification('12254943')


@contextmanager
def does_not_raise():
    yield


@pytest.mark.parametrize("example_input, expectation", [
	(12254943, does_not_raise()),
	(12254942, pytest.raises(InvalidData)),
])
def test_product_ids(example_input, expectation):
    """Test how much I know division."""
    with expectation:
        obj = classify()
        assert obj.get_classification(example_input) is not None