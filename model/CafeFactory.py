from .Expresso import Expresso
from .Capuccino import Capuccino
from .Latte import Latte
from .Moccacino import Moccacino
from .Gourmet import Gourmet

class CafeFactory:
    #    Cria objetos de café com base no tipo escolhido.

   @staticmethod
    
   def criar_cafe(tipo, tamanho="medio", intensidade="normal"):
        tipo = tipo.lower()

        if tipo == "expresso":
            return Expresso(tamanho=tamanho, intensidade=intensidade)
        
        elif tipo == "capuccino":
            return Capuccino(tamanho=tamanho, intensidade=intensidade)
        
        elif tipo == "latte":
            return Latte(tamanho=tamanho, intensidade=intensidade)
        
        elif tipo == "moccacino":
            return Moccacino(tamanho=tamanho, intensidade=intensidade)
        
        elif tipo == "gourmet":
            return Gourmet(tamanho=tamanho, intensidade=intensidade)
        
        else:
            raise ValueError("Tipo de café inválido.")