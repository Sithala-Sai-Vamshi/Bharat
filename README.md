# FAQ Management API 🚀

This is a backend API for managing FAQs (Frequently Asked Questions) with multi-language support. The project includes API endpoints to perform CRUD (Create, Read, Update, Delete) operations on FAQ objects, with translation features using Google Translate API or `googletrans`. The API also supports fallback to English if a translation is unavailable.

---

## 📌 Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
4. [API Endpoints](#api-endpoints)
5. [Testing](#testing)
6. [Postman Collection](#postman-collection)
7. [Deployment](#deployment)
8. [Additional Information](#additional-information)

---

## 📖 Project Overview

The FAQ Management API allows users to manage frequently asked questions with the ability to handle multiple languages. The project includes features such as:

- **🔄 CRUD Operations**: Create, Read, Update, Delete FAQs.
- **🌍 Multi-Language Support**: Auto-translate FAQ questions and answers to multiple languages (e.g., English, Hindi, Bengali).
- **🛠️ Admin Interface**: Easily manage FAQs via Django’s admin panel.
- **🗄️ Database Support**: PostgreSQL (recommended) or other suitable database.
- **🔗 Google Translate API (`googletrans` or similar)**: For auto-translating FAQs. Consider API usage limits and costs.
- **⚡ Caching**: Efficient caching of translated FAQs to improve performance (using Redis or Memcached).

---

## 🛠️ Technologies Used

- **🐍 Django**: Web framework for Python.
- **📡 Django REST Framework**: For building the API.
- **🗄️ PostgreSQL**: Database for storing FAQ data.
- **🌎 Google Translate API (`googletrans` or alternative)**: For auto-translating FAQs.
- **🖥️ Gunicorn or UWSGI**: Production-ready WSGI HTTP Server.
- **⚡ Redis or Memcached**: For caching.
- **🐳 Docker**: Containerization of the app for easy deployment (Optional).
- **🛠️ Docker Compose**: Managing multi-container Docker applications (Optional).
- **☁️ [Your Deployment Platform (e.g., Heroku, AWS, Google Cloud)]**: *(Specify the platform you used if applicable)*

---

## ⚙️ Setup Instructions

### 📌 Prerequisites

- Python 3.9+ (or your project's Python version)
- Docker (Optional, for containerization)
- PostgreSQL (or your database choice)
- Git

### 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/faq_project.git
   cd faq_project
   ```
2. Apply the migrations:

   ```bash
   python manage.py migrate
   ```
3. Create a superuser for Django's admin panel:

   ```bash
   python manage.py createsuperuser
   ```
4. Run the development server:

   ```bash
   python manage.py runserver
   ```
5. The app should be accessible at:

   ```bash
   http://localhost:8000/
   ```

---

## 🔗 API Endpoints
- **Create FAQ**: `POST /api/faqs/` (JSON: question, answer, translations)
- **Get FAQs**: `GET /api/faqs/` (JSON: array of FAQs with id, question, answer, translations)
- **Update FAQ**: `PUT /api/faqs/{id}/` (JSON: question, answer, translations)
- **Delete FAQ**: `DELETE /api/faqs/{id}/`

---

## 🧪 Testing 

Testing is done using pytest and Django's test client. To run tests, ensure you have pytest installed:

```bash
pip install pytest
```

Then run the tests:

```bash
pytest
```

---

## 📮 Postman Collection

For testing API responses, you can use Postman to manually test the endpoints or automate the tests using the Postman Collection.
   
A Postman collection with all the CRUD endpoints is available for testing. You can download it from [here](https://drive.google.com/file/d/1Yv6DhvyW_Nr5N_00mtgaxA89TFKeOK9b/view?usp=drive_link) or import it directly into Postman.
The collection includes the following tests:

- ✅ Creating a new FAQ
- 📄 Retrieving all FAQs
- ✏️ Updating an FAQ
- ❌ Deleting an FAQ

---

## 🚀 Deployment

### 🐳 Docker (Optional)
To deploy the app using Docker, follow the steps below:

1. Build the Docker image:
   ```bash
   docker-compose build
   ```
2. Start the application:
   ```bash
   docker-compose up
   ```
3. Access the app in your browser at `http://localhost:8000`

---

## ℹ️ Additional Information

For any queries, feel free to reach out via email or open an issue in the GitHub repository. Contributions and suggestions are always welcome! 😊
