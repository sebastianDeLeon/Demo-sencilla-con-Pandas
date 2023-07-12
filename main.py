from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

# Realizar en Python o R lo siguiente.
data = pd.read_csv("avocado.csv")

print("1. Obtener Cuantas filas y cuantas columnas tiene el conjunto de datos")
print(data.shape)

print("\n2. Mostrar los primeros 100 registros")
print(data.head(100))

print("\n3. Mostrar los últimos 20 registros")
print(data.tail(20))

print("\n4. Cual es el precio mínimo, máximo y promedio del aguacate en ese conjunto de datos")
print("El precio minimo es:",data["AveragePrice"].min())
print("El precio maximo es:",data["AveragePrice"].max())

print("\n5.Generar un gráfico de tipo scatter usando  para la x la variable 'year' y  para y la variable 'AveragePrice' para 3 regiones (las que usted elija), los 3 sub-conjuntos deben mostrarse en el mismo gráfico.")
region = data[data["region"] == "SanDiego"]
region1 = data[data["region"] == "StLouis"]
region2 = data[data["region"] == "Seattle"]

g1 = plt.subplot()
region.plot(x = 'year', y = 'AveragePrice', kind = 'scatter', color = 'red', ax = g1)
region1.plot(x = 'year', y = 'AveragePrice', kind = 'scatter', color = 'green', ax = g1)
region2.plot(x = 'year', y = 'AveragePrice', kind = 'scatter', color = 'blue', ax = g1)
plt.show()


# x = data[data["region"] == "StLouis"]
#
# print(x)

#imprimir el objeto de datos

# print(pd.DataFrame(data,columns = ["AveragePrice","year","type"]))
# print(data.columns)
# print(type(data))
