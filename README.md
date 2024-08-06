# JsonDB Project

<p align="center">
  <img src="./assets/logo.png" alt="Logo" height="128px">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/json-%23000000.svg?&style=for-the-badge&logo=json&logoColor=white"/>
  <img src="https://img.shields.io/github/license/DavyJonesCodes/JsonDB-Python?style=for-the-badge"/>
</p>

The JsonDB Project provides a lightweight, file-based database system, designed to make data storage and retrieval simple and intuitive. Built in Python, it leverages the versatility of JSON for data manipulation, making it an ideal solution for small projects, prototypes, or for educational purposes where a full-scale database system isn't required.

## 🚀 Features

- **Simple CRUD Operations**: Easily create, read, update, and delete records with straightforward Python methods.
- **Lightweight and Portable**: No need for complex database setups. Your data is stored in a single JSON file.
- **Flexible Data Models**: Store anything from simple key-value pairs to complex nested structures.
- **Search Functionality**: Includes basic search capabilities to filter through data based on keys or patterns.
- **Minimal Setup**: With just a few lines of code, integrate JsonDB into any Python project.

## 🏁 Getting Started

### Prerequisites

- Python 3.6 or newer

### Installation

You can download the `jsonDB.py` file directly for your platform using the following commands:

#### Windows

**Option 1: Using PowerShell (no extra installations needed)**:
Open PowerShell and run:

```powershell
Invoke-WebRequest -Uri https://raw.githubusercontent.com/DavyJonesCodes/json-db-python/master/jsonDB.py -OutFile jsonDB.py
```

**Option 2: Using `wget`**:
If you have `wget` installed, you can use the following command in Command Prompt or PowerShell:

```cmd
wget -O jsonDB.py https://raw.githubusercontent.com/DavyJonesCodes/json-db-python/master/jsonDB.py
```

#### Linux and macOS

Open your terminal and run:

```bash
wget -O jsonDB.py https://raw.githubusercontent.com/DavyJonesCodes/json-db-python/master/jsonDB.py
```

### Usage

Here's how to get started with JsonDB in your project:

```python
from jsonDB import JsonDB

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

## 📁 Project Structure

- `jsonDb.py`: The core database module, implementing CRUD operations and data storage in JSON format.
- `main.py`: An example script demonstrating how to use the JsonDB for basic data management tasks.
- `data.json`: A sample JSON file used by `main.py` to illustrate data storage and retrieval.

## 🤝 Contributing

Contributions to the JsonDB Project are welcome! Whether it's reporting a bug, discussing potential improvements, or contributing code, we value your input.

Please feel free to submit issues and pull requests.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
