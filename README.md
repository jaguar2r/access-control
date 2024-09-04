### Access Control: Flask User Management API

#### Description
This project implements a user management API using Flask and MongoDB. It supports the creation and validation of user data, encapsulating best practices through the use of Blueprints for code organization. The development and production environment setup is facilitated by Docker, ensuring deployment ease and environment consistency.

#### Features
- **User Creation**: Allows for the creation of new users with data validation.
- **JWT Authentication**: Implements JWT for secure authentication (this item can be added if planned).
- **Dockerized**: Simplifies deployment with Docker containers.

#### Technologies Used
- **Python**: Programming language.
- **Flask**: Python web framework for development.
- **MongoDB**: NoSQL database for data storage.
- **Docker**: Platform for developing, deploying, and running applications in containers.

#### Requirements
- Docker
- Docker Compose

#### Directory Structure
```
access_control/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── user/
│       ├── __init__.py
│       ├── models.py
│       └── routes.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── run.py
```

#### Setup and Execution

1. **Clone the Repository**
   ```bash
   git clone git@github.com:jaguar2r/access-control.git
   cd access-control
   ```

2. **Build and Run with Docker**
   ```bash
   docker-compose up --build
   ```

   This will build the necessary containers and start the services defined in `docker-compose.yml`, including the API and MongoDB database.

3. **Access the API**
   - The API will be available at `http://localhost:5000/`
   - Use endpoints like `/user/create` to create a new user.

#### API Usage

- **Create User**
  - **Endpoint**: `/user/create`
  - **Method**: POST
  - **Body**:
    ```json
    {
      "username": "newuser",
      "password": "secret-password"
    }
    ```

#### Maintenance and Contributions

Contributions to the project are welcome. To contribute:
1. Fork the repository.
2. Create a new branch for your modifications.
3. Submit your changes for review.
4. Make a pull request.

#### License

[MIT License](https://opensource.org/licenses/MIT)
