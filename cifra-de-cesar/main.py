alfabeto_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabeto_lower = "abcdefghijklmnopqrstuvwxyz"


def converter_letra(letra):
    """
    Essa função retorna o caractere correspondente em 4 casas a partir da letra informada.
    (caracteres com acentuação não serão convertidos)
    :param letra: Letra informada, pode ser maiuscula ou minuscula
    :type letra: str
    :return: string com o caractere correspondente em 4
    casas a frente, caso o caractere informado seja invalido, retorna o caractere informado
    """
    if letra.isupper():
        for i in range(len(alfabeto_upper)):
            if letra == alfabeto_upper[i]:
                novo_index = i + 4
                if novo_index > len(alfabeto_upper):
                    novo_index = novo_index - len(alfabeto_upper)
                elif novo_index == len(alfabeto_upper):
                    novo_index = 0
                return alfabeto_upper[novo_index]
    elif letra.islower():
        for i in range(len(alfabeto_lower)):
            if letra == alfabeto_lower[i]:
                novo_index = i + 4
                if novo_index > len(alfabeto_lower):
                    novo_index = novo_index - len(alfabeto_lower)
                elif novo_index == len(alfabeto_lower):
                    novo_index = 0
                return alfabeto_lower[novo_index]
    else:
        return letra
    return letra


def criptografia(texto):
    """
    Função que realiza a criptografia de um texto informado usando a função `converter_letra`.
    :param texto: Texto informado
    :type texto: str
    :return: Texto criptografado
    """
    novo_texto = ""
    for i in range(len(texto)):
        novo_texto = novo_texto + converter_letra(texto[i])
    return novo_texto


t = input('Digite o texto que deseja criptografar: ')
print(criptografia(t))
