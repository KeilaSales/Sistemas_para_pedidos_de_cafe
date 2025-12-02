from model.Cafe import Cafe
from model.MaquinaCafe import MaquinaCafe
from model.CafeFactory import CafeFactory
from model.Expresso import Expresso
from model.Capuccino import Capuccino
from model.Adicionais import Chocolate, Chantilly, CremeDeAvela, LeiteEmPo, Canela
from datetime import datetime

# 1. Cria o café expresso. Apenas tamanho, intensidade, grão e açúcar são necessários,
# pois o preço e as gramas são calculados automaticamente com base no tamanho.

Maquina = MaquinaCafe()


print("\n=== CAFÉ EXPRESSO (chocolate e chantilly)===\n")
cafe_expresso = CafeFactory.criar_cafe(
    tipo="expresso",
    tamanho="pequeno",
    intensidade="forte",
)
# Padrão Decorator (Composição em cascata)
# Adicionando Chocolate ao café base
cafe_decorado = Chocolate(cafe_expresso)
# Adicionando Chantilly ao café já decorado
cafe_final = Chantilly(cafe_decorado)

# --- Fluxo ---

print("=== Preparando ===")
# Prepara o café (Executa a lógica de preparo de todos os Decorators)
Maquina.preparar_pedido(cafe_final)
# Exibindo o objeto novamente para ver a hora de preparo
print("=== Finalizado ===")
print(cafe_final)
print(f"Hora de Preparo Registrada: {cafe_final.hora_preparo}")



print("\n=== CAPUCCINO (com creme de avelã)===\n")
capuccino = CafeFactory.criar_cafe(
    tipo="capuccino",
    tamanho="medio",
    intensidade="normal"
)
#Decorator
capuccino_final = CremeDeAvela(capuccino)

print("=== Preparando ===")
# Executa a lógica de Capuccino + Decorator
Maquina.preparar_pedido(capuccino_final)
print("=== Finalizado ===")
print(capuccino_final)
print(f"Hora de Preparo Registrada: {capuccino_final.hora_preparo}")



print("\n=== MOCCACINO (com Canela) ===\n")
moccacino = CafeFactory.criar_cafe(
      tipo="moccacino",
      tamanho="medio",
      intensidade="forte"
)

moccacino_final = Canela(moccacino)

print("=== Preparando ===")
# Usa o Singleton para preparar o Moccacino
Maquina.preparar_pedido(moccacino_final)

print("=== Finalizado ===")
print(moccacino_final)
print(f"Hora de Preparo Registrada: {moccacino_final.hora_preparo}")



print("\n=== LATTE (com Chantilly) ===\n")
latte = CafeFactory.criar_cafe(
    tipo="latte",
    tamanho="medio",
    intensidade="normal"
)

latte_final = Chantilly(latte)

print("=== Preparando ===")

Maquina.preparar_pedido(latte_final)

print("=== Finalizado ===")
print(latte_final)
print(f"Hora de Preparo Registrada: {latte_final.hora_preparo}")



print("\n=== GOURMET (com Creme de Avelã) ===\n")
gourmet = CafeFactory.criar_cafe(
    tipo="gourmet",
    tamanho="medio",
    intensidade="forte"
)

gourmet_final = CremeDeAvela(gourmet)

print("=== Preparando ===")

Maquina.preparar_pedido(gourmet_final)

print("=== Finalizado ===")
print(gourmet_final)
print(f"Hora de Preparo Registrada: {gourmet_final.hora_preparo}")



print("\n=== TESTE FINAL: Validação do Singleton ===\n")

# Tenta obter a instância da máquina novamente (deve ser a mesma MAQUINA)
maquina_duplicada = MaquinaCafe()

print(f"\nID da Máquina original (MAQUINA): {id(Maquina)}")
print(f"ID da Máquina duplicada: {id(maquina_duplicada)}")

if Maquina is maquina_duplicada:
    print("Sucesso: Ambas as referências apontam para o mesmo objeto Singleton!")
else:
    print("Falha: O Padrão Singleton não está funcionando.")

# Verifica se o registro de pedidos da Máquina Única contém 2 itens
print(f"\nRegistro de Preparos:")
for item in Maquina.registro_preparos:
    print(f"- {item['nome']} preparado às {item['hora']}")
