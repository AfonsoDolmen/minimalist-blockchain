from chain.blockchain import Blockchain
from chain.transactions import Transaction

if __name__ == '__main__':
    # Instancia uma nova blockchain
    blockchain = Blockchain()

    # Cria uma nova transação
    tx = Transaction('Afonso', 'SYSTEM', 1, 'Teste')
    blockchain.add_transaction(tx=tx)

    # Imprime na tela todos os blocos presentes na blockchain
    print('-' * 50)
    print(blockchain)
    print('-' * 50)
