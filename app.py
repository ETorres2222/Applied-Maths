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

st.markdown(r"""---""")
st.title("Aplicación — Viga idealizada con vibración axial")

st.markdown(r"""
Para ver el caso aplicativo, se idealiza un elemento estructural del edificio como una **viga trabajando únicamente en vibración axial**.

Una viga real puede vibrar de varias formas:

- vibración axial,
- vibración por flexión,
- torsión,
- modos combinados.

En este ejercicio no se analiza la flexión de la viga.  
Se considera solamente la propagación de ondas longitudinales a lo largo de su eje.

Por esta razón, la variable de campo se toma como:

$$
u(x,t)
$$

donde:

- $u(x,t)$ es el desplazamiento axial,
- $x$ es la coordenada a lo largo del eje de la viga,
- $t$ es el tiempo.

Bajo esta hipótesis, la viga se comporta como una barra elástica unidimensional.
""")

st.subheader("Modelo físico adoptado")

st.markdown(r"""
Se considera una viga de longitud:

$$
L = 4.06 \ \text{m}
$$

idealizada como una barra axial elástica.

El fenómeno considerado es el alargamiento y acortamiento longitudinal del elemento,
no su deflexión transversal.

Por tanto, la ecuación gobernante es:

$$
\frac{\partial^2 u}{\partial t^2}
=
c^2
\frac{\partial^2 u}{\partial x^2}
$$

donde:

$$
c=
\sqrt{\frac{E}{\rho}}
$$

es la velocidad de propagación de la onda axial en el material.
""")

st.subheader("Condiciones de frontera")

st.markdown(r"""
Para mantener consistencia con el desarrollo de Fourier seno, se consideran extremos restringidos:

$$
u(0,t)=0
$$

$$
u(L,t)=0
$$

Estas condiciones indican que el desplazamiento axial es nulo en ambos extremos. Esto produce funciones propias de la forma:

$$
X_n(x)
=
\sin
\left(
\frac{n\pi x}{L}
\right)
$$

Por eso la solución se expresa mediante una serie de Fourier seno.
""")

st.subheader("Frecuencias naturales axiales")

st.markdown(r"""
Las frecuencias angulares naturales son:

$$
\omega_n
=
c
\frac{n\pi}{L}
$$

Sustituyendo la longitud:

$$
L = 4.06 \ \text{m}
$$

se obtiene:

$$
\omega_n
=
c
\frac{n\pi}{4.06}
$$

Esto significa que cada modo axial de vibración posee una frecuencia natural propia.

El modo fundamental corresponde a:

$$
n=1
$$

por tanto:

$$
\omega_1
=
c
\frac{\pi}{4.06}
$$
""")

st.subheader("Interpretación aplicada")

st.markdown(r"""
La solución:

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

representa la vibración axial de la viga como una superposición de modos.

Cada término de la serie tiene dos partes:

- una forma espacial,
- una variación temporal.

La forma espacial indica cómo se deforma axialmente la viga a lo largo de su longitud.

La parte temporal indica cómo oscila esa forma con el tiempo.
""")

st.subheader("Primeros tres modos axiales de vibración")

st.markdown(r"""
Para visualizar la aplicación, se calculan los tres primeros modos axiales de una viga idealizada
como una **barra elástica en vibración longitudinal**.

En este modelo no se analiza flexión.  
Solo se analiza el desplazamiento axial:

$$
u(x,t)
$$

Se adopta una longitud:

$$
L = 4.06 \ \text{m}
$$

y un concreto con resistencia a compresión:

$$
f'_c = 210 \ \text{kg/cm}^2
$$

Para estimar el módulo de elasticidad del concreto se usa la aproximación:

$$
E =
15000 \sqrt{f'_c}
$$

donde:

- $E$ se obtiene en $\text{kg/cm}^2$,
- $f'_c$ se introduce en $\text{kg/cm}^2$.
""")

L = 4.06
fc = 210          # kg/cm2
rho = 2400       # kg/m3

E_kg_cm2 = 15000 * np.sqrt(fc)
E_MPa = E_kg_cm2 * 0.0980665
E = E_MPa * 1e6

st.markdown(rf"""
Sustituyendo:

$$
E =
15000\sqrt{{210}}
=
{E_kg_cm2:,.2f}
\ \text{{kg/cm}}^2
$$

Convirtiendo a unidades del Sistema Internacional:

$$
E =
{E_MPa:,.2f}
\ \text{{MPa}}
=
{E/1e9:.2f}
\ \text{{GPa}}
$$

Se adopta además una densidad típica del concreto armado definida en el proyecto de:

$$
\rho = 2400 \ \text{{kg/m}}^3
$$
""")

st.subheader("Velocidad de propagación axial")

st.markdown(r"""
Para una barra elástica en vibración longitudinal, la velocidad de propagación de la onda axial es:

$$
c =
\sqrt{
\frac{E}{\rho}
}
$$

donde:

- $c$ es la velocidad de propagación axial,
- $E$ es el módulo de elasticidad del material,
- $\rho$ es la densidad del material.
""")

c = np.sqrt(E / rho)

st.markdown(rf"""
Sustituyendo:

$$
c =
\sqrt{{\frac{{{E:.2e}}}{{{rho}}}}}
=
{c:.2f}
\ \text{{m/s}}
$$
""")

st.subheader("Cálculo de los valores propios")

st.markdown(r"""
Para extremos restringidos:

$$
u(0,t)=0
$$

$$
u(L,t)=0
$$

las funciones propias son:

$$
X_n(x)
=
\sin
\left(
\frac{n\pi x}{L}
\right)
$$

y los valores propios son:

$$
\lambda_n
=
\left(
\frac{n\pi}{L}
\right)^2
$$

El valor propio $\lambda_n$ mide la frecuencia espacial del modo.  
Mientras mayor es $\lambda_n$, más ondas internas tiene el modo dentro de la longitud $L$.
""")

st.subheader("Frecuencias naturales")

st.markdown(r"""
La frecuencia angular natural de cada modo se calcula como:

$$
\omega_n
=
c
\frac{n\pi}{L}
$$

y la frecuencia en Hertz se obtiene mediante:

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

- $n=1$ corresponde al modo fundamental.
- $n=2$ corresponde al segundo modo axial.
- $n=3$ corresponde al tercer modo axial.
- En este modelo axial idealizado, las frecuencias aumentan proporcionalmente con $n$.
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

st.markdown(r"""
Las formas modales calculadas son:

$$
X_1(x)
=
\sin
\left(
\frac{\pi x}{L}
\right)
$$

$$
X_2(x)
=
\sin
\left(
\frac{2\pi x}{L}
\right)
$$

$$
X_3(x)
=
\sin
\left(
\frac{3\pi x}{L}
\right)
$$

Estas funciones cumplen las condiciones de frontera:

$$
X_n(0)=0
$$

$$
X_n(L)=0
$$

por eso son compatibles con una barra idealizada con extremos restringidos.
""")