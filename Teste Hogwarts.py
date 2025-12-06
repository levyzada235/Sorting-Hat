import time               #Dá ritmo ao texto 

def pausa(seg=1):
  time.sleep(seg)

Gryffindor = 0
Ravenclaw = 0             #Variável das casas de Hogwarts
Hufflepuff = 0
Slytherin = 0

print("Welcome to the Sorting Hat's Houses test!\n")          #Mensagem de boas vindas
pausa(2)                                              
print("Answer with sincerity... The Sorting Hat is watching you!", end="\n\n")
pausa(5)

print("Q1) Do you like Dawn or Dusk?")                 #Primeira pergunta
print("1) Dawn")
print("2) Dusk", end ="\n")
print()

answer = int(input("Enter your answer (1-4): "))       #Resposta do usuário
print()

if answer == 1:
  Ravenclaw += 1
  Gryffindor += 1
elif answer == 2:                            #Distribuição de pontos com base na resposta do usuário
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input.")

print("A curious choice... let's see where it leads \n")              #Resposta do chapéu seletor
pausa(2)

print("Q2) When I’m dead, I want people to remember me as:")          #Segunda pergunta
print("The Good")
print("The Great")
print("The Wise")
print("The Bold")

answer = int(input("Enter your answer (1-4): "))              #Resposta do usuário
print()

if answer == 1:
  Hufflepuff += 2
elif answer == 2:
  Slytherin += 2                                              #Distribuição de pontos com base na resposta do usuário
elif answer == 3:
  Ravenclaw += 2
elif answer == 4:
  Gryffindor += 2
else:
  print("Wrong input.")

print("I see potential here... a lot of potential \n")        #Resposta do Chapéu Seletor
pausa(2)

print("Q3) Which kind of instrument most pleases your ear?")  #Terceira pergunta
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

answer = int(input("Enter your answer (1-4) "))               #Resposta do usuário
print()

if answer == 1:
  Slytherin += 4
elif answer == 2:
  Hufflepuff += 4
elif answer == 3:                                             #Distribuição de pontos com base na resposta do usuário
  Ravenclaw += 4
elif answer == 4:
  Gryffindor += 4
else:
  print("Wrong input.")

print("Hmm... Interesting, very interesting \n")              #Resposta do Chapéu Seletor
pausa(2)

print("The Sorting Hat is now making his choice...\n")
pausa(2)
                                                              #O Chapéu Seletor está escolhendo a sua casa em Hogwarts
print("THE SORTING HAT SAYS...")
pausa(2)
print()

major = max(Gryffindor, Slytherin, Hufflepuff, Ravenclaw)
if major == Gryffindor:
  print("Congratulations, you are selected for Gryffindor!")
elif major == Slytherin:
  print("Congratulations, you are selected for Slytherin!")                #Resposta final do Chapéu Seletor com base nas respostas
elif major == Hufflepuff:
  print("Congratulations, you are selected for Hufflepuff!")
else:
  print("Congratulations, you are selected for Ravenclaw!")