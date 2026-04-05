# Recovered Final Notebook Notes (Spanish)

> This notebook was not present in the git history of `TP_Final_METOP`, but it was found in the sibling repository `ejercicios.regresion` with the title `TRABAJO FINAL` and a Colab badge pointing to `TPFINAL_VOTOS_ROSARIO.ipynb`. It is preserved here as the most likely original final-delivery notebook.

<a href="https://colab.research.google.com/github/TorradoSantiago/ejercicios.regresion/blob/master/TPFINAL_VOTOS_ROSARIO.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## TRABAJO FINAL

##DATOS ROSARIO

##MAPA ARGENTINA

## YUXTAPOSICION

## AGREGANDO VULNERABILIDAD SANITARIA

mas codigo

dataset educativo

poblacion mayor a 18 con primaria completa sin secundario completo

## REGRESION LOGISTICA

El modelo de regresión logística se ajustó correctamente con los siguientes coeficientes:

Intercepto (coef_intercept_bin): -1.5090
Pendiente (coef_slope_bin): 0.00187
Estos coeficientes indican que existe una relación entre el nivel educativo y la probabilidad de votar por "Libertarios". El signo positivo de la pendiente sugiere que a medida que aumenta el nivel educativo (representado por P18A_SOLOP), también aumenta ligeramente la probabilidad de votar por "Libertarios".

La relación positiva que encontramos en la regresión logística, donde la pendiente es positiva, efectivamente sugiere que a medida que aumenta el porcentaje de personas con educación primaria completa pero sin secundario completo (es decir, menor nivel educativo formal), aumenta la probabilidad de votar por "Libertarios". Esto significa que en áreas con menor nivel educativo formal, hay una tendencia más alta hacia el voto a "Libertarios".

Este hallazgo puede ser útil para entender mejor el perfil demográfico y educativo del apoyo a "Libertarios" en Rosario. Si deseas explorar más sobre cómo otras variables pueden influir en la intención de voto, o si necesitas realizar análisis estadísticos adicionales para confirmar estos resultados, estaré encantado de ayudarte con eso.

## regresion universitarios

Intercepto (-1.0571): Este valor es el logaritmo de odds de votar por "Libertarios" cuando el porcentaje de personas con educación universitaria es 0. En otras palabras, si no hay personas con educación universitaria completa en un radio censal, la log-odds de que alguien vote por "Libertarios" es -1.0571. probabilidad inicial baja de votar por "Libertarios" cuando no hay educación universitaria presente.

Coeficiente para 'P18A_UNIVE' (-0.00218): Este coeficiente te indica cómo cambian las log-odds de votar por "Libertarios" por cada aumento de un punto porcentual en el porcentaje de población con educación universitaria completa. Un coeficiente negativo implica que a medida que aumenta el porcentaje de personas con educación universitaria, la probabilidad de votar por "Libertarios" disminuye. El valor negativo muestra una relación inversa entre la educación universitaria y votar por "Libertarios".

Odds Ratio (0.9978): El Odds Ratio es una forma más interpretable de entender el impacto del coeficiente. Un Odds Ratio menor que 1 también indica una relación inversa. En este caso, por cada incremento del 1% en la población con educación universitaria completa, las odds de votar por "Libertarios" se multiplican por 0.9978, lo que implica una pequeña disminución. El valor cercano a 1 sugiere que cada incremento porcentual tiene un efecto relativamente pequeño en las odds, aunque es consistentemente negativo.