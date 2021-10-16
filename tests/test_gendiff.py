import os
import json
import yaml
import pytest

from gendiff.differ import generate_diff
from gendiff.stylish import stylish
from gendiff.plain import plain


def get_path(filename):
    return os.path.join('tests/fixtures', filename)


@pytest.fixture
def expected_plain():
    with open(get_path('result_plain.txt')) as f:
        expected = f.read()
    return expected


@pytest.fixture
def expected_nested():
    with open(get_path('result_nested.txt')) as f:
        expected = f.read()
    return expected


@pytest.fixture
def plain_format():
    with open(get_path('result_plain_format.txt')) as f:
        expected = f.read()
    return expected


def test_generate_diff_json(expected_plain):
    filepath1 = get_path('plain1.json')
    filepath2 = get_path('plain2.json')

    file1 = json.load(open(filepath1))
    file2 = json.load(open(filepath2))

    diff = generate_diff(file1, file2)
    assert stylish(diff) == expected_plain

    diff = generate_diff(file2, file1)
    assert stylish(diff) != expected_plain


def test_generate_diff_yaml(expected_plain):
    filepath1 = get_path('plain1.yml')
    filepath2 = get_path('plain2.yml')

    file1 = yaml.safe_load(open(filepath1))
    file2 = yaml.safe_load(open(filepath2))

    diff = generate_diff(file1, file2)
    assert stylish(diff) == expected_plain

    diff = generate_diff(file2, file1)
    assert stylish(diff) != expected_plain


def test_generate_diff_nested_json(expected_nested):
    filepath1 = get_path('nested1.json')
    filepath2 = get_path('nested2.json')

    file1 = json.load(open(filepath1))
    file2 = json.load(open(filepath2))

    diff = generate_diff(file1, file2)
    assert stylish(diff) == expected_nested

    diff = generate_diff(file2, file1)
    assert stylish(diff) != expected_nested


def test_generate_diff_nested_yaml(expected_nested):
    filepath1 = get_path('nested1.yml')
    filepath2 = get_path('nested2.yml')

    file1 = yaml.safe_load(open(filepath1))
    file2 = yaml.safe_load(open(filepath2))

    diff = generate_diff(file1, file2)
    assert stylish(diff) == expected_nested

    diff = generate_diff(file2, file1)
    assert stylish(diff) != expected_nested


def test_plain_format(plain_format):
    filepath1 = get_path('nested1.json')
    filepath2 = get_path('nested2.json')

    file1 = json.load(open(filepath1))
    file2 = json.load(open(filepath2))

    diff = generate_diff(file1, file2)
    assert plain(diff) == plain_format
