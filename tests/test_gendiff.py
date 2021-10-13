import pytest
from gendiff.scripts.gendiff import generate_diff


@pytest.fixture(scope="module", autouse=True)
def expected():
    with open('tests/fixtures/result.txt') as f:
        expected = f.read()
    return expected


def test_generate_diff_json(expected):
    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert diff == expected

    diff = generate_diff('tests/fixtures/file2.json', 'tests/fixtures/file1.json')
    assert diff != expected


def test_generate_diff_yaml(expected):
    diff = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
    assert diff == expected

    diff = generate_diff('tests/fixtures/file2.yml', 'tests/fixtures/file1.yml')
    assert diff != expected
