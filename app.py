import requests 
import sys      

def get_joke():
    url_api = "https://v2.jokeapi.dev/joke/Any?lang=fr&type=single"
    
    print("Connexion à l'API des blagues...")

    try:
        
        response = requests.get(url_api, timeout=5)
        response.raise_for_status() 
        data = response.json()

        if data.get("error"):
            print(f"L'API a retourné une erreur : {data.get('message')}")
            sys.exit(1) 

        print("\n Voici la blague : ")
        print("="*30)
        print(f"Catégorie : {data['category']}")
        print(f"\n    {data['joke']}") 
        print("="*30)

    except requests.exceptions.Timeout:
        print("Erreur : La requête a pris trop de temps (timeout).")
    except requests.exceptions.RequestException as e:
        print(f"Erreur : Un problème est survenu avec la requête : {e}")
    except KeyError:
        print("Erreur : La réponse de l'API n'a pas le format attendu (clé 'joke' absente).")


if __name__ == "__main__":
    get_joke()
