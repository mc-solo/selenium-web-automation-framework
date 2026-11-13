# Selenium Web Automation Framework

[![Selenium Tests](https://github.com/mc-solo/selenium-web-automation-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/mc-solo/selenium-web-automation-framework/actions/workflows/ci.yml)

A clean, practical Selenium test framework in **Python + pytest**, built around the
Page Object Model. It tests two public demo apps end to end in headless Chrome,
with explicit waits throughout and a daily CI run on GitHub Actions.

## What it tests

| App | Area | Tests |
| --- | --- | --- |
| SauceDemo (`saucedemo.com`) | Login: valid, locked-out, wrong password, empty, logout | 5 |
| SauceDemo (`saucedemo.com`) | Shop: 6 products, sort by price/name, cart badge, 2-item cart, full checkout | 6 |
| TodoMVC (`demo.playwright.dev/todomvc`) | Add, complete, filter active/completed, clear completed, delete | 7 |
| **Total** | | **18** |

Only public demo sites are used. SauceDemo login uses its public demo
credentials (`standard_user` / `secret_sauce`), shown on the login page itself.
No real account, private backend, or client system is involved.

## Project structure

```
.
├── config/
│   └── config.ini              # browser, URLs, timeouts, demo credentials
├── src/
│   ├── pages/
│   │   ├── base_page.py        # explicit waits, shared find/click/type helpers
│   │   ├── login_page.py       # SauceDemo login page
│   │   ├── inventory_page.py   # products, cart, checkout
│   │   └── todo_page.py        # TodoMVC page
│   └── utils/
│       ├── config_loader.py    # reads config.ini
│       └── driver_factory.py   # headless Chrome via webdriver-manager
├── tests/
│   ├── conftest.py             # fresh driver per test, page fixtures
│   ├── test_saucedemo_login.py
│   ├── test_saucedemo_shop.py
│   └── test_todomvc.py
├── .github/workflows/ci.yml    # CI on push/PR + daily cron
├── pytest.ini                  # markers: smoke, regression, login, cart, todo
└── requirements.txt
```

## How it works

- **Page Object Model**: every page has one class; locators live with the page,
  tests read like the flow a user follows.
- **Base page**: all interaction goes through explicit waits
  (`WebDriverWait` + expected conditions). No `time.sleep()`, no implicit waits.
- **Driver factory**: one place builds headless Chrome; `webdriver-manager`
  downloads the matching ChromeDriver, so nothing needs installing by hand.
- **Config file**: URLs, timeouts, and demo credentials live in
  `config/config.ini`, not in the tests.
- **Fixtures**: `conftest.py` gives each test a fresh browser and closes it
  afterwards, so tests stay independent.

## How to run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

pytest                 # full suite: 18 tests
pytest -m smoke        # smoke only: 7 tests
pytest -m regression   # full suite via marker: 18 tests
pytest -m login        # login tests: 5 tests
pytest -m cart         # cart tests: 4 tests
pytest -m todo         # TodoMVC tests: 7 tests
pytest --html=report.html --self-contained-html   # with an HTML report
```

Chrome is required. Set `headless = false` in `config/config.ini` to watch a
run in a visible browser.

## CI

`.github/workflows/ci.yml` runs on every push and pull request to `main`, on
a **daily cron at 06:00 UTC** (`0 6 * * *`), and on manual dispatch. It sets
up Python 3.12, installs dependencies, runs the full suite in headless Chrome
on `ubuntu-latest`, and uploads the HTML report as an artifact (14 days).

## Verification status

- **Collected:** 18 tests (`pytest --collect-only`), all collected cleanly.
- **Local run, 2026-11-13:** 18 errors, 0 passed, 0 failed. Every test errored
  in the fixture with `WebDriverException: cannot find Chrome binary` — this
  Linux machine has no Chrome/Chromium installed, and the Chrome download
  did not complete here. The tests themselves were not able to execute, so
  this is **not a passing run**; it is an environment gap, not a test failure.
- **Not yet verified green:** the suite still needs one green run, either on a
  machine with Chrome installed or via the GitHub Actions CI run, before the
  counts above can be called passing.

## Stack

Python 3.12 · pytest 8.3.4 · Selenium 4.27.1 · webdriver-manager 4.0.2 ·
pytest-html 4.1.1 · GitHub Actions
