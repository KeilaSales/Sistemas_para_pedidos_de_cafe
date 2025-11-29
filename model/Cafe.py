from abc import ABC, abstractmethod
from datetime import datetime, time

class Cafe(ABC):

    def __init__(self, nome, preco, tamanho, intensidade, gramas):
        self.nome = nome
        self.preco = preco
        self.tamanho = tamanho.lower()
        self.intensidade = intensidade.lower()
        self.gramas = gramas
        self.hora_preparo = None  # será definido ao preparar 
                                  # então no caso ele vai atualizar quando
                                  # utilizar o método preparar atribui a hr dee agr 

    @property
    def intensidade (self):
        return self.__intensidade 
    
    @intensidade.setter
    def intensidade (self, intensidadee):
        intensidades_validas = ["suave", "normal", "forte"]
        if intensidadee not in intensidades_validas:
            raise ValueError("Intensidade inválida. Use: suave, normal ou forte.")
        self.__intensidade = intensidadee

    @property
    def tamanho (self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho (self, tamanhoo):
        tamanhos_validos = ["pequeno", "medio", "médio", "grande"] # cria um enum 
        if tamanhoo not in tamanhos_validos:
            raise ValueError("Tamanho inválido. Use: pequeno, médio ou grande.")
        self.__tamanho = tamanhoo

    @property
    def preco (self):
        return self.__preco
    
    @preco.setter
    def preco (self, precoo):
        if precoo < 0.00:
            raise ValueError ('Preço deve ser positivo !')
        self.__preco = precoo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome (self, nomee):
        if (nomee == None):
            raise ValueError (f"Nome é um campo obrigatório.")
        self.__nome = nomee.title()

    @property
    def gramas (self):
        return self.__gramas
    
    @gramas.setter
    def gramas (self, gramass):
        if gramass < 0 :
            raise ValueError ("As gramas devem tem um valor positivo !")
        self.__gramas = gramass
        
    @property
    def hora_preparo (self):
        return self.__hora_preparo
    
    @hora_preparo.setter
    def hora_preparo (self, horario):
        self.__hora_preparo = horario
      
###### MÉTODOS ##########

    @abstractmethod
    def preparar(self):
        data_hora = datetime.now()
        hora_agr = data_hora.time()
        self.hora_preparo = hora_agr
        pass
 

     
    def _str_(self):
         #Exibição simples do café.
         return f"{self.nome} - {self.tamanho} - R$ {self.preco:.2f}"
