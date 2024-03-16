# main.py
from jsonDB import JsonDB  # Assuming your class is saved in a file named jsondb.py

def main():
    # Initialize the database
    db = JsonDB('data.json')

    # Storing various types of values
    db['string'] = 'Hello, World!'  # Store a string
    db['number'] = 42  # Store a number
    db['list'] = [1, 2, 3, 4, 5]  # Store a list
    db['dict'] = {'key': 'value', 'another_key': 123}  # Store a dictionary

    # Retrieving and displaying a stored value
    print("The stored string:", db['string'])
    print("The stored number:", db['number'])
    print("The stored list:", db['list'])
    print("The stored dict:", db['dict'])

    # Demonstrating the get method (similar to __getitem__, but safer)
    print("Using get to retrieve the number:", db.get('number'))  # Same as db['number']
    print("Using get to try retrieving a non-existent key (returns None):", db.get('non_existent_key'))

    # Deleting an item
    del db['number']  # Delete the 'number' entry
    print("After deleting 'number', trying to retrieve it (should show None):", db.get('number'))

    # Demonstrating the keys method with a regex pattern
    # First, let's add a few more items to provide a good example for searching keys
    db['user_id_123'] = {'name': 'Alice'}
    db['user_id_456'] = {'name': 'Bob'}
    db['config_value'] = True

    # Now, let's find all keys that start with 'user_id'
    matching_keys = db.keys('^user_id_')
    print("Keys that match '^user_id_':", matching_keys)

    # Showing all keys with an empty query (should return all keys)
    all_keys = db.keys()
    print("All keys in the database:", all_keys)

if __name__ == '__main__':
    main()
