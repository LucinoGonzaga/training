# 3. Estruturas de controle

> Estruturas de controle
As estruturas condicionais nos permitem executar diferentes blocos de código segundo se cumpra ou não uma determinada condição. Em Python, as estruturas condicionais mais utilizadas são if, if-else e if-elif-else.

- IF

A estrutura if é utilizada para executar um bloco de código se uma condição for verdadeira. A sintaxe básica é a seguinte:

```
if condicao:

   # Bloco de código a executar se a condição for verdadeira
   instruções
```

Exemplo:

```
idade = 18


if idade >= 18:
   print ("Você é maior de idade.")
```

Neste exemplo, se a variável idade for maior ou igual a 18, será executado o bloco de código dentro do if e será impressa a mensagem "Você é maior de idade."

- IF-ELSE

A estrutura if-else nos permite especificar um bloco de código alternativo que será executado se a condição do if for falsa. A sintaxe básica é a seguinte:

```
idade = 15

if idade >= 18:
   print ("Você é maior de idade.")

else:
   print ("Você é menor de idade.")
```

Neste exemplo, se a variável idade for maior ou igual a 18, será executado o bloco de código dentro do if e será impressa a mensagem "Você é maior de idade." Caso contrário, será executado o bloco de código dentro do else e será impressa a mensagem "Você é menor de idade."

- IF-ELIF-ELSE

A estrutura if-elif-else nos permite especificar múltiplas condições e blocos de código alternativos. A sintaxe básica é a seguinte:

```
if condicao1:

   # Bloco de código a executar se a condicao1 for verdadeira
   instruções

elif condicao2:

   # Bloco de código a executar se a condicao2 for verdadeira
   instruções

else:

   # Bloco de código a executar se nenhuma condição anterior for verdadeira
   instruções
```

Exemplo:

```
nota = 85


if nota >= 90:
   print ("Excelente")

elif nota >= 80:
   print ("Muito bom")

elif nota >= 70:
   print ("Bom")

else:
   print ("Precisa melhorar")
```

Neste exemplo, são avaliadas múltiplas condições em ordem. Se a variável nota for maior ou igual a 90, será impresso "Excelente". Se não se cumprir a primeira condição, mas nota for maior ou igual a 80, será impresso "Muito bom". Se não se cumprirem as condições anteriores, mas nota for maior ou igual a 70, será impresso "Bom". Se nenhuma das condições anteriores for verdadeira, será executado o bloco else e será impresso "Precisa melhorar".

# 3.1. Loops

Os loops nos permitem repetir um bloco de código várias vezes. Em Python, os loops mais comuns são for e while.

- for

O loop for é utilizado para iterar sobre uma sequência (como uma lista, uma tupla ou uma string) ou qualquer objeto iterável. A sintaxe básica é a seguinte:

```
for variável in sequência:
    # Bloco de código a repetir
    instruções
```

Exemplo:

```
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
```

Neste exemplo, o loop for itera sobre a lista frutas. Em cada iteração, a variável fruta assume o valor de um elemento da lista, e o bloco de código dentro do loop é executado. Neste caso, cada fruta é impressa em uma linha separada.

- While

O loop while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira. A sintaxe básica é a seguinte:

```
while condição:
    # Bloco de código a repetir
    instruções
```

Exemplo:

```
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

Neste exemplo, o loop while é executado enquanto a variável contador for menor que 5. Em cada iteração, o valor de contador é impresso e depois incrementado em 1 pela instrução contador += 1. O loop será interrompido quando contador atingir o valor de 5.

É importante ter cuidado ao usar o loop while, pois, se a condição nunca se tornar falsa, o loop será executado indefinidamente, o que é conhecido como um loop infinito.

> Controle de loops

Python fornece algumas instruções especiais para controlar o fluxo de execução dentro dos loops:

- Break

A instrução break é utilizada para sair prematuramente de um loop, independentemente da condição. Quando um break é encontrado, o loop é interrompido e o fluxo de execução continua com a próxima instrução fora do loop.

```
contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break
```

Neste exemplo, o loop while é executado indefinidamente devido à condição True. No entanto, dentro do loop é utilizada uma estrutura condicional if para verificar se contador é igual a 5. Quando essa condição é satisfeita, a instrução break é executada, fazendo com que o loop seja interrompido e o fluxo de execução continue com a próxima instrução fora do loop.

- Continue

A instrução continue é utilizada para pular o restante do bloco de código dentro de um loop e passar para a próxima iteração.

Exemplo:

```
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

Neste exemplo, o loop for itera sobre os números de 0 a 9 utilizando a função range(). Dentro do loop, verifica-se se o número é divisível por 2 utilizando o operador de módulo %. Se o número for divisível por 2 (ou seja, se for par), a instrução continue é executada, fazendo com que o restante do bloco de código seja pulado e passando para a próxima iteração do loop. Como resultado, apenas os números ímpares serão impressos.

- Pass

A instrução pass é uma operação nula que não faz nada. É utilizada como um marcador de posição quando uma instrução é sintaticamente necessária, mas nenhuma ação é desejada.

Exemplo:

```
for i in range(5):
    pass
```

Neste exemplo, o loop for itera sobre os números de 0 a 4, mas nenhuma ação é realizada dentro do loop devido à instrução pass. Isso pode ser útil quando se está desenvolvendo um programa e se deseja reservar um bloco de código para implementá-lo mais tarde.

Conclusão: As estruturas de controle são ferramentas poderosas que nos permitem controlar o fluxo de execução de nossos programas. Com as estruturas condicionais (if, if-else, if-elif-else) podemos tomar decisões baseadas em condições, enquanto que com os loops (for, while) podemos repetir blocos de código várias vezes. Além disso, as instruções break, continue e pass nos fornecem um controle adicional sobre o comportamento dos loops.
