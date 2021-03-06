# Probabilidades en un examen tipo test

## Introducción

La idea es responder a preguntas del estilo: ¿Puedo aprobar si hago un examen tipo test sin estudiar? ¿La probabilidad está de mi lado si contesto aleatoriamente? ¿Qué probabilidad tengo de aprobar si contesto la mitad al azar? ¿Y si estoy seguro de la mitad? ¿Y de sacar un notable? ¿Y un sobresaliente?...

## Funcionamiento

Este programa ayuda a visualizar el cálculo de probabilidades mostrando todas las posibles combinaciones de respuestas dado un número determinado de preguntas y calculando la probabilidad de que ocurra cada uno de los eventos posibles asumiendo que todas las preguntas se contestan al azar.

Para calcular las posibilidades se generan todas las combinaciones para 8 preguntas o menos, esto es un algoritmo de fuerza bruta   que resulta ilustrativo pero poco eficiente.

Para más de 8 preguntas se usan fórmulas de matemática combinatoria y probabilidad que generan los cálculos al instante, por ejemplo la siguiente fórmula para calcular todas las posibles combinaciones de respuestas:
```
r = Número de respuestas posibles (normalmente 4: A, B, C y D)
p = Número de preguntas contestadas al azar
c = Número de combinaciones posibles
```
c = r <sup>p</sup>, por ejemplo si contestamos 10 preguntas con 4 opciones de respuesta, hay 4<sup>10</sup> = 1048576 posibilidades.

## Uso

El programa está escrito en Python 3, consite en un único fichero y no tiene parámetros de ejecución. Suponiendo que tienes Python 3 instalado en un tu PC, sólo hay que ejecutar el programa de esta forma:
```
python main.py
```
El programa pregunta primero el número de preguntas que queremos calcular.

La segunda pregunta es si quieres imprimir todas las posibilidades por consola. A partir de 5 preguntas hay más de 1000 posibilidades con lo que empieza a ser poco práctico imprimirlas y cada vez más costoso en carga computacional, por lo tanto, no se imprimirán más si se seleccionan más de 8 preguntas, mostrando únicamente los cálculos de probabilidades.
