import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Ejercicio 4.2.1 - EDP",
    layout="centered"
)

st.markdown("""
<style>

@media print {

    header {
        display: none !important;
    }

    footer {
        display: none !important;
    }

    section[data-testid="stSidebar"] {
        display: none !important;
    }

    .block-container {
        max-width: 100% !important;
        padding-top: 0 !important;
    }

    h1, h2, h3 {
        page-break-after: avoid;
    }

    .element-container {
        page-break-inside: avoid;
    }
}

</style>
""", unsafe_allow_html=True)


st.title("Ejercicio 4.2.1 — Clasificación de EDP")

st.subheader("Sistema analizado")

st.markdown(r"""
Se analiza un **edificio sometido a excitación sísmica**.

El fenómeno físico relevante corresponde a la **propagación de ondas mecánicas**
en una estructura elástica. La variable de campo es el desplazamiento:

$$
\mathbf{u}(x,y,z,t)
$$
""")

st.subheader("EDP gobernante")

st.markdown(r"""
La ecuación de elastodinámica puede escribirse como:

$$
\rho \frac{\partial^2 \mathbf{u}}{\partial t^2}
=
\nabla \cdot \boldsymbol{\sigma}
+
\mathbf{b}
$$

donde $\rho$ es la densidad, $\mathbf{u}$ el campo de desplazamientos,
$\boldsymbol{\sigma}$ el tensor de tensiones y $\mathbf{b}$ las fuerzas de cuerpo.
""")

st.subheader("Simplificación unidimensional")

st.markdown(r"""
Para identificar el tipo de EDP, se considera una barra elástica con vibración longitudinal:

$$
u = u(x,t)
$$

La ecuación se reduce a:

$$
\rho \frac{\partial^2 u}{\partial t^2}
=
E \frac{\partial^2 u}{\partial x^2}
$$

Dividiendo entre $\rho$:

$$
\frac{\partial^2 u}{\partial t^2}
=
\frac{E}{\rho}
\frac{\partial^2 u}{\partial x^2}
$$

Definiendo:

$$
c = \sqrt{\frac{E}{\rho}}
$$

se obtiene la ecuación de onda:

$$
\frac{\partial^2 u}{\partial t^2}
=
c^2
\frac{\partial^2 u}{\partial x^2}
$$
""")

st.subheader("Clasificación")

st.markdown(r"""
La forma general de una EDP lineal de segundo orden es:

$$
A u_{xx} + B u_{xt} + C u_{tt} = 0
$$

La ecuación de onda puede escribirse como:

$$
c^2 u_{xx} - u_{tt} = 0
$$

Por comparación:

$$
A = c^2, \qquad B = 0, \qquad C = -1
$$

El discriminante es:

$$
B^2 - 4AC
=
0^2 - 4(c^2)(-1)
=
4c^2
$$

Como $c^2 > 0$:

$$
B^2 - 4AC > 0
$$
""")

st.success("La EDP resultante es hiperbólica.")

st.subheader("Condiciones de frontera e iniciales")

st.markdown(r"""
Para el edificio, una condición de frontera típica es la base empotrada:

$$
\mathbf{u} = 0
$$

Esta corresponde a una condición de **Dirichlet**.

Además, al ser un problema dependiente del tiempo, se requieren condiciones iniciales:

$$
\mathbf{u}(x,y,z,0)=\mathbf{0}
$$

$$
\frac{\partial \mathbf{u}}{\partial t}(x,y,z,0)=\mathbf{0}
$$
""")

st.subheader("Resultado")

st.markdown(r"""
| Concepto | Resultado |
|---|---|
| Sistema | Edificio bajo excitación sísmica |
| Fenómeno | Propagación de ondas mecánicas |
| Campo | Desplazamientos |
| Variable | $\mathbf{u}(x,y,z,t)$ |
| EDP | Elastodinámica |
| Forma simplificada | Ecuación de onda |
| Clasificación | Hiperbólica |
| Frontera principal | Dirichlet |
""")



st.markdown(r"""---""")
st.title("Ejercicio 4.2.2 — Separación de Variables y Series de Fourier")

st.markdown(r"""
Ecuación de onda unidimensional:

$$
\frac{\partial^2 u}{\partial t^2}
=
c^2
\frac{\partial^2 u}{\partial x^2}
$$

$u(x,t)$ es el desplazamiento, $x$ la posición, $t$ el tiempo y $c$ la velocidad de propagación.
""")

st.subheader("a) Hipótesis de separación")

st.markdown(r"""
Se propone:

$$
u(x,t)=X(x)T(t)
$$

Sustituyendo en la ecuación de onda:

$$
X(x)T''(t)
=
c^2X''(x)T(t)
$$

Dividiendo por $c^2X(x)T(t)$:

$$
\frac{T''(t)}{c^2T(t)}
=
\frac{X''(x)}{X(x)}
=
-\lambda
$$
""")

