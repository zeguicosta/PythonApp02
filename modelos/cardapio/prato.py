from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        # super() acessa informações de outra classe
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return self._nome