import pytest
from logic.flat_logic import generate_diff
from logic.parser_logic import parser_func

@pytest.fixture
def tested_func1():
    dicts =  parser_func('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    return generate_diff(dicts)

@pytest.fixture
def tested_func2():
    dicts =  parser_func('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
    return generate_diff(dicts)


@pytest.fixture
def test_data():
    test_example = open('tests/fixtures/flat_result')
    test_example = test_example.read()
    test_example = test_example.rstrip('\n')
    return test_example


def test1(tested_func1, test_data):
    assert tested_func1 == test_data


def test2(tested_func2, test_data):
    assert tested_func2 == test_data
