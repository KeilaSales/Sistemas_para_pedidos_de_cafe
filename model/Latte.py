from .Cafe import Cafe 
from datetime import datetime

class Latte(Cafe):
    
    def __init__(self, tamanho="medio", intensidade="normal", grao="fino", acucar="cristal"): 
        
        tamanho_padrao = tamanho.lower()
        
        if (tamanho_padrao == 'pequeno'):
            preco = 6.50
            gramas = 18
        elif (tamanho_padrao == 'medio' or tamanho_padrao == 'médio'):
            preco = 8.50
            gramas = 22
        elif (tamanho_padrao == 'grande'):
            preco = 11.00
            gramas = 28
        else:
            raise ValueError('Tamanho inválido. Use pequeno, médio ou grande')
            
        super().__init__(
            nome="Latte", 
            preco=preco, 
            tamanho=tamanho,
            intensidade=intensidade,
            gramas=gramas 
        )

        self.grao = grao
        self.acucar = acucar
       
        self._leite_vaporizado = "sim" 

    
    @property
    def grao(self):
        return self.__grao
    
    @grao.setter
    def grao(self, tipo_grao):
        tipos_validos = ["extra-fino", "fino", "medio"]
        if tipo_grao:
            tipo_grao_padrao = tipo_grao.lower()
            if tipo_grao_padrao not in tipos_validos:
                raise ValueError("Tipo de grão inválido. Use: extra-fino, fino ou medio.")
            self.__grao = tipo_grao_padrao
        else:
            self.__grao = None

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

    @property
    def leite_vaporizado(self):
        return self._leite_vaporizado



    def calcular_preco(self):
        """
        Implementa o método abstrato. Retorna APENAS o preço base, 
        confiando que o Padrão Decorator fará a soma dos adicionais.
        """
        return self.preco 

    def preparar(self):

        print(f"\n--- Preparo Base: {self.nome} ({self.tamanho}) ---")
        
        print(f"- Extraindo base de café ({self.gramas}g).")
        if self.leite_vaporizado == "sim":
            print("- Adicionando e vaporizando leite para criar espuma.")
        
        print(f"- Servido com {self.acucar}.")
        
        self.registrar_preparo()
        print(f"Preparo finalizado às {self.hora_preparo}!")


    def descricao_detalhada(self):

        desc = f"Latte {self.tamanho} ({self.intensidade}). Base de café, Leite Vaporizado: Sim, Açúcar: {self.acucar}."
        
        return desc