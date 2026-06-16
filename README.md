# Personal Finance Tracker

A REST API for tracking personal income and expenses, built with FastAPI and SQLite.

## Tech Stack

- **FastAPI** — async REST framework
- **SQLAlchemy 2** — ORM with SQLite
- **Pydantic v2** — request/response validation
- **Uvicorn** — ASGI server

## Getting Started

### Prerequisites

- Python 3.10+

### Setup

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt
```

### Run the server

```bash
uvicorn backend.main:app --reload
```

The API will be available at `http://localhost:8000`.  
Interactive docs (Swagger UI) at `http://localhost:8000/docs`.

## API Reference

### Transactions

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/transactions` | List all transactions |
| `POST` | `/transactions` | Create a transaction |
| `PUT` | `/transactions/{id}` | Update a transaction |
| `DELETE` | `/transactions/{id}` | Delete a transaction |

### Example: Create a transaction

```bash
curl -X POST http://localhost:8000/transactions \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Grocery run",
    "amount": 85.50,
    "category": "Food",
    "type": "expense"
  }'
```

### Example response

```json
{
  "id": 1,
  "description": "Grocery run",
  "amount": 85.50,
  "category": "Food",
  "type": "expense",
  "date": "2026-06-16T10:30:00"
}
```

## Project Structure

```
personal-finance-tracker/
├── backend/
│   ├── main.py        # FastAPI app and route handlers
│   ├── models.py      # SQLAlchemy ORM models
│   ├── schemas.py     # Pydantic request/response schemas
│   ├── database.py    # DB engine and session factory
│   └── requirements.txt
└── .gitignore
```

## Data Model

**Transaction**

| Field | Type | Description |
|-------|------|-------------|
| `id` | int | Auto-generated primary key |
| `description` | string | Short description of the transaction |
| `amount` | float | Transaction amount |
| `category` | string | e.g. Food, Transport, Salary |
| `type` | string | `income` or `expense` |
| `date` | datetime | Auto-set to creation time |
