from model.Cafe import Cafe
from model.MaquinaCafe import MaquinaCafe
from model.CafeFactory import CafeFactory
from model.Expresso import Expresso
from model.Capuccino import Capuccino
from model.Adicionais import Chocolate, Chantilly, CremeDeAvela, LeiteEmPo, Canela
from datetime import datetime

# --- Teste ---

# 1. Cria o café expresso. Apenas tamanho, intensidade, grão e açúcar são necessários,
# pois o preço e as gramas são calculados automaticamente com base no tamanho.

Maquina = MaquinaCafe()


print("=== CAFÉ EXPRESSO (chocolate e chantilly)===")
cafe_expresso = CafeFactory.criar_cafe(
    tipo="expresso",
    tamanho="pequeno",
    intensidade="forte",
)

# 2. Demonstração do Padrão Decorator (Composição em cascata)
# Adicionando Chocolate ao café base
cafe_decorado = Chocolate(cafe_expresso)
# Adicionando Chantilly ao café já decorado
cafe_final = Chantilly(cafe_decorado)


# --- Demonstração do Fluxo ---

# Exibe a descrição formatada usando o método __str__ da classe base
print(cafe_final) 
# Exibe a descrição detalhada e o preço final
print(f"Preço Calculado: R$ {cafe_final.preco:.2f}")
print(f"Descrição Detalhada: {cafe_final.descricao_detalhada()}") # Chama o método de acúmulo de string

print("\n=== Preparando ===")
# Prepara o café (Executa a lógica de preparo de todos os Decorators)
# O método preparar() geralmente não retorna nada (None)
Maquina.preparar_pedido(cafe_final)
# A linha abaixo deve ser 'print(None)' se o preparar não retornar nada
# Por isso, é melhor omitir o print(resultado) e focar na saída do próprio preparar
# print(resultado) 

# Exibindo o objeto novamente para ver a hora de preparo
print("\n=== Finalizado ===")
print(cafe_final)
print(f"Hora de Preparo Registrada: {cafe_final.hora_preparo}")


print("\n=== CAPUCCINO (com creme de avelã)===")

# 1. Cria o Capuccino (Base: R$ 9.50. Ingredientes internos fixos: leite vaporizado e pó)
capuccino = CafeFactory.criar_cafe(
    tipo="capuccino",
    tamanho="medio",
    intensidade="normal"
)

# 2. Demonstração do Padrão Decorator (Composição)
# Adicionando Creme de Avelã (Total: R$ 9.50 + R$ 3.50 = R$ 13.00)
capuccino_final = CremeDeAvela(capuccino)

# --- Demonstração do Fluxo ---

# A descrição deve mostrar os ingredientes fixos e o adicional.
print(capuccino_final) 
# Preço Calculado: R$ 13.00
print(f"Preço Calculado: R$ {capuccino_final.preco:.2f}")
print(f"Descrição Detalhada: {capuccino_final.descricao_detalhada()}")


print("\n=== Preparando ===")
# Prepara o Capuccino (Executa a lógica de Capuccino + Decorator)
Maquina.preparar_pedido(capuccino_final)

# Exibindo o objeto novamente para ver a hora de preparo
print("\n=== Finalizado ===")
print(capuccino_final)
print(f"Hora de Preparo Registrada: {capuccino_final.hora_preparo}")


print("\n=== TESTE FINAL: Validação do Singleton ===")

# 1. Tenta obter a instância da máquina novamente (deve ser a mesma MAQUINA)
maquina_duplicada = MaquinaCafe()

print(f"\nID da Máquina original (MAQUINA): {id(Maquina)}")
print(f"ID da Máquina duplicada: {id(maquina_duplicada)}")

if Maquina is maquina_duplicada:
    print("Sucesso: Ambas as referências apontam para o mesmo objeto Singleton!")
else:
    print("Falha: O Padrão Singleton não está funcionando.")

# 2. Verifica se o registro de pedidos da Máquina Única contém 2 itens
print(f"\nRegistro de Preparos (2 itens esperados):")
for item in Maquina.registro_preparos:
    print(f"- {item['nome']} preparado às {item['hora']}")
