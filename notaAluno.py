from enum import Enum

# Aprendendo no python

# Importar pacotes
# Exibir no console
# Criar Input
# Criar variável
# Principais tipos de variáveis (int, float, str)
# Converter tipos de variáveis
# Como funciona uma variável em Python
# Escopos
# Execução do python
# Array
# Manipulação do array (Adicionar, alterar, remover, limpar)
# Criar funções
# Chamar funções criadas
# Condicionais (if, elif, else)
# Laços de repetições (for) e (while)
# Função de return
# Criar enum
# Padrão de nomenclatura para Python

# Dificuldade em escopos de variáveis

def imprime_linha():
    print("----------------------")

def preenche_nome():
    global nome
    nome = input("Qual é seu nome ? ")

def preenche_idade():
    global idade
    idade = int(input("Qual é a sua idade ? "))

def imprime_nome():
    print("Seu nome é " + str(nome) + ".")

def imprime_idade():
    print("Você tem " + str(idade) + " anos.")

def valida_nota():
    ultimaNota = notas[-1]
    if ultimaNota <= notaMaxima:
        return True
    else:
        del(notas[-1])
        return False

def adiciona_nota(mensagem_input):
    numero = float(input(mensagem_input))
    nota = abs(numero)
    notas.append(nota)
    notaValida = valida_nota()

    # Condição - se a nota é inválida..
    while notaValida == False:
        print("Essa nota é inválida. Adicione uma nota de 0 a 10.")
        numero = float(input())
        nota = abs(numero)
        notas.append(nota)
        notaValida = valida_nota()

def preenche_notas():
    adiciona_nota("Digite sua primeira nota. ")
    adiciona_nota("Digite sua segunda nota. ")
    adiciona_nota("Digite sua terceira nota. ")

def soma_notas():
    global somaDasNotas
    somaDasNotas = 0

    for nota in notas:
        somaDasNotas += nota

def calcula_nota_media():
    casasDecimais = 2
    global notaMedia
    notaMedia = round(somaDasNotas / totalDeNotas, casasDecimais)

def imprime_nota_media():
    print("A média do aluno " + nome + " é, " + str(notaMedia))

def imprime_todas_notas():
    for nota in notas:
        print(nota)

def altera_nota():
    index = int(input("Qual nota você quer alterar ? "))
    novaNota = float(input("Nova nota: "))
    notas[index] = novaNota
    soma_notas()
    calcula_nota_media()

def verifica_aprovacao():
    if notaMedia >= notaMediaEscolar:
        aprovado()
    else:
        reprovado()

def aprovado():
    set_estado_aluno(AlunoEstado.APROVADO)
    print("Parabéns! Você foi aprovado!")

def reprovado():
    set_estado_aluno(AlunoEstado.REPROVADO)
    print("Infelizmente, você foi reprovado!")

class AlunoEstado(Enum):
    APROVADO = 1
    REPROVADO = 2
    RECUPERACAO = 3

def set_estado_aluno(estado):
    global aluno_estado
    aluno_estado = estado

# Variáveis
nome = ""
idade = 0
notas = []

notaMedia = 0
notaMediaEscolar = 6
notaMaxima = 10

totalDeNotas = 3
somaDasNotas = 0
aluno_estado = AlunoEstado.APROVADO

# Algoritmo
imprime_linha()
preenche_nome()
preenche_idade()

imprime_linha()
imprime_nome()
imprime_idade()

imprime_linha()
preenche_notas()


imprime_linha()
soma_notas()
calcula_nota_media()
print("Notas do aluno, " + nome)
print()
imprime_todas_notas()
print()
imprime_nota_media()


imprime_linha()
altera_nota()
print()
print("Nota alterada com sucesso!")
imprime_todas_notas()
print()
print("Agora, a nota média do aluno " + str(nome) + ", é " + str(notaMedia))


imprime_linha()
verifica_aprovacao()
imprime_linha()