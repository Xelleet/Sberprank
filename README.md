<!-- PROD-STYLE README -->

```
   _____       _             _____             _    
  / ____|     | |           |  __ \           | |   
 | (___   __ _| | ___ _ __  | |__) |__  ___ __| | ___ 
  \___ \ / _` | |/ _ \ '__| |  ___/ _ \/ __/ _` |/ _ \
  ____) | (_| | |  __/ |    | |  |  __/ (_| (_| |  __/
 |_____/ \__,_|_|\___|_|    |_|   \___|\___\__,_|\___|
                                                        
           💰 SberPank — Banking Prototype
```

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)
![Build: Passing](https://img.shields.io/badge/build-passing-brightgreen)

---

## Overview

**SberPank** is an educational banking application prototype implementing:

- User authentication  
- Account management  
- Transactions and transfers  
- Loan management  

Designed for **Python 3.11** and **Django 4.2**.

---

## Installation

```bash
git clone https://github.com/your-username/sberprank.git
cd sberprank
python -m venv env
# Linux / MacOS
source env/bin/activate
# Windows
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## Usage

| Module | Status | Description |
|--------|--------|-------------|
| Authentication | ✅ | Register/Login users |
| Accounts | ✅ | View/Create/Deposit accounts |
| Transactions | ✅ | View/Transfer funds |
| Loans | ✅ | Apply/View/Pay loans |

---

## API Endpoints

| Endpoint | Method | Status | Description |
|---------|--------|--------|-------------|
| `/api/users/login/` | POST | ✅ | User login |
| `/api/users/register/` | POST | ✅ | Register new user |
| `/api/accounts/` | GET | ✅ | List accounts |
| `/api/accounts/create/` | POST | ✅ | Create account |
| `/api/transactions/` | GET | ✅ | List transactions |
| `/api/transactions/transfer/` | POST | ✅ | Transfer funds |
| `/api/loans/apply/` | POST | ✅ | Apply for loan |
| `/api/loans/` | GET | ✅ | List loans |
| `/api/loans/{loan_id}/` | GET | ✅ | Loan details |
| `/api/loans/{loan_id}/pay/` | POST | ✅ | Make payment |

---

## Testing

```bash
python manage.py test
```

> All tests passed. Application stable.

---

## Contribution

Contributions are welcome via **pull requests** and **issues**.  
Follow the **contribution guidelines** in `CONTRIBUTING.md`.

---

## License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## Notes

- Badges indicate current build, dependency versions, and license compliance.  
- Minimalistic style ensures clarity for developers and stakeholders.  
- Compatible with **dark and light themes** on GitHub.

