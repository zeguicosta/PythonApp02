from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    # Todas as classes derivadas precisam obrigatoriamente da aplicação de desconto
    @abstractmethod
    def aplicar_desconto(self):
        pass