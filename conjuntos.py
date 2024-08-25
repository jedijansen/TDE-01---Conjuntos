def ler_arquivo(conjuntos.txt):
    with open(conjuntos.txt, 'r') as arquivo:
        linhas = arquivo.readlines()
    return linhas

def processar_operacoes(linhas):
    num_operacoes = int(linhas[0].strip())
    resultados = []
    indice = 1

    for _ in range(num_operacoes):
        operacao = linhas[indice].strip()
        conjunto1 = set(linhas[indice + 1].strip().split(', '))
        conjunto2 = set(linhas[indice + 2].strip().split(', '))
        
        if operacao == 'U':
            resultado = conjunto1.union(conjunto2)
            descricao = f"União: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"
        elif operacao == 'I':
            resultado = conjunto1.intersection(conjunto2)
            descricao = f"Interseção: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"
        elif operacao == 'D':
            resultado = conjunto1.difference(conjunto2)
            descricao = f"Diferença: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"
        elif operacao == 'C':
            resultado = {(a, b) for a in conjunto1 for b in conjunto2}
            descricao = f"Produto Cartesiano: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"
        
        resultados.append(descricao)
        indice += 3

    return resultados

def escrever_resultados(resultados, nome_arquivo_saida):
    with open(nome_arquivo_saida, 'w') as arquivo:
        for resultado in resultados:
            arquivo.write(resultado + '\n')

def main():
    nome_arquivo_entrada = 'entrada.txt'
    nome_arquivo_saida = 'saida.txt'
    
    linhas = ler_arquivo(nome_arquivo_entrada)
    resultados = processar_operacoes(linhas)
    escrever_resultados(resultados, nome_arquivo_saida)
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main(
