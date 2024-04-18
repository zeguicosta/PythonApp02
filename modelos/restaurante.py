from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    """Representa um restaurante e suas características."""

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        # _ Serve para proteger a variável
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        print('-' * 90)
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    # @property modifica como um atributo é lido
    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '✅' if self._ativo else '❌'
    
    def alterar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    # self neste caso identifica o restaurante que está sendo avaliado
    def receber_nota(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return '-'
        else:
            # Pega todas as avaliações e para cada avaliação, pega somente a nota e soma todas elas
            soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_notas = len(self._avaliacao)
            media = round(soma_notas / quantidade_notas, 1)
            return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do Restaurante {self._nome}\n')
        # A função enumerate é utilizada quando queremos tanto o índice de cada elemento como o seu valor
        # start = 1, determina o inicio do indice da lista como 1
        for i, item in enumerate(self._cardapio, start = 1):
            # Se tem o atributo
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)