# 🏦 SberPrank

<div align="center">

**A modern banking API built with Django REST Framework**

[![Django](https://img.shields.io/badge/Django-4.2.23-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.16.1-9B59B6?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io/)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [API Endpoints](#-api-endpoints)
- [Usage Examples](#-usage-examples)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**SberPrank** is a comprehensive banking API that simulates core banking operations including account management, multi-currency transactions, and loan processing. Built with Django REST Framework, it provides a robust backend for financial applications with JWT authentication, currency conversion, and transaction tracking.

### Key Highlights

- 🔐 **Secure Authentication** - JWT-based user authentication
- 💱 **Multi-Currency Support** - RUB, USD, EUR accounts with automatic conversion
- 💸 **Transaction Management** - Transfers, deposits, withdrawals with fee calculation
- 📊 **Loan System** - Complete loan application and payment tracking
- 🌐 **CORS Enabled** - Ready for frontend integration

---

## ✨ Features

### 👤 User Management
- User registration and authentication
- JWT token-based authentication
- User profiles with additional information
- Automatic account creation on registration

### 💳 Account Management
- Create multiple accounts in different currencies (RUB, USD, EUR)
- View account balances and details
- Account activation/deactivation
- Unique 20-digit account numbers

### 💰 Transactions
- **Transfers** - Send money between accounts with currency conversion
- **Deposits** - Replenish account balances
- **Debits** - Withdraw funds from accounts
- **Loan Payments** - Automatic loan payment processing
- Exchange rate calculation
- Transaction fees
- Transaction history tracking

### 🏦 Loan Management
- Apply for loans with customizable terms
- Interest rate calculation (default 12%)
- Monthly payment calculation
- Loan status tracking (pending, approved, rejected, paid)
- Payment schedule management
- Remaining balance tracking

---

## 🛠 Tech Stack

| Category | Technology |
|----------|-----------|
| **Framework** | Django 4.2.23 |
| **API** | Django REST Framework 3.16.1 |
| **Authentication** | djangorestframework-simplejwt 5.5.1 |
| **CORS** | django-cors-headers 4.7.0 |
| **Database** | SQLite3 (development) |
| **Server** | Gunicorn 23.0.0 |
| **Language** | Python 3.x |

---

## 📁 Project Structure

```
sberprank/
├── sberprank/              # Main project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py            # Root URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
│
├── users/                  # User management app
│   ├── models.py          # User Profile model
│   ├── views.py           # Authentication views
│   ├── serializers.py     # User serializers
│   └── urls.py            # User endpoints
│
├── accounts/               # Account management app
│   ├── models.py          # Account model
│   ├── views.py           # Account CRUD operations
│   ├── serializers.py     # Account serializers
│   └── urls.py            # Account endpoints
│
├── transactions/           # Transaction management app
│   ├── models.py          # Transaction model
│   ├── views.py           # Transaction processing
│   ├── serializers.py     # Transaction serializers
│   └── urls.py            # Transaction endpoints
│
├── loans/                  # Loan management app
│   ├── models.py          # Loan and LoanPayment models
│   ├── views.py           # Loan operations
│   ├── serializers.py     # Loan serializers
│   └── urls.py            # Loan endpoints
│
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── db.sqlite3             # SQLite database (development)
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd sberprank
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations

```bash
python manage.py migrate
```

### Step 5: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Step 6: Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

---

## ⚙️ Configuration

### Environment Variables

For production, consider setting these in your environment:

```python
SECRET_KEY = 'your-secret-key-here'
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']
```

### CORS Settings

Update `CORS_ALLOWED_ORIGINS` in `settings.py` to include your frontend URL:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://your-frontend-domain.com"
]
```

### Database

The project uses SQLite by default. For production, consider PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 📡 API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/api/register/` | Register new user | ❌ |
| `POST` | `/api/login/` | Login and get JWT tokens | ❌ |
| `GET` | `/api/profile/` | Get user profile | ✅ |

### Accounts

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/accounts/` | List user's accounts | ✅ |
| `GET` | `/api/accounts/{id}/` | Get account details | ✅ |
| `POST` | `/api/accounts/create/` | Create new account | ✅ |
| `POST` | `/api/accounts/deposit/` | Deposit funds | ✅ |

### Transactions

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/transactions/` | List transactions | ✅ |
| `POST` | `/api/transactions/transfer/` | Transfer money | ✅ |
| `POST` | `/api/transactions/deposit/` | Deposit to account | ✅ |

### Loans

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/loans/` | List user's loans | ✅ |
| `POST` | `/api/loans/apply/` | Apply for a loan | ✅ |
| `POST` | `/api/loans/{id}/pay/` | Make loan payment | ✅ |

---

## 💡 Usage Examples

### Register a New User

```bash
curl -X POST http://127.0.0.1:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "password2": "securepassword123"
  }'
```

### Login

```bash
curl -X POST http://127.0.0.1:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepassword123"
  }'
```

### Create an Account

```bash
curl -X POST http://127.0.0.1:8000/api/accounts/create/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "currency": "USD"
  }'
```

### Transfer Money

```bash
curl -X POST http://127.0.0.1:8000/api/transactions/transfer/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "from_account_id": 1,
    "to_account_id": 2,
    "amount": "1000.00",
    "description": "Payment for services"
  }'
```

### Apply for a Loan

```bash
curl -X POST http://127.0.0.1:8000/api/loans/apply/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "account_id": 1,
    "amount": "50000.00",
    "term_months": 12,
    "interest_rate": "12.00"
  }'
```

---

## 🌐 Deployment

### Render Deployment

The project is configured for deployment on Render:

1. Connect your repository to Render
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `gunicorn sberprank.wsgi:application`
4. Add environment variables in Render dashboard
5. Update `ALLOWED_HOSTS` in settings

### Environment Variables for Production

```bash
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=sberprank-2.onrender.com
```

---

## 🔒 Security Considerations

- ⚠️ **Change SECRET_KEY** before deploying to production
- ⚠️ **Set DEBUG=False** in production
- ⚠️ **Use environment variables** for sensitive data
- ⚠️ **Configure CORS** properly for your frontend
- ⚠️ **Use HTTPS** in production
- ⚠️ **Consider using PostgreSQL** instead of SQLite for production

---

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

Run tests for a specific app:

```bash
python manage.py test users
python manage.py test accounts
python manage.py test transactions
python manage.py test loans
```

---

## 📝 API Documentation

Access the Django admin panel for database management:

```
http://127.0.0.1:8000/admin/
```

For interactive API documentation, consider integrating:
- [drf-yasg](https://github.com/axnsan12/drf-yasg) (Swagger/OpenAPI)
- [django-rest-framework-simplejwt](https://github.com/jazzband/djangorestframework-simplejwt) documentation

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Built with ❤️ for learning and fun

---

## 🙏 Acknowledgments

- Django REST Framework team
- All contributors and users of this project

---

<div align="center">

**Made with Django & DRF**

⭐ Star this repo if you find it helpful!

</div>

