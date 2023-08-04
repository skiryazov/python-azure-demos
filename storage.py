from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connection_string = "your_connection_string_here"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = "your_container_name_here"
container_client = blob_service_client.get_container_client(container_name)

blob_name = "your_blob_name_here"
blob_client = container_client.get_blob_client(blob_name)

blob_data = blob_client.download_blob()
blob_contents = blob_data.content_as_text()

print(blob_contents)