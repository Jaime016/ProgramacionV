import pandas as pd
import matplotlib.pyplot as plt

# Cargar CSV
df = pd.read_csv('LibrosAnibal.csv')

# 1. Libro con mejor calificación
max_puntaje = df['calificacion_puntaje'].max()
mejores_libros = df[df['calificacion_puntaje'] == max_puntaje]
print("Libro(s) con mejor calificación:")
print(mejores_libros[['titulo', 'autor', 'calificacion_puntaje']])

# 2. Autor con más libros
autor_mas_libros = df['autor'].value_counts()
autor_mas_libros.plot(kind='bar', title='Cantidad de libros por autor')
plt.savefig('graficos/libros_por_autor.png')
plt.show()

# 3. Género más popular
genero_mas_popular = df['genero'].value_counts()
genero_mas_popular.plot(kind='pie', title='Géneros más populares', autopct='%1.1f%%')
plt.savefig('graficos/generos_populares.png')
plt.show()
