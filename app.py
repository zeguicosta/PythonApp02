from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_pizza = Restaurante('Dominos', 'Pizza')
restaurante_sushi = Restaurante('Tokyo Sushi', 'Sushi')
restaurante_mexicano = Restaurante('Taco Loco', 'Mexicano')

bebida_suco = Bebida('Suco de Laranja', 5.0, 'Grande')
prato_pizza = Prato('Pizza de Bacon', 72.0, 'A especialidade da casa')

def main():
    print(bebida_suco)
    print(prato_pizza)

if __name__ == '__main__':
    main()