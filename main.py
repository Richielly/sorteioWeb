import random
import streamlit as st
import time
import pandas as pd
import lista as lista

#file2 = 'https://docs.google.com/spreadsheets/d/1PPYJRjeq798DU6HjVGjWXguzZAeesJpa_PsBrFwpGEQ/edit?usp=sharing'

container_1 = st.container()
if st.sidebar.button("Limpar"):
    lista.limpar_lista()
tipo = st.sidebar.radio("Tipo sorteio", ["Arquivo", "Sequência numérica"])
numeros = 0;
if tipo == "Sequência numérica":

    quantidade = st.sidebar.number_input("Quantidade de números para sorteio")

    if st.button('Iniciar Sorteio'):
            with st.empty():

                if len(lista.historico_lista()) == 0:
                    lista_numeros = list(lista.lista_numeros(quantidade))
                    with open("lista.txt", "w") as arq:
                        arq.write(str(lista_numeros))

                num = open("lista.txt", "r")

                with st.empty():
                    for seconds in range(101):
                        st.title(f"👑 Embaralhando números ... {seconds} % ")
                        time.sleep(.05)

                lista_de_numeros = lista.historico_lista()
                numero = (random.choice(lista_de_numeros))
                lista_de_numeros.remove(str(numero))

                with open("lista.txt", "w") as arq:
                    arq.write(str(lista_de_numeros))

                st.info('Quantidade de números participantes para ser sorteado: ' + str(len(lista.historico_lista())))

                st.balloons()
                time.sleep(2)
                st.title(f'🎁 O número sorteado foi ... ' + numero + ' 🎁')

                with container_1:
                    st.title("Números sorteados: ")
                    st.header(str(lista.historico_sorteado(numero)).replace("'",""))
                    st.title("")



if tipo == "Arquivo":
    file = st.sidebar.file_uploader("Choose an excel file", type="xlsx")

    def sorteio(df):
        barra = st.progress(0)
        with st.empty():
            for seconds in range(101):
                st.write(f"⏳ Carregando números participantes {seconds} % ")
                time.sleep(.1)
                barra.progress(seconds)
            time.sleep(.1)
            for seconds in range(101):
                st.write(f" Escolhendo o vencedor {seconds} % ")
                time.sleep(.1)
                barra.progress(seconds)
            st.header("✔ número sorteado!")
        time.sleep(1)
        numero = (random.randrange(1, numeros))
        st.header('O Número da Sorte foi ... ' + str(numero))
        sorteado = df.loc
        arquivo = st.success("A pessoa sorteada foi " + sorteado[numero].values[1] + ' ' + sorteado[numero].values[2] + " parabéns.")
        st.balloons()

    if (file is not None):
        df = pd.read_excel(file)
        numeros = df.nome.count()
        df.set_index('numero', inplace=True)
        if(st.sidebar.checkbox('Dados')):
            st.write(df.head(numeros))
        st.info('Quantidade de números participantes no sorteio: ' + str(numeros))
        if st.button('Iniciar Sorteio'):
            sorteio(df)


