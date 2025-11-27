from abc import ABC, abstractmethod
from datetime import datetime

class Cafe(ABC):

    """
    Classe abstrata base para todos os cafés.
    Define estrutura e obriga as subclasses a implementarem descrição e preço.
    """

    def __init__(self, nome, preco, tamanho, intensidade, gramas):
        self.nome = nome
        self.preco = preco
        self.tamanho = tamanho.lower()
        self.intensidade = intensidade.lower()
        self.gramas = gramas
        self.hora_preparo = None 

    