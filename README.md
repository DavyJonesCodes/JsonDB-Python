# JsonDB Project

The JsonDB Project provides a lightweight, file-based database system, designed to make data storage and retrieval simple and intuitive. Built in Python, it leverages the versatility of JSON for data manipulation, making it an ideal solution for small projects, prototypes, or for educational purposes where a full-scale database system isn't required.

## Features

- **Simple CRUD Operations**: Easily create, read, update, and delete records with straightforward Python methods.
- **Lightweight and Portable**: No need for complex database setups. Your data is stored in a single JSON file.
- **Flexible Data Models**: Store anything from simple key-value pairs to complex nested structures.
- **Search Functionality**: Includes basic search capabilities to filter through data based on keys or patterns.
- **Minimal Setup**: With just a few lines of code, integrate JsonDB into any Python project.

## Getting Started

### Prerequisites

- Python 3.6 or newer

### Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/json-db-project.git
cd json-db-project
```

## Usage

Here's a quick example to get you started:
```py
from jsonDb import JsonDB

# Initialize the database
db = JsonDB('data.json')

# Adding data
db['user1'] = {'name': 'John Doe', 'age': 30}
db['user2'] = {'name': 'Jane Doe', 'age': 25}

# Retrieving data
print(db['user1'])  # Output: {'name': 'John Doe', 'age': 30}

# Updating data
db['user1']['age'] = 31

# Deleting data
del db['user2']

# Searching for keys (example with regex)
print(db.keys('user.*'))  # Output: ['user1']
```

## Contributing

Contributions to the JsonDB Project are welcome! Whether it's reporting a bug, discussing potential improvements, or contributing code, we value your input.

Please feel free to submit issues and pull requests.
