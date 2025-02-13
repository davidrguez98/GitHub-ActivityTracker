import requests

def GitHub_report():

    user_name = input("Introduce el nombre del usuario de Git Hub: ")

    base_url = "https://api.github.com"
    user_url = f"{base_url}/users/{user_name}" #Acceso al perfil del usuario

    user_data = requests.get(user_url).json()

    if "status" in user_data and user_data["status"] == "404":
        print(f"Usuario {user_name} no encontrado.")
        return
    
    report = {
        "Nombre": user_data.get("name", "None"),
        "Fecha de creación": user_data.get("created_at"),
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
            languages.append(key)
            print(languages) #Quiero que me aparezcan todos los lenguajes que se han usado. Ya después representarlos en una lista y en una sección a parte el más usado.

GitHub_report()