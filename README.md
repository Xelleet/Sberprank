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
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

**SberPank** — учебный проект, имитирующий банковское приложение с возможностью управления счетами, транзакциями и займами.

---

## 🚀 Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/your-username/sberprank.git
cd sberprank
```

2. Создайте виртуальное окружение и активируйте его:

```bash
python -m venv env
# Linux / MacOS
source env/bin/activate
# Windows
env\Scripts\activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Примените миграции базы данных:

```bash
python manage.py migrate
```

5. Запустите сервер разработки:

```bash
python manage.py runserver
```

---

## 🛠 Использование

Приложение предоставляет следующие возможности:

### 👤 Аутентификация пользователей
- Регистрация нового пользователя  
- Вход в существующий аккаунт  

### 💼 Управление счетами
- Просмотр списка счетов пользователя  
- Создание нового счёта  
- Пополнение счёта  

### 💸 Транзакции
- Просмотр списка транзакций  
- Перевод средств между счетами  

### 🏦 Управление займами
- Оформление нового займа  
- Просмотр списка займов  
- Погашение займа  

---

## 🔗 API

| Endpoint | Метод | Описание |
|---------|--------|----------|
| `/api/users/login/` | POST | Вход |
| `/api/users/register/` | POST | Регистрация |
| `/api/accounts/` | GET | Список счетов |
| `/api/accounts/create/` | POST | Создать счёт |
| `/api/transactions/` | GET | Список транзакций |
| `/api/transactions/transfer/` | POST | Перевод |
| `/api/loans/apply/` | POST | Подать заявку на займ |
| `/api/loans/` | GET | Список займов |
| `/api/loans/{loan_id}/` | GET | Детали займа |
| `/api/loans/{loan_id}/pay/` | POST | Погасить займ |

---

## 🤝 Вклад в проект

Приветствуются issue и pull‑request’ы.

---

## 🧪 Тестирование

```bash
python manage.py test
```

---

## 📜 Лицензия

Проект распространяется под лицензией **MIT**.

---

> 🔥 Этот README оптимизирован для тёмной темы GitHub и выглядит аккуратно при любом просмотре.
