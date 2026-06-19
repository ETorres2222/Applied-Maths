import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Ejercicio 4.2.1 - EDP",
    layout="centered"
)

st.markdown("""
<style>
@media print {
    header, footer, section[data-testid="stSidebar"] {
        display: none !important;
    }

    .block-container {
        max-width: 100% !important;
        padding-top: 0 !important;
        padding-left: 12mm !important;
        padding-right: 28mm !important;
        transform: translateX(-8mm);
        overflow: visible !important;
    }

    .element-container, .stMarkdown {
        overflow: visible !important;
    }

    @page {
        size: A4;
        margin: 15mm;
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
Se aplica el método de separación de variables a una **viga idealizada como barra axial**.

Una viga real puede presentar flexión, torsión y vibración axial.  
En este ejercicio se considera únicamente la **vibración axial**, por lo que el desplazamiento se modela como:

$$
u(x,t)
$$

donde:

- $x$ es la coordenada a lo largo del eje de la viga,
- $t$ es el tiempo,
- $u(x,t)$ es el desplazamiento axial.

Bajo esta idealización, la ecuación gobernante es la ecuación de onda unidimensional:

$$
\frac{\partial^2 u}{\partial t^2}
=
c^2
\frac{\partial^2 u}{\partial x^2}
$$
""")

st.subheader("Datos del modelo aplicado")

L = 4.06
fc = 210
rho = 2400

E_kg_cm2 = 15000 * np.sqrt(fc)
E_MPa = E_kg_cm2 * 0.0980665
E = E_MPa * 1e6
c = np.sqrt(E / rho)

st.markdown(rf"""
Se considera una longitud:

$$
L = {L} \ \text{{m}}
$$

y un concreto con resistencia a compresión:

$$
f'_c = {fc} \ \text{{kg/cm}}^2
$$

Para estimar el módulo de elasticidad se usa:

$$
E =
15000\sqrt{{f'_c}}
$$

Sustituyendo:

$$
E =
15000\sqrt{{210}}
=
{E_kg_cm2:,.2f}
\ \text{{kg/cm}}^2
$$

Convirtiendo al Sistema Internacional:

$$
E =
{E_MPa:,.2f}
\ \text{{MPa}}
=
{E/1e9:.2f}
\ \text{{GPa}}
$$

Se adopta una densidad del concreto armado:

$$
\rho =
{rho}
\ \text{{kg/m}}^3
$$

La velocidad de propagación axial es:

$$
c =
\sqrt{{
\frac{{E}}{{\rho}}
}}
=
{c:.2f}
\ \text{{m/s}}
$$
""")

st.subheader("Separación de variables")

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

Dividiendo entre $c^2X(x)T(t)$:

$$
\frac{T''(t)}{c^2T(t)}
=
\frac{X''(x)}{X(x)}
=
-\lambda
$$

De aquí se obtienen dos problemas:

$$
X''(x)+\lambda X(x)=0
$$

$$
T''(t)+c^2\lambda T(t)=0
$$
""")

st.subheader("Condiciones de frontera y modos espaciales")

st.markdown(r"""
Se consideran extremos axialmente restringidos:

$$
u(0,t)=0
$$

$$
u(L,t)=0
$$

Por tanto:

$$
X(0)=0
$$

$$
X(L)=0
$$

El problema espacial queda:

$$
X''(x)+\lambda X(x)=0
$$

con:

$$
X(0)=0,
\qquad
X(L)=0
$$

Este problema genera los valores propios:

$$
\lambda_n
=
\left(
\frac{n\pi}{L}
\right)^2
$$

y las funciones propias:

$$
X_n(x)
=
\sin
\left(
\frac{n\pi x}{L}
\right)
$$

donde $n=1,2,3,\ldots$

El valor $\lambda_n$ mide la frecuencia espacial del modo.  
Mientras mayor es $n$, más ondas internas aparecen dentro de la longitud $L$.
""")

st.subheader("Frecuencias naturales axiales")

st.markdown(r"""
La frecuencia angular natural de cada modo se obtiene de:

$$
\omega_n^2
=
c^2\lambda_n
$$

Por tanto:

$$
\omega_n
=
c
\frac{n\pi}{L}
$$

La frecuencia en Hertz es:

$$
f_n
=
\frac{\omega_n}{2\pi}
$$
""")

modes = []

for n in range(1, 4):
    lambda_n = (n * np.pi / L) ** 2
    omega_n = c * n * np.pi / L
    f_n = omega_n / (2 * np.pi)

    modes.append({
        "Modo n": n,
        "lambda_n [1/m²]": round(lambda_n, 4),
        "omega_n [rad/s]": round(omega_n, 2),
        "f_n [Hz]": round(f_n, 2)
    })

st.table(modes)

st.markdown(r"""
Interpretación:

- El modo 1 es el modo fundamental.
- El modo 2 tiene una onda interna adicional.
- El modo 3 tiene una forma espacial más oscilatoria.
- En este modelo axial idealizado, las frecuencias crecen proporcionalmente con $n$.
""")

st.subheader("Formas modales")

x = np.linspace(0, L, 400)

fig, ax = plt.subplots()

for n in range(1, 4):
    Xn = np.sin(n * np.pi * x / L)
    ax.plot(x, Xn, label=f"Modo {n}")

ax.set_xlabel("x [m]")
ax.set_ylabel("X_n(x)")
ax.set_title("Primeros tres modos axiales")
ax.legend()
ax.grid(True)

st.pyplot(fig)

st.subheader("Solución general en serie")

st.markdown(r"""
La solución completa se obtiene como superposición de modos:

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

donde:

$$
\omega_n
=
c
\frac{n\pi}{L}
$$

Los coeficientes se determinan a partir de las condiciones iniciales:

$$
u(x,0)=f(x)
$$

$$
\frac{\partial u}{\partial t}(x,0)=g(x)
$$

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

st.success("La ecuación de onda se mantiene porque la viga fue idealizada únicamente en vibración axial.")