from .Cafe import Cafe 
from datetime import datetime

class Gourmet(Cafe):
    
    def __init__(self, tamanho="medio", intensidade="forte", grao="extra-fino", acucar="mascavo"): 
        
        tamanho_padrao = tamanho.lower()
        
        if (tamanho_padrao == 'pequeno'):
            preco = 8.00
            gramas = 14
        elif (tamanho_padrao == 'medio' or tamanho_padrao == 'médio'):
            preco = 12.00
            gramas = 20
        elif (tamanho_padrao == 'grande'):
            preco = 16.00
            gramas = 26
        else:
            raise ValueError('Tamanho inválido. Use pequeno, médio ou grande')

        super().__init__(
            nome="Gourmet", 
            preco=preco, 
            tamanho=tamanho,
            intensidade=intensidade,
            gramas=gramas 
        )

        self.grao = grao
        self.acucar = acucar

        self._leite_vaporizado = "sim" 
        self._leite_em_po = "sim"

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

    @property
    def leite_em_po(self):
        return self._leite_em_po

    def calcular_preco(self):
        return self.preco 

    def preparar(self):

        print(f"\n--- Preparo Base: {self.nome} ({self.tamanho}) ---")
        
        print(f"- Extraindo base de café ({self.grao} - {self.gramas}g).")
        
        if self.leite_vaporizado == "sim":
            print("- Adicionando leite e vaporizando para uma textura cremosa.")
        
        if self.leite_em_po == "sim":
            print("- Polvilhando leite em pó, essencial para o toque Gourmet.")
        
        print(f"- Servido com {self.acucar} mascavo.")
        
        self.registrar_preparo()
        print(f"Preparo finalizado às {self.hora_preparo}!")


    def descricao_detalhada(self):
        desc = f"Gourmet {self.tamanho} ({self.intensidade}). Base: Café {self.grao}, Açúcar {self.acucar}, c/ Leite Vaporizado e Leite em Pó."
        
        return desc