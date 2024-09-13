# FastAPI Workshop

Welcome to the FastAPI Workshop! This guide will walk you through setting up a FastAPI application, using Pydantic for data validation, integrating a database, adding authentication, and writing test cases.

## Table of Contents

1. [Introduction to Pydantic](#introduction-to-pydantic)
2. [Building Your First API](#building-your-first-api)
3. [Database Integration](#database-integration)
4. [Authentication](#authentication)
5. [Testing Your API](#testing-your-api)

---

## 1. Introduction to Pydantic

Pydantic is a data validation and settings management library using Python type annotations. It helps ensure data integrity by validating input data.

### Example

```python
from pydantic import BaseModel

class UserProfile(BaseModel):
    """
    User profile model.
    """
    user_phone_number: str
```

Pydantic will raise validation errors if data doesn't conform to the specified types.

---

## 2. Building Your First API

FastAPI is a modern, fast web framework for building APIs with Python 3.7+.

### Getting Started

Create a file named `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()
```

### Adding your first API

```python
from fastapi import FastAPI

from models.user_profile import UserProfile

app = FastAPI()

@app.get('')
def get_user_list() -> list[UserProfile]:
    return []
```


### Running the Server

Run the server using Uvicorn:

```bash
fastapi dev main.py
```

Navigate to `http://127.0.0.1:8000` to see your API in action!

---

## 3. Database Integration

We currently implemented python's `gloabls` as an in memory database.

## 4. Authentication

FastAPI provides easy integration with authentication systems like OAuth2.

### OAuth2 Example

Add OAuth2 authentication in `main.py`:


## 5. Testing Your API


### Install pytest


### Test Example



### Running Tests

