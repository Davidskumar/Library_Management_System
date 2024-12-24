# Library Management System API

## Overview
A lightweight Flask-based RESTful API for managing books and members in a library. This project provides secure token-based authentication, CRUD operations, search functionality, and pagination, making it ideal for learning and prototyping API development.

> ⭐ If you find this project helpful, please star this repository to show your support!
---

## How to Run the Project

### Prerequisites
1. Python (>=3.8) installed on your system.
2. A package manager such as `pip`.

### Steps to Run
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Davidskumar/Library_Management_System.git
   cd library-management-system
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```
   The application will start and run at `http://127.0.0.1:5000`.

4. **Use the API**
   - Use tools like Postman or `curl` to interact with the endpoints.
   - A sample `Authorization` token is generated upon login (`/login` endpoint). Use it to access protected routes.

---

## Design Choices

1. **Framework**: Flask was chosen for its simplicity and suitability for small-scale API development projects.
2. **In-Memory Storage**: 
   - Data for books and members are stored in memory (Python lists) to keep the implementation lightweight.
   - This avoids the complexity of integrating a database for this prototype.
3. **Token-Based Authentication**: 
   - Basic token authentication is used to secure endpoints. Each user receives a unique token upon login.
   - Sessions are stored in-memory.
4. **Pagination and Filtering**:
   - Pagination was implemented for books (`/books` endpoint) to handle large datasets efficiently.
   - Filtering by title and author improves usability and demonstrates basic query parameter handling.
5. **RESTful Design**:
   - The API follows REST principles, using standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) for CRUD operations.

---

## Assumptions and Limitations

### Assumptions
1. User authentication is based on a hardcoded user database (`{'admin': 'password'}`).
2. IDs for books and members are auto-incremented starting from 1.
3. Tokens are stored in memory and expire only upon logout.

### Limitations
1. **No Database Integration**:
   - Data is not persistent and is lost when the application stops.
   - Future versions can include a database like SQLite or PostgreSQL for persistence.
2. **Simple Authentication**:
   - No password hashing or advanced security measures are implemented.
   - A more robust system with JWT authentication can be added for production.
3. **Limited Functionality**:
   - The project focuses on CRUD operations, leaving room for features like lending/returning books or advanced search.
4. **Concurrency Issues**:
   - Since data is stored in memory, concurrent access or modification may lead to data inconsistencies.
5. **Scalability**:
   - The current implementation is not optimized for large-scale usage or deployment.

---

This project is a starting point for exploring Flask-based API development and can be extended with additional features and integrations.
