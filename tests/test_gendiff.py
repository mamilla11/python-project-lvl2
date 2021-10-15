import os
import pytest
from gendiff.scripts.gendiff import generate_diff


def get_path(filename):
    os.path.join('tests/fixtures', filename)


@pytest.fixture
def expected_plain():
    with open(get_path('result_plain.txt') as f:
        expected = f.read()
    return expected


@pytest.fixture
def expected_nested():
    with open(get_path('result_nested.txt') as f:
        expected = f.read()
    return expected


def test_generate_diff_json(expected_plain):
    diff = generate_diff(get_path('plain1.json', get_path('plain2.json')))
    assert diff == expected

    diff = generate_diff(get_path('plain2.json', get_path('plain1.json')))
    assert diff != expected


def test_generate_diff_yaml(expected_plain):
    diff = generate_diff(get_path('plain1.yml', get_path('plain2.yml')))
    assert diff == expected

    diff = generate_diff(get_path('plain2.yml', get_path('plain1.yml')))
    assert diff != expected


def test_generate_diff_nested_json(expected_nested):
    diff = generate_diff(get_path('nested1.json', get_path('nested2.json')))
    assert diff == expected

    diff = generate_diff(get_path('nested2.json', get_path('nested1.json')))
    assert diff != expected


def test_generate_diff_nested_json(expected_nested):
    diff = generate_diff(get_path('nested1.yml', get_path('nested2.yml')))
    assert diff == expected

    diff = generate_diff(get_path('nested2.yml', get_path('nested1.yml')))
    assert diff != expected

