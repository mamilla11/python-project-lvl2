import os
import json
import yaml
import pytest

from gendiff.differ import generate_diff
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.tojson import tojson


def get_path(filename):
    return os.path.join('tests/fixtures', filename)


@pytest.fixture(scope="module", autouse=True)
def stylish_diff_plain():
    with open(get_path('stylish_diff_plain.txt')) as f:
        expected = f.read()
    return expected


@pytest.fixture(scope="module", autouse=True)
def stylish_diff_nested():
    with open(get_path('stylish_diff_nested.txt')) as f:
        expected = f.read()
    return expected


@pytest.fixture(scope="module", autouse=True)
def plain_diff_nested():
    with open(get_path('plain_diff_nested.txt')) as f:
        expected = f.read()
    return expected


@pytest.fixture(scope="module", autouse=True)
def json_diff_nested():
    with open(get_path('json_diff_nested.txt')) as f:
        expected = f.read()
    return expected


@pytest.fixture(scope="module", autouse=True)
def plain_json():
    filepath1 = get_path('before_plain.json')
    filepath2 = get_path('after_plain.json')
    return filepath1, filepath2


@pytest.fixture(scope="module", autouse=True)
def plain_yaml():
    filepath1 = get_path('before_plain.yml')
    filepath2 = get_path('after_plain.yml')
    return filepath1, filepath2


@pytest.fixture(scope="module", autouse=True)
def nested_json():
    filepath1 = get_path('before_nested.json')
    filepath2 = get_path('after_nested.json')
    return filepath1, filepath2


@pytest.fixture(scope="module", autouse=True)
def nested_yaml():
    filepath1 = get_path('before_nested.yml')
    filepath2 = get_path('after_nested.yml')
    return filepath1, filepath2


def test_stylish_diff_plain_json(plain_json, stylish_diff_plain):
    file1, file2 = plain_json

    diff = generate_diff(file1, file2)
    assert diff == stylish_diff_plain

    diff = generate_diff(file2, file1)
    assert diff != stylish_diff_plain


def test_stylish_diff_plain_yaml(plain_yaml, stylish_diff_plain):
    file1, file2 = plain_yaml

    diff = generate_diff(file1, file2)
    assert diff == stylish_diff_plain

    diff = generate_diff(file2, file1)
    assert diff != stylish_diff_plain


def test_stylish_diff_nested_json(nested_json, stylish_diff_nested):
    file1, file2 = nested_json

    diff = generate_diff(file1, file2, 'stylish')
    assert diff == stylish_diff_nested

    diff = generate_diff(file2, file1, 'stylish')
    assert diff != stylish_diff_nested


def test_stylish_diff_nested_yaml(nested_yaml, stylish_diff_nested):
    file1, file2 = nested_yaml

    diff = generate_diff(file1, file2, 'stylish')
    assert diff == stylish_diff_nested

    diff = generate_diff(file2, file1, 'stylish')
    assert diff != stylish_diff_nested


def test_plain_diff_nested_json(nested_json, plain_diff_nested):
    file1, file2 = nested_json

    diff = generate_diff(file1, file2, 'plain')
    assert diff == plain_diff_nested


def test_json_diff_nested_yaml(nested_yaml, json_diff_nested):
    file1, file2 = nested_yaml

    diff = generate_diff(file1, file2, 'json')
    assert diff == json_diff_nested


def test_unknown_diff_nested_json(nested_json):
    file1, file2 = nested_json

    diff = generate_diff(file1, file2, 'yaml')
    assert diff == None
