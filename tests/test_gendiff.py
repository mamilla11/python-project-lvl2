from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/result.txt') as f:
        expected = f.read()

    diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert diff == expected

    diff = generate_diff('tests/fixtures/file2.json', 'tests/fixtures/file1.json')
    assert diff != expected
