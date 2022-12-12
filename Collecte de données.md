__________________________________________________________________________________________________

# Collecte de données

__________________________________________________________________________________________________

### Introduction

Ce rapport fait référence à la partie collecte de données de la SAÉ 24. Cette collecte de données consistait en la connexion à un broker mqtt puis d'en extraire les données afin de les envoyer  dans une base de données SQL ou dans un fichier csv. 



### Connexion au broker

Pour la connexion au borker nous avons besoin de définir

- Sur quel broker faut-il se connecter

- Quel est sont topic

- Sur quel port faut-il se connecter
  
  Ensuite on vérifie que la connexion est bien établie avec le broker

```python
'''
------------------------------------------------------------------------------------------------------------------------
Definition des variables pour la connexion  au broker 
------------------------------------------------------------------------------------------------------------------------
'''

broker = 'test.mosquitto.org'  # subscribe topic
port = 1883
topic = "IUT/Colmar/SAE24/Maison1"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'

iddonnees = 0

'''
------------------------------------------------------------------------------------------------------------------------
Connexion au Broker Mqtt
------------------------------------------------------------------------------------------------------------------------
'''

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


```

### Connexion à la base SQL

Pour se connecter à la base SQL il faut définir 

- L'adresse du serveur SQL (ici il est en local)

- Dans quelle base doit-on travailler 

- Avec quel utilisateur et mot de passe si il y en a un 

```python
'''
------------------------------------------------------------------------------------------------------------------------
Connexion à la base SQL
------------------------------------------------------------------------------------------------------------------------
'''

mydb = mysql.connector.connect(
    host="localhost",
    user="toto",
    password="toto",
    database="sae24"
)

mycursor = mydb.cursor()
```

### Traitement des données

- Tout d'abord on trie le message afin de récupérer les informations essentiels

- Ensuite on écrit les données dans un fichierr csv pour chaque capteur 

- Enfin on envoie les données dans la base SQL 

```python
'''
------------------------------------------------------------------------------------------------------------------------
Traitement des donnnées
------------------------------------------------------------------------------------------------------------------------
'''
def traiter_donnee(chaine):
    chaine = chaine.split(",")
    id = chaine[0].split("=")[1]
    piece = chaine[1].split("=")[1]
    date = chaine[2].split("=")[1]
    time = chaine[3].split("=")[1]
    temp = chaine[4].split("=")[1]
--------------------------------------------------------------------------------------------------------------------------
    if id == "B8A5F3569EFF":
        chaine = f"{id};{piece};{date};{time};{temp};"
        file = open("capteur1.csv", "a")  # Ecrit les donneés du capteur dans un fichier csv
        file.write(chaine + "\n")
        file.close()

    if id == "A72E3F6B79BB":
        chaine = f"{id};{piece};{date};{time};{temp};"
        file = open("capteur2.csv", "a")
        file.write(chaine + "\n")
        file.close()

---------------------------------------------------------------------------------------------------------------------------
    timestamp = date + " , " + time
    global iddonnees
    iddonnees += 1
    global mycursor
    sql = "INSERT INTO donnees (temperature,timestamp,capteur_idcapteur) VALUES ( %s, %s, %s)"
    if id == 'A72E3F6B79BB':
        val = (temp, timestamp, 2)
    if id == "B8A5F3569EFF":
        val = (temp, timestamp, 1)
    mycursor.execute(sql, val)

    mydb.commit()

```

#### Envoie des données sur le client Mqtt

On envoie un message de confirmation comme quoi l'information mqtt est bien reçu 

```python
'''
------------------------------------------------------------------------------------------------------------------------
Envoie des données sur le client Mqtt
------------------------------------------------------------------------------------------------------------------------
'''
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        traiter_donnee(msg.payload.decode())
        print(f"Recived {msg.payload.decode()}from {msg.topic} topic")
    client.subscribe(topic)
    client.on_message = on_message

```
