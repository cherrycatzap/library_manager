📚 Library Management System
A web-based backend system built using Django and Django REST Framework to manage books, authors, and borrowing records in a library, complete with asynchronous report generation and real-time inventory tracking.

🔑 Features
✅ Full CRUD for Books, Authors, and Borrowings
📄 Auto-generated API Documentation using Swagger UI (drf-yasg)
⏱️ Asynchronous JSON report generation (borrowing statistics & library metrics) using Celery
📊 Background tasks handled with Redis, enabling real-time insights
📦 Automated inventory management – borrowing updates stock in real-time
🔐 Token-based Authentication (optional for protected routes)
🧠 Scalable, modular architecture – easy to plug in pagination, filters, search, and more
🧪 Built with a three-model schema to ensure relational consistency and data integrity

🛠️ Technologies Used
Python 3.x

Django

Django REST Framework

Celery + Redis

drf-yasg (Swagger for API docs)

SQLite (default, easily switchable to PostgreSQL/MySQL)

🚀 Setup Instructions
bash
Copy
Edit
git clone https://github.com/yourusername/library_manager.git
cd library_manager