st.subheader("b) Problema de Sturm-Liouville")

st.markdown(r"""
De la separación se obtienen dos ecuaciones.

Problema espacial:

$$
X''(x)+\lambda X(x)=0
$$

Problema temporal:

$$
T''(t)+c^2\lambda T(t)=0
$$

Para extremos restringidos:

$$
u(0,t)=0,
\qquad
u(L,t)=0
$$

por tanto:

$$
X(0)=0,
\qquad
X(L)=0
$$
""")

st.markdown(r"""
El problema espacial queda:

$$
X''(x)+\lambda X(x)=0,
\qquad
X(0)=0,
\qquad
X(L)=0
$$

Sus valores propios son:

$$
\lambda_n=
\left(
\frac{n\pi}{L}
\right)^2
$$

y sus funciones propias:

$$
X_n(x)=
\sin
\left(
\frac{n\pi x}{L}
\right)
$$

con $n=1,2,3,\ldots$
""")

st.subheader("c) Coeficientes de Fourier")

st.markdown(r"""
Las condiciones iniciales son:

$$
u(x,0)=f(x)
$$

$$
\frac{\partial u}{\partial t}(x,0)=g(x)
$$

La frecuencia angular de cada modo es:

$$
\omega_n^2=c^2\lambda_n
$$

$$
\omega_n=
c\frac{n\pi}{L}
$$
""")

st.markdown(r"""
Los coeficientes asociados al desplazamiento inicial son:

$$
A_n
=
\frac{2}{L}
\int_0^L
f(x)
\sin
\left(
\frac{n\pi x}{L}
\right)
dx
$$

Los coeficientes asociados a la velocidad inicial son:

$$
B_n
=
\frac{2}{L\omega_n}
\int_0^L
g(x)
\sin
\left(
\frac{n\pi x}{L}
\right)
dx
$$
""")

st.subheader("d) Solución en serie")

st.markdown(r"""
La solución temporal de cada modo es:

$$
T_n(t)
=
A_n\cos(\omega_n t)
+
B_n\sin(\omega_n t)
$$

Combinando la parte espacial y temporal:

$$
u(x,t)
=
\sum_{n=1}^{\infty}
\left[
A_n\cos(\omega_n t)
+
B_n\sin(\omega_n t)
\right]
X_n(x)
$$

Como:

$$
X_n(x)=
\sin
\left(
\frac{n\pi x}{L}
\right)
$$

entonces:
""")

st.success("Solución general")

st.markdown(r"""
$$
u(x,t)
=
\sum_{n=1}^{\infty}
\left[
A_n\cos(\omega_n t)
+
B_n\sin(\omega_n t)
\right]
\sin
\left(
\frac{n\pi x}{L}
\right)
$$

con:

$$
\omega_n=
c\frac{n\pi}{L}
$$
""")

# st.subheader("e) Verificación gráfica de la convergencia con Python")

# st.markdown(r"""
# Se aproxima la serie usando un número finito de armónicas:

# $$
# N=5,\quad 10,\quad 20
# $$

# Caso usado para visualizar:

# $$
# f(x)=x(L-x),
# \qquad
# g(x)=0
# $$
# """)

# L = 1.0
# c = 1.0
# x = np.linspace(0, L, 500)
# t = st.slider("Tiempo $t$", 0.0, 2.0, 0.0, 0.01)

# def f(x):
#     return x * (L - x)

# def g(x):
#     return 0 * x

# def compute_A(n):
#     xi = np.linspace(0, L, 2000)
#     integrand = f(xi) * np.sin(n * np.pi * xi / L)
#     return (2 / L) * np.trapz(integrand, xi)

# def compute_B(n):
#     xi = np.linspace(0, L, 2000)
#     omega_n = c * n * np.pi / L
#     integrand = g(xi) * np.sin(n * np.pi * xi / L)
#     return (2 / (L * omega_n)) * np.trapz(integrand, xi)

# def u_series(x, t, N):
#     total = np.zeros_like(x)

#     for n in range(1, N + 1):
#         omega_n = c * n * np.pi / L
#         A_n = compute_A(n)
#         B_n = compute_B(n)

#         total += (
#             A_n * np.cos(omega_n * t)
#             + B_n * np.sin(omega_n * t)
#         ) * np.sin(n * np.pi * x / L)

#     return total

# fig, ax = plt.subplots()

# ax.plot(x, f(x), linestyle="--", label="$f(x)$")

# for N in [5, 10, 20]:
#     ax.plot(x, u_series(x, t, N), label=f"N = {N}")

# ax.set_xlabel("x")
# ax.set_ylabel("u(x,t)")
# ax.set_title("Convergencia de la serie de Fourier")
# ax.legend()
# ax.grid(True)

# st.pyplot(fig)

# st.success("La aproximación mejora al aumentar el número de armónicas.")