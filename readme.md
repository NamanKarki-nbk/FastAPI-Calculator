# 📤 Submission: FastAPI Calculator

**GitHub Repository:**  
https://github.com/NamanKarki-nbk/FastAPI-Calculator

**Screen Recording Link:**  
➡️ https://youtu.be/ZGUhvW_AMKM

This project includes:
- A FastAPI calculator app
- Full Dockerization
- GitHub Actions CI (tests + linting)
- Unit testing with pytest
- Code quality checks (black, flake8, pre-commit)


---

## 🚀 Features

* Perform basic arithmetic via API:

  * `/add`
  * `/subtract`
  * `/multiply`
  * `/divide`
* Environment configuration via `.env`
* Containerized with Docker
* CI/CD with GitHub Actions
* Code quality enforced with `black`, `flake8`, and `pre-commit`
* Unit tested with `pytest`

---

## 📂 Project Structure

```
fastapi-calculator/
├── app/
│   ├── main.py
│   ├── api/routes.py
│   ├── core/config.py
│   └── services/operations.py
├── tests/test_routes.py
├── requirements.txt
├── Dockerfile
├── .env
├── .gitignore
├── .pre-commit-config.yaml
└── .github/workflows/ci.yml
```

---

## ⚙️ Getting Started

### ✅ Local Setup

1. Clone the repo and create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   uvicorn app.main:app --reload
   ```

4. Visit Swagger UI:

   ```
   http://localhost:8000/docs
   ```

---

## 🐳 Run with Docker

### Build image:

```bash
docker build -t fastapi-calculator .
```

### Run container:

```bash
docker run -d -p 8000:8000 fastapi-calculator
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🥪 Run Tests

```bash
pytest
```

---

## 🧹 Code Quality

```bash
black .
flake8 .
pre-commit run --all-files
```

---

## 🔄 GitHub Actions (CI/CD)

The workflow runs on push/pull request to `main` and performs:

* Black formatting check
* Flake8 lint check
* Pytest for unit tests

---

## 🧪 Example API Call

```bash
GET /add?a=3&b=4
Response: { "result": 7.0 }
```

---

## 👨‍💻 Author

Naman Karki
[GitHub Repo](https://github.com/NamanKarki-nbk/FastAPI-Calculator)

---

## ✅ Submission Checklist

* [✅] 12-Factor structure
* [✅] Dockerized
* [✅] GitHub Actions CI
* [✅] Pre-commit setup
* [✅] Unit test added
* [✅] README complete
* [✅] Working Swagger UI
