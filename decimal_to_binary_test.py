from deci2bin import decimal_to_binary

def test_num():
    out = decimal_to_binary(0)
    assert out == "0"

    out = decimal_to_binary(1)
    assert out == "1"

    out = decimal_to_binary(2)
    assert out == "10"

    out = decimal_to_binary(3)
    assert out == "11"
