import re
import json


class JsonDB:
    """A simple JSON-backed database class."""

    def __init__(self, filename='data.json'):
        """
        Initializes the database by loading data from a specified JSON file.

        :param filename: The path to the JSON file used for data storage. Defaults to 'data.json'.
        """
        self.filename = filename
        self._data = self.load_data()

    def load_data(self) -> dict:
        """
        Loads and returns the data from the JSON file specified by self.filename.

        If the file does not exist or contains invalid JSON, this method returns an empty dictionary.

        :return: A dictionary containing the data loaded from the JSON file.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_data(self):
        """
        Saves the current state of self._data to the JSON file specified by self.filename.

        The data is formatted with an indentation of 4 spaces for readability.
        """
        with open(self.filename, 'w') as file:
            json.dump(self._data, file, indent=4)

    def __setitem__(self, key: str, value):
        """
        Sets the value for a given key in the database and immediately saves the updated data to the JSON file.

        :param key: The key under which the value is stored.
        :param value: The value to be stored.
        """
        self._data[key] = value
        self.save_data()

    def __getitem__(self, key: str):
        """
        Retrieves the value for a given key from the database.

        :param key: The key whose value is to be retrieved.
        :return: The value associated with the given key.
        """
        return self._data[key]

    def __delitem__(self, key: str):
        """
        Deletes the entry associated with the given key from the database and saves the updated data to the JSON file.

        :param key: The key whose entry is to be deleted.
        """
        del self._data[key]
        self.save_data()

    def get(self, key: str):
        """
        Retrieves the value for a given key from the database, similar to __getitem__.

        :param key: The key whose value is to be retrieved.
        :return: The value associated with the given key.
        """
        if key in self._data.keys():
            return self._data[key]
        
        return None

    def keys(self, query: str = "") -> list:
        """
        Searches for and returns a list of keys that match a given query string or regex pattern.

        :param query: A string or regex pattern to match against the keys. If empty, all keys are returned.
        :return: A list of keys that match the query.
        """
        if not query:
            query = ""

        # Trying to compile the query into a regex pattern. If it fails, treat it as a normal string.
        try:
            pattern = re.compile(query)
        except re.error:
            pattern = None

        matching_keys = [key for key in list(self._data.keys()) if (pattern.search(key) if pattern else query in key)]

        return matching_keys
