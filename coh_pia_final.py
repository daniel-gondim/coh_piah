import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    #RECEBE duas assinaturas (listas)
    i = 0
    soma_tracos_linguisticos = 0
    #[4.34, 0.05, 0.02, 12.81, 2.16, 0.0], ass2 = [3.96, 0.05, 0.02, 22.22, 3.41, 0.0])
    for i in range(0,5):
        soma_tracos_linguisticos += abs(as_a[i] - as_b[i])
        i = i + 1

    grau_similaridade_ab = abs(soma_tracos_linguisticos) / 6

    return grau_similaridade_ab

def calcula_assinatura(texto):
#    "\n"
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []

    for sentenca in sentencas:
        lista_frases_dentro_da_sentenca = separa_frases(sentenca)
        frases.extend(lista_frases_dentro_da_sentenca)

    for frase in frases:
        todas_as_palavras_da_frase = separa_palavras(frase)
        palavras.extend(todas_as_palavras_da_frase)

    soma_de_todas_as_palavras = 0
    for palavra in palavras:
        #a,pai
        tamanho_de_uma_palavra = len(palavra)
        soma_de_todas_as_palavras += tamanho_de_uma_palavra

    numero_total_de_palavras = len(palavras)
    wal = soma_de_todas_as_palavras / numero_total_de_palavras

    numero_de_palavras_diferentes = n_palavras_diferentes(palavras)
    ttr = numero_de_palavras_diferentes / numero_total_de_palavras

    numero_de_palavras_unicas = n_palavras_unicas(palavras)
    hlr = numero_de_palavras_unicas / numero_total_de_palavras

    soma_dos_numeros_de_caracteres_em_todas_as_sentencas = 0
    for sentenca in sentencas:
        numero_de_caracteres_em_uma_sentenca = len(sentenca)
        soma_dos_numeros_de_caracteres_em_todas_as_sentencas += numero_de_caracteres_em_uma_sentenca

    sal = soma_dos_numeros_de_caracteres_em_todas_as_sentencas / len(sentencas)
    sac = len(frases) / len(sentencas)

    soma_dos_numeros_de_caracteres_em_todas_as_frases = 0
    for frase in frases:
        numero_de_caractres_em_uma_frase = len(frase)
        soma_dos_numeros_de_caracteres_em_todas_as_frases += numero_de_caractres_em_uma_frase
    pal = soma_dos_numeros_de_caracteres_em_todas_as_frases / len(frases)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    #'''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    grau_de_similaridade_dos_textos = []

    for texto in textos:
        assinatura_texto = calcula_assinatura(texto)
        compara = compara_assinatura(ass_cp, assinatura_texto)
        grau_de_similaridade_dos_textos.append(compara)

    # valor máximo dessa listas
    #qual o índice

    valor_maximo = max(grau_de_similaridade_dos_textos)
    infectado_com_coh_piah = grau_de_similaridade_dos_textos.index(valor_maximo)

    #return valor_maximo
    print("O autor do texto" + str(infectado_com_coh_piah) + "está infectado com COH-PIAH.")

    #print(grau_de_similaridade_dos_textos)
    #print(infectado_com_coh_piah)

def main():
    ass_cp = le_assinatura()

    textos = le_textos()

    return(avalia_textos(textos, ass_cp))


main()
