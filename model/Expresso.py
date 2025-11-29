from Cafe import Cafe 

class Expresso(Cafe):

    def __init__(self, tamanho="medio", intensidade="forte"):
        # 1. Lógica para definir o PREÇO BASE com base no tamanho
        preco_base = 0
        tamanho_padrao = tamanho.lower()

        if tamanho_padrao == "pequeno": preco_base = 4.00
        elif tamanho_padrao == "médio" or tamanho_padrao == "medio": preco_base = 5.00
        elif tamanho_padrao == "grande": preco_base = 6.50
        
        super().__init__(
            nome="Café Expresso", 
            preco_inicial=preco_base, 
            tamanho=tamanho,
            intensidade=intensidade
        )

    @property
    def gramas(self):
        tam = self.tamanho
        if tam == "pequeno": return 7
        if tam == "médio" or tam == "medio": return 10
        if tam == "grande": return 14
        return 0
    
    @property
    def preco_final(self):
        preco = self.preco_inicial
        
        # SOMA o preço de todos os objetos adicionais anexados (Decorator)
        for adicional in self.__adicionais:
            preco += adicional.preco_adicional
            
        return preco
    
    @property
    def descricao(self):
        desc = f"Expresso ({self.intensidade}) {self.tamanho} com {self.gramas}g."
        
        # Adiciona a descrição de todos os objetos adicionais
        adicionais_str = ", ".join([a.nome for a in self._adicionais])
        if adicionais_str:
            desc += f" Adicionais: {adicionais_str}."
        
        return desc


    # 6. Método de Preparo
    def preparar(self):
        print(f"\n--- Preparando {self.nome} ---")
        super().preparar() # Chama o método base
        print(f"- Extraindo {self.gramas}g de café intenso.")