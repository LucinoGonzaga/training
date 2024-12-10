# 1. Introdução ao Python

Python foi criado por Guido van Rossum, um programador holandês, no final dos anos 80 e início dos anos 90. A primeira versão do Python, a 0.9.0, foi lançada em 1991. Guido van Rossum nomeou a linguagem em homenagem ao grupo de comédia britânico Monty Python, do qual era um grande fã. 

Python foi projetado com o objetivo de ser uma linguagem fácil de ler e escrever, com uma sintaxe clara e concisa. Ao longo dos anos, evoluiu e ganhou popularidade até se tornar uma das linguagens de programação mais utilizadas no mundo. 

> Características

Python tem várias características que o tornam atraente tanto para iniciantes quanto para programadores experientes: 

- Legibilidade
- Tipagem dinâmica
- Interpretado
- Multiplataforma
- Ampla biblioteca padrão
- Comunidade ativa

> Aplicações

Python é utilizado em uma ampla gama de aplicações e domínios, alguns exemplos são:  
- Desenvolvimento web
- Ciência de dados
- Inteligência artificial e machine learning
- Automatização de tarefas
- Desenvolvimento de jogos

# 1.1. Instalação e configuração
Baixar e instalar Python
Para começar a programar em Python, primeiro você deve baixar e instalar Python no seu computador. Siga estes passos: 

# 1.2. Seu primeiro programa Python

> "Olá Mundo"

É uma tradição no mundo da programação começar com um programa simples chamado "Olá Mundo". Este programa simplesmente mostra a mensagem "Olá Mundo" na tela. 

- Abra seu IDE ou editor de texto preferido e crie um novo arquivo.
- Nomeie o arquivo como "ola_mundo.py". A extensão ".py" indica que é um arquivo de Python. 
- No arquivo, escreva o seguinte código:

    print ("Olá, Mundo!")

- Salve o arquivo e execute o programa. Se estiver utilizando um IDE, procure a opção "Run" ou "Execute". 

Você verá que a mensagem "Olá, Mundo!" é impressa na tela.

> Conceitos básicos da sintaxe em Python

Antes de mergulharmos em conceitos mais avançados, é importante familiarizar-se com alguns aspectos básicos da sintaxe do Python.

- Indentação

No Python, a indentação (espaços ou tabulações no início de uma linha) é utilizada para delimitar blocos de código. Diferente de outras linguagens que utilizam chaves ou palavras-chave, o Python utiliza a indentação para determinar o escopo das declarações. Por exemplo: 

```
if condition:

    # Bloco de código se a condição for verdadeira

    instrucao1
    instrucao2

else:

    # Bloco de código se a condição for falsa

    instrucao3
    instrucao4
```

- Comentários

Os comentários são linhas de texto no código que são ignoradas pelo interpretador do Python. Eles são utilizados para explicar ou documentar o código. No Python, os comentários de uma única linha começam com o símbolo #, enquanto os comentários de várias linhas são delimitados por três aspas """ . Por exemplo:


```
# Este é um comentário de uma única linha

"""
Este é um comentário
de várias linhas
"""
```

- Sensibilidade a maiúsculas e minúsculas
Python distingue entre maiúsculas e minúsculas. Portanto, variável, Variável e VARIÁVEL são consideradas variáveis diferentes.

- Ponto e vírgula

Diferente de outras linguagens, o Python não requer o uso de ponto e vírgula (;) ao final de cada instrução. No entanto, se você desejar escrever várias instruções em uma única linha, pode separá-las com um ponto e vírgula. Por exemplo:

    instrucao1; instrucao2; instrucao3

- Uso de parênteses

Os parênteses são utilizados para agrupar expressões, definir funções e realizar chamadas a funções. Por exemplo:

    resultado = (a + b) * c