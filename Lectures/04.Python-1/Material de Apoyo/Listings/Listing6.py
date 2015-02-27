carros = 100
espacio_en_un_carro = 4.0
conductores = 30
pasajeros = 90
carros_no_manejados = carros - conductores
carros_manejados = conductores
capacidad_de_carpooling = carros_manejados * espacio_en_un_carro
promedio_de_pasajeros_por_carro = pasajeros / carros_manejados


print "Existen", carros, "carros disponibles"
print "Tan solo hay", conductores, "conductores disponibles."
print "Van a haber", carros_no_manejados, "carros vacios hoy"
print "Podemos llevar", capacidad_de_carpooling, "personas"
print "Tenemos", pasajeros, "personas para hacer carpooling"
print "Necesitamos al menos", promedio_de_pasajeros_por_carro, "en cada carro"