import math
import random
import time

prime = True
asciidict = {i: chr(i) for i in range(128)}
deasciidict = {value: key for key, value in asciidict.items()}


# prime_nums = []


def prime_num_gen(minimum):
    num_to_check = minimum
    global prime
    while True:
        prime = True
        # This uses the Fermat primality test as a probabilistic algorithm to check if a number is prime.
        # See https://en.wikipedia.org/wiki/Fermat_primality_test
        for i in range(5):
            a = random.randrange(2, num_to_check - 1)
            formul = fast_modular_exponentiation(a, num_to_check - 1, num_to_check)
            if formul != 1:
                prime = False
                break
        if prime:
            return num_to_check
        num_to_check += 1


def fast_modular_exponentiation(base, exponent, modulus):
    reversed_binary_string_of_exponent = bin(exponent)[2:][::-1]
    base_exponents = [base]
    current_power_of_two = 2
    while current_power_of_two <= exponent:
        current_power_of_two *= 2
        base_exponents.append((base_exponents[-1] * base_exponents[-1]) % modulus)
    final_mod_values = []
    for i in range(len(reversed_binary_string_of_exponent)):
        if reversed_binary_string_of_exponent[i] == "1":
            final_mod_values.append(base_exponents[i])
    result = 1
    for j in range(len(final_mod_values)):
        result *= final_mod_values[j]
        result = result % modulus
    return result % modulus


def pad(message):
    newm = ""
    for letter in message:
        ans = str(deasciidict[letter])
        ans = ("0" * (3 - len(ans))) + ans
        newm += ans
    return int(newm)


def unpad(message):
    newm = ""
    message = str(message)
    message = ("0" * ((3 - len(message)) % 3)) + message
    new_list = [int(message[x:x + 3]) for x in range(0, len(message), 3)]
    for letter in new_list:
        newm += asciidict[letter]
    return newm


def inverse(a, modulus):
    t = 0
    newt = 1
    r = modulus
    newr = a
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        return "a in not invertible"
    if t < 0:
        t = t + modulus
    return t


def get_min_p_or_q():
    bin_p = "0b1"
    for _ in range(1024):
        bin_p += str(round(random.random()))
    return int(bin_p, 2)


p_min = get_min_p_or_q()
q_min = get_min_p_or_q()

print(f"Minimum value for first prime coefficient is: {p_min}")
print(f"Minimum value for second prime coefficient is: {q_min}")

start = time.time()
p = prime_num_gen(p_min)
q = prime_num_gen(q_min)
n = p * q
tn = math.lcm(p - 1, q - 1)
e = random.randrange(1000, 1000000)
while True:
    e = prime_num_gen(e + 1)
    if tn % e != 0:
        break
d = inverse(e, tn)
final_time = time.time() - start

print(f"First prime coefficient is: {p}")
print(f"Second prime coefficient is {q}")
print(f"Product of first prime coefficient and second prime coefficient is: {n}")
print(f"Lowest common multiple of first prime coefficient minus one and second prime coefficient minus one is: {tn}\n")
print(f"Encryption key is: {e} and decryption key in {d}")
print(f"Time to generate encryption and decryption keys: {round(final_time, 4)} seconds\n")

while True:
    um = input("Enter a message to encrypt (letters and spaces only): ")
    m = pad(um)
    if 0 <= m < n:
        break
    print("Padded message is too long to encrypt try again")

start = time.time()
c = fast_modular_exponentiation(m, e, n)
mid = time.time()
nm = fast_modular_exponentiation(c, d, n)
end = time.time()

unm = unpad(nm)

encrypt_time = mid - start
decrypt_time = end - mid
final_time = end - start
print(f"Unpadded message is: {um}")
print(f"Unpadded decrypted message is: {unm}")
print(f"Padded message is: {m}")
print(f"padded decrypted message is {nm}")
print(f"Ciphertext is: {c}")
print(f"Time to encrypt is: {round(encrypt_time, 4)} seconds")
print(f"Time to decrypt is: {round(decrypt_time, 4)} seconds")
print(f"Time to encrypt and decrypt is: {round(final_time, 4)} seconds\n")

choice = input('Enter "y" to simulate a hack attack, or "n" to quit: ').strip().lower()
if choice != 'y':
    print("Exiting simulator.")
    exit()

print("\n--- Starting Hack Simulation ---")
start = time.time()
pr = prime_num_gen(math.isqrt(n))
opr = pr
while True:
    if n % pr == 0:
        break
    pr = prime_num_gen(pr + 1)
    print(pr - opr)

hacked_p = pr
hacked_q = n // pr
final_time = time.time() - start
print(f"Hacked! First prime coefficient is: {hacked_p} and second prime coefficient is: {hacked_q}")
print(f"Time for hacker to find the two prime coefficients: {round(final_time, 4)} seconds")

start = time.time()
hacked_d = inverse(e, math.lcm(hacked_p - 1, hacked_q - 1))
hacked_m = unpad(fast_modular_exponentiation(c, hacked_d, n))

final_time = time.time() - start

print(
    f"Time to find decryption key and decrypt message when prime coefficients are known by hacker: {round(final_time, 4)} seconds")
print(f"Decryption key found by hacker is: {hacked_d}")
print(f"Ciphertext: {c} is known as it was intercepted by hacker")
print(f"Message decrypted by hacker is: {hacked_m}")
