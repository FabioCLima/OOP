# user.py

import hashlib
import os


class User:
    """Represents a user with a username and password."""

    def __init__(self, username: str, password: str) -> None:
        """
        Initializes a User object with the given username and password.

        Args:
            username (str): The username of the user.
            password (str): The plaintext password of the user.
        """
        self.username = username
        self.password = password

    @property
    def password(self):
        """
        Getter method for the password property.

        Raises:
            AttributeError: Password is write-only.
        """
        raise AttributeError("Password is write-only.")

    @password.setter
    def password(self, plaintext: str) -> None:

        """
        Setter method for the password property.

        Hashes the plaintext password using PBKDF2-HMAC-SHA256 and stores the
        hashed password securely.

        Args:
            plaintext (str): The plaintext password to be hashed and stored
            securely.
        """
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(
            "sha256", plaintext.encode("utf-8"), salt, 100_000
        )
