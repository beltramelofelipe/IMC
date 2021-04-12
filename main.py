peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if (imc < 18.5):
  print('seu imc é de {: .1f}, está abaixo do peso'.format(imc))
elif (imc >= 18.5 and imc <= 25):
  print('seu imc é de {: .1f}, seu peso é ideal'.format(imc))
elif (imc > 25 and imc <= 30):
  print('seu imc é de {: .1f}, você está com sobrepeso'.format(imc))
elif (imc > 30 and imc <= 40):
  print('seu imc é de {: .1f}, você está com obesidade'.format(imc))
else:
  print('seu imc é de {: .1f}, você está com obesidade mórbida'.format(imc))
