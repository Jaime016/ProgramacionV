import pandas as pd
import matplotlib.pyplot as plt

# Cargar CSV
df = pd.read_csv('Libros.csv')

# 1. Libro con mejor calificación
max_puntaje = df['calificacion_puntaje'].max()
mejores_libros = df[df['calificacion_puntaje'] == max_puntaje]
print("Libro(s) con mejor calificación:")
print(mejores_libros[['titulo', 'autor', 'calificacion_puntaje']])

# 2. Autor con más libros
autor_mas_libros = df['autor'].value_counts()
plt.figure(figsize=(10, 6))
autor_mas_libros.plot(kind='bar', title='Cantidad de libros por autor', color='skyblue', edgecolor='black')
plt.xlabel("Autor")
plt.ylabel("Cantidad de Libros")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('graficos/libros_por_autor.png', dpi=300)
plt.close()

# 3. Género más popular
genero_mas_popular = df['genero'].value_counts()
plt.figure(figsize=(8, 8))
genero_mas_popular.plot(kind='pie', title='Géneros más populares', autopct='%1.1f%%',
                        startangle=140, colors=plt.cm.Pastel1.colors, wedgeprops={'edgecolor': 'black'})
plt.ylabel('')  # Ocultar eje Y
plt.tight_layout()
plt.savefig('graficos/generos_populares.png', dpi=300)
plt.close()
