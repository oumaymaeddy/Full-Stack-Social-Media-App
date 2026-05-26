# 📱 Full-Stack Social Media App

A full-stack social media web application built with **Django REST Framework** (backend) and **React** (frontend). Users can register, create posts, like and comment on content, and manage their profiles.

---

## ✨ Features

- 🔐 **User Authentication** — Register, login, logout with JWT tokens
- 📝 **Post Management** — Create, edit, delete posts (CRUD)
- ❤️ **Likes & Comments** — Interact with other users' content
- 👤 **User Profiles** — View and update personal information
- 🔗 **RESTful API** — Clean API endpoints with Django REST Framework
- 🗄️ **ORM Database Management** — Structured data with Django ORM

---

## 🛠️ Tech Stack

### Backend
| Technology | Purpose |
|---|---|
| Python / Django | Web framework |
| Django REST Framework | API development |
| Django ORM | Database management |
| pytest | Unit testing |

### Frontend
| Technology | Purpose |
|---|---|
| React | UI framework |
| JavaScript (ES6+) | Frontend logic |
| Axios | API communication |

---

## 📁 Project Structure

```
Full-Stack-Social-Media-App/
├── CoreRoot/          # Django project settings
├── core/              # Main Django app (models, views, serializers)
├── social-media-app   # React frontend
├── manage.py          # Django management
├── pytest.ini         # Test configuration
└── uploads/           # Media files
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10+
- Node.js 18+
- pip

### 1. Clone the repository
```bash
git clone https://github.com/oumaymaeddy/Full-Stack-Social-Media-App.git
cd Full-Stack-Social-Media-App
```

### 2. Backend Setup
```bash
# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

### 3. Frontend Setup
```bash
cd social-media-app
npm install
npm start
```

### 4. Access the app
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000/api/`

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and get JWT token |
| GET | `/api/posts/` | Get all posts |
| POST | `/api/posts/` | Create a new post |
| PUT | `/api/posts/:id/` | Update a post |
| DELETE | `/api/posts/:id/` | Delete a post |
| POST | `/api/posts/:id/like/` | Like a post |
| POST | `/api/posts/:id/comment/` | Comment on a post |

---

## 🎓 About This Project

This is a personal project I built from scratch to deepen my full-stack development skills. It demonstrates my ability to independently design and develop a complete web application — from database modeling and REST API architecture to a dynamic React frontend — without any academic guidance.

---

## 👩‍💻 Author

**Oumayma Eddy**
- GitHub: [@oumaymaeddy](https://github.com/oumaymaeddy)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
