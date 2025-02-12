import requests
from datetime import datetime

def GitHub_report():

    user_name = input("Introduce el nombre del usuario de Git Hub: ")

    base_url = "https://api.github.com"
    user_url = f"{base_url}/users/{user_name}" #Acceso al perfil del usuario

    user_data = requests.get(user_url).json()

    now_date_utc = datetime.now()
    """ active_time = now_date_utc - user_data.get("created_at") """
    print(now_date_utc) #Me da la hora correctamente
    print(user_data) #Estoy viendo que parámetro me daría la fecha de creación, porque tengo problemas con "created_at". No sé si es porque no puedo hacer más
                     #peticiones o porque está mal


    
    #Lo demás está practicamente bien, pero no me es necesario para comprobar el tiempo.

    """ if "status" in user_data and user_data["status"] == "404":
        print(f"Usuario {user_name} no encontrado.")
        return
    
    report = {
        "Nombre": user_data.get("name", "None"),
        "Fecha de creación": user_data.get("created_at"),
        "Tiempo de uso": active_time,
        "Repositorios": user_data.get("public_repos", 0)
    }

    for key, value in report.items():
        print(f"{key}: {value}")

    repository_url = user_data["repos_url"] #Acceso a la url de repositorios dentro del perfil de usuario
    repository_data = requests.get(repository_url).json() 

    for repo in repository_data:

        print(f"\nNombre de repositorio: {repo.get("name")}")


        language_url = repo.get("languages_url") #Acceso a la url de lenguajes dentro de los repositorios
        language_data = requests.get(language_url).json()

        for key in language_data.items():
            languages = [] 
            languages.append(list(key[0]))
            print(f"Lenguaje más usado: {languages[0]}")
            print(f"Lenguajes usados: {languages}")#Tengo que arreglar esto. Necesito que se va un listado de los lenguajes y no que se imprima el nombre de cada uno

#Hay que probar la cuenta atrás que se añade en el report """

GitHub_report()