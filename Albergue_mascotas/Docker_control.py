from os import system
import os

def menu():
    print('\n##########################')
    print('#    Control de docker   #')
    print('##########################\n')

    print('======================')
    print('Seleccione una opción')
    print('======================\n')

    print("\n1. Ver imágenes creadas.")
    print("2. Ver contenedores activos y desactivos.")
    print("3. Ver último contenedor creado.")
    print("4. Borrrar contenedor con id de imágen.")
    print("5. Construir contenedor de Django.")
    print("6. Publicando contenedor de Django.")
    print("7. Borrrar contenedor con id de contenedor.")
    print("8. Buil con docker composer.")
    print("9. Up con docker compose.")
    print("10. Down con docker compose.")
    print("11. Makemigrations docker-compose -> Django.")
    print("12. Migrate docker-compose -> Django.")
    print("13. Collectstatic docker-compose -> Django.")
    print("14. Ingresar a contenedor.")
    print("15. Iniciar docker desktop.")
    print("16. Docker create y push a docker hub.")
    print("17. Docker login.")
    print("18. Salir.\n")


while True:
    menu()
    opc = input("Ingrese una opción: ")
    os.system ("clear")

    if opc == '1':
        print('=================================================================================')
        print("Mostrando lista de imáges")
        print("\nsudo docker image ls\n")
        system(f"sudo docker image ls")
        print('=================================================================================')


    elif opc == '2':
        print('=================================================================================')
        print("Mostrando contenedores activos y desactivos")
        print("\nsudo docker ps -a\n")
        system(f"sudo docker ps -a")
        print('=================================================================================')


    elif opc == '3':
        print('=================================================================================')
        print("Mostrando último contenedor creado")
        print("\nsudo docker ps -l\n")
        system(f"sudo docker ps -l")
        print('=================================================================================')


    elif opc == '4':
        print('=================================================================================')
        print("Mostrando lista de imáges")
        print("\nsudo docker image ls\n")
        system(f"sudo docker image ls")

        print("\nBorrando contenedor con id de imágen")
        image = input("\nIngrese ID de imágen: ")
        print(f"\nsudo docker rmi -f {image}\n")
        system(f"sudo docker rmi -f {image}")
        print('=================================================================================')


    elif opc == '5':
        print('=================================================================================')
        print("Construyendo contenedor de Django\n")
        nombre = input("Ingrese el nombre para su contenedor: ")
        tag = input("Ingrese el nombre del tag: ")
        print(f'\nsudo docker build -t "{nombre}:{tag}" .\n')
        system(f'sudo docker build -t "{nombre}:{tag}" .')
        print('=================================================================================')


    elif opc == '6':
        print('=================================================================================')
        print("Publicando contenedor de Django\n")
        nombre = input("Ingrese el nombre para su contenedor: ")
        print(f"\nsudo docker run --publish 8000:8000 {nombre}\n")
        system(f"sudo docker run --publish 8000:8000 {nombre}")
        print('=================================================================================')


    elif opc == '7':
        print('=================================================================================')
        print("Mostrando contenedores activos y desactivos")
        print("\nsudo docker ps -a\n")
        system(f"sudo docker ps -a")

        print("\nBorrando contenedor con id de contenedor\n")
        contenedor = input("Ingrese ID del contenedor: ")
        print(f"\nsudo docker rm -f {contenedor}\n")
        system(f"sudo docker rm -f {contenedor}")
        print('=================================================================================')


    elif opc == '8':
        print('=================================================================================')
        print("Buil con docker composer\n")
        print(f"\nsudo COMPOSE_HTTP_TIMEOUT=200 docker-compose up --build\n")
        system(f"sudo COMPOSE_HTTP_TIMEOUT=200 docker-compose up --build")
        print('=================================================================================')

    elif opc == '9':
        print('=================================================================================')
        print("Up con docker compose\n")
        print(f"\nsudo COMPOSE_HTTP_TIMEOUT=200 docker-compose up -d\n")
        system(f"sudo COMPOSE_HTTP_TIMEOUT=200 docker-compose up -d")
        print('=================================================================================')

    elif opc == '10':
        print('=================================================================================')
        print("Down con docker compose\n")
        print(f"\nsudo COMPOSE_HTTP_TIMEOUT=200 docker-compose down\n")
        system(f"sudo COMPOSE_HTTP_TIMEOUT=200 docker-compose down")
        print('=================================================================================')

    elif opc == '11':
        print('=================================================================================')
        print("Makemigrations docker-compose -> Django\n")
        print(f"\nsudo COMPOSE_HTTP_TIMEOUT=200 docker-compose run django_app python manage.py makemigrations\n")
        system(f"sudo COMPOSE_HTTP_TIMEOUT=200 docker-compose run django_app python manage.py makemigrations")
        print('=================================================================================')

    elif opc == '12':
        print('=================================================================================')
        print("Migrate docker-compose -> Django\n")
        print(f"\nsudo COMPOSE_HTTP_TIMEOUT=200 docker-compose run django_app python manage.py migrate\n")
        system(f"sudo COMPOSE_HTTP_TIMEOUT=200 docker-compose run django_app python manage.py migrate")
        print('=================================================================================')

    elif opc == '13':
        print('=================================================================================')
        print("Collectstatic docker-compose -> Django\n")
        print(f"\nsudo COMPOSE_HTTP_TIMEOUT=200 docker-compose run django_app python manage.py collectstatic\n")
        system(f"sudo COMPOSE_HTTP_TIMEOUT=200 docker-compose run django_app python manage.py collectstatic")
        print('=================================================================================')

    elif opc == '14':
        print('=================================================================================')
        print("Borrando contenedor con id de contenedor\n")
        contenedor = input("Ingrese ID del contenedor: ")
        print(f"\nsudo docker exec -it {contenedor} psql -U postgres\n")
        system(f"sudo docker exec -it {contenedor} psql -U postgres")
        print('=================================================================================')

    elif opc == '15':
        print('=================================================================================')
        print("Iniciando docker desktop\n")
        print(f"\nsudo systemctl --user start docker-desktop\n")
        system(f"sudo systemctl --user start docker-desktop")
        print('=================================================================================')

    elif opc == '16':
        print('=================================================================================')
        print("Docker login\n")
        print(f"\nsudo docker login\n")
        system(f"sudo docker login")



        print("\nMostrando lista de imáges")
        print("\nsudo docker image ls\n")
        system(f"sudo docker image ls")



        print("\nDocker create y push a docker hub\n")
        usuario = input("Nombre de usuario: ")
        repositorio = input("Nombre del repositorio de imágen: ")
        tag = input("Nombre del tag de la imágen: ")

        print("\nCreando variante")

        print(f"\nsudo docker tag {repositorio} {usuario}/{repositorio}:{tag}\n")
        system(f"sudo docker tag {repositorio} {usuario}/{repositorio}:{tag}")

        print(f"\nPush a repository de {usuario}.")
        print(f"\nsudo docker push {usuario}/{repositorio}:{tag}\n")
        system(f"sudo docker push {usuario}/{repositorio}:{tag}")

        print('=================================================================================')

    elif opc == '17':
        print('=================================================================================')
        print("Docker login\n")
        print(f"\nsudo docker login\n")
        system(f"sudo docker login")
        print('=================================================================================')


    elif opc == '18':
        print('===================')
        print("||   Saliendo.   ||")
        print('===================')
        break


    else:
        menu()
        opc = input("Ingrese una opción: ")
        os.system ("clear")


'''
#############################################
#   Menú creado por:                        #
#       Héctor Fernando Carrera Soto        #
#       Github: https://github.com/hefecaso #
#############################################
'''
