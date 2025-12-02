# Sistemas_para_pedidos_de_cafe

Este projeto demonstra, de forma organizada e funcional, a aplicação de Pilares da Programação Orientada a Objetos e Padrões de Design Estruturais e Criacionais em um sistema de pedidos de café.

- Objetivo do Sistema
O sistema permite criar e processar pedidos de café, aplicando regras de negócio e adicionais dinâmicos (como Chocolate e Chantilly).

Funcionalidades principais

* Criação de diferentes tipos de café (Expresso, Capuccino, Latte, Gourmet, etc.).
* Cálculo de preço e gramas baseados no tamanho (Lógica Condicional).
* Adição dinâmica de ingredientes e custos utilizando o Padrão Decorator.
* Processamento centralizado de todos os pedidos por uma única máquina (Singleton).

- Pilares de POO 

Abstração: A classe Cafe é abstrata, definindo o conceito e o contrato fundamental que todo café deve seguir (ex: métodos preparar(), calcular_preco()).

Encapsulamento: Atributos internos (como __tamanho, _leite_vaporizado) são protegidos e acessados via Getters (@property) e Setters para garantir a validação (ex: tamanho válido, preço positivo).

Herança: Utilizada para a especialização: Expresso, Capuccino, e outros, herdam de Cafe e da base do Decorator (CafeDecorator).

Polimorfismo: Os objetos são tratados uniformemente (como um Cafe), mas cada um executa sua própria lógica especializada (ex: Expresso.preparar() vs. Capuccino.preparar()).