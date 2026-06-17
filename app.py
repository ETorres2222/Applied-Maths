import streamlit as st

st.set_page_config(
    page_title="Ejercicio 4.2.1 - Clasificación de EDP",
    layout="wide"
)

st.title("Ejercicio 4.2.1 — Selección e Identificación del Tipo de EDP")

st.header("1. Sistema analizado")

st.write("""
El sistema seleccionado corresponde a un edificio sometido a excitación sísmica.
El fenómeno físico relevante es la vibración dinámica de una estructura elástica.
""")

st.info("""
Sistema: Edificio bajo excitación sísmica  
Fenómeno: Propagación de ondas mecánicas  
Campo: Campo vectorial de desplazamientos  
EDP: Elastodinámica  
Clasificación: Hiperbólica
""")

st.header("2. Variable de campo")

st.write("""
La variable principal es el campo vectorial de desplazamientos:
""")

st.latex(r"""
\mathbf{u}(x,y,z,t)
=
\begin{bmatrix}
u_x(x,y,z,t) \\
u_y(x,y,z,t) \\
u_z(x,y,z,t)
\end{bmatrix}
""")

st.write("""
donde:

- \(x,y,z\) representan la posición de un punto dentro de la estructura.
- \(t\) representa el tiempo.
- \(\mathbf{u}\) representa el desplazamiento de dicho punto.
""")

st.header("3. Ecuación de elastodinámica")

st.write("""
La ecuación general de movimiento de un sólido continuo es:
""")

st.latex(r"""
\rho
\frac{\partial^2 \mathbf{u}}
{\partial t^2}
=
\nabla \cdot \boldsymbol{\sigma}
+
\mathbf{b}
""")

st.write("""
Esta ecuación puede interpretarse como:
""")

st.latex(r"""
\text{Inercia}
=
\text{Fuerzas internas}
+
\text{Fuerzas externas distribuidas}
""")

st.write("""
donde:

- \(\rho\) es la densidad del material.
- \(\mathbf{u}\) es el vector de desplazamientos.
- \(\frac{\partial^2 \mathbf{u}}{\partial t^2}\) representa la aceleración.
- \(\boldsymbol{\sigma}\) es el tensor de tensiones.
- \(\mathbf{b}\) son fuerzas de cuerpo por unidad de volumen.
""")

st.header("4. Simplificación unidimensional")

st.write("""
Para identificar la naturaleza de la EDP, se puede considerar una barra elástica sometida a vibraciones longitudinales.
En este caso:
""")

st.latex(r"""
u = u(x,t)
""")

st.write("""
La ecuación se reduce a:
""")

st.latex(r"""
\rho
\frac{\partial^2 u}
{\partial t^2}
=
E
\frac{\partial^2 u}
{\partial x^2}
""")

st.write("""
donde:

- \(E\) es el módulo de elasticidad.
- \(\rho\) es la densidad.
- \(u(x,t)\) es el desplazamiento longitudinal.
""")

st.write("""
Dividiendo entre \(\rho\):
""")

st.latex(r"""
\frac{\partial^2 u}
{\partial t^2}
=
\frac{E}{\rho}
\frac{\partial^2 u}
{\partial x^2}
""")

st.write("""
Definiendo la velocidad de propagación:
""")

st.latex(r"""
c =
\sqrt{
\frac{E}{\rho}
}
""")

st.write("""
se obtiene la ecuación de onda:
""")

st.latex(r"""
\frac{\partial^2 u}
{\partial t^2}
=
c^2
\frac{\partial^2 u}
{\partial x^2}
""")

st.header("5. Clasificación de la EDP")

st.write("""
La forma general de una EDP lineal de segundo orden en dos variables independientes es:
""")

st.latex(r"""
A
\frac{\partial^2 u}{\partial x^2}
+
B
\frac{\partial^2 u}{\partial x \partial t}
+
C
\frac{\partial^2 u}{\partial t^2}
+
D
\frac{\partial u}{\partial x}
+
E
\frac{\partial u}{\partial t}
+
F u
+
G
=
0
""")

st.write("""
Para clasificar la EDP se consideran únicamente los términos de segundo orden:
""")

st.latex(r"""
A u_{xx}
+
B u_{xt}
+
C u_{tt}
""")

st.write("""
La ecuación de onda puede escribirse como:
""")

st.latex(r"""
c^2
\frac{\partial^2 u}{\partial x^2}
-
\frac{\partial^2 u}{\partial t^2}
=
0
""")

st.write("""
Comparando:
""")

st.latex(r"""
A=c^2,
\qquad
B=0,
\qquad
C=-1
""")

st.write("""
El discriminante es:
""")

st.latex(r"""
B^2-4AC
""")

st.write("""
Sustituyendo:
""")

st.latex(r"""
0^2
-
4(c^2)(-1)
=
4c^2
""")

st.write("""
Como \(c^2 > 0\), entonces:
""")

st.latex(r"""
B^2-4AC > 0
""")

st.success("""
Por lo tanto, la ecuación se clasifica como una EDP hiperbólica.
""")

st.header("6. Condiciones de frontera")

st.write("""
Para un edificio sometido a acción sísmica, una condición típica consiste en considerar la base empotrada.
Esto implica:
""")

st.latex(r"""
\mathbf{u}=0
""")

st.write("""
en la base de la estructura.

Esta es una condición de Dirichlet, porque se prescribe directamente el valor de la variable de campo.
""")

st.header("7. Condiciones iniciales")

st.write("""
Como la ecuación depende del tiempo, también se requieren condiciones iniciales.
Generalmente se puede asumir:
""")

st.latex(r"""
\mathbf{u}(x,y,z,0)=\mathbf{0}
""")

st.latex(r"""
\frac{\partial \mathbf{u}}
{\partial t}
(x,y,z,0)
=
\mathbf{0}
""")

st.write("""
Esto significa que la estructura parte sin desplazamiento inicial y sin velocidad inicial.
""")

st.header("8. Relación con FEM")

st.write("""
Luego de discretizar el problema continuo mediante el Método de Elementos Finitos, se obtiene la ecuación de movimiento dinámico:
""")

st.latex(r"""
M\ddot{u}
+
C\dot{u}
+
Ku
=
F(t)
""")

st.write("""
donde:

- \(M\ddot{u}\) representa las fuerzas de inercia.
- \(C\dot{u}\) representa las fuerzas de amortiguamiento.
- \(Ku\) representa las fuerzas elásticas.
- \(F(t)\) representa las fuerzas externas aplicadas.
""")

st.header("Resultado final")

st.markdown("""
| Concepto | Resultado |
|---|---|
| Sistema | Edificio sometido a excitación sísmica |
| Fenómeno | Vibración dinámica estructural |
| Campo | Campo vectorial de desplazamientos |
| Variable | \(\\mathbf{u}(x,y,z,t)\) |
| EDP gobernante | Ecuación de elastodinámica |
| Forma simplificada | Ecuación de onda |
| Clasificación | Hiperbólica |
| Condición de frontera principal | Dirichlet |
| Condiciones iniciales | Desplazamiento y velocidad inicial |
""")