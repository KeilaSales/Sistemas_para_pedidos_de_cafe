from .Cafe import Cafe #base Cafe
from datetime import datetime

class Expresso(Cafe):
    
    def __init__(self, tamanho="medio", intensidade="forte",grao = "extra-fino",acucar = "refinado"): 
        tamanho_padrao = tamanho.lower()
        #ajusta o preco conforme o tamanho
        if (tamanho_padrao == 'pequeno'):
             preco = 5
             gramas = 10
        elif (tamanho_padrao == 'medio'):
             preco = 7
             gramas = 13
        elif (tamanho_padrao == 'grande'):
             preco = 9
             gramas = 15
        else:
             raise ValueError('Tamanho inválido. Use pequeno, médio ou grande')
            
        # nome, preco, tamanho, intensidade, gramas
        super().__init__(
            nome="Café Expresso", 
            preco= preco, 
            tamanho= tamanho,
            intensidade=intensidade,
            gramas= gramas
        )
        self.__grao = grao
        self.__acucar = acucar

    #setter de "grao"
    @property
    def grao(self):
            return self.__grao
    
    @grao.setter
    def grao(self, tipo_grao):
        # exemplo de validação do grao
        tipos_validos = ["extra-fino", "fino", "medio"]

        if tipo_grao:
            tipo_grao_padrao = tipo_grao.lower()
            if tipo_grao_padrao not in tipos_validos:
               raise ValueError("Tipo de grão inválido. Use: extra-fino, fino ou medio.")
           
        if tipo_grao:
        #se o tipo grao for falso
            self.__grao = tipo_grao_padrao
        else:
            self.__grao = None


#setter de "acucar"
    @property
    def acucar(self):
        return self.__acucar
    
    @acucar.setter
    def acucar(self, tipo_acucar):
        tipos_validos = ["refinado", "cristal", "mascavo"]
        
        if tipo_acucar:
            tipo_acucar_padrao = tipo_acucar.lower()
            if tipo_acucar_padrao not in tipos_validos:
                 raise ValueError("Tipo de açúcar inválido.")
            
            self.__acucar = tipo_acucar_padrao
        else:
            self.__acucar = None

    def calcular_preco(self):
       
      return self.preco


    def preparar(self):
       """Implementa o método abstrato 'preparar'."""
       print(f"\n--- Preparo Base: {self.nome} ({self.tamanho}) ---")
       print(f"- Extraindo {self.gramas}g de café {self.grao}.")
    
       # Chama o registrador e imprime a descrição final (limpeza)
       self.registrar_preparo() 
       print(f"Preparo finalizado às {self.hora_preparo}!")


    def descricao_detalhada(self):
       
       desc = f"Expresso {self.tamanho} ({self.intensidade}) com {self.gramas}g de café {self.grao} e açucar {self.acucar}"
       
       return desc


