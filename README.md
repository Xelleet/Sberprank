<!-- ASCII Banner -->
```
  ____       _             ____             _    
 / ___|  ___| | ___  ___  |  _ \ ___  _   _| | __
 \___ \ / _ \ |/ _ \/ __| | |_) / _ \| | | | |/ /
  ___) |  __/ |  __/\__ \ |  __/ (_) | |_| |   < 
 |____/ \___|_|\___||___/ |_|   \___/ \__,_|_|\_\
                                                 
        💰 Учебный банковский проект SberPank
```

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-green?logo=django&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-yellow)
![Status: Ready](https://img.shields.io/badge/Status-Ready-brightgreen)

**SberPank** — учебный проект, имитирующий банковское приложение с управлением счетами, транзакциями и займами.

---

## 🚀 Установка

✅ Клонируйте репозиторий:

```bash
git clone https://github.com/your-username/sberprank.git
cd sberprank
```

✅ Создайте виртуальное окружение и активируйте его:

```bash
python -m venv env
# Linux / MacOS
source env/bin/activate
# Windows
env\Scripts\activate
```

✅ Установите зависимости:

```bash
pip install -r requirements.txt
```

✅ Примените миграции:

```bash
python manage.py migrate
```

✅ Запустите сервер разработки:

```bash
python manage.py runserver
```

---

## 🛠 Использование

Приложение предоставляет следующие возможности:

### 👤 Аутентификация пользователей
- 🟢 Регистрация нового пользователя  
- 🟢 Вход в существующий аккаунт  

### 💼 Управление счетами
- 🟢 Просмотр списка счетов  
- 🟢 Создание нового счёта  
- 🟢 Пополнение счёта  

### 💸 Транзакции
- 🟢 Просмотр списка транзакций  
- 🟢 Перевод средств между счетами  

### 🏦 Управление займами
- 🟢 Оформление нового займа  
- 🟢 Просмотр списка займов  
- 🟢 Погашение займа  

---

## 🔗 API

| Endpoint | Метод | Статус | Описание |
|---------|--------|--------|----------|
| `/api/users/login/` | POST | 🟢 | Вход |
| `/api/users/register/` | POST | 🟢 | Регистрация |
| `/api/accounts/` | GET | 🟢 | Список счетов |
| `/api/accounts/create/` | POST | 🟢 | Создать счёт |
| `/api/transactions/` | GET | 🟢 | Список транзакций |
| `/api/transactions/transfer/` | POST | 🟢 | Перевод |
| `/api/loans/apply/` | POST | 🟢 | Подать заявку на займ |
| `/api/loans/` | GET | 🟢 | Список займов |
| `/api/loans/{loan_id}/` | GET | 🟢 | Детали займа |
| `/api/loans/{loan_id}/pay/` | POST | 🟢 | Погасить займ |

---

## 🤝 Вклад в проект

📝 Приветствуются issue и pull‑request’ы для улучшений.

---

## 🧪 Тестирование

```bash
python manage.py test
```

> 🔵 Все тесты ✅ пройдены, функционал стабилен.

---

## 📜 Лицензия

Проект распространяется под лицензией **MIT**.

---
