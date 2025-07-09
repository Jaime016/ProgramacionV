import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Crear carpeta graficos si no existe
if not os.path.exists('graficos'):
    os.makedirs('graficos')

# Leer CSV y convertir calificacion_puntaje a numérico (float)
df = pd.read_csv('Libros.csv')
df['calificacion_puntaje'] = pd.to_numeric(df['calificacion_puntaje'], errors='coerce')

# Configurar estilo general
sns.set(style="whitegrid", font="DejaVu Sans", font_scale=1.2)

# 1. Calificación promedio por género
promedio_genero = df.groupby('genero')['calificacion_puntaje'].mean().sort_values(ascending=False)
plt.figure(figsize=(max(12, len(promedio_genero)), 6))
ax = sns.barplot(x=promedio_genero.index, y=promedio_genero.values,
                 palette="flare", hue=promedio_genero.index, dodge=False, legend=False, edgecolor="black")
plt.title('Calificación Promedio por Género', fontsize=18, weight='bold')
plt.ylabel('Promedio (1 a 5)')
plt.xlabel('Género')
plt.xticks(rotation=45, ha='right')
for i, val in enumerate(promedio_genero.values):
    ax.text(i, val + 0.05, f"{val:.2f}", ha='center', fontsize=11,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
sns.despine()
plt.tight_layout()
plt.savefig("graficos/promedio_calificaciones_por_genero.png", dpi=300)
plt.close()

# 2. Cantidad de libros por autor
libros_por_autor = df.groupby('autor').size().sort_values(ascending=False)
plt.figure(figsize=(max(12, len(libros_por_autor)), 6))
ax = sns.barplot(x=libros_por_autor.index, y=libros_por_autor.values,
                 palette="mako", hue=libros_por_autor.index, dodge=False, legend=False, edgecolor="black")
plt.title('Cantidad de Libros por Autor', fontsize=18, weight='bold')
plt.ylabel('Cantidad de Libros')
plt.xlabel('Autor')
plt.xticks(rotation=45, ha='right')
for i, val in enumerate(libros_por_autor.values):
    ax.text(i, val + 0.1, f"{val}", ha='center', fontsize=11,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
sns.despine()
plt.tight_layout()
plt.savefig("graficos/cantidad_libros_por_autor.png", dpi=300)
plt.close()

# 3. Distribución de géneros (pastel) - Top 10
generos = df['genero'].value_counts()
generos_top = generos.head(10)
plt.figure(figsize=(8, 8))
patches, texts, autotexts = plt.pie(
    generos_top.values,
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('pastel'),
    wedgeprops={'edgecolor': 'black'}
)
plt.legend(patches, generos_top.index, loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Distribución de los 10 Géneros Más Usados', fontsize=18, weight='bold')
plt.tight_layout()
plt.savefig("graficos/distribucion_generos_top10.png", dpi=300)
plt.close()

# 4. Promedio de calificaciones por autor
promedio_autor = df.groupby('autor')['calificacion_puntaje'].mean().sort_values(ascending=False)
plt.figure(figsize=(max(12, len(promedio_autor)), 6))
ax = sns.barplot(x=promedio_autor.index, y=promedio_autor.values,
                 palette="rocket", hue=promedio_autor.index, dodge=False, legend=False, edgecolor="black")
plt.title('Calificación Promedio por Autor', fontsize=18, weight='bold')
plt.ylabel('Promedio (1 a 5)')
plt.xlabel('Autor')
plt.xticks(rotation=45, ha='right')
for i, val in enumerate(promedio_autor.values):
    ax.text(i, val + 0.05, f"{val:.2f}", ha='center', fontsize=11,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
sns.despine()
plt.tight_layout()
plt.savefig("graficos/promedio_calificaciones_por_autor.png", dpi=300)
plt.close()

# 5. Número de calificaciones por libro (Top 20)
calificaciones_por_libro = df.groupby('titulo').size().sort_values(ascending=False).head(20)
plt.figure(figsize=(max(12, len(calificaciones_por_libro)), 6))
ax = sns.barplot(x=calificaciones_por_libro.index, y=calificaciones_por_libro.values,
                 palette="muted", hue=calificaciones_por_libro.index, dodge=False, legend=False, edgecolor="black")
plt.title('Número de Calificaciones por Libro (Top 20)', fontsize=18, weight='bold')
plt.ylabel('Cantidad de Calificaciones')
plt.xlabel('Libro')
plt.xticks(rotation=45, ha='right')
for i, val in enumerate(calificaciones_por_libro.values):
    ax.text(i, val + 0.1, f"{val}", ha='center', fontsize=11,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
sns.despine()
plt.tight_layout()
plt.savefig("graficos/numero_calificaciones_por_libro.png", dpi=300)
plt.close()

print("¡Todos los gráficos fueron generados y guardados en la carpeta 'graficos/'!")

