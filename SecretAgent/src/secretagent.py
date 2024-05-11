# secretagent.py

class SecretAgent:

    _codeword = ""

    def __init__(self, codename: str):

        """
        The initializer method that creates two attributes for the SecretAgent
        class.

        self.codename: the code name of the secret agent
        """
        self.codename = codename
        self._secrets = []  # _secrets: nonpublic


class Message:

    def __init__(self) -> None:
        self.__format = "UTF-8"
