Grazioso Salvare CRUD Operations BY JAMAR SAMPSON
Purpose
This Python module provides CRUD (Create, Read, Update, Delete) operations for the Grazioso Salvare project, allowing interaction with the MongoDB database containing animal shelter data.

Usage
MongoDB Driver
We use pymongo as the Python driver for MongoDB due to its ease of use and comprehensive documentation.

### CRUD Class
The `AnimalShelter` class provides the following methods:
- `create(data)`: Inserts a document into the database.
- `read(query)`: Queries documents from the database.
- `update(query, update_data)`: Updates documents in the database.
- `delete(query)`: Deletes documents from the database.


Example
Here's how to use the CRUD class:

from test_crud_operations import AnimalShelter

# Connection details
MONGO_HOST = 'nv-desktop-services.apporto.com'
MONGO_PORT = 33567
MONGO_USER = 'aacuser'
MONGO_PASS = 'SAMPSONSNHUCS340'
DB = 'AAC'
COLLECTION = 'animals'

# Instantiate the AnimalShelter class
shelter = AnimalShelter(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, DB, COLLECTION)

# Create a new document
test_animal = {
    "animal_id": "German Shepherd",
    "animal_type": "Dog",
    "breed": "German Shepherd Mix",
    "color": "Brown/Black",
    "date_of_birth": "2020-06-03",
    "outcome_type": "Adoption"
}
print("Create:", shelter.create(test_animal))

# Read documents
query = {"animal_id": "German Shepherd"}
results = shelter.read(query)
if results:
    print(results[0])  # Print first matching document

# Update documents
update_query = {"animal_id": "German Shepherd"}
update_data = {"color": "Black/Brown/Tan"}
print("Update:", shelter.update(update_query, update_data))

# Verify update
updated_doc = shelter.read({"animal_id": "German Shepherd"})
if updated_doc:
    print("Updated color:", updated_doc[0]["color"])

# Delete documents
delete_query = {"animal_id": "German Shepherd"}
print("Delete:", shelter.delete(delete_query))