from .transactions import Transaction
from .block import Block


class Blockchain:
    """
    Classe responsável por representar a blockchain
    """

    def __init__(self):
        self.blocks = []
        self.__generate_genesis()

    def __repr__(self) -> str:
        chain_data = ""

        for block in self.blocks:
            chain_data += f'\nBlock Hash: {block.hash}\n'
            chain_data += f'Previous Hash: {block.previous_hash}\n'
            chain_data += f'Created At: {block.created_at}\n'
            chain_data += f'Transaction: {block.transaction.sender} -> {block.transaction.receiver} | Amount: {block.transaction.amount} | Message: {block.transaction.message}\n'
            chain_data += '-'*50 + '\n'

        return chain_data

    def __generate_genesis(self) -> None:
        """
        Gera o bloco gênesis
        """
        genesis_transaction = Transaction(
            'Afonso', 'Teste', 10, 'I am the first')
        genesis_block = Block(None, genesis_transaction)

        self.blocks.append(genesis_block)

    def add_transaction(self, tx: Transaction) -> None:
        """
        Adiciona uma nova transação ao blockchain
        """
        # Cria um novo bloco
        block = Block(self.blocks[-1].hash, transaction=tx)

        # Adiciona o bloco a blockchain
        self.blocks.append(block)
