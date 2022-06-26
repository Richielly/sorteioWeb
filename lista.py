lista_num = []
sorteados = []
def lista_numeros(quantidade):
    global lista_num
    for n in range(int(quantidade)):
        n += 1
        lista_num.append(str(n))
    return lista_num

def historico_lista():
    return lista_num

def historico_sorteado(num_sorteado):
    global sorteados
    if num_sorteado != '0':
        sorteados.append(num_sorteado)
    return sorteados

def limpar_lista():
    lista_num.clear()
    sorteados.clear()
    return "Lista limpa com sucesso."