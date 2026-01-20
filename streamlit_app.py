import streamlit as st

st.image("./img/neurona.jpg", width=500)
st.markdown("## ¡Hola neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    st.markdown("## Una neurona con una entrada y un peso")

    w = st.slider("Peso", 0.0, 5.0, 0.0, 0.01, key="w_tab1")
    x = st.number_input("Introduzca el valor de la entrada", key="x_tab1")

    y1 = x * w

    if st.button("Calcular la salida", key="b_tab1"):
        st.write(f"La salida de la neurona es {y1}")

with tab2:
    col1, col2 = st.columns(2)

    with col1:
        w0 = st.slider("Peso w0", 0.0, 5.0, 0.0, 0.01, key="w0_tab2")
        x0 = st.number_input("Entrada x0", key="x0_tab2")

    with col2:
        w1 = st.slider("Peso w1", 0.0, 5.0, 0.0, 0.01, key="w1_tab2")
        x1 = st.number_input("Entrada x1", key="x1_tab2")  

    y2 = x0 * w0 + x1 * w1

    if st.button("Calcular la salida", key="b_tab2"):
        st.write(f"La salida de la neurona es {y2}")

with tab3:
    col1, col2, col3 = st.columns(3)

    with col1:
        w0 = st.slider("Peso w0", 0.0, 5.0, 0.0, 0.01, key="w0_tab3")
        x0 = st.number_input("Entrada x0", key="x0_tab3")

    with col2:
        w1 = st.slider("Peso w1", 0.0, 5.0, 0.0, 0.01, key="w1_tab3")
        x1 = st.number_input("Entrada x1", key="x1_tab3")  
    
    with col3:
        w2 = st.slider("Peso w2", 0.0, 5.0, 0.0, 0.01, key="w2_tab3")
        x2 = st.number_input("Entrada x2", key="x2_tab3") 

    sesgo = st.number_input("Introduzca el valor del sesgo", key="sesgo")

    y3 = (x0 * w0 + x1 * w1 + x2 * w2) + sesgo 

    if st.button("Calcular la salida", key="b_tab3"):
        st.write(f"La salida de la neurona es {y3}")