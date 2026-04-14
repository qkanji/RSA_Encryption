# RSA_Encryption

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

A from-scratch, dependency-free Python implementation of the RSA cryptosystem demonstrating asymmetric encryption mechanics, large prime generation, and the computational complexity of integer factorization.

## Architecture & Mechanics

* **Large Prime Generation**: Generates 1024-bit randomized prime coefficients ($p$, $q$) to compute the public modulus ($n$) and totient ($\lambda(n)$), architected to simulate production-scale RSA dimensions.
* **Probabilistic Primality Testing**: Implements the Fermat Primality Test as a heuristic filter to validate candidate primes, bypassing the $O(\sqrt{n})$ time complexity of deterministic bounds for values of high magnitude.
* **Modular Exponentiation**: Utilizes a fast modular exponentiation algorithm (right-to-left binary method) for executing the core one-way trapdoor function during encryption and decryption.
* **Extended Euclidean Algorithm**: Computes the modular multiplicative inverse to derive the private decryption key ($d$) from the public exponent ($e$).
* **Custom Padding Scheme**: Maps ASCII plaintext strings to zero-padded integer arrays to ensure the message constraint $0 \le m < n$ is satisfied prior to transformation.
* **Factorization Attack Simulation**: Features a safe, interactive execution branch that benchmarks a brute-force integer factorization attack against the public modulus $n$, empirically demonstrating the computational bottleneck that underpins RSA security.
* **Sieve of Eratosthenes (`primes.py`)**: Includes an alternative deterministic sequence generator for producing primes up to a bounded limit $n$, used for exact algorithm complexity comparisons.

## Tech Stack

* **Language**: Python 3.x
* **Dependencies**: Standard Library only (`math`, `random`, `time`)

## Motivation & Background

This project originated from a deep curiosity about asymmetric encryption and the mathematical mechanics of one-way functions. It serves as a practical implementation to explore operations like modular exponentiation that are computationally irreversible. By researching the RSA cryptosystem and manually building the encryption, decryption, and key-generation processes from scratch, this repository demonstrates a foundational understanding of cryptographic concepts and algorithm design.

## Local Setup

No external packages are required.

```bash
# Clone the repository
git clone https://github.com/qkanji/RSA_Encryption.git
cd RSA_Encryption

# Run the primary encryption/decryption sequence
python main.py

# Run the deterministic prime sieve
python primes.py
```