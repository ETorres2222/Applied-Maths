import streamlit as st

st.title("Módulo 2 — EDP: Fenómeno de campo continuo")

st.header("Selección e identificación del tipo de EDP")

st.markdown("""
Identificar el fenómeno de campo continuo relevante en el sistema elegido
y clasificar la EDP resultante según:

- \(B^2 - 4AC < 0\): elíptica  
- \(B^2 - 4AC = 0\): parabólica  
- \(B^2 - 4AC > 0\): hiperbólica
""")

st.subheader("Mi solución")

fenomeno = st.text_input("Fenómeno elegido", "Transferencia de calor")

A = st.number_input("A", value=1.0)
B = st.number_input("B", value=0.0)
C = st.number_input("C", value=1.0)

disc = B**2 - 4*A*C

st.write("Discriminante:", disc)

if disc < 0:
    st.success("La EDP es elíptica")
elif disc == 0:
    st.warning("La EDP es parabólica")
else:
    st.info("La EDP es hiperbólica")

st.subheader("Condiciones de frontera")
st.text_area("Escribe aquí tus condiciones de frontera")