import pytest
from logic.json_logic import generate_diff


@pytest.fixture
def tested_func():
    return generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')


@pytest.fixture
def test_data():
    test_example = open('tests/fixtures/json_result')
    test_example = test_example.read()
    test_example = test_example.rstrip('\n')
    return test_example


def test1(tested_func, test_data):
    assert tested_func == test_data
