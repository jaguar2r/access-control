# Authentication API

This project is a **Flask-based Authentication API** built using the **MVC (Model-View-Controller)** architecture. The API uses **JWT (JSON Web Tokens)** for authentication and **MongoDB** for storing user data (email and password). The project also includes a **Nginx** server for load balancing and proxying requests, and is orchestrated with **Docker Compose**.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Technologies Used](#technologies-used)
3. [Authentication Flow](#authentication-flow)
4. [API Endpoints](#api-endpoints)
5. [Running the Application](#running-the-application)
6. [Environment Variables](#environment-variables)
7. [Gunicorn and Nginx](#gunicorn-and-nginx)
8. [Testing the API](#testing-the-api)
    - [Using cURL](#using-curl)
    - [Using Postman](#using-postman)

## Project Structure

This project follows the **MVC (Model-View-Controller)** architecture, which separates the application into three distinct layers:
- **Model (M)**: Manages the data and interacts with MongoDB.
- **View (V)**: Responsible for formatting and returning HTTP responses (usually in JSON).
- **Controller (C)**: Handles the business logic, coordinates models and views, and processes requests.

## Technologies Used

- **Flask**: Python micro-framework for building web applications.
- **Gunicorn**: WSGI HTTP Server for Flask in production.
- **MongoDB**: NoSQL database for storing user data.
- **JWT (JSON Web Tokens)**: Used for session-based authentication.
- **Nginx**: Reverse proxy server for load balancing and routing.
- **Docker**: Containerization of services.
- **Docker Compose**: Manages multi-container setups (Flask, MongoDB, Nginx).

## Authentication Flow

The API uses **JWT** for authentication, with the following flow:

1. **User Registration**: Users can register by providing an email and password. The password is hashed using `bcrypt` before being stored in MongoDB.
2. **User Login**: Users log in with their email and password, and a **JWT token** is generated and returned if the credentials are valid. This token includes an expiration time.
3. **Token-Based Authentication**: For subsequent requests, users include the JWT token in the `Authorization` header to access protected routes.

### JWT Structure
- JWT tokens consist of three parts: **Header**, **Payload**, and **Signature**.
  - **Header**: Contains metadata about the token, such as the algorithm used.
  - **Payload**: Contains user data and the token expiration time.
  - **Signature**: A cryptographic hash ensuring the token's integrity.

### Token Expiration:
Tokens have an expiration time (e.g., 15 minutes). After the token expires, users must log in again to get a new token.

## API Endpoints

### 1. **POST /auth/register**
Registers a new user with an email and password.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "status": "success",
  "data": "User registered successfully"
}
```

### 2. **POST /auth/login**
Logs in a user and returns a JWT token.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "token": "JWT_TOKEN_HERE"
  }
}
```

### 3. **GET /auth/protected**
Accesses a protected route that requires a valid JWT token in the `Authorization` header.

**Headers:**
```
Authorization: Bearer JWT_TOKEN_HERE
```

**Response:**
```json
{
  "status": "success",
  "data": "Access granted"
}
```

## Running the Application

To run the application, ensure **Docker** and **Docker Compose** are installed. Follow these steps:

1. Clone the repository:

2. Build and start the containers using Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. The application will be available at `http://localhost`.

### Accessing the API
- Use the `/auth/register` and `/auth/login` endpoints to interact with the authentication API.

## Environment Variables

Sensitive information, such as the **SECRET_KEY** and **MONGO_URI**, is stored in a `.env` file. To configure the environment variables:

1. Create a `.env` file in the root directory.

2. Add the following variables:
```bash
FLASK_APP=app/app.py
FLASK_ENV=development
MONGO_URI=mongodb://mongo:27017/auth_db
SECRET_KEY=your_secret_key_here
```

## Gunicorn and Nginx

### Gunicorn Configuration:
Gunicorn is used as the WSGI server to run the Flask app. The **Dockerfile** includes the following command:

```bash
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

- **`-w 4`**: Number of worker processes to handle requests.
- **`-b 0.0.0.0:5000`**: Binds Gunicorn to listen on port 5000.
- **`app:app`**: Refers to the Flask app instance.

### Nginx Configuration:
Nginx acts as a reverse proxy, forwarding requests to Gunicorn, which handles the Flask application.

1. Nginx listens on port **80** and forwards requests to Gunicorn.
2. Gunicorn processes the requests and returns the response to Nginx, which then forwards it to the client.

## Testing the API

You can test the API using **cURL** or **Postman**.

### Using cURL

#### 1. Register a New User:
```bash
curl -X POST http://localhost/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123"}'
```

#### 2. Login to Get a JWT Token:
```bash
curl -X POST http://localhost/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123"}'
```

#### 3. Access Protected Route:
```bash
curl -X GET http://localhost/auth/protected \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### Using Postman

#### 1. Register:
- **Method**: POST
- **URL**: `http://localhost/auth/register`
- **Body**: raw, JSON format:
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```

#### 2. Login:
- **Method**: POST
- **URL**: `http://localhost/auth/login`
- **Body**: raw, JSON format:
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```

#### 3. Use Token for Protected Routes:
- **Method**: GET
- **URL**: `http://localhost/auth/protected`
- **Headers**:
  - Key: `Authorization`
  - Value: `Bearer YOUR_JWT_TOKEN`

### Troubleshooting
- **Connection Issues**: Ensure the application is running and accessible on the correct port.
- **JWT Token Expired**: Login again to get a new token.
- **Invalid Token**: Verify that the token is correctly passed in the `Authorization` header with the `Bearer` prefix.

### TODO

- Sanitize data before performing select/insert operations on the database.
- Add API documentation/specification.
- Translate response messages from Portuguese to English.
