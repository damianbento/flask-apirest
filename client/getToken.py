from getpass import getpass
import requests

def realizar_solicitud(url, data):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=data, headers=headers)
    return response

def main():
    try:
        username = input("Ingresa el nombre de usuario: ")
        password = getpass("Ingrese el password: ")
        url = "http://xxx.xxx.xxx.xxx:3000/api/login"  # Reemplaza esto con la URL de tu API
        data = {
            username: "usuario",
            password: "contrasena"

        }

        response = realizar_solicitud(url, data)

        if response.status_code == 200:
            print("Solicitud exitosa:")
            print(response.json())
        else:
            print("Error en la solicitud:")
            print(f"Código de estado: {response.status_code}")
            print(response.json())

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
