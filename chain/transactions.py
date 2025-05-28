from utils.crypto import Crypto


class Transaction:
    """
    Classe responsável por representar cada transação
    """

    def __init__(self, sender: str, receiver: str, amount: int, message: str) -> None:
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.message = message
        self.hash = self.__generate_hash()

    def __serialize(self) -> bytes:
        """
        Serializa as informações em uma estrutura compacta para ser criptografada
        """
        return f'{self.sender}{self.receiver}{self.amount}{self.message}'.encode()

    def __generate_hash(self) -> str:
        """
        Gera o hash
        """
        return Crypto.double_sha256(self.__serialize())
