from .Cafe import Cafe 
from datetime import datetime

class Moccacino(Cafe):
    
    def __init__(self, tamanho="medio", intensidade="forte", leite_vaporizado="sim", chocolate="sim"): 
        
        # Define preco e gramas baseados no tamanho
        tamanho_padrao = tamanho.lower()
        
        if (tamanho_padrao == 'pequeno'):
            preco = 8.50
            gramas = 16  
        elif (tamanho_padrao == 'medio' or tamanho_padrao == 'médio'):
            preco = 11.00
            gramas = 20
        elif (tamanho_padrao == 'grande'):
            preco = 14.00
            gramas = 25
        else:
            raise ValueError('Tamanho inválido. Use pequeno, médio ou grande')
            
        super().__init__(
            nome="Moccacino", 
            preco=preco, 
            tamanho=tamanho,
            intensidade=intensidade,
            gramas=gramas 
        )
        
        self._leite_vaporizado = "sim"
        self._chocolate = "sim"

    
    @property
    def leite_vaporizado(self):
        return self._leite_vaporizado

    @property
    def chocolate(self):
        return self._chocolate
    
    # NOTA: Setters de validação para leite_vaporizado e chocolate seriam necessários aqui,
    # mas foram omitidos para focar na estrutura de Moccacino.

    # --- MÉTODOS ABSTRATOS IMPLEMENTADOS ---

    def calcular_preco(self):
       
      return self.preco
    
    def preparar(self):

        print(f"\n--- Preparo Base: {self.nome} ({self.tamanho}) ---")
        
        print(f"- Extraindo base de café.")
        
        # Ingredientes essenciais do Moccacino
        if self.chocolate == "sim":
            print("- Adicionando calda de chocolate.")
        if self.leite_vaporizado == "sim":
            print("- Adicionando e vaporizando leite.")
            
        # 2. Chama o registrador e finaliza
        self.registrar_preparo() 
        print(f"Preparo finalizado às {self.hora_preparo}!")


    def descricao_detalhada(self):
        #Implementa o método abstrato: Retorna uma string detalhada do café.
        desc = f"Moccacino {self.tamanho} ({self.intensidade}). Contém leite vaporizado: {self.leite_vaporizado}, chocolate: {self.chocolate}."
        
        return desc