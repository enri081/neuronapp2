import streamlit as st
import numpy as np
import math

# Cabecera 
st.image("img/neurona.jpg", width=360)
st.header("Simulador de neurona")

# Definición de la clase Neuron
class Neuron:
  FUNCIONES = {
        "sigmoid": lambda x: 1.0 / (1.0 + np.exp(-x)),
        "tanh": np.tanh,
        "relu": lambda x: np.maximum(0.0, x),
    }

  def __init__(self, weights, bias, func):
    self.weights = np.array(weights, dtype=float)
    self.bias = float(bias)
    self.func = str(func)

  def run(self, input_data):
    y = np.dot(np.array(input_data, dtype=float), self.weights) + self.bias
    result = self.FUNCIONES.get(self.func)
    return result(y)

  def changeBias(self, n):
    self.bias = n

  def changeWeights(self, n):
    self.weights = n

# Nº de pesos y entradas 
number_of_inputs = st.slider("Elige el número de entradas/pesos que tendrá la neurona", 1, 10)

# Pesos
st.subheader("Pesos")
w = []
colw = st.columns(number_of_inputs)
for i in range(number_of_inputs):
    with colw[i]:
        w_i = st.number_input(label=f"w{i}", value=0.0, step=0.1, key=f"w_{i}",)
        w.append(w_i)
st.text(f"w = {w}")

# Entradas
st.subheader("Entradas")
x = []
colx = st.columns(number_of_inputs)
for i in range(number_of_inputs):
    with colx[i]:
        x_i = st.number_input(label=f"x{i}", value=0.0, step=0.1, key=f"x_{i}",)
        x.append(x_i)

st.text(f"x = {x}")

# Sesgo
col1, col2 = st.columns(2)
with col1:
    st.subheader("Sesgo")
    b = st.number_input("Introduce el valor del sesgo")

with col2:
    st.subheader("Función de activación")
    func_chosen = st.selectbox('Elige la función de activación', ('Sigmoide', 'ReLU', 'Tangente hiperbólica'))

# Mapeado a nombres definido en clase Neuron
FUNCTIONS_NAME = {'Sigmoide': 'sigmoid', 'ReLU': 'relu', 'Tangente hiperbólica': 'tanh'}

# Salida
if st.button("Calcular la salida"):
    neurons_output = Neuron(weights=w, bias=b, func=FUNCTIONS_NAME[func_chosen])
    st.text(f"La salida de la neurona es {neurons_output.run(input_data=x)}")