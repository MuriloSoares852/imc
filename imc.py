# ---- Calculadora de IMC (Índice de massa corporal) -----

print("Olá! Vamos calcular seu IMC.")
print("Por favor, use ponto (.) para casas decimais, se necessário.")

# Comando "try-except" para garantir que o usuário digite apenas números
try:
    # Pede ao usuário para digitar o peso e a altura
    peso = float(input("Digite seu peso em kg (ex: 80.5): "))
    altura = float(input("Digite sua altura em metros (ex: 1.80): "))

    # Fórmula para o cálculo do IMC: peso / (altura * altura)
    imc = peso / (altura **2)

    # Define a classificação com base no resultado do IMC

    if imc <= 18.5:
        classificacao = "Baixo peso"
    elif imc <= 25:
        classificacao = "Peso adequado"
    elif imc <= 30:
        classificacao = "Sobrepeso"
    elif imc <= 35:
        classificacao = "Obesidade grau 1" 
    elif imc <= 40:
        classificacao = "Obesidade grau 2"
    else:
        classificacao = "Obesidade grau 3"

    # Apresenta o resultado de forma facíl e resumida
    # O :.2f formata o número para exibir apenas 2 casas decimais
    print(f"Seu IMC é de {imc:.2f} kg/m².")
    print(f"Classificação: {classificacao}")

    # Adiciona uma recomenação imporntante
    print("Atenção: Este cálculo é um indicador, mas não substitui uma consulta real com um profissional.")

except ValueError:
    # Mensagem de erro caso o usuário digite qualquer texto ao em vez de números
    print("Erro: Por favor, digite apenas números para peso e altura. ")


































