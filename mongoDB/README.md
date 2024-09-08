The simplest way to access MongoDB running inside a **Docker container** (managed by Docker Compose) is to connect directly to the container that is running MongoDB and use the **MongoDB Shell** (`mongosh`) to view the data. Here are the steps you can follow to do that:

### 1. **Check if MongoDB is running in Docker Compose**
Ensure that MongoDB is running correctly inside your Docker Compose setup. You can check the running services with the following command:

```bash
docker compose ps
```

Verify that the MongoDB service is active.

### 2. **Connect to the MongoDB container**
Once MongoDB is running in Docker Compose, you can open a terminal inside the container using the `docker exec` command:

```bash
docker exec -it <mongo_container_name> mongosh
```

Replace `<mongo_container_name>` with the name of the MongoDB container, which you can find by listing the services with `docker compose ps`. For example, if the MongoDB container is named `mongodb`:

```bash
docker exec -it mongodb mongosh
```

This will open the interactive MongoDB Shell (`mongosh`) inside the container.

### 3. **Run MongoDB commands**

Now that you are inside the MongoDB Shell, you can execute commands to interact with the database. Some useful commands include:

- **List databases:**
  ```bash
  show dbs
  ```

- **Access a specific database:**
  ```bash
  use auth_db
  ```

- **List collections:**
  ```bash
  show collections
  ```

- **View documents in a collection:**
  ```bash
  db.users.find().pretty()
  ```
