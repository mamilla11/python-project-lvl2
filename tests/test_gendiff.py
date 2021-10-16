import os
import json
import yaml
import pytest

from gendiff.differ import differ
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.tojson import tojson


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


@pytest.fixture
def json_format():
    with open(get_path('result_json_format.txt')) as f:
        expected = f.read()
    return expected


def test_differ_json(expected_plain):
    filepath1 = get_path('plain1.json')
    filepath2 = get_path('plain2.json')

    file1 = json.load(open(filepath1))
    file2 = json.load(open(filepath2))

    diff = differ(file1, file2)
    assert stylish(diff) == expected_plain

    diff = differ(file2, file1)
    assert stylish(diff) != expected_plain


def test_differ_yaml(expected_plain):
    filepath1 = get_path('plain1.yml')
    filepath2 = get_path('plain2.yml')

    file1 = yaml.safe_load(open(filepath1))
    file2 = yaml.safe_load(open(filepath2))

    diff = differ(file1, file2)
    assert stylish(diff) == expected_plain

    diff = differ(file2, file1)
    assert stylish(diff) != expected_plain


def test_differ_nested_json(expected_nested):
    filepath1 = get_path('nested1.json')
    filepath2 = get_path('nested2.json')

    file1 = json.load(open(filepath1))
    file2 = json.load(open(filepath2))

    diff = differ(file1, file2)
    assert stylish(diff) == expected_nested

    diff = differ(file2, file1)
    assert stylish(diff) != expected_nested


def test_differ_nested_yaml(expected_nested):
    filepath1 = get_path('nested1.yml')
    filepath2 = get_path('nested2.yml')

    file1 = yaml.safe_load(open(filepath1))
    file2 = yaml.safe_load(open(filepath2))

    diff = differ(file1, file2)
    assert stylish(diff) == expected_nested

    diff = differ(file2, file1)
    assert stylish(diff) != expected_nested


def test_plain_format(plain_format):
    filepath1 = get_path('nested1.json')
    filepath2 = get_path('nested2.json')

    file1 = json.load(open(filepath1))
    file2 = json.load(open(filepath2))

    diff = differ(file1, file2)
    assert plain(diff) == plain_format


def test_json_format(json_format):
    filepath1 = get_path('nested1.yml')
    filepath2 = get_path('nested2.yml')

    file1 = yaml.safe_load(open(filepath1))
    file2 = yaml.safe_load(open(filepath2))

    diff = differ(file1, file2)
    assert tojson(diff) == json_format
