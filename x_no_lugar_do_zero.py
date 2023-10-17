number = "0165031806510"
number_final = ""


for digit in "0165031806510":
    if digit == "0":
        number_final += "X"
    else:
        number_final += digit

print(number_final)