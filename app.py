from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_pizza = Restaurante('Dominos', 'Pizza')
restaurante_sushi = Restaurante('Tokyo Sushi', 'Sushi')
restaurante_mexicano = Restaurante('Taco Loco', 'Mexicano')

bebida_suco = Bebida('Suco de Laranja', 5.0, 'Grande')
prato_pizza = Prato('Pizza de Bacon', 72.0, 'A especialidade da casa.')

bebida_suco.aplicar_desconto()
prato_pizza.aplicar_desconto()

restaurante_pizza.adicionar_no_cardapio(bebida_suco)
restaurante_pizza.adicionar_no_cardapio(prato_pizza)

def main():
    # Não é necessário o uso dos parênteses ao chamar a função exibir_cardapio por causa 
    # do uso do @property, assim como foi feito em media_avaliacao, por ser uma função que
    # apenas retorna uma string
    restaurante_pizza.exibir_cardapio

if __name__ == '__main__':
    main()