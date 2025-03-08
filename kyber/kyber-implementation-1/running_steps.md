# Kyber_Py - Post-Quantum Cryptography Implementation

Kyber_Py is an implementation of the ML-KEM (Kyber Key Encapsulation Mechanism), a post-quantum cryptographic algorithm. This application enables users to generate key pairs, encapsulate shared secrets, and decapsulate ciphertexts securely.

## Usage Instructions

### Security Levels

The application supports three security levels:  
- `512` (Kyber-512) – Standard security  
- `768` (Kyber-768) – Medium security  
- `1024` (Kyber-1024) – High security  

You can specify the desired level using the `--level` parameter.

---

### Generating Key Pairs

To generate a key pair using **ML-KEM**, specify the security level (`512`, `768`, or `1024`):

```sh
python main.py keygen --mode ml-kem --level <level>
```

For example, to generate keys at the 512-bit security level:

```sh
python main.py keygen --mode ml-kem --level 512
```

This command will output:

```
Keys generated and saved: public_key.bin, private_key.bin
```

It creates the following files:
- `public_key.bin` – The public key used for encryption.
- `private_key.bin` – The private key used for decryption.

---

### Encapsulation (Encrypting a Shared Secret)

To encapsulate a shared secret and generate a ciphertext:

```sh
python main.py encaps --mode ml-kem --level <level>
```

Example for 512-bit security:

```sh
python main.py encaps --mode ml-kem --level 512
```

Output:

```
Shared secret and ciphertext saved: shared_secret.bin, ciphertext.bin
```

This command generates:
- `shared_secret.bin` – The encapsulated shared secret.
- `ciphertext.bin` – The ciphertext containing the encrypted shared secret.

---

### Decapsulation (Decrypting the Shared Secret)

To decrypt the ciphertext and retrieve the shared secret:

```sh
python main.py decaps --mode ml-kem --level <level>
```

Example for 512-bit security:

```sh
python main.py decaps --mode ml-kem --level 512
```

Output:

```
Decrypted shared secret saved: decrypted_secret.bin
```

This creates:
- `decrypted_secret.bin` – The decrypted shared secret.

---

### Verifying Decryption

To verify whether the decrypted shared secret matches the original:

```sh
python main.py decaps --verify
```

Output (if successful):

```
Decrypted shared secret saved: decrypted_secret.bin
Decapsulation successful: Secrets match!
```

This ensures that the decryption process was successful and that the original shared secret has been correctly recovered.

---

## Notes

- Supported security levels: `512`, `768`, and `1024`.
- Ensure all dependencies are installed before running the application.
- Always execute the commands from the project's root directory.
- Keep private keys secure and do not share them to maintain security.

