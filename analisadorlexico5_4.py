def keywords():
    keywords = [
    "E", 
    "VETOR", 
    "INICIO", 
    "CASO", 
    "CONST", 
    "DIV",
    "FAÇA", 
    "SENAO", 
    "FIM", 
    "PARA", 
    "FUNCAO", 
    "SE", 
    "MOD", 
    "NAO", 
    "DE", 
    "OU", 
    "PROCEDIMENTO", 
    "ALGORITMO", 
    "REGISTRO", 
    "REPITA", 
    "ENTAO", 
    "TIPO", 
    "ATE", 
    "VAR", 
    "ENQUANTO",
    "LEIA",
    "ESCREVA",
    "ESCREVAL",
    "PASSO",
    "FIM_PARA",
    "FIM_ENQUANTO",
    "FIM_SE",
    "RESTO",
    "INTEIRO",
    "REAL",
    "LOGICO",
    "LITERAL",
    "MATRIZ",
    "VERDADEIRO",
    "FALSO",
    ]
    return keywords

def operadores():
    operadores = {
    "<-": "atribuicao",
    "..": "pontoponto",
    ".": "ponto",
    ":": "doispontos",
    ";": "pontovirgula",
    ",": "virgula",
    "[": "colchete_esq",
    "]": "colchete_dir",
    "(": "parentese_esq",
    ")": "parentese_dir",
    "=": "igual",
    "<=": "menor_igual",
    ">=": "maior_igual",
    "<>": "diferente",
    ">": "maior_que",
    "<": "menor_que",
    "/": "divisao",
    "-": "menos",
    "*": "mul",
    "+": "soma",
    }
    return operadores

def delimitadores():
    delimitadores = {
    "\t": "TAB",
    "\n": "NEWLINE",
    "(": "LPAR",
    ")": "RPAR",
    "[": "LBRACE",
    "]": "RBRACE",
    "{": "LCBRACE",
    "}": "RCBRACE",
    "=": "ASSIGN",
    ":": "COLON",
    ",": "COMMA",
    ";": "SEMICOL",
    }
    return delimitadores

import re

# função para listar os tokens e seus atributos
def verificarTokens(token):
    identificadores = re.compile(r"^[a-zA-Z_]+[a-zA-Z0-9_]*")
    Caracter_Especial = re.compile(r"[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\"")   
    digito = re.compile(r"^(\d+)$")
    decimal = re.compile(r"\d+[.]\d+")

    if token.upper() in keywords():
        print("[ " + token + " | keyword ]")
    elif token in operadores().keys():
        print("[ " + token + " | ", operadores()[token] + " ]")
    elif token in delimitadores():
        description = delimitadores()[token]
        if description == 'TAB' or description == 'NEWLINE':
            print(description)
        else:
            print("[ " + token + " | ", description + " ]")

    elif re.match(identificadores, token):
        print("[ " + token + " | identificador ]" )
    elif re.match(digito, token):
        if re.match(decimal, token):
            print("[ " + token + " | decimal ]")
        else:
            print("[ " + token + " | inteiro ]")
    elif re.match(Caracter_Especial, token) or "'" in token or '"' in token:
        print("[ " + token + " | char1 ]" )

    return True

# Retorna um array com todos os tokens de cada linha
def analiseLexica(line):
    tokens = line.split(" ")
    for delimitador in delimitadores().keys():
        for token in tokens:
            if token == delimitador:
                pass
            elif delimitador in token:
                pos = token.find(delimitador)
                tokens.remove(token)
                token = token.replace(delimitador, " ")
                extra = token[:pos]
                token = token[pos + 1 :]
                tokens.append(delimitador)
                tokens.append(extra)
                tokens.append(token)
            else:
                pass
    for token in tokens:
        if isWhiteSpace(token):
            tokens.remove(token)
        elif " " in token:
            tokens.remove(token)
            token = token.split(" ")
            for d in token:
                tokens.append(d)
    return tokens

# Verifica se há ou não espaço em branco
def isWhiteSpace(word):
    ptrn = [ " ", "\t", "\n"]
    for item in ptrn:
        if word == item:
            return True
        else:
            return False

# Função que abre o arquivo e exibe o conteúdo com chamadas à outras funções
def tokenizer(path):
    try:
        f = open(path, encoding = "ISO-8859-1", mode='r')
        programa = f.read() 
        # Remover comentários
        remove_Multi_Comentarios = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", programa)
        remove_Um_Comentario = re.sub("//.*", "", remove_Multi_Comentarios)
        comentarios_Removidos = remove_Um_Comentario
        lines = comentarios_Removidos.split('\n')
        count = 0
        for line in lines:
            count = count + 1
            tokens = analiseLexica(line)
            print("\n-LINHA ", count, "\n")
            #print("Tokens: ", tokens)
            for token in tokens:
                verificarTokens(token)
        return True
    except FileNotFoundError:
        print("\nInvald Path. Retry")
        menuInserir()

# Menu para inserir arquivo
def menuInserir():
    path = input("Insira o caminho do código-fonte: ")
    tokenizer(path)
    opc = int(input("""\n1. Tentar novamente\n2. Sair\n"""))
    if opc == 1:
        menuInserir()
    elif opc == 2:
        print("Saindo...")
    else:
        print('Pedido inválido.')
        menuInserir()

menuInserir()