from animal_shelter import AnimalShelter

# Connection details
USER = 'aacuser'
PASS = 'SAMPSONSNHUCS340'
HOST = 'nv-desktop-services.apporto.com'
PORT = 33567
DB = 'AAC'
COL = 'animals'

# Initialize AnimalShelter
shelter = AnimalShelter(USER, PASS, HOST, PORT, DB, COL)

# Test data
test_animal = {
    "animal_id": "K22257",
    "name": "Kiko",
    "breed": "German Shepherd",
    "age": 3,
    "color": "Black/Tan"
}

print("=== CRUD OPERATION TESTING ===")

# CREATE Test
print("\n1. Testing CREATE operation...")
create_result = shelter.create(test_animal)
print(f"Create successful: {create_result}")

# READ Test
print("\n2. Testing READ operation...")
read_result = shelter.read({"animal_id": "K22257"})
if read_result:
    print("Found document:")
    print(read_result[0])
else:
    print("No matching document found")

# UPDATE Test
print("\n3. Testing UPDATE operation...")
update_result = shelter.update(
    {"animal_id": "K22257"},
    {"color": "Black/Brown", "age": 4}
)
print(f"Documents updated: {update_result}")

# Verify Update
updated_doc = shelter.read({"animal_id": "K22257"})[0]
print(f"Updated color: {updated_doc['color']}")
print(f"Updated age: {updated_doc['age']}")

# DELETE Test
print("\n4. Testing DELETE operation...")
delete_result = shelter.delete({"animal_id": "K22257"})
print(f"Documents deleted: {delete_result}")
print("Delete operation skipped (commented out for safety)")

print("\n=== TESTING COMPLETE ===")