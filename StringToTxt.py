from azure.storage.blob import BlobServiceClient
import os

# Der zu speichernde Text
text_to_store = "Dies ist ein Beispieltext, der in einer Blob-Datei gespeichert wird."

# Lokale Datei erstellen
local_file_name = "beispiel.txt"
with open(local_file_name, "w", encoding="utf-8") as file:
    file.write(text_to_store)

# Verbindung zum Azure Blob Storage
connection_string = "<DefaultEndpointsProtocol=https;AccountName=azcominfraimport;AccountKey=PnR01Ed3w1lQZtgtPGzjmdU2sgj0yPTj/Co8pFGRhLswxAYz8GL4hwtpIYTlzomTa2BNFDvtHWog+AStu2WoZw==;EndpointSuffix=core.windows.net>"
container_name = "<janeriksmuckeligeecke>"

# BlobServiceClient erstellen
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Container-Client
container_client = blob_service_client.get_container_client(container_name)

# Blob-Client für die Datei
blob_client = container_client.get_blob_client(local_file_name)

# Datei hochladen
with open(local_file_name, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"Die Datei '{local_file_name}' wurde erfolgreich in den Blob-Speicher hochgeladen.")
