# Quando o *args está como parâmetro, não é obrigatório passar argumentos
def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

print(soma_todos_numeros(4))
print(soma_todos_numeros(4, 6))
print(soma_todos_numeros(4, 6, 9))


# Como os args formam tuplas, podemos usar funções de tuple
def soma_todos_numeros_tupla(*args):
    return sum(args)

print(soma_todos_numeros_tupla(4))
print(soma_todos_numeros_tupla(4, 6))
print(soma_todos_numeros_tupla(4, 6, 9))

numeros = (1, 2, 3, 4)

print(soma_todos_numeros_tupla(*numeros)) # o '*' informa para o python que estou passando uma coleção
                                          # e ele precisará desempacotar os valores.

def verifica_info(*args):
    if "Vinícius" in args and "Lenci" in args:
        return "Bem vindo, Vini Lenci!"
    return "Eu não tenho certeza quem você é..."

print(verifica_info("Vinícius", "Lenci"))
print(verifica_info(False, "Lenci", "Vinícius", 19))
print(verifica_info("Lenci", "oi", 19))