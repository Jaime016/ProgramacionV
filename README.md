
```

## Instalar Python
Asegurate de tener Python instalado. Recomendado: Python 3.10 o superior
Podés verificarlo con:
```bash
python --version
```
## Crear un entorno virtual
Desde la raíz del proyecto:

```bash
python -m venv venv
```
Activar el entorno:

Windows:
```bash
venv\Scripts\activate
```
Linux/Mac:
```bash
source venv/bin/activate
```

## Instalar Django y otras dependencias
Con el entorno virtual activado, ejecutá:
```bash
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary matplotlib seaborn pandas
```
O desde un archivo requirements.txt:
```bash
pip install -r requirements.txt
```

## Crear un nuevo proyecto Django
```bash
django-admin startproject login_project
cd login_project
```
## Creación de las aplicaciones
```bash
python manage.py startapp users     # Para autenticación y usuarios
python manage.py startapp libros    # Para libros, autores, géneros, calificaciones
```

## Crear la base de datos
En PGAdmin crear la base de datos Biblioteca y se configura la conexion a la base de datos:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'login_project_db',
        'USER': 'login_user',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
# ¿Cómo funciona la aplicación?
## Autenticación y usuarios:
Los usuarios pueden registrarse con un nombre de usuario y contraseña (/api/register/).

Luego, inician sesión para obtener un token JWT (/api/token/).

Ese token se usa para acceder a rutas protegidas (perfil, gestión de libros, etc.) enviándolo en los headers con Authorization: Bearer <token>.

## Gestión de libros:

La app libros permite crear, leer, actualizar y eliminar libros.

Cada libro está relacionado con un autor, un género y puede tener calificaciones.

Se puede cargar libros de a uno o en carga masiva (varios libros desde un JSON en Postman).

## Base de datos:

Se usa PostgreSQL para almacenar usuarios, libros, autores, géneros y calificaciones.

Los modelos están definidos para guardar las relaciones y atributos.

## Análisis y reportes:

Se exportan los datos de libros y calificaciones a CSV.

Un script externo usa pandas y matplotlib para generar gráficos (promedio de calificaciones, distribución de géneros, libros por autor, etc.).

Estos gráficos se guardan como imágenes en una carpeta graficos/ para análisis visual.

## En uso cotidiano:
Un usuario se registra y loguea.

Puede ver o modificar libros (si tiene permisos).

Se cargan datos masivamente para acelerar el proceso.

Los administradores o analistas pueden correr el script para obtener reportes gráficos automáticos que resumen el estado de la colección y calificaciones.

## Postman
### Registrarse
```http
GET http://127.0.0.1:8000/api/register/
```
Json:
```json
{
  "username": "Jaime",
  "password": "12345678"
}
```
![image](https://github.com/user-attachments/assets/352a4fba-f7af-4d46-9a22-f5a07cd91060)

## Token
```http
POST http://127.0.0.1:8000/api/token/ 
```
Json:
```json
{
    "username": "Jaime",
    "password": "12345678"
}
```
![image](https://github.com/user-attachments/assets/f24bc998-884b-49c8-b0dd-cafc1e069e7f)

## Libros
### Listar Todos los Libros
```http
GET http://127.0.0.1:8000/api/libros/
```
Para acceder a los endpoints protegidos, enviá el token en el header:
```bash
Authorization: Bearer <token>
```
![image](https://github.com/user-attachments/assets/68b2aabd-388d-4157-b402-88e609b6d7c9)

### Obtener por ID
```http
GET http://127.0.0.1:8000/api/libros/10/
```
Para acceder a los endpoints protegidos, enviá el token en el header:
```bash
Authorization: Bearer <token>
```
![image](https://github.com/user-attachments/assets/2d379ab9-2c28-4ff9-adb1-911a651fada5)

### Insertar
```http
POST http://127.0.0.1:8000/app/libros/
```
Json:
```json
{
    "numero": 0,
    "id": 10,
    "titulo": "Luces y sombras",
    "autor": 20,
    "genero": 6,
    "calificacion": 3
}
```
Para acceder a los endpoints protegidos, enviá el token en el header:
```bash
Authorization: Bearer <token>
```
![image](https://github.com/user-attachments/assets/99bead0a-302c-424d-9222-197a52ac7007)

### Actualizar
```http
PUT http://127.0.0.1:8000/api/libros/10/
```
Se pasa el ID del libro en la URL.
Json:
```json
{
    "numero": 0,
    "id": 10,
    "titulo": "Luces y sombras",
    "autor": 22,
    "genero": 6,
    "calificacion": 2
}
```
Para acceder a los endpoints protegidos, enviá el token en el header:
```bash
Authorization: Bearer <token>
```
![image](https://github.com/user-attachments/assets/d1e60c45-f435-4778-a9d4-aec52dba3581)

### Eliminar
```http
DELETE http://127.0.0.1:8000/api/libros/10/
```
Se pasa el ID del libro en la URL.

Para acceder a los endpoints protegidos, enviá el token en el header:
```bash
Authorization: Bearer <token>
```
![image](https://github.com/user-attachments/assets/fdc48fae-beae-4957-b4c8-6a2eecb2f387)


## Codigo del View:
Codigo para Listar todos y Insertar:
```python
from rest_framework import viewsets
from .models import Libro, Autor, Genero, Calificacion
from .serializers import LibroSerializer, AutorSerializer, GeneroSerializer, CalificacionSerializer

