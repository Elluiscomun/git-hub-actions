# Pokémon API Project

This project is a Python application that interacts with the Pokémon REST API to fetch and display information about Pokémon.

## Project Structure

```
pokemon-api-project
├── src
│   ├── main.py                # Entry point of the application
│   ├── api
│   │   └── pokemon_api.py     # Handles communication with the Pokémon API
│   ├── services
│   │   └── pokemon_service.py  # Provides higher-level methods to interact with the API
│   └── utils
│       └── __init__.py        # Utility functions and constants
├── requirements.txt            # Project dependencies
├── .gitignore                  # Files and directories to ignore by Git
└── README.md                   # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd pokemon-api-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage

- The application fetches data from the Pokémon API and allows users to retrieve information about specific Pokémon or all Pokémon.
- You can modify the `main.py` file to customize the interaction with the API based on your needs.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.