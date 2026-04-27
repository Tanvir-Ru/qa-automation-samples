# 🚀 QA Automation Samples

[![Playwright Tests](https://github.com/Tanvir-Ru/qa-automation-samples/actions/workflows/playwright-tests.yml/badge.svg)](https://github.com/Tanvir-Ru/qa-automation-samples/actions/workflows/playwright-tests.yml)

A collection of automation test samples demonstrating my skills as a **Senior QA Engineer / SDET**. Includes web, API, and mobile automation frameworks with CI/CD integration.

**Author:** Tanvir Hossain — Senior QA Engineer | SDET  
📧 iamtanvir.cse@gmail.com | 🔗 [LinkedIn](https://www.linkedin.com/in/tanvir-hossain-cse/) | 🐙 [GitHub](https://github.com/Tanvir-Ru)

---

## 📁 Repository Structure
qa-automation-samples/
├── .github/workflows/
│ └── playwright-tests.yml # CI/CD pipeline (GitHub Actions)
├── playwright-demo-test.spec.ts # Playwright web automation
├── playwright.config.ts # Playwright configuration
├── package.json # Node.js dependencies
├── postman-api-collection.json # Postman API tests
├── appium-mobile-test.py # Appium mobile automation
└── README.md # This file



---

## 1. 🎭 Playwright — Web Automation

**File:** `playwright-demo-test.spec.ts`

End-to-end test suite for [SauceDemo](https://www.saucedemo.com) — a public demo e-commerce site.

### Test Cases Covered:
- ✅ Login with valid credentials
- ❌ Login with invalid credentials (error validation)
- 🛒 Add item to shopping cart
- 💳 Complete checkout flow (login → add to cart → checkout → verify order)

### Run Locally:

```bash
# Install dependencies
npm install

# Install Playwright browsers
npx playwright install

# Run all tests (headless)
npm run test:playwright

# Run tests with browser visible
npm run test:playwright:headed

# Debug mode
npm run test:playwright:debug


CI/CD Integration:
Tests run automatically via GitHub Actions on:
Every push to main branch
Every pull request
Daily schedule (6 AM UTC)

2. 📬 Postman — API Testing
File: postman-api-collection.json
Complete API test collection for JSONPlaceholder — a free fake REST API.

API Endpoints Tested:
Method	Endpoint	What It Tests
GET	/posts	Retrieve all posts + array validation
GET	/posts/1	Retrieve single post + JSON schema
POST	/posts	Create new post + response validation
PUT	/posts/1	Update existing post
DELETE	/posts/1	Delete post + status code

How to Import & Run:
Open Postman application
Click Import → Upload Files
Select postman-api-collection.json
Click Run collection or run individual requests

Included Tests (Pre-written in Postman):
Status code validation (200, 201, 404)
Response time < 2000ms
JSON body structure validation
Data type checking (id is number, title is string)
Array length assertions

3. 📱 Appium — Mobile Automation
File: appium-mobile-test.py
Mobile test suite for Android Calculator app — demonstrates mobile automation capabilities.

Test Cases Covered:
➕ Addition: 5 + 3 = 8
➖ Subtraction: 10 - 4 = 6
✖️ Multiplication: 4 × 7 = 28
🧹 Clear button functionality

Prerequisites:
# Install Appium Python client
pip install appium-python-client

# Install Appium server (globally)
npm install -g appium

# Install UiAutomator2 driver
appium driver install uiautomator2

Run Tests:
# Terminal 1: Start Appium server
appium

# Terminal 2: Run the test script
python appium-mobile-test.py

Requirements Before Running:
✅ Android emulator running OR real Android device connected
✅ USB debugging enabled (for real device)
✅ Calculator app installed (default on most Android devices)

Note: Update desired_caps in the script for your specific device/emulator.

🛠️ Tech Stack Summary
Category	      Technologies Demonstrated
Web Automation -> Playwright, TypeScript
API Testing	Postman -> REST API, JSON Schema
Mobile Automation	Appium -> Python, Android
CI/CD	GitHub Actions -> YAML
Test Design	-> Page Objects, Assertions, Waits, Data Validation

📊 Skills Demonstrated
        Skill                              	Evidence
Test automation framework design	-> playwright.config.ts with multi-browser support
Cross-browser testing             -> Tests run on Chromium, Firefox, WebKit
CI/CD integration                 ->	GitHub Actions workflow with scheduled runs
API testing (CRUD)                -> Complete Postman collection with assertions
Mobile testing                    -> Appium script for real/emulated Android
Performance testing readiness   	-> JMeter plan available (on request)
Version control	                  -> Clean Git workflow


🔜 Coming Soon
Cypress test examples
k6 performance test scripts
Dockerized test environment
Test report generation (Allure)
API test automation with REST Assured (Java)



📞 Contact
Tanvir Hossain
Senior QA Engineer | SDET
Email: iamtanvir.cse@gmail.com
LinkedIn: linkedin.com/in/tanvir-hossain-cse
GitHub: github.com/Tanvir-Ru
Location: Dhaka, Bangladesh (UTC+6)

📄 License
This project is for portfolio and demonstration purposes. Feel free to use as a reference.
                         
