import hashlib


class Crypto:
    """
    Classe responsável por conter os métodos para criptografia
    """
    @staticmethod
    def double_sha256(data: bytes):
        """
        Gera o hash necessário
        """
        return hashlib.sha256(hashlib.sha256(data).digest()).hexdigest()
