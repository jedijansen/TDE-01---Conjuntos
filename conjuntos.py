# Gustavo Jansen Butenas 

#Função para ler 
def lendo_arquivotxt(entrada):
    with open(entrada, 'r') as arquivo:
        conjuntos = arquivo.readlines()
    return conjuntos

#Função para receber a quantidade de operações e fazer as operações
def calculando_operaçoes(l):
    qtddOperacoes = int(l[0].strip())
    resultados = []
    i = 1

    for indice in range(qtddOperacoes):
        operacao = l[i].strip()
        conjunto1 = set(l[i + 1].strip().split(', '))
        conjunto2 = set(l[i + 2].strip().split(', '))
        
        if operacao == 'U':
            resultado = conjunto1.union(conjunto2)
            resultadosOperacoes = f"\nUnião (U): Conjunto 1 {conjunto1}, Conjunto 2 {conjunto2}. Resultado: {resultado}\n"
        elif operacao == 'I':
            resultado = conjunto1.intersection(conjunto2)
            resultadosOperacoes = f"\nInterseção (I): Conjunto 1 {conjunto1}, Conjunto 2 {conjunto2}. Resultado: {resultado}\n"
        elif operacao == 'D':
            resultado = conjunto1.difference(conjunto2)
            resultadosOperacoes = f"\nDiferença (D): Conjunto 1 {conjunto1}, Conjunto 2 {conjunto2}. Resultado: {resultado}\n"
        elif operacao == 'C':
            resultado = {(a, b) for a in conjunto1 for b in conjunto2}
            resultadosOperacoes = f"\nProduto Cartesiano (C): Conjunto 1 {conjunto1}, Conjunto 2 {conjunto2}. Resultado: {resultado}\n"
        
        resultados.append(resultadosOperacoes)
        i += 3

    return resultados

#Função para imprimir resultados no arquivo de saída
def escrever_resultados(resultados, arquivoSaida):
    with open(arquivoSaida, 'w') as arquivo:
        for resultado in resultados:
            arquivo.write(resultado + '\n')

#Função main para executar as funções
def main():
    arquivoEntrada = input()
    arquivoSaida = 'saida.txt'
    
    linhas = lendo_arquivotxt(arquivoEntrada)
    resultados = calculando_operaçoes(linhas)
    escrever_resultados(resultados, arquivoSaida)
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":

#Biblioteca para as funções do Sistema Operacional
    import os

#Arquivos no Diretório
    arquivosDiretorio = os.listdir()
    print(f"\nArquivos no Diretório:\n{arquivosDiretorio}\nEscolha o arquivo que deseja executar: ")
    main()  
