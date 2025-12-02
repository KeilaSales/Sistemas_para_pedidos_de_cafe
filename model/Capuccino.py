from .Cafe import Cafe
from datetime import datetime

class Capuccino(Cafe):
    
    def __init__(self, tamanho="medio", intensidade="forte", leite_vaporizado="sim", leite_em_po="não"):
        
        tamanho_padrao = tamanho.lower()
        
        if (tamanho_padrao == 'pequeno'):
             preco = 7.00
             gramas = 14
        elif (tamanho_padrao == 'medio' or tamanho_padrao == 'médio'):
             preco = 9.50
             gramas = 18
        elif (tamanho_padrao == 'grande'):
             preco = 12.00
             gramas = 22
        else:
             raise ValueError('Tamanho inválido. Use pequeno, médio ou grande')
             
        super().__init__(
            nome="Capuccino", 
            preco=preco, 
            tamanho=tamanho,
            intensidade=intensidade,
            gramas=gramas 
        )
        
        # 3. Inicializa os novos atributos específicos do Capuccino
        # Usamos os setters para aplicar formatação/validação
        self._leite_vaporizado = "sim"
        self._leite_em_po = "sim"

    # --- Propriedades e Setters para Leite Vaporizado ---
    
    @property
    def leite_vaporizado(self):
        # O Getter agora lê o atributo interno que foi criado acima.
        return self._leite_vaporizado

    @property
    def leite_em_po(self):
        return self._leite_em_po

    # --- MÉTODOS ABSTRATOS IMPLEMENTADOS ---

    def calcular_preco(self):
       
      return self.preco

    def preparar(self):
        """Implementa o método abstrato 'preparar' com nova lógica de ingredientes."""
        print(f"\n--- Preparo Base: {self.nome} ({self.tamanho}) ---")
        
        # Lógica de preparo do Capuccino
        print(f"- Extraindo base de café ({self.gramas}g).")
        
        if self.leite_vaporizado == "sim":
            print("- Adicionando e vaporizando leite.")
        
        if self.leite_em_po == "sim":
            print("- Polvilhando leite em pó.")

        self.registrar_preparo()
        print(f"Preparo finalizado às {self.hora_preparo}!")

    def descricao_detalhada(self):

        desc = f"Capuccino {self.tamanho} ({self.intensidade}). Base de café, leite vaporizado: {self.leite_vaporizado}, leite em pó: {self.leite_em_po}."
        
        return desc