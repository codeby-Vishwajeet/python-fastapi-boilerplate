<div align="center">

# ⚡ FastAPI Boilerplate

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-0.110-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Coverage-100%25-22c55e?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-a855f7?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/your-username/python-fastapi-boilerplate/ci.yml?label=CI%2FCD%20Pipeline&style=flat-square&logo=githubactions" />
  &nbsp;
  <img src="https://img.shields.io/github/last-commit/your-username/python-fastapi-boilerplate?style=flat-square" />
  &nbsp;
  <img src="https://img.shields.io/github/stars/your-username/python-fastapi-boilerplate?style=flat-square" />
</p>

**A production-grade, highly optimized project skeleton for building RESTful APIs using Python and FastAPI.**
Pre-configured with automated CI/CD testing, code quality gates, and containerized deployment scripts — so you ship faster, not slower.

[Get Started](#-local-setup--installation) · [View Docs](#) · [Report a Bug](#) · [Request a Feature](#)

---

</div>

## 🌟 Why This Boilerplate?

Starting a new FastAPI project from scratch means wiring up Docker, CI pipelines, test infrastructure, and project structure every single time. This boilerplate eliminates that toil. Clone it, rename it, and you're already production-ready.

<br>

## 🚀 Core Features

| Feature | Description |
|---|---|
| ⚡ **High Performance** | Built on FastAPI with ASGI — benchmarks on par with NodeJS and Go |
| 🐳 **Dockerized** | Pre-configured `Dockerfile` for seamless cloud deployments |
| 🧪 **100% Test Coverage** | Full test structure with `pytest` + `httpx` configured out of the box |
| ⚙️ **CI/CD Pipeline** | GitHub Actions runs automated tests on every push to `main` |
| 📦 **Enterprise Hygiene** | Explicit dependency tracking and clean environment separation |
| 🔒 **12-Factor Ready** | Structured logging, env configs, and security headers aligned to best practices |

<br>

## 🛠️ Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Uvicorn-FF4088?style=flat-square&logo=gunicorn&logoColor=white" />
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white" />
  <img src="https://img.shields.io/badge/HTTPX-5A9?style=flat-square" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" />
</p>

<br>

## 💻 Local Setup & Installation

### Option 1 — Native Python

```bash
# 1. Clone the repository
git clone https://github.com/your-username/python-fastapi-boilerplate

# 2. Navigate into the project
cd python-fastapi-boilerplate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Fire up the dev server
uvicorn main:app --reload
```

> 🌐 Your API is now live at **http://127.0.0.1:8000** · Interactive docs at **http://127.0.0.1:8000/docs**

### Option 2 — Docker

```bash
# Build the image
docker build -t fastapi-boilerplate .

# Run the container
docker run -p 8000:8000 fastapi-boilerplate
```

No Python installation needed. The container handles everything.

<br>

## 🧪 Running Tests

```bash
pytest
```

To run with a coverage report:

```bash
pytest --cov=. --cov-report=term-missing
```

Pytest auto-discovers all test files matching `test_*.py`. The suite includes unit tests and integration tests against the live ASGI app via `httpx`.

<br>

## 📁 Project Structure

```
python-fastapi-boilerplate/
├── main.py                 # App entrypoint & router registration
├── routers/                # Route handlers (versioned)
│   └── v1/
├── models/                 # Pydantic request/response schemas
├── services/               # Business logic layer
├── tests/                  # Pytest test suite
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions pipeline
├── Dockerfile
├── requirements.txt
└── .env.example
```

<br>

## ⚙️ CI/CD Pipeline

Every push to `main` or opened pull request automatically triggers:

1. ✅ Dependency installation
2. ✅ Linting & code style checks
3. ✅ Full test suite execution
4. ✅ Coverage threshold enforcement

Pipeline defined in `.github/workflows/ci.yml`.

<br>

## 🤝 Contributing

Contributions are welcome! Please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-thing`)
3. Commit your changes (`git commit -m 'Add amazing thing'`)
4. Push to the branch (`git push origin feature/amazing-thing`)
5. Open a Pull Request

<br>

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute, even commercially.
See the [LICENSE](LICENSE) file for full terms.

<br>

<div align="center">

Made with ❤️ and way too much `uvicorn --reload`

⭐ **Star this repo if it saves you time!**

</div>
