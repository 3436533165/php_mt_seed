#!/usr/bin/env python3
# php_mt_seed - PHP mt_rand() seed cracker

def php_mt_rand(seed, n):
    mt = [0] * 624
    mt[0] = seed & 0xFFFFFFFF
    for i in range(1, 624):
        mt[i] = (1812433253 * (mt[i-1] ^ (mt[i-1] >> 30)) + i) & 0xFFFFFFFF

    for _ in range(n):
        for i in range(624):
            y = (mt[i] & 0x80000000) + (mt[(i+1) % 624] & 0x7FFFFFFF)
            mt[i] = mt[(i+397) % 624] ^ (y >> 1)
            if y & 1:
                mt[i] ^= 0x9908B0DF
        y = mt[623]
        y ^= y >> 11
        y ^= (y << 7) & 0x9D2C5680
        y ^= (y << 15) & 0xEFC60000
        y ^= y >> 18
    return y

def crack(hint):
    print(f"Cracking seed for value: {hint}")
    for seed in range(0, 0xFFFFFFFF + 1):
        if php_mt_rand(seed, 1) == hint:
            second = php_mt_rand(seed, 2)
            print(f"Seed found: {seed}")
            print(f"Next mt_rand() value: {second}")
            return seed, second
    print("Seed not found")
    return None, None

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <mt_rand_output>")
        print(f"Example: python {sys.argv[0]} 1219893521")
        sys.exit(1)
    hint = int(sys.argv[1])
    crack(hint)
