import os, uuid
import time
import sys
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


try:
    print("Azure Blob Storage Python quickstart sample")

    # Quickstart code goes here
    account_url: str = "https://aksbiswasa.blob.core.windows.net"
    # client_id: str = "c0c56602-ad3a-4396-b446-bd922800447f"
    # default_credential = DefaultAzureCredential(managed_identity_client_id=client_id)
    default_credential = DefaultAzureCredential()
    # Create the BlobServiceClient object
    blob_service_client: BlobServiceClient = BlobServiceClient(account_url, credential=default_credential)
    container_name: str = "container"
    blob_name: str = "demo.txt"

    # Create a local directory to hold blob data
    local_path = "./data"
    os.mkdir(local_path)
    local_file_name = str(uuid.uuid4()) + ".txt"


    download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
    container_client = blob_service_client.get_container_client(container= container_name) 
    print("\nDownloading blob to \n\t" + download_file_path)

    with open(file=download_file_path, mode="wb") as download_file:
        download_file.write(container_client.download_blob(blob_name).readall())

    print("Download completed")
    input("Enter any key to quit.") 
    sys.exit()

except Exception as ex:
    print('Exception:')
    print(ex)