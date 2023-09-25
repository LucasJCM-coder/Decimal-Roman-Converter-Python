from src.main import number_to_roman


def test_receive_1_return_i():
    assert number_to_roman(1) == 'I'


def test_receive_3_return_iii():
    assert number_to_roman(3) == 'III'


def test_receive_4_return_iv():
    assert number_to_roman(4) == 'IV'


def test_receive_5_return_v():
    assert number_to_roman(5) == 'V'


def test_receive_9_return_ix():
    assert number_to_roman(9) == 'IX'


def test_receive_10_return_x():
    assert number_to_roman(10) == 'X'


def test_receive_40_return_xl():
    assert number_to_roman(40) == 'XL'


def test_receive_50_return_l():
    assert number_to_roman(50) == 'L'


def test_receive_90_return_xc():
    assert number_to_roman(90) == 'XC'


def test_receive_100_return_c():
    assert number_to_roman(100) == 'C'


def test_receive_400_return_cd():
    assert number_to_roman(400) == 'CD'


def test_receive_500_return_d():
    assert number_to_roman(500) == 'D'


def test_receive_900_return_cm():
    assert number_to_roman(900) == 'CM'


def test_receive_1000_return_m():
    assert number_to_roman(1000) == 'M'


def test_receive_3999_return_mmmcmxcix():
    assert number_to_roman(3999) == 'MMMCMXCIX'
