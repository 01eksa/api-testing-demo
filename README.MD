# API Testing Demo

Automated REST API testing example with `requests` and `pytest`.

Tested against [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — a free public fake API.

## Key Features

- **Data-Driven Testing (DDT):** Test logic is strictly separated from test data (stored in `config.py`), allowing easy scalability for multiple endpoints.
- **Full CRUD Coverage:** Automated tests for `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` requests across all supported resources.
- **Deep Object Validation:** Custom recursive assertion mechanism to strictly validate deeply nested JSON responses (e.g., complex `address` and `company` objects).
- **Standard Behavior Checks:** Verifies expected HTTP status codes (200, 201) and handles negative scenarios (e.g., 404 on missing resources).

## Project structure

```text
.
├── tests/
│   ├── __init__.py
│   ├── config.py        # Base URL and robust test data dictionaries
│   └── test_generic.py  # Parametrized tests and recursive validators
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.12+
- pip

## Setup

```bash
pip install -r requirements.txt
```

## Running tests

```bash
pytest
```

## Dependencies

```
requests==2.32.5
pytest==9.0.2
```
