from datetime import datetime
from .transactions import Transaction
from utils.crypto import Crypto


class Block:
    """
    Classe responsável por representar um bloco
    """

    def __init__(self, previous_hash: str, transaction: Transaction) -> None:
        self.previous_hash = previous_hash
        self.transaction = transaction
        self.created_at = datetime.now()
        self.hash = self.__generate_hash()

    def __repr__(self) -> str:
        return f'Block Hash: {self.hash}\nTransaction: {self.transaction}'

    def __serialize(self) -> bytes:
        return f'{self.previous_hash}{self.transaction.hash}'.encode()

    def __generate_hash(self) -> str:
        return Crypto.double_sha256(self.__serialize())

    def show_block_info(self) -> None:
        """
        Mostra a transação atual armazenada
        """
        print(f'Block Hash: {self.hash}')
        print(f'Current Transaction: {self.transaction.hash}')
