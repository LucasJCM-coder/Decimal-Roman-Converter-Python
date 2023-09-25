from src.main import roman_to_number


def test_receive_i_return_1():
    assert roman_to_number('I') == 1


def test_receive_iii_return_3():
    assert roman_to_number('III') == 3


def test_receive_iv_return_4():
    assert roman_to_number('IV') == 4


def test_receive_v_return_5():
    assert roman_to_number('V') == 5


def test_receive_ix_return_9():
    assert roman_to_number('IX') == 9


def test_receive_x_return_10():
    assert roman_to_number('X') == 10


def test_receive_xl_return_40():
    assert roman_to_number('XL') == 40


def test_receive_l_return_50():
    assert roman_to_number('L') == 50


def test_receive_xc_return_90():
    assert roman_to_number('XC') == 90


def test_receive_c_return_100():
    assert roman_to_number('C') == 100


def test_receive_cd_return_400():
    assert roman_to_number('CD') == 400


def test_receive_d_return_500():
    assert roman_to_number('D') == 500


def test_receive_cm_return_900():
    assert roman_to_number('CM') == 900


def test_receive_m_return_1000():
    assert roman_to_number('M') == 1000


def test_receive_mmmcmxcix_return_3999():
    assert roman_to_number('MMMCMXCIX') == 3999


