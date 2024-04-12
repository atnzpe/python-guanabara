# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re


# Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):

    pattern = r"\(\d{2}\) 9\d{4}-\d{4}"

    x = re.match(pattern, phone_number)
    if x:

        result = "Número de telefone válido."

    else:
        result = f"Número de telefone inválido."

    return result


# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input('Digite seu telefone. Ex (XX) 9XXXX-XXXX:\n->')

# Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)
# Imprime o resultado:
print(result)
