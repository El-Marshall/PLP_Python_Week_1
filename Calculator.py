# 💬 Demande des entrées à l'utilisateur
num1 = float(input("Entrez le premier nombre : "))
num2 = float(input("Entrez le deuxième nombre : "))
operation = input("Choisissez une opération (+, -, *, /) : ")

# 🧮 Effectue l'opération choisie
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Erreur : division par zéro.")
else:
    print("Opération Impossible.")