import requests
import matplotlib.pyplot as plt
import argparse
import os
from datetime import datetime

def obtener_fecha_actual():
    hoy = datetime.today()
    fecha_formateada = hoy.strftime("%d/%m/%Y")
    return fecha_formateada

def obtener_forks(nombre_usuario, nombre_repo, token):
    # URL para obtener la lista de forks
    url_forks = f"https://api.github.com/repos/{nombre_usuario}/{nombre_repo}/forks"

    # Encabezados con el token de autenticación
    headers = {'Authorization': f'token {token}'}

    # Realizar una solicitud GET a la API de GitHub
    respuesta = requests.get(url_forks, headers=headers)

    if respuesta.status_code == 200:
        forks = respuesta.json()

        # Crear una lista para almacenar los nombres de usuario de quienes han hecho fork
        usuarios_forks = []

        for fork in forks:
            # Obtener el nombre de usuario del propietario del fork
            nombre_usuario_fork = fork['owner']['login']
            usuarios_forks.append(nombre_usuario_fork)

        return usuarios_forks
    else:
        return None

def obtener_actividad(nombre_usuario, nombre_repo, token):
    # Obtener la lista de usuarios que han hecho fork del repositorio
    usuarios_forks = obtener_forks(nombre_usuario, nombre_repo, token)
    
    if usuarios_forks:
        # Crear un diccionario para almacenar la actividad de cada usuario
        actividad_usuarios = {}

        for usuario in usuarios_forks:
            # Obtener la cantidad de commits del usuario en su repositorio fork
            url_contribuciones = f"https://api.github.com/repos/{usuario}/{nombre_repo}/commits?author={usuario}"
            headers = {'Authorization': f'token {token}'}
            respuesta_contribuciones = requests.get(url_contribuciones, headers=headers)
            if respuesta_contribuciones.status_code == 200:
                cantidad_contribuciones = 0
                for commit in respuesta_contribuciones.json():
                    if commit['author']['login'] == usuario:
                        cantidad_contribuciones += 1
                actividad_usuarios[usuario] = cantidad_contribuciones
                

        # Ordenar el diccionario por la cantidad de contribuciones (actividad)
        usuarios_ordenados = sorted(actividad_usuarios.items(), key=lambda x: x[1], reverse=True)

        return usuarios_ordenados
    else:
        print("No se encontraron forks del repositorio.")
        return None

def main(token):
    # Nombre de usuario y nombre del repositorio
    nombre_usuario = "andresmup"
    nombre_repo = "recursos-analisis-datos"

    # Obtener la lista de actividad de los usuarios que han hecho fork y han realizado commits en sus forks
    lista_actividad_usuarios = obtener_actividad(nombre_usuario, nombre_repo, token)

    #Selecciono el top 5
    top_5_actividad_usuarios = lista_actividad_usuarios[:5]

    #Si hay actividad hago el gráfico
    if top_5_actividad_usuarios:
        # Extraer nombres de usuarios y cantidad de commits
        nombres = [x[0] for x in top_5_actividad_usuarios]
        commits = [x[1] for x in top_5_actividad_usuarios]

        # Seleccionar una paleta de colores
        paleta_color = 'tab20b'
        colores =  plt.cm.get_cmap(paleta_color, len(top_5_actividad_usuarios))
        
        # Convertir el objeto ListedColormap en una lista de colores
        colores_lista = [colores(i) for i in range(len(top_5_actividad_usuarios))]
        
        # Crear el gráfico de barras
        plt.figure(figsize=(10,6))
        bars = plt.bar(nombres, commits, color=colores_lista)
        
        # Obtener la fecha actual
        fecha_actual = obtener_fecha_actual()

        # Añadir etiquetas y título
        plt.xlabel('Nombres usuarios')
        plt.ylabel('Cantidad de Commits')
        plt.title(f'Estudiantes con más actividad ({fecha_actual})')

        # Rotar los nombres en el eje x para mayor legibilidad
        plt.xticks(rotation=60)

        # Mostrar el valor encima de cada barra
        for bar, cantidad in zip(bars, commits):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), cantidad, ha='center', va='bottom')

        # Mostrar el gráfico
        plt.tight_layout()

        # Definir el nombre del gráfico
        filename = 'Top_5_most_actives_students.png'

        # Ruta de la carpeta donde deseas guardar el archivo
        folder_path = 'actions_resources'

        # Verificar si la carpeta existe, si no, crearla
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Ruta completa del archivo
        full_path = os.path.join(folder_path, filename)

        # Verificar si el archivo ya existe y eliminarlo si es necesario
        if os.path.exists(full_path):
            os.remove(full_path)

        # Guardar el gráfico
        plt.savefig(full_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script que utiliza un token.")
    parser.add_argument("token", help="Token a utilizar.")
    args = parser.parse_args()
    main(args.token)