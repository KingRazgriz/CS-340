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
print("\n[READ] Fetching test animal...")
# Fixed variable name from 'dogs' to 'animal'
animal = shelter.read({"animal_id": "TEST_123"})  # Query by animal_id instead of type
if animal:  # Check if document was found
    print(animal[0])
else:
    print("Animal not found")

# UPDATE 
print("\n[UPDATE] Modifying dog colors...")
# Fixed query to use animal_id instead of breed
update_result = shelter.update(
    {"animal_id": "TEST_123"},  # Changed from "German Shepherd"
    {"color": "Black/Brown/Tan"}
)
print("Documents updated:", update_result)

# Verify update
updated_doc = shelter.read({"animal_id": "TEST_123"})
if updated_doc:  # Check if document exists
    print("\nUpdated document color:", updated_doc[0]["color"])
else:
    print("\nDocument not found after update")

# DELETE (commented out)
print("\n[DELETE] Safety check:")
# delete_result = shelter.delete({"animal_id": "TEST_123"})  # Properly commented out
# print("Documents deleted:", delete_result)
print("Delete operation skipped (commented out for safety)")

print("\n=== TEST COMPLETE ===")