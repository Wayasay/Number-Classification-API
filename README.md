
# Number Classification API

## Overview

This project is a Flask-based API that classifies numbers and provides interesting mathematical properties about them, along with a fun fact.

## API Specification

### Endpoint

**GET** `/api/classify-number?number=<number>`

### Response Format

#### 200 OK
```json
{
    "is_prime": <boolean>,
    "digit_sum": <integer>,
    "fun_fact": <string>,
    "properties": <array of strings>,
    "is_perfect": <boolean>
}
```

#### 400 Bad Request
```json
{
    "number": "alphabet",
    "error": true
}
```

## Example Request

```sh
curl -X GET "https://number-classification-api-cyan.vercel.app/api/classify-number?number=371"
```

## Example Response

```json
{
    "is_prime": false,
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371",
    "properties": ["armstrong", "odd"],
    "is_perfect": false
}
```

## Requirements

- Python 3.x
- Flask 3.1.0
- requests 2.32.3

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the Flask server:
    ```sh
    python index.py
    ```

2. The server will be running at `http://127.0.0.1:5000`.

## Deployment

This project is configured to be deployed on Vercel. Here is the API Endpoint: https://number-classification-api-cyan.vercel.app/