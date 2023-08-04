# Run the following to install the library:
# pip install azure.cosmos.cosmos_client
import azure.cosmos.cosmos_client as cosmos_client
from azure.cosmos.partition_key import PartitionKey

# Initialize the Cosmos DB client
url = 'https://<INSERT_ACCOUNT>.documents.azure.com:443/'
key = '<INSERT_key>'
client = cosmos_client.CosmosClient(url, {'masterKey': key})

# Retrieve all items from the container
database_name = 'ToDoList' # Change the name if not using the default
container_name = 'Items' # Change the name if not using the default

db = client.create_database_if_not_exists(id=database_name)
container = db.create_container_if_not_exists(id=container_name, partition_key=PartitionKey(path='/id', kind='Hash'))


print('Reading all items in a container\n')

item_list = list(container.read_all_items(max_item_count=10))

print('Found {0} items'.format(item_list.__len__()))

for doc in item_list:
    print('Item Id: {0}'.format(doc.get('id')))
#    print('Name: {0}'.format(doc.get('name')))
