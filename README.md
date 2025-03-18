# DevOps-Application
# Microservices-Based Application using Docker and Docker Compose

## Project Overview
This project is a microservices-based application that includes the following components:
- **Web Service:** A Flask web application that serves HTTP requests.
- **Worker Service:** A background processing service that handles asynchronous tasks.
- **Database Service:** A PostgreSQL database to store application data.

The application demonstrates containerization using Docker and service orchestration with Docker Compose.

---

## Project Components
### 1. Web Service
- Framework: **Flask** (Python)
- Displays name, roll number, and a short bio on the index page.
- Exposed on **http://localhost:8081**.

### 2. Worker Service
- Background processing using a simple Python worker script.
- Simulates async task processing.

### 3. Database Service
- **PostgreSQL** database with persistent storage using Docker volumes.
- Stores data for the web and worker services.

---

## Prerequisites
- **Docker:** [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose:** [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd microservices-app
```

### 2. Build and Run the Application
```bash
docker-compose up --build
```

### 3. Access the Web Application
- Open your browser and navigate to: **http://localhost:8081**
- You should see a page displaying:
  - **Name:** Karthik Raj
  - **Roll No:** 2022BCD0041
  - **Short Bio:** [Your bio here]

### 4. Verify Services
- **Logs:** Check container logs using `docker-compose logs`
- **Container Status:**
```bash
docker ps
```

### 5. Shutdown
```bash
docker-compose down
```

---

## Files used:

  - **Dockerfile** for both Web and Worker services
  - **docker-compose.yml**
  - **Code for Web and Worker Services**
- Provide a **PDF document** with:
  - Steps to execute the application
  - Screenshots of:
    - Terminal output (`docker-compose up` logs)
    - `docker ps` output
    - Web page showing the index page

---

## Troubleshooting
- Ensure all containers are running with `docker ps`
- Check logs for errors using `docker-compose logs`
- Rebuild containers if necessary:
```bash
docker-compose up --build --force-recreate
```

---

## Author
- **Name:** Karthik Raj
- **Roll No:** 2022BCD0041
