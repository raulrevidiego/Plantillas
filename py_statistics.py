# ============================================================
#          PLANTILLA PYTHON - LIBRERIA STATISTICS
# ============================================================

import statistics as stats


# DATOS DE EJEMPLO (sustituye por tu lista de numeros)
datos = [<v1>, <v2>, <v3>, <v4>, <v5>]


# MEDIDAS DE TENDENCIA CENTRAL
stats.mean(datos)           # Media aritmetica -> suma / n
stats.fmean(datos)          # Media aritmetica rapida como float (Python 3.8+)
stats.geometric_mean(datos) # Media geometrica -> raiz_n(v1*v2*...*vn), todos > 0
stats.harmonic_mean(datos)  # Media armonica -> n / (1/v1 + 1/v2 + ...), util en tasas
stats.median(datos)         # Mediana -> valor central (interpolada si n es par)
stats.median_low(datos)     # Mediana baja -> el menor de los dos centrales si n es par
stats.median_high(datos)    # Mediana alta -> el mayor de los dos centrales si n es par
stats.mode(datos)           # Moda -> valor mas frecuente (error si empate en <3.8)
stats.multimode(datos)      # Lista con todas las modas (Python 3.8+)


# MEDIDAS DE DISPERSION
stats.pstdev(datos)         # Desviacion estandar de la POBLACION (divide entre n)
stats.stdev(datos)          # Desviacion estandar de la MUESTRA   (divide entre n-1)
stats.pvariance(datos)      # Varianza de la POBLACION
stats.variance(datos)       # Varianza de la MUESTRA

# Con media precalculada (evita recalcularla si ya la tienes)
media = stats.mean(datos)
stats.stdev(datos, xbar=media)
stats.variance(datos, xbar=media)


# CUANTILES  (divide los datos en partes iguales)
stats.quantiles(datos, n=4)    # Cuartiles Q1, Q2, Q3
stats.quantiles(datos, n=10)   # Deciles
stats.quantiles(datos, n=100)  # Percentiles
stats.quantiles(datos, n=4, method='inclusive')  # Para muestras pequenas o discretas


# CORRELACION Y REGRESION  (Python 3.10+)
x = [<x1>, <x2>, <x3>, <x4>]
y = [<y1>, <y2>, <y3>, <y4>]   # Misma longitud que x

stats.correlation(x, y)         # Coeficiente de Pearson -> entre -1 y 1
stats.covariance(x, y)          # Covarianza entre dos variables

pendiente, intercepto = stats.linear_regression(x, y)
# pendiente  -> cuanto aumenta y por cada unidad de x
# intercepto -> valor de y cuando x = 0
# Prediccion: y_pred = pendiente * <nuevo_x> + intercepto


# DISTRIBUCIONES  (Python 3.8+)

# Normal (gaussiana) - campana de Gauss
dist_normal = stats.NormalDist(mu=<media>, sigma=<desv_std>)
dist_normal.pdf(<x>)            # Densidad de probabilidad en x
dist_normal.cdf(<x>)            # P(X <= x) -> probabilidad acumulada
dist_normal.inv_cdf(<p>)        # x tal que P(X <= x) = p  (percentil)
dist_normal.mean                # Media de la distribucion
dist_normal.stdev               # Desviacion estandar
dist_normal.zscore(<x>)         # Z-score -> cuantas sigma esta x de la media

# Combinar distribuciones (suma y diferencia de variables aleatorias)
dist_a = stats.NormalDist(mu=<m1>, sigma=<s1>)
dist_b = stats.NormalDist(mu=<m2>, sigma=<s2>)
dist_a + dist_b                 # Suma de dos distribuciones normales independientes
dist_a - dist_b                 # Diferencia

# Ajustar automaticamente mu y sigma desde tus datos
dist_datos = stats.NormalDist.from_samples(datos)


# PATRON DE USO HABITUAL
datos = [<v1>, <v2>, <v3>, <v4>, <v5>]

resumen = {
    "media":     stats.mean(datos),
    "mediana":   stats.median(datos),
    "moda":      stats.multimode(datos),
    "varianza":  stats.variance(datos),
    "desv_std":  stats.stdev(datos),
    "cuartiles": stats.quantiles(datos, n=4),
}

for clave, valor in resumen.items():
    print(f"{clave:>10}: {valor}")
