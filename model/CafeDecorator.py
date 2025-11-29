from .Cafe import Cafe

class CafeDecorator(Cafe):
    
    #Classe base para todos os adicionais (Decorator).
    #Recebe um café e adiciona comportamento sem alterar a classe original.
   

    def __init__(self, cafe):
        self.cafe = cafe  # composição (decorando o café original)

    @property
    def nome(self):
        return self.cafe.nome

    @property
    def preco(self):
        return self.cafe.preco

    @property
    def tamanho(self):
        return self.cafe.tamanho

    @property
    def intensidade(self):
        return self.cafe.intensidade

    @property
    def gramas(self):
        return self.cafe.gramas

    @property
    def hora_preparo(self):
        return self.cafe.hora_preparo

    def preparar(self):
        # Primeiro prepara o café original
        self.cafe.preparar()

    def __str__(self):
        # Repassa a chamada __str__ para o objeto envolvido
        return self.descricao_detalhada()
    
    
    # MÉTODOS ABSTRATOS QUE DEVEM SER REPASSADOS (E DEPOIS SOBRESCRITOS NOS ADICIONAIS)

   # Se Cafe exigir 'calcular_preco':
    def calcular_preco(self):
       return self.cafe.calcular_preco() 

    # Se Cafe exigir 'descricao_detalhada':
    def descricao_detalhada(self):
       return self.cafe.descricao_detalhada()

