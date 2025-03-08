import argparse
import os
from kyber_py.src.kyber_py.ml_kem import ML_KEM_512, ML_KEM_768, ML_KEM_1024
from kyber_py.src.kyber_py.kyber import Kyber512, Kyber768, Kyber1024


class KyberApp:
    def __init__(self, mode="ml-kem", level=512):
        """
        Initialize the application with a chosen mode and security level.
        """
        self.mode = mode.lower()
        self.level = level
        self.scheme = self.get_scheme()

    def get_scheme(self):
        """
        Get the correct key encapsulation mechanism based on user selection.
        """
        if self.mode == "ml-kem":
            if self.level == 512:
                return ML_KEM_512
            elif self.level == 768:
                return ML_KEM_768
            elif self.level == 1024:
                return ML_KEM_1024
        elif self.mode == "kyber":
            if self.level == 512:
                return Kyber512
            elif self.level == 768:
                return Kyber768
            elif self.level == 1024:
                return Kyber1024
        raise ValueError("Invalid mode or security level.")

    def generate_keys(self):
        """
        Generate a public-private key pair.
        """
        ek, dk = self.scheme.keygen()
        self.save_key("public_key.bin", ek)
        self.save_key("private_key.bin", dk)
        print(f" Keys generated and saved: public_key.bin, private_key.bin")

    def encapsulate(self):
        """
        Encapsulate a shared secret using the public key.
        """
        ek = self.load_key("public_key.bin")
        key, ct = self.scheme.encaps(ek)
        self.save_key("ciphertext.bin", ct)
        self.save_key("shared_secret.bin", key)
        print(f" Shared secret and ciphertext saved: shared_secret.bin, ciphertext.bin")

    def decapsulate(self):
        """
        Decapsulate a shared secret using the private key.
        """
        dk = self.load_key("private_key.bin")
        ct = self.load_key("ciphertext.bin")
        key = self.scheme.decaps(dk, ct)
        self.save_key("decrypted_secret.bin", key)
        print(f" Decrypted shared secret saved: decrypted_secret.bin")

    def verify_decapsulation(self):
        """
        Verify if the decrypted shared secret matches the original shared secret.
        """
        try:
            shared_secret = self.load_key("shared_secret.bin")
            decrypted_secret = self.load_key("decrypted_secret.bin")

            if shared_secret == decrypted_secret:
                print(" Decapsulation successful: Secrets match!")
            else:
                print(" Error: Decrypted secret does not match the original shared secret.")
        except FileNotFoundError as e:
            print(f" File missing: {e}")

    @staticmethod
    def save_key(filename, data):
        """
        Save a key to a file.
        """
        with open(filename, "wb") as f:
            f.write(data)

    @staticmethod
    def load_key(filename):
        """
        Load a key from a file.
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} not found.")
        with open(filename, "rb") as f:
            return f.read()


def main():
    parser = argparse.ArgumentParser(description="Kyber ML-KEM Key Encapsulation Application")
    parser.add_argument("action", choices=["keygen", "encaps", "decaps"], help="Action to perform")
    parser.add_argument("--mode", choices=["ml-kem", "kyber"], default="ml-kem", help="Select cryptographic mode")
    parser.add_argument("--level", type=int, choices=[512, 768, 1024], default=512, help="Security level")
    parser.add_argument("--verify", action="store_true", help="Verify if decapsulation is successful")

    args = parser.parse_args()
    
    app = KyberApp(mode=args.mode, level=args.level)

    if args.action == "keygen":
        app.generate_keys()
    elif args.action == "encaps":
        app.encapsulate()
    elif args.action == "decaps":
        app.decapsulate()
        if args.verify:
            app.verify_decapsulation()


if __name__ == "__main__":
    main()
