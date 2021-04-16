import random
import streamlit as st
import time
import pandas as pd

file = st.sidebar.file_uploader("Choose an excel file", type="xlsx")
file2 = 'https://docs.google.com/spreadsheets/d/1PPYJRjeq798DU6HjVGjWXguzZAeesJpa_PsBrFwpGEQ/edit?usp=sharing'

#df2 = pd.read_html(file2, header=1)[0]
numeros = 0;

st.title("Sorteio Equiplano")

def sorteio(df):
    barra = st.progress(0)
    with st.empty():
        for seconds in range(101):
            st.write(f"⏳ Carregando números participantes {seconds} % ")
            time.sleep(.1)
            barra.progress(seconds)
        time.sleep(1)
        for seconds in range(101):
            st.write(f" Escolhendo o vencedor {seconds} % ")
            time.sleep(.1)
            barra.progress(seconds)
        st.header("✔ número sorteado!")
    time.sleep(2)
    numero = (random.randrange(1, numeros))
    st.header('O Número da Sorte foi ... ' + str(numero))
    sorteado = df.loc
    arquivo = st.success(sorteado[numero].values[2] + ' ' + sorteado[numero].values[1] + ", pela resposta ao chamado " + str(
        sorteado[numero].values[0]) + " Parabéns.")
    st.balloons()

if (file is not None):
    df = pd.read_excel(file)
    numeros = df.usuario.count()
    df.set_index('No', inplace=True)
    if(st.sidebar.checkbox('Dados')):
        st.write(df.head(numeros))
    st.info('Quantidade de números participantes no sorteio: ' + str(numeros))
    if st.button('Iniciar Sorteio'):
        sorteio(df)
