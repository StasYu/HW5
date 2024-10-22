# task 1 github test process

from src.hw5_yu_stas.python_script import is_prime
from src.hw5_yu_stas.python_script import primes
from src.hw5_yu_stas.python_script import checksum
from src.hw5_yu_stas.python_script import pipeline


def test_functions():
    assert is_prime(13)
    assert primes(3) == [2, 3, 5]
    assert checksum([1, 2, 6, 24]) == 6012369
    assert pipeline() == 7785816


if __name__ == "__main__":
    test_functions()
