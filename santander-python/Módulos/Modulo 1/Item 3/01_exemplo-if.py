# Exemplo adaptado na aula 3.
def verificar_idade():
   try:
         idade = int(input("Digite sua idade: "))

         if idade == 15:
            print ("Você tem 15 anos.")
         elif idade >= 15 and idade < 18:
            print ("Você tem mais de 15 e menos de 18 anos.")
         elif idade >= 18 and idade < 60:
            print ("Você é um adulto, tem mais de 18 e menos de 60.")
         elif idade == 60:
            print ("Você tem 60 anos.") 
         elif idade > 60:
            print ("Você tem mais de 60 anos.") 
         else:
            print ("Você tem menos de 15 anos.")
   except ValueError:
      print("Por favor, insira um número válido.")

verificar_idade()   