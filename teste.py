from model.Cafe import Cafe
from model.MaquinaCafe import MaquinaCafe
from model.CafeFactory import CafeFactory
from model.Expresso import Expresso
from model.Capuccino import Capuccino
from model.Adicionais import Chocolate, Chantilly, CremeDeAvela, LeiteEmPo, Canela
from datetime import datetime

# --- INICIALIZAÇÃO E FLUXO ---

# 1. PASSO: INICIALIZA O CENTRO DE TUDO (SINGLETON)

# Garante que apenas uma instância da Máquina de Café exista.
Maquina = MaquinaCafe()

# TESTE 1:
print("\n----------------------------------------------------------\n")
print("\n=== CAFÉ EXPRESSO (chocolate e chantilly)===\n")

# 2. CRIAÇÃO: Pedido à FACTORY
# A Factory cria a instância 'Expresso' com a lógica de preço/gramas.
cafe_expresso = CafeFactory.criar_cafe(
    tipo="expresso",
    tamanho="pequeno",
    intensidade="forte",
)

#  3. DECORATOR: (Composição em cascata)
# O objeto base 'cafe_expresso' é envelopado (decorado) sequencialmente.
# Adicionando Chocolate ao café base
cafe_decorado = Chocolate(cafe_expresso)
# Adicionando Chantilly ao café já decorado
cafe_final = Chantilly(cafe_decorado)

# --- PREPARO: INÍCIO ---
print("=== Preparando ===")
# 4. EXECUÇÃO SINGLETON: A m,aquina inicia o processo central
# Chama Maquina.preparar_pedido(), que chama cafe_final.preparar().
# O fluxo de execução desce pela cascata Decorator.
# Prepara o café (Executa a lógica de preparo de todos os Decorators)
Maquina.preparar_pedido(cafe_final)

# --- PREPARO: FIM ---

print("=== Finalizado ===")
# O __str__ do Decorator final (Chantilly) é chamado, mostrando a descrição acumulada.
print(cafe_final)
print(f"Hora de Preparo Registrada: {cafe_final.hora_preparo}")


print("\n----------------------------------------------------------\n")
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


print("\n----------------------------------------------------------\n")
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


print("\n----------------------------------------------------------\n")
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


print("\n----------------------------------------------------------\n")
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


print("\n----------------------------------------------------------\n")
print("\n=== TESTE FINAL: Validação do Singleton ===\n")

# 
# 5. VALIDAÇÃO SINGLETON: Tenta obter a instância da máquina novamente (deve ser a mesma MAQUINA)
maquina_duplicada = MaquinaCafe()

print(f"\nID da Máquina original (MAQUINA): {id(Maquina)}")
print(f"ID da Máquina duplicada: {id(maquina_duplicada)}")

if Maquina is maquina_duplicada:
    print("Sucesso: Ambas as referências apontam para o mesmo objeto Singleton!")
else:
    print("Falha: O Padrão Singleton não está funcionando.")

# 6. VALIDAÇÃO DO REGISTRO DE PREPAROS
# Confirma se a Máquina Única registrou todos os 5 pedidos.
print(f"\nRegistro de Preparos:")
for item in Maquina.registro_preparos:
    print(f"- {item['nome']} preparado às {item['hora']}")
