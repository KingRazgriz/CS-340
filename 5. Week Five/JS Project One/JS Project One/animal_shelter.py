from pymongo import MongoClient

class AnimalShelter:
    """CRUD operations for Animal Collection in MongoDB."""

    def __init__(self, username, password, host, port, db, collection):
        """Start the MongoClient & the database with collection names."""
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
        self.database = self.client[db]
        self.collection = self.database[collection]

    def create(self, data):
        """Add new documentation into the collection."""
        if data is not None:
            result = self.collection.insert_one(data)
            return True if result.acknowledged else False
        else:
            raise Exception("Cannot save due to data parameter being empty.")

    def read(self, query):
        """Call for documents in the collection."""
        if query is not None:
            cursor = self.collection.find(query)
            return [doc for doc in cursor]
        else:
            raise Exception("Call parameter is empty.")
            
    def update(self, query, update_data):
        """Update documents - returns count modified"""
        if not query or not update_data:
            raise Exception("Need both query and update data")
        return self.collection.update_many(query, {"$set": update_data}).modified_count

    def delete(self, query):
        """Delete - Remove documents"""
        if query:
            return self.collection.delete_many(query).deleted_count
        raise Exception("Nothing to delete - query parameter empty")

# Example usage demonstraing all CRUD operations.
if __name__ == "__main__":
    USER = 'aacuser'
    PASS = 'SAMPSONSNHUCS340'
    HOST = 'nv-desktop-services.apporto.com'
    PORT = 33567
    DB = 'AAC'
    COL = 'animals'

     # Initialize the connection.
    shelter = AnimalShelter(USER, PASS, HOST, PORT, DB, COL)
    
    # Test the data.
    sample_data = {"animal_id": "K22257", "name": "Kiko", "breed": "German Shepherd"}
     
    # CREATE the test.
    print("CREATE:", shelter.create(sample_data))  # True if successful.
    
    # READ the test.
    print("READ:", shelter.read({"animal_id": "K22257"}))  # Returns the document.
    
    # UPDATE the test.
    print("UPDATE:", shelter.update(
        {"animal_id": "K22257"}, 
        {"name": "Kiko Jr.", "age": 3}
    ))  # Returns the number of documents modified.
    
    # Verify the update.
    print("READ AFTER UPDATE:", shelter.read({"animal_id": "K22257"}))
    
    # DELETE the test.
    print("DELETE:", shelter.delete({"animal_id": "K22257"}))  # Returns the number deleted.
    
    # Verify deletion.
    print("READ AFTER DELETE:", shelter.read({"animal_id": "K22257"}))  # Should be empty.