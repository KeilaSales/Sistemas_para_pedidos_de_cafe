from abc import ABC, abstractmethod
from datetime import datetime

class Cafe(ABC):

    """
    Classe abstrata base para todos os cafés.
    Define estrutura e obriga as subclasses a implementarem descrição e preço.
    """

    def __init__(self, nome, preco_inicial, tamanho, intensidade):
        # É o método construtor da classe. Ele é chamado automaticamente quando você cria uma nova instância (objeto) da classe.
        self.nome = nome
        self.preco_inicial = preco_inicial
        self.__tamanho = tamanho.lower()
        self.__intensidade = intensidade.lower()
        self.__hora_preparo = None 

    @property
    def tamanho(self):
        # Getter: Retorna o valor do atributo "privado"
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, novo_tamanho):
        tamanho_padrao = novo_tamanho.lower()
        tamanhos_validos = ["pequeno", "medio", "médio", "grande"]

        if tamanho_padrao not in tamanhos_validos:
            raise ValueError("Tamanho inválido. Use: pequeno, médio ou grande.")
        # Setter: Aplica a lógica (aqui, garantir minúsculas) antes de atribuir ao "privado"
        self.__tamanho = tamanho_padrao

    @property
    def intensidade(self):
        return self.__intensidade
    
    @intensidade.setter
    def intensidade(self, nova_intensidade):
        #Verifica se a intensidade informada é válida.
        intensidade_padrao = nova_intensidade.lower()

        intensidades_validas = ["suave", "normal", "forte"]
        if intensidade_padrao not in intensidades_validas:
            raise ValueError("Intensidade inválida. Use: suave, normal ou forte.")
        
        self.__intensidade = intensidade_padrao

    @property
    def hora_preparo(self):
        # Adiciona lógica (por exemplo, retorna uma mensagem se ainda não foi setado)
        if self.__hora_preparo is None:
            return "O café ainda não foi preparado."
        return self.__hora_preparo
    
    @hora_preparo.setter
    def hora_preparo(self, momento: datetime):
        # Lógica de validação pode ir aqui (ex: se é um objeto datetime)
        self.__hora_preparo = momento
        
    @abstractmethod
    def descricao(self):
        # A subclasse DEVE implementar 
        pass

    @abstractmethod
    def preco_final(self):
        # A subclasse DEVE implementar
        pass

    @abstractmethod
    def gramas(self):
        pass