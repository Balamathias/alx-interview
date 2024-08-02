'''
Bitwise operators are used to compare (binary) numbers:
'''

def test_bitwise():
    assert 5 & 3 == 1 # 5 = 101, 3 = 011, 1 = 001
    assert 5 | 3 == 7
    assert 5 ^ 3 == 6
    assert ~5 == -6
    assert 5 << 1 == 10
    assert 5 >> 1 == 2

test_bitwise()


def safely_parse_string(s: str) -> int:
    assert s is not None, 's is None'
    assert s != '', 's is empty'
    assert s.isnumeric(), 's is not numeric'
    return (int(s))


def test_safely_parse_string():
    assert safely_parse_string('5') == 5
    try:
        safely_parse_string(None)
    except AssertionError as e:
        assert str(e) == 's is None'
        print(e)
    try:
        safely_parse_string('')
    except AssertionError as e:
        assert str(e) == 's is empty'
        print(e)
    try:
        safely_parse_string('a')
    except AssertionError as e:
        assert str(e) == 's is not numeric'
        print(e)

test_safely_parse_string()