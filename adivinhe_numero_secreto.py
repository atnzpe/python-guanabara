secret_number = 777

number = int(input("Digite aqui: "))

while number != secret_number:
    print(
        """
+==============================+
| Ha ha!                       |
| Você está preso no meu loop! |
|                              |      
+==============================+
"""
    )
    number = int(input("Digite aqui: "))

print(
    """
+========================+
|                        |
| Muito bem, trouxa!     |
| Você está livre agora. |
|                        |
+========================+
"""
)


