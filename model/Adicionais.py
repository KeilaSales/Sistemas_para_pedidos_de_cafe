from .CafeDecorator import CafeDecorator 

class Chocolate(CafeDecorator):

    custo = 2.50
  
    def __init__(self, cafe):
        super().__init__(cafe)

    @property
    def preco(self):
        return self.cafe.preco + self.custo

    def preparar(self):
        super().preparar()

    def descricao_detalhada(self):
    # Pede a descrição do objeto envolvido e anexa sua parte.
       return self.cafe.descricao_detalhada() + " com Chocolate"

class LeiteExtra(CafeDecorator):
    
    custo = 1.00
    
    def __init__(self, cafe):
        super().__init__(cafe)

    @property
    def preco(self):
        return self.cafe.preco + self.custo
    
    def preparar(self):
        super().preparar()
    
    def descricao_detalhada(self):
    # Pede a descrição do objeto envolvido e anexa sua parte.
       return self.cafe.descricao_detalhada() + " com Leite Extra"

class Chantilly(CafeDecorator):
    
    custo = 1.50
    
    def __init__(self, cafe):
        super().__init__(cafe)

    @property
    def preco(self):
        return self.cafe.preco + self.custo
    
    def preparar(self):
        super().preparar()
    
    def descricao_detalhada(self):
    # Pede a descrição do objeto envolvido e anexa sua parte.

       return self.cafe.descricao_detalhada() + " com Chantilly"

class LeiteEmPo(CafeDecorator):
    custo = 1.20
    
    def __init__(self, cafe):
        super().__init__(cafe)

    @property
    def preco(self):
        return self.cafe.preco + self.custo
    
    def preparar(self):
        super().preparar()
    
    def descricao_detalhada(self):
    # Pede a descrição do objeto envolvido e anexa sua parte.
       return self.cafe.descricao_detalhada() + " com Leite em Pó"


class CremeDeAvela(CafeDecorator):
    
    custo = 3.50
    
    def __init__(self, cafe):
        super().__init__(cafe)

    @property
    def preco(self):
        return self.cafe.preco + self.custo
    
    def preparar(self):
        super().preparar()
    
    def descricao_detalhada(self):
    # Pede a descrição do objeto envolvido e anexa sua parte.
       return self.cafe.descricao_detalhada() + " com Creme de Avelã"
    
class Canela(CafeDecorator):

    custo = 0.50
    
    def __init__(self, cafe):
        super().__init__(cafe)

    @property
    def preco(self):
        return self.cafe.preco + self.custo
    
    def preparar(self):
        super().preparar()
    
    def descricao_detalhada(self):
    # Pede a descrição do objeto envolvido e anexa sua parte.
       return self.cafe.descricao_detalhada() + " com Canela"

