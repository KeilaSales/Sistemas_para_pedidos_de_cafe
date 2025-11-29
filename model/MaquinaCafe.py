class MaquinaCafe:
    
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Garante que apenas a primeira chamada cria a instância.
        """
        if cls._instance is None:
            # Se for a primeira vez, cria a instância original
            cls._instance = super(MaquinaCafe, cls).__new__(cls)
            print("Máquina de Café: Inicializando a ÚNICA instância.")
        
        # Em todas as chamadas, retorna a mesma instância
        return cls._instance

    def __init__(self):
        # Proteção para o __init__ não rodar múltiplas vezes
        if hasattr(self, '_inicializado'):
            return
        self._inicializado = True
        self.registro_preparos = []
        
    def preparar_pedido(self, cafe):
        """
        Recebe o objeto Cafe (que já está decorado com adicionais)
        e inicia o preparo.
        """
        print(f"\n[Máquina de Café Única] Preparando pedido: {cafe.nome}...")
        
        # A Máquina delega a lógica específica de preparo ao próprio objeto Cafe
        cafe.preparar() 
        
        self.registro_preparos.append({
            "nome": cafe.nome, 
            "hora": cafe.hora_preparo,
            "descricao": cafe.descricao_detalhada()
        })
        
        print(f"[Máquina de Café Única] Preparo concluído e registrado.")
        return cafe