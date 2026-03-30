# HeatCalico
Un proyecto mediocre y decadente para una materia de Métodos Numéricos :P. Hay mucha complejidad porque soy un masoquista de mierda y obligué a mi equipo a usar la **ecuación del calor** en un miserable vaso de agua UwU.

$$\Large \frac{\partial u}{\partial t} - \alpha \nabla^2 u = 0$$

## Resumen
Básicamente, las cosas están así: nuestra maestra de Métodos Numéricos nos hizo elegir un proyecto para el semestre donde utilizáramos los métodos numéricos para predecir fenómenos naturales. Nosotros, como tenemos un cierto retraso mental, elegimos "Proyecto 2: Enfriamiento de una bebida caliente" y ahora tenemos que invertir parte del tiempo de nuestras vacaciones trabajando en esta mezcolanza.

> Como yo, `znil0`, soy el único que puede digerir las atrocidades que los físicos han escrito sin desmayarse entre terribles sufrimientos, tendré que arreglarmelas para soportar las ganas de hacerlo todo yo \*inserte aquí león furro llorando\*, porque sino la muela se va a enojar conmigo. Además, tampoco se me puede culpar, llevaba rato queriendo experimentar con Series de Fourier-Bessel, el laplaciano en coordenadas cilíndricas, la ecuación del calor y todo eso. Sé que probablemente todo esto me vaya a explotar en la cara, pero pues me da igual, no creo ni acabar la carrera. Con suerte, los proyectos de los demás equipos serán tan mierdosos que el nuestro brillará con luz propia solo por el esfuerzo que le hemos puesto.

## Integrantes del equipo
- La Muela 🦷
- El que no veía (pero yabe) 👁️
- Monitorman 🖥️
- Yo, uwu 🦁

## ¿Cuál es el plan?
Vamos a crear un programa en Python usando `Flet` (una librería parecida a Swing) para la interfaz y `numpy` si es posible. El objetivo es conseguir un programa que al teclear ciertos datos iniciales, pueda predecir el cambio de temperatura de un vaso con algún líquido.

Ya de por sí es problemático lidiar con fenómenos físicos porque dependen de muchos factores ambientales. Pero idealmente, usaremos dos planteamientos matemáticos distintos:

### Plan A: Ecuación del Calor
Con esta ecuación diferencial parcial que parece sencilla a primera vista (pero es peor que un tumor en el qlo) podemos predecir la temperatura de un cuerpo en cada uno de los puntos que lo conforman. La ecuación se plantea de forma genérica como

$$\Large \frac{\partial u}{\partial t} - \alpha \nabla^2 u = 0$$

donde la función $u(x_1, x_2, ..., x_n, t)$ representa la temperatura en un punto fijado por las coordenadas $x_n$ (que no necesariamente son cartesianas) y el tiempo $t$. El símbolo $\nabla^2$ representa el operador laplaciano que dependiendo de las coordenadas, se puede volver un verdadero infierno.

$$\Large \nabla^2 u = \frac{\partial^2 u}{\partial r^2} + \frac{1}{r}\frac{\partial u}{\partial r} + \frac{1}{r^2}\frac{\partial^2 u}{\partial \theta^2} + \frac{\partial ^2 u}{\partial z^2}$$

Evidentemente, usar la ecuación del calor en un vaso con agua es como usar las malditas Ecuaciones de Campo de Einstein para calcular la velocidad de un carro, ¿pero a quién no le gusta matar hormigas con cañonazos? Quizás le ponga avena, o algún líquido espeso para que se enfrie de manera desigual y poder decir *"Uy, miren, que inteligentes somos, nuestro programa sabe que el centro está calientito y el exterior ta frio!!"* y así.

En fin, que como los vasos suelen ser cilíndricos, tendremos que usar coordenadas cilíndricas y series de Fourier-Bessel. (Las series de Fourier-Bessel reducen el laplaciano en coordenadas cilíndricas, las funciones de Bessel son como una especie de función especial).

> Aún no tengo el desarrollo completo, pero lo tendré eventualmente. Solo que me acabo de mudar y mientras escribo esto estoy sacando una infinidad de trastos y armatostes de cajas que ni sabía que existían. Tanto así que por cada día que pasa, mi variable $M$ que representa numéricamente mis ganas de morirme aumenta exponencialmente. Les juro que si me tengo que mudar una vez más en lo que queda de este año, voy a regalar todas mis cosas y me voy a tirar de un edificio.

### Plan B: Ley de Enfriamiento de Newton
Con esta ley desabrida y decepcionante podemos predecir la manera en la que la temperatura de un cuerpo decrece al pasar el tiempo, asumiendo que la temperatura en el mismo se distribuya uniformemente sobre el mismo (lo cual suele ser el caso en líquidos como el agua). Este es nuestro plan B a prueba de errores, diseñado para que mi equipo no repruebe si me muero antes de que pueda terminar el otro planteamiento.

Básicamente es una ecuación diferencial lineal de primer orden

$$\Large \frac{dT(t)}{dt} = -r(T - T_m)$$

que se resuelve trivialmente mediante separación de variables, quedando como

$$\Large T(t) = T_m + (T_0 - T_m)e^{-rt}\text{.}$$

Utiliza una cierta constante $r$ que representa el ritmo en el que se pierde calor, pero probablemente podamos estimarla tecleando dos mediciones de temperatura y comparando. *([este](https://es.wikipedia.org/wiki/Ley_del_enfriamiento_de_Newton) es el artículo en Wikipedia)*

## ¿Por qué le pusiste ese nombre?
Porque sí, todos mis proyectos tienen nombres de animales, y como *la muela* no me dió nombres que me convencieran, y además, *el que yabe* tiene la costumbre de dar nombres que hacen referencia a crímenes de guerra, mejor elegí esa kk de nombre. Échenle la culpa a mi equipo.

PD: Si lo cambian, los apuñalo mientras duermen ÒwÓ.
