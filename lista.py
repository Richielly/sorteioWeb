lista_num = []
def lista_numeros(quantidade):
    global lista_num
    for n in range(int(quantidade)):
        n += 1
        lista_num.append(str(n))
    return lista_num

def historico_lista():
    return lista_num

