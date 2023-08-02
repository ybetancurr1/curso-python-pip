import random

# Game => Piedra, papel o tijera? Voy a hacer un juego de 3 iteraciones, en el cual el usuario ingresa uno de los 3 valores y jugará contra la PC
user_score = 0
pc_score = 0
for item in range(3):

  ## vars

  user_option = input('piedra, papel o tijera =>  ')
  

  ## tuple
  pc_option = ('piedra', 'papel', 'tijera')
  user_option = user_option.lower()
  if not user_option in pc_option:
    print('Perdiste! Escoge una opción válida')
    continue
  rand = random.randint(0, 2)
  
  if (user_option == pc_option[rand]):
    print(f"usted eligió: {user_option}")
    print(f"la máquina eligió: {pc_option[rand]}")
    print('Resultado: Empate')
    user_score += 1
    pc_score += 1
  elif (pc_option[rand] == 'papel' and user_option == 'tijera'):
    print(f"usted eligió: {user_option}")
    print(f"la máquina eligió: {pc_option[rand]}")
    print('Resultado: ganaste')
    user_score += 1
  elif (pc_option[rand] == 'tijera' and user_option == 'piedra'):
    print(f"usted eligió: {user_option}")
    print(f"la máquina eligió: {pc_option[rand]}")
    print('Resultado: ganaste')
    user_score += 1
  elif (pc_option[rand] == 'piedra' and user_option == 'papel'):
    print(f"usted eligió: {user_option}")
    print(f"la máquina eligió: {pc_option[rand]}")
    print('Resultado: ganaste')
    user_score += 1
  
  else:
    print(f"usted eligió: {user_option}")
    print(f"la máquina eligió: {pc_option[rand]}")
    print('Resultado: perdiste!')
    pc_score += 1

print(f"El resultado final es ... Usuario = {user_score} PC = {pc_score}")
if pc_score > user_score:
  print('La PC ganó! :(')
elif pc_score < user_score:
  print('Ganaste! :)')
else:
  print('Empate! :/')