# Vista para Libros
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

# Vista para Autores
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

# Vista para Géneros
class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

# Vista para Calificaciones
class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer
```

Codigo para obtener por id, actualizar y eliminar.
```python
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    # Obtener un libro por ID (ya incluido con GET /api/libros/<id>/)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    # Actualizar libro por ID (ya incluido con PUT/PATCH)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # Eliminar libro por ID (ya incluido con DELETE)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
```

# Reportes gráficos automáticos
La aplicación incluye un comando personalizado para generar 10 reportes gráficos sobre libros, calificaciones, géneros y usuarios, utilizando Pandas, Seaborn y Matplotlib.

Cómo ejecutar el script
Desde la terminal, ejecutar:

```bash
python manage.py reportes
```
Esto generará las gráficas en formato .png dentro de una carpeta reportes/ en la raíz del proyecto.

## Reportes generados

```bash
python manage.py reportes
```

### UN PROMEDIO DE CALIFICACIONES POR LIBROS
Archivo: promedio_calificaciones_por_autor.png

Descripción: Muestra un promedio de calificaciones por libros 

Ejemplo visual:

![promedio_calificaciones_por_autor](https://github.com/user-attachments/assets/cd6f53bd-389c-4c1a-8655-5f36adadd8ee)


### UN PROMEDIO DE CALIFICACIONES POR LIBROS
Archivo: numero_calificaciones_por_libro.png

Descripción: Muestra un numero de calificaciones por libros 

Ejemplo visual:

![numero_calificaciones_por_libro](https://github.com/user-attachments/assets/fba060df-6253-49df-ad69-5711d927547a)

### TOP DE DISTRIBUCION DE GENERO
Archivo: distribucion_generos_top10.png

Descripción: Muestra las distribuciones de los generos 

Ejemplo visual:

![distribucion_generos_top10](https://github.com/user-attachments/assets/16ac92a0-9c6b-43c2-8b23-df8eb6e4361a)


### TOP DE CALIFICACIONES 
Archivo: distribucion_calificaciones.png

Descripción: muestra una distribuccion de calificaciones 

Ejemplo visual:

![distribucion_calificaciones](https://github.com/user-attachments/assets/aa8610c6-0229-430d-ac59-1dd9a9315ae0)


### TOP CALIFICACION POR AUTOR
Archivo: cantidad_libros_por_autor.png

Descripción: Muestra la calificacion segun los autores

Ejemplo visual:

![cantidad_libros_por_autor](https://github.com/user-attachments/assets/0371149e-6b48-48e6-931c-d409ffd8fce7)


## Recomendaciones por Género
Este proyecto incluye un comando personalizado que permite obtener una lista de los libros mejor calificados dentro de un género específico.

### Archivo
```bash
libros/management/commands/libros_por_genero.py
```

### ¿Qué hace este script?
-ejecuta un comando personalizado de Django definido en libros/management/commands/libros_por_genero.py.
-Este comando realiza consultas a la base de datos y muestra en consola los libros mejor calificados por género.
-Es útil para generar reportes o tareas administrativas directamente desde la terminal.

### Ejecución
Para ejecutarlo, usá el siguiente comando:
```bash
python manage.py recomendaciones
```
Luego, el sistema te pedirá que ingreses un ID de género:

Y el resultado se verá así:

![image](https://github.com/user-attachments/assets/14338d8d-5ff0-4514-b469-1c088717f0d5)

### Validaciones
Si se ingresa un ID que no es un número, muestra un error.

Si no se encuentran libros para ese género, informa al usuario con una advertencia.

# Licencia
Este proyecto está licenciado bajo los términos de la Licencia MIT.

### Licencias de terceros
Este proyecto utiliza varias bibliotecas de terceros. A continuación, se listan junto con sus respectivas licencias:
```html
 Name                           Version      License
 Django                         5.2.3        BSD License
 PyJWT                          2.9.0        MIT License
 asgiref                        3.8.1        BSD License
 contourpy                      1.3.2        BSD License
 cycler                         0.12.1       BSD License
 djangorestframework            3.16.0       BSD License
 fonttools                      4.58.4       MIT
 kiwisolver                     1.4.8        BSD License
 matplotlib                     3.10.3       Python Software Foundation License
 numpy                          2.3.1        BSD License
 packaging                      25.0         Apache Software License; BSD License
 pandas                         2.3.0        BSD License
 pillow                         11.3.0       UNKNOWN
 psycopg2-binary                2.9.10       GNU Library or Lesser General Public License (LGPL)
 pyparsing                      3.2.3        MIT License
 python-dateutil                2.9.0.post0  Apache Software License; BSD License
 pytz                           2025.2       MIT License
 seaborn                        0.13.2       BSD License
 six                            1.17.0       MIT License
 sqlparse                       0.5.3        BSD License
 tzdata                         2025.2       Apache Software License
```
