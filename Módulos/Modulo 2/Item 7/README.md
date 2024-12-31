# 7. Entradas/saídas

Em Python, a entrada e saída de dados nos permite interagir com o usuário e manipular arquivos. Podemos solicitar informações ao usuário, mostrar resultados na tela e ler ou escrever dados em arquivos externos.

> Entrada de dados do usuário

Para obter informações do usuário durante a execução do programa, podemos utilizar a função input(). Esta função mostra uma mensagem na tela e espera que o usuário insira um valor.

```
nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")

print("Olá, " + nome + "!")
print("Você tem " + idade + " anos.")
```
Neste exemplo, solicita-se ao usuário que insira seu nome e idade utilizando a função input(). Os valores inseridos são armazenados nas variáveis nome e idade, respectivamente. Em seguida, essas variáveis são utilizadas para mostrar uma saudação personalizada na tela.

A função input() sempre retorna uma cadeia de texto. Se você deseja trabalhar com outros tipos de dados, como números inteiros ou flutuantes, deve realizar uma conversão explícita utilizando funções como int() ou float().

```
idade = int(input("Insira sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

Neste exemplo, solicita-se ao usuário que insira sua idade e converte o valor inserido para um número inteiro utilizando int(). Em seguida, utiliza-se uma estrutura condicional para verificar se a idade é maior ou igual a 18 e mostrar uma mensagem correspondente.

> Saída de dados

Para mostrar informações na tela, utilizamos a função print(). Esta função recebe um ou mais argumentos e os mostra no console.

Podemos utilizar a f-string (formatação de cadeias) para inserir variáveis diretamente dentro de uma cadeia de texto.

```
nome = "Juan"
idade = 25

print(f"Olá, meu nome é {nome} e tenho {idade} anos.")
```

Neste caso, as variáveis são inseridas dentro da cadeia utilizando chaves {} e a cadeia é precedida pela letra f para indicar que é uma f-string.

## 7.1. Leitura e escrita de arquivos

Python nos permite ler e escrever dados em arquivos externos. Podemos abrir arquivos em diferentes modos, como leitura ("r"), escrita ("w") ou anexar ("a"), e realizar operações de leitura e escrita.

> Leitura de arquivos

Para ler o conteúdo de um arquivo, primeiro devemos abri-lo utilizando a função open() em modo de leitura ("r"). Depois, podemos ler o conteúdo do arquivo utilizando métodos como read() ou readlines().

```
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
```

Neste exemplo, o arquivo "dados.txt" é aberto em modo de leitura utilizando open(). Depois, todo o conteúdo do arquivo é lido utilizando o método read() e armazenado na variável conteudo. Finalmente, o conteúdo é mostrado na tela e o arquivo é fechado utilizando o método close().

> Escrita de arquivos

Para escrever dados em um arquivo, abrimos em modo de escrita ("w") utilizando a função open(). Se o arquivo não existir, será criado automaticamente. Se o arquivo já existir, seu conteúdo será sobrescrito.

```
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()
```

Neste exemplo, o arquivo "dados.txt" é aberto em modo de escrita utilizando open(). Depois, a string "Olá, mundo!" é escrita no arquivo utilizando o método write(). Finalmente, o arquivo é fechado utilizando o método close().

É importante fechar sempre os arquivos depois de utilizá-los para liberar os recursos do sistema. 

Você também pode utilizar a declaração with para manejar a abertura e fechamento de arquivos de maneira automática.

```
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

Neste caso, o arquivo é aberto utilizando a declaração with e é fechado automaticamente uma vez que se sai do bloco with, mesmo se ocorrer uma exceção.

A entrada e saída de dados em Python nos oferece uma grande flexibilidade para interagir com o usuário e manipular arquivos externos. Podemos solicitar informações ao usuário, mostrar resultados na tela e ler ou escrever dados em arquivos de texto. Lembre-se sempre de manejar adequadamente a abertura e fechamento de arquivos, e considerar as possíveis exceções que podem ocorrer durante as operações de entrada/saída.


