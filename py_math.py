# ============================================================
#          PLANTILLA PYTHON - LIBRERÍA MATH
# ============================================================

import math


# CONSTANTES
math.pi       # 3.14159...  número π
math.e        # 2.71828...  número de Euler
math.tau      # 6.28318...  2π
math.inf      # Infinito positivo
math.nan      # Not a Number (valor indefinido)


# REDONDEO Y VALOR ABSOLUTO
math.floor(<x>)       # Redondea hacia abajo → ej: floor(2.9) = 2
math.ceil(<x>)        # Redondea hacia arriba → ej: ceil(2.1) = 3
math.trunc(<x>)       # Elimina decimales sin redondear → trunc(-2.9) = -2
math.fabs(<x>)        # Valor absoluto como float → fabs(-5) = 5.0
round(<x>, <n>)       # Redondea a n decimales (builtin, no necesita math)


# POTENCIAS Y RAÍCES
math.sqrt(<x>)        # Raíz cuadrada → sqrt(9) = 3.0
math.pow(<x>, <y>)    # x elevado a y como float → pow(2, 3) = 8.0
math.exp(<x>)         # e elevado a x → exp(1) = 2.718...
math.log(<x>)         # Logaritmo natural (base e)
math.log(<x>, <base>) # Logaritmo en la base indicada → log(100, 10) = 2.0
math.log2(<x>)        # Logaritmo en base 2
math.log10(<x>)       # Logaritmo en base 10
math.isqrt(<n>)       # Raíz cuadrada entera (sin decimales) → isqrt(10) = 3


# TRIGONOMETRÍA  (ángulos en radianes)
math.sin(<rad>)       # Seno
math.cos(<rad>)       # Coseno
math.tan(<rad>)       # Tangente
math.asin(<x>)        # Arcoseno   → devuelve radianes, x entre -1 y 1
math.acos(<x>)        # Arcocoseno → devuelve radianes, x entre -1 y 1
math.atan(<x>)        # Arcotangente → devuelve radianes
math.atan2(<y>, <x>)  # Arcotangente de y/x, respeta el cuadrante correcto

# Conversión de ángulos
math.radians(<grados>)  # Grados → radianes → radians(180) = π
math.degrees(<rad>)     # Radianes → grados → degrees(π) = 180.0


# HIPERBÓLICAS
math.sinh(<x>)        # Seno hiperbólico
math.cosh(<x>)        # Coseno hiperbólico
math.tanh(<x>)        # Tangente hiperbólica


# COMBINATORIA Y NÚMEROS ENTEROS
math.factorial(<n>)         # n! → factorial(5) = 120
math.comb(<n>, <k>)         # Combinaciones sin repetición → C(n,k) = n!/(k!(n-k)!)
math.perm(<n>, <k>)         # Permutaciones → P(n,k) = n!/(n-k)!
math.gcd(<a>, <b>)          # Máximo común divisor → gcd(12, 8) = 4
math.lcm(<a>, <b>)          # Mínimo común múltiplo → lcm(4, 6) = 12  (Python 3.9+)


# COMPROBACIONES
math.isinf(<x>)       # True si x es infinito (+ o -)
math.isnan(<x>)       # True si x es NaN
math.isfinite(<x>)    # True si x es un número finito real
math.isclose(<a>, <b>, rel_tol=1e-9)  # True si a y b son aproximadamente iguales


# MISCELÁNEA
math.fsum([<v1>, <v2>, <v3>])   # Suma de floats con mayor precisión que sum()
math.prod([<v1>, <v2>, <v3>])   # Producto de todos los elementos (Python 3.8+)
math.dist((<x1>,<y1>), (<x2>,<y2>))  # Distancia euclidiana entre dos puntos
math.hypot(<x>, <y>)            # Hipotenusa → √(x²+y²), equivale a dist desde origen
math.copysign(<x>, <y>)         # Devuelve |x| con el signo de y
math.remainder(<x>, <y>)        # Resto según IEEE 754 (distinto a x % y)


# PATRÓN DE USO HABITUAL
angulo_grados = <grados>
angulo_rad    = math.radians(angulo_grados)   # Convierte antes de usar trig
seno          = math.sin(angulo_rad)

resultado     = math.sqrt(math.pow(<a>, 2) + math.pow(<b>, 2))  # Pitágoras
