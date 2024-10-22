import random
from typing import List
import sys


def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def primes(count: int) -> List[int]:
    primes_list = []
    number = 2
    while len(primes_list) < count:
        if is_prime(number):
            primes_list.append(number)
        number += 1
    return primes_list


def checksum(x: List[int]) -> int:
    control_value = 0
    for i in x:
        control_value += i
        control_value *= 113

    control_value %= 10000007
    return int(control_value)


# def pipeline(count_num: int, seed_num: int) -> int:
def pipeline() -> int:
    print("Введите количество простых чисел")
    count_num = int(sys.stdin.read().strip())
    print("\nВведите seed")
    seed_num = int(sys.stdin.read().strip())
    print()
    primes_list = primes(count_num)
    random.seed(seed_num)
    random.shuffle(primes_list)
    print("Список простых чисел:")
    for nums in primes_list:
        print(nums)
    print()
    return checksum(primes_list)


if __name__ == "__main__":
    result = pipeline()
    print(f"Контрольная сумма: {result}")
