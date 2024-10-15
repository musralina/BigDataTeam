import random
import math
from typing import List


# 1
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# 2
def primes(count: int) -> List[int]:
    prime_list = []
    num = 2
    while len(prime_list) < count:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list


# 3
def checksum(x: List[int]) -> int:
    mod_value = 10_000_007
    checksum_value = 0
    for num in x:
        checksum_value = (checksum_value + num) * 113 % mod_value
    return checksum_value


# 4
def pipeline() -> int:
    prime_list = primes(1000)
    random.seed(100)
    random.shuffle(prime_list)
    return checksum(prime_list)


# 5
def main():
    result = pipeline()
    print(f"Checksum: {result:,}")


if __name__ == "__main__":
    main()
