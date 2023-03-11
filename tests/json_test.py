from gendiff.diff import travel
from gendiff.parsers.json_parser import parser_func
from gendiff.parsers.flat_parser import flat_formatter
from gendiff.parsers.plain_parser import plain_formatter
import pytest


@pytest.fixture
def tested_func1():
    dicts = parser_func('tests/fixtures/file2.json',
                        'tests/fixtures/file1.json'
                        )
    dic1, dic2 = dicts
    differ = travel(dic1, dic2)
    return flat_formatter(differ)


@pytest.fixture
def tested_func2():
    dicts = parser_func('tests/fixtures/file2.yml',
                        'tests/fixtures/file1.yml'
                        )
    dic1, dic2 = dicts
    differ = travel(dic1, dic2)
    return flat_formatter(differ)


@pytest.fixture
def tested_func3():
    dicts = parser_func('tests/fixtures/file11.json',
                        'tests/fixtures/file22.json'
                        )
    dic1, dic2 = dicts
    differ = travel(dic1, dic2)
    return flat_formatter(differ)


@pytest.fixture
def tested_func4():
    dicts = parser_func('tests/fixtures/file11.json',
                        'tests/fixtures/file22.json'
                        )
    dic1, dic2 = dicts
    differ = travel(dic1, dic2)
    return plain_formatter(differ)


@pytest.fixture
def test_data1():
    test_example = open('tests/fixtures/short_result')
    test_example = test_example.read()
    test_example = test_example.rstrip('\n')
    return test_example


@pytest.fixture
def test_data2():
    test_example = open('tests/fixtures/flat_result')
    test_example = test_example.read()
    test_example = test_example.rstrip('\n')
    return test_example


@pytest.fixture
def test_data3():
    test_example = open('tests/fixtures/plain_result')
    test_example = test_example.read()
    test_example = test_example.rstrip('\n')
    return test_example


def test1(tested_func1, test_data1):
    assert tested_func1 == test_data1


def test2(tested_func2, test_data1):
    assert tested_func2 == test_data1


def test3(tested_func3, test_data2):
    assert tested_func3 == test_data2


def test4(tested_func4, test_data3):
    assert tested_func4 == test_data3
