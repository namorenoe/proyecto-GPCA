import os
from data.processed.limpiar_datos import simular_datos
from scripts.analizar_datos import analizar_datos
from scripts.graficar_resultados import graficar_resultados
from scripts.generar_reporte import generar_reporte


# Simular datos
df = simular_datos()

# Analizar datos
analisis = analizar_datos(df)
print(analisis)

# Generar gráfico
graficar_resultados(df)

# Generar reporte
generar_reporte(df)

print("Proceso completado. Resultados guardados en la carpeta 'resultados'.")