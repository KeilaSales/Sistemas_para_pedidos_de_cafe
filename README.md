# Sistemas_para_pedidos_de_cafe

Este projeto demonstra, de forma organizada e funcional, a aplicação de Pilares da Programação Orientada a Objetos e Padrões de Design Estruturais e Criacionais em um sistema de pedidos de café.

. Objetivo do Sistema

O sistema permite criar e processar pedidos de café, aplicando regras de negócio e adicionais dinâmicos (como Chocolate e Chantilly).

 . Funcionalidades principais   

* Criação de diferentes tipos de café (Expresso, Capuccino, Latte, Gourmet, etc.).
* Cálculo de preço e gramas baseados no tamanho (Lógica Condicional).
* Adição dinâmica de ingredientes e custos utilizando o Padrão Decorator.
* Processamento centralizado de todos os pedidos por uma única máquina (Singleton).

. Pilares de POO 

* Abstração: A classe Cafe é abstrata, definindo o conceito e o contrato fundamental que todo café deve seguir (ex: métodos preparar(), calcular_preco()).

* Encapsulamento: Atributos internos (como __tamanho, _leite_vaporizado) são protegidos e acessados via Getters (@property) e Setters para garantir a validação (ex: tamanho válido, preço positivo).

* Herança: Utilizada para a especialização: Expresso, Capuccino, e outros, herdam de Cafe e da base do Decorator (CafeDecorator).

* Polimorfismo: Os objetos são tratados uniformemente (como um Cafe), mas cada um executa sua própria lógica especializada (ex: Expresso.preparar() vs. Capuccino.preparar()).

. Padrões de Projeto 

* Decorator: É um padrão estrutural que permite adicionar responsabilidades (custo e descrição) ao objeto Cafe dinamicamente (composição em cascata), sem alterar as classes base. (CafeDecorator e classes como Chocolate, Chantilly)

* Factory: É um padrão criacional e atua como o guichê de pedidos centralizado, criando o tipo correto de café (Expresso, Latte, etc.) com base no nome e parâmetros. (CafeFactory)

* Singleton: É um padrão criacional que garante que haja apenas uma instância da Máquina de Café em todo o sistema. A Máquina atua como o orquestrador central que inicia o preparo. (MaquinaDeCafe)

. Estrutura de Arquivos e Descrição 

* Cafe.py: 	Superclasse que define a interface base e implementa setters de validação (tamanho, intensidade, preço, etc.).Cafe (Abstrata)

* CafeDecorator.py:	Base do Decorator e implementa o repasse (pass-through) de todos os métodos e atributos para o objeto envolvido (self.cafe). CafeDecorator (Abstrata)

* Expresso.py, Capuccino.py, etc: Implementam o contrato abstrato (preparar(), calcular_preco()) e a lógica condicional de preco/gramas por tamanho. Subclasses de Café

* Adicionais.py: São os Decorators Concretos que herdam de CafeDecorator e adicionam seu custo específico e a descrição ao objeto. Chocolate, Chantilly, Canela, etc.	

* CafeFactory.py: Cria as classes de café (instanciação centralizada). CafeFactory.	

* MaquinaDeCafe.py:	Singleton = Controla o processo de preparar_pedido e o registro de logs. MaquinaDeCafe.

* teste.py: Arquivo principal usado para demonstrar a integração de todos os padrões.

* Diagrama UML:
  
![Diagrama_TOO](https://github.com/user-attachments/assets/af50cc0b-e9bf-499a-8878-79c04a2d6d79)
