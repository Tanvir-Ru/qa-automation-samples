# 🧪 QA Automation Samples

[![Playwright Tests](https://github.com/Tanvir-Ru/qa-automation-samples/actions/workflows/playwright-tests.yml/badge.svg)](https://github.com/Tanvir-Ru/qa-automation-samples/actions/workflows/playwright-tests.yml)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=playwright&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat&logo=postman&logoColor=white)
![Appium](https://img.shields.io/badge/Appium-6D00CC?style=flat&logo=appium&logoColor=white)
![JMeter](https://img.shields.io/badge/JMeter-D22128?style=flat&logo=apachejmeter&logoColor=white)

> A portfolio-grade collection of QA automation samples demonstrating expertise across **Web**, **API**, **Mobile**, and **Performance** testing — with full **CI/CD integration** via GitHub Actions.

**Author:** Tanvir Hossain — Senior QA Engineer | SDET  
📧 [iamtanvir.cse@gmail.com](mailto:iamtanvir.cse@gmail.com) &nbsp;|&nbsp; 🔗 [LinkedIn](https://www.linkedin.com/in/tanvir-hossain-cse/) &nbsp;|&nbsp; 🐙 [GitHub](https://github.com/Tanvir-Ru) &nbsp;|&nbsp; 📍 Dhaka, Bangladesh

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [Tech Stack](#-tech-stack)
- [1. Playwright — Web Automation](#1--playwright--web-automation)
- [2. Postman — API Testing](#2--postman--api-testing)
- [3. Appium — Mobile Automation](#3--appium--mobile-automation)
- [4. JMeter — Performance Testing](#4--jmeter--performance-testing)
- [5. CI/CD — GitHub Actions](#5--cicd--github-actions)
- [Getting Started](#-getting-started)
- [Skills Demonstrated](#-skills-demonstrated)
- [Coming Soon](#-coming-soon)
- [Contact](#-contact)

---

## 🔍 Overview

This repository showcases real-world QA automation scripts across multiple layers of the testing pyramid. Each file is a standalone, runnable sample that reflects industry best practices, clean code structure, and practical test coverage.

| Layer | Tool | Language | Target |
|---|---|---|---|
| Web (E2E) | Playwright | TypeScript | SauceDemo e-commerce |
| API | Postman + Newman | JSON | JSONPlaceholder REST API |
| Mobile | Appium | Python | Android Calculator App |
| Performance | JMeter | XML | HTTP load scenarios |
| CI/CD | GitHub Actions | YAML | Automated pipeline |

---

## 📁 Repository Structure

```
qa-automation-samples/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml      # CI/CD pipeline (GitHub Actions)
├── playwright-demo-test.spec.ts      # Playwright web E2E tests
├── playwright.config.ts              # Playwright multi-browser config
├── package.json                      # Node.js dependencies
├── postman-api-collection.json       # Postman REST API test collection
├── appium-mobile-test.py             # Appium mobile automation (Python)
├── jmeter-performance-test.jmx       # JMeter performance test plan
└── README.md                         # This file
```

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Web Automation | Playwright, TypeScript |
| API Testing | Postman, Newman, REST |
| Mobile Testing | Appium, Python, Android |
| Performance Testing | Apache JMeter |
| CI/CD | GitHub Actions |
| Package Management | Node.js / npm, pip |

---

## 1. 🎭 Playwright — Web Automation

**File:** [`playwright-demo-test.spec.ts`](./playwright-demo-test.spec.ts)  
**Config:** [`playwright.config.ts`](./playwright.config.ts)

End-to-end test suite for [SauceDemo](https://www.saucedemo.com) — a publicly available demo e-commerce application, commonly used for testing practice.

### ✅ Test Cases

| # | Test | Description |
|---|---|---|
| 1 | Happy path checkout | Login → Add item to cart → Fill shipping info → Complete order |
| 2 | Invalid login | Attempts login with wrong password, asserts error message |

### 🔑 Key Techniques Used

- `data-test` attribute selectors (stable, non-brittle locators)
- `expect` assertions with URL matching and text content validation
- Sequential user flow testing (multi-step E2E)
- `test.describe` grouping for organized test suites

### ▶️ Run Locally

```bash
# Install dependencies
npm install

# Install Playwright browsers
npx playwright install

# Run all tests
npx playwright test

# Run with UI mode (headed)
npx playwright test --ui

# Run a specific file
npx playwright test playwright-demo-test.spec.ts

# View HTML report after run
npx playwright show-report
```

---

## 2. 📬 Postman — API Testing

**File:** [`postman-api-collection.json`](./postman-api-collection.json)

A complete REST API test collection for [JSONPlaceholder](https://jsonplaceholder.typicode.com) — a free, open fake API for testing and prototyping.

### ✅ Endpoints Tested

| Method | Endpoint | What Is Validated |
|---|---|---|
| `GET` | `/posts` | Status 200, response is an array, length > 0 |
| `GET` | `/posts/1` | Status 200, JSON schema (id, title, body, userId) |
| `POST` | `/posts` | Status 201, created resource returned with correct fields |
| `PUT` | `/posts/1` | Status 200, updated fields reflected in response |
| `DELETE` | `/posts/1` | Status 200, successful deletion confirmed |

### 🔑 Key Techniques Used

- Status code assertions (`pm.response.to.have.status`)
- Response time validation (`< 2000ms`)
- JSON schema and data type checks
- Environment-agnostic design (can point to any base URL)

### ▶️ How to Import & Run

**In Postman (UI):**
1. Open Postman → click **Import**
2. Upload `postman-api-collection.json`
3. Hit **Run collection** to execute all requests

**Via CLI with Newman:**
```bash
# Install Newman globally
npm install -g newman

# Run the collection
newman run postman-api-collection.json

# Run with HTML report
npm install -g newman-reporter-htmlextra
newman run postman-api-collection.json -r htmlextra
```

---

## 3. 📱 Appium — Mobile Automation

**File:** [`appium-mobile-test.py`](./appium-mobile-test.py)

Mobile test suite for the Android Calculator app, demonstrating native mobile automation using Appium with Python.

### ✅ Test Cases

| # | Operation | Input | Expected Result |
|---|---|---|---|
| 1 | Addition | 5 + 3 | 8 |
| 2 | Subtraction | 10 − 4 | 6 |
| 3 | Multiplication | 4 × 7 | 28 |
| 4 | Clear | Any input | Display cleared |

### 🔑 Key Techniques Used

- `desired_capabilities` for device/app configuration
- Element interaction via Appium locator strategies
- Result assertion against expected calculator output
- Teardown and session cleanup

### ⚙️ Prerequisites

Before running, ensure:

- ✅ Android emulator is running **OR** a real Android device is connected via USB
- ✅ USB Debugging is enabled on the device
- ✅ Appium server is running (`appium` command in terminal)
- ✅ Calculator app is installed (pre-installed on most Android devices)
- ✅ Update `desired_caps` in the script to match your device/emulator details

### ▶️ Run Locally

```bash
# Install Python dependencies
pip install Appium-Python-Client

# Start Appium server (in a separate terminal)
appium

# Run the test
python appium-mobile-test.py
```

---

## 4. ⚡ JMeter — Performance Testing

**File:** [`jmeter-performance-test.jmx`](./jmeter-performance-test.jmx)

An Apache JMeter test plan for HTTP performance and load testing. Useful for identifying response time degradation, throughput limits, and system behaviour under concurrent load.

### ▶️ Run Locally

```bash
# GUI mode (for editing/viewing)
jmeter -t jmeter-performance-test.jmx

# Non-GUI mode (for actual load execution)
jmeter -n -t jmeter-performance-test.jmx -l results.jtl

# Generate HTML dashboard report
jmeter -g results.jtl -o ./report
```

> **Note:** Apache JMeter must be installed. Download from [jmeter.apache.org](https://jmeter.apache.org/download_jmeter.cgi).

---

## 5. 🔄 CI/CD — GitHub Actions

**File:** [`.github/workflows/playwright-tests.yml`](./.github/workflows/playwright-tests.yml)

Playwright tests are automatically executed on every push and pull request via GitHub Actions.

### Pipeline Features

- Triggers on `push` and `pull_request` to `main`
- Installs Node.js dependencies and Playwright browsers
- Runs the full test suite in headless mode
- Uploads test reports as build artifacts
- Badge status visible at the top of this README

### View Live Runs

👉 [Actions Tab](https://github.com/Tanvir-Ru/qa-automation-samples/actions)

---

## 🚀 Getting Started

### Prerequisites

| Tool | Version | Required For |
|---|---|---|
| Node.js | ≥ 18.x | Playwright |
| npm | ≥ 9.x | Playwright |
| Python | ≥ 3.8 | Appium |
| Java | ≥ 11 | JMeter |
| Appium | ≥ 2.x | Mobile tests |
| Apache JMeter | ≥ 5.x | Performance tests |
| Postman / Newman | Latest | API tests |

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/Tanvir-Ru/qa-automation-samples.git
cd qa-automation-samples

# Install Node dependencies (for Playwright)
npm install
npx playwright install

# Install Python dependencies (for Appium)
pip install Appium-Python-Client

# Run Playwright tests
npx playwright test
```

---

## 💡 Skills Demonstrated

| Skill | Evidence |
|---|---|
| E2E test design | Full login-to-checkout flow with assertions at each step |
| Stable locator strategy | Uses `data-test` attributes — not brittle CSS/XPath |
| Multi-browser testing | Playwright config supports Chromium, Firefox, WebKit |
| REST API coverage | Full CRUD coverage with schema and status validation |
| Mobile test automation | Appium Python scripts for Android native app |
| Performance test planning | JMeter plan with configurable load parameters |
| CI/CD integration | GitHub Actions pipeline with automated test runs |
| Clean code | Descriptive test names, comments, structured test files |
| Version control | Organised Git history with meaningful commit messages |

---

## 🔜 Coming Soon

- [ ] Cypress test examples (JavaScript)
- [ ] k6 performance test scripts
- [ ] REST Assured API tests (Java)
- [ ] Allure test report integration
- [ ] Dockerized test environment
- [ ] Data-driven testing with external test data files
- [ ] Page Object Model (POM) refactor for Playwright tests

---

## 📞 Contact

**Tanvir Hossain**  
Senior QA Engineer | SDET

| | |
|---|---|
| 📧 Email | [iamtanvir.cse@gmail.com](mailto:iamtanvir.cse@gmail.com) |
| 🔗 LinkedIn | [linkedin.com/in/tanvir-hossain-cse](https://www.linkedin.com/in/tanvir-hossain-cse/) |
| 🐙 GitHub | [github.com/Tanvir-Ru](https://github.com/Tanvir-Ru) |
| 📍 Location | Dhaka, Bangladesh (UTC+6) |

---

## 📄 License

This repository is intended for **portfolio and demonstration purposes**.  
Feel free to use these scripts as a reference or learning resource.

---

<p align="center">
  <i>Built with ❤️ to showcase real-world QA automation skills</i>
</p>
