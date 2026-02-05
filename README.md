# 💸 FastAPI Transaction Manager

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green)
![Status](https://img.shields.io/badge/Status-MVP-orange)

A robust, production-ready web application for managing financial transactions. Built with **FastAPI** (Backend) and **Jinja2** (Server-Side Rendering), designed to demonstrate modern CRUD architectural patterns and secure web practices.

This project serves as a foundational module for larger Sovereign AI and B2B integration systems.

---

## 🚀 Features

* **Full CRUD Cycle**: Create, Read, Update, and Delete transactions securely.
* **Security First**: Implements `POST` methods for state-changing operations to prevent CSRF vulnerabilities.
* **PRG Pattern**: Uses the **Post-Redirect-Get** architectural pattern to prevent duplicate form submissions and ensure a smooth user experience.
* **Data Validation**: Leverages Python type hints and FastAPI's `Form(...)` validation to ensure data integrity.
* **Responsive UI**: Clean, professional interface powered by Bootstrap 5.

---

## 🛠️ Tech Stack

* **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
* **Templating**: [Jinja2](https://jinja.palletsprojects.com/)
* **Server**: Uvicorn (ASGI)
* **Frontend**: HTML5, CSS3, Bootstrap 5 (CDN)
* **Architecture**: MVC-style separation of concerns, ready for Docker containerization.

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/DenisNaumov7777/fastapi-transaction-manager.git](https://github.com/DenisNaumov7777/fastapi-transaction-manager.git)
cd fastapi-transaction-manager

```

### 2. Create a virtual environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

*(Ensure you have `fastapi[standard]` and `jinja2` installed)*

### 4. Run the application

You can run the server using `fastapi dev` for development or python directly.

```bash
# Development mode with auto-reload
fastapi dev main.py

# OR Production mode
python main.py

```

### 5. Access the Dashboard

Open your web browser and navigate to:
👉 **http://0.0.0.0:8080** (or http://localhost:8080)

---

## 📂 Project Structure

```text
fastapi-transaction-manager/
├── templates/             # HTML Templates (Jinja2)
│   ├── base.html          # Base layout (Navbar, CSS)
│   ├── transactions.html  # Main dashboard (Read/Delete)
│   ├── form.html          # Creation form (Create)
│   └── edit.html          # Editing form (Update)
├── main.py                # Application entry point & Logic
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

```

---

## 👤 Author

**Denis Naumov**

* 📍 Cologne, Germany

---

*This project is designed for educational purposes and as a portfolio demonstration of secure FastAPI web development.*

```

