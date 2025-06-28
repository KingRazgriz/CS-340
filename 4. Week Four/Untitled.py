#!/usr/bin/env python
# coding: utf-8

# In[20]:


from test_crud_operations import AnimalShelter

# Connection details
MONGO_HOST = 'nv-desktop-services.apporto.com'
MONGO_PORT = 33567
MONGO_USER = 'aacuser'
MONGO_PASS = 'SAMPSONSNHUCS340'
DB = 'AAC'
COLLECTION = 'animals'

# Initialize connection
shelter = AnimalShelter(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, DB, COLLECTION)

# Test document with unique ID
test_animal = {
    "animal_id": "TEST_123",  # Change this for each test run
    "animal_type": "Dog",
    "breed": "German Shepherd Mix",
    "color": "Brown/Black",
    "date_of_birth": "2020-06-03",
    "outcome_type": "Adoption"
}

print("=== CRUD TESTING ===")

# CREATE
print("\n[CREATE] Adding test animal...")
create_result = shelter.create(test_animal)
print("Success:", create_result)

# READ
print("\n[READ] Fetching dogs (first 5 results):")
animal = shelter.read({"animal_type": "Dog"})[:5]
for doc in dogs:
    print(doc)

# UPDATE 
print("\n[UPDATE] Modifying dog colors...")
update_result = shelter.update(
    {"animal_id": "German Shepherd"},
    {"color": "Black/Brown/Tan"}
)
print("Documents updated:", update_result)

# Verify update
updated_doc = shelter.read({"animal_id": "German Shepherd"})[0]
print("\nUpdated document color:", updated_doc["color"])

# DELETE (commented out)
print("\n[DELETE] Safety check:")
delete_result = shelter.delete({"animal_id": "TEST_123"})
print("Documents deleted:", delete_result)
print("Delete operation not executed (commented out)")

print("\n=== TEST COMPLETE ===")


# In[ ]:





# In[ ]:




