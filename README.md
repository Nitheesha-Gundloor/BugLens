# BugLens 🔍

### AI-Powered Python Code Bug Analyzer

BugLens is a Python-based code analysis web application that helps developers identify, understand, and fix common Python programming issues. It combines static code analysis, runtime error detection, rule-based explanations, and local AI-powered analysis to provide actionable debugging information.

---

## 📌 Problem Statement

Debugging Python programs often requires identifying syntax errors, understanding runtime exceptions, finding potential code issues, and determining appropriate fixes. Traditional debugging approaches may require manually inspecting code and repeatedly executing programs.

BugLens provides a centralized platform that automatically analyzes Python code and presents detected issues with explanations and suggested solutions.

---

## 🎯 Objectives

- Detect common Python code issues automatically.
- Identify syntax and runtime errors.
- Perform static analysis without executing the code.
- Provide understandable explanations for detected issues.
- Suggest possible fixes for programming errors.
- Use local AI to provide deeper explanations and corrected code.
- Provide a simple web-based interface for code analysis.

---

## 🚀 Features

### 1. Syntax Analysis

Detects Python syntax errors before further analysis is performed.

### 2. AST Analysis

Uses Python's Abstract Syntax Tree (AST) to inspect the structure of Python programs.

### 3. Static Code Analysis

BugLens detects several common coding issues, including:

- Unused variables
- Unused imports
- Mutable default arguments
- Bare `except` statements
- Undefined variables
- Dangerous `eval()` usage
- Possible division-by-zero issues
- Unreachable code
- Incorrect `None` comparisons
- Debug `print()` statements

### 4. Runtime Analysis

BugLens executes submitted Python code with a timeout and analyzes runtime failures such as:

- `ZeroDivisionError`
- `NameError`
- `TypeError`

Runtime analysis provides information such as:

- Error type
- Line number
- Source line
- Program output
- Error details

### 5. Rule-Based Explanations

Detected issues are connected to an explanation engine that provides:

- Issue description
- Why the issue matters
- Suggested improvement

### 6. Local AI Code Analysis

BugLens integrates with **Ollama** and the local `qwen2.5-coder:7b` model to provide:

- AI-generated explanations
- Reason for the error
- Suggested fixes
- Corrected Python code
- Summary of changes made

The AI analysis runs locally without requiring an external API key.

### 7. Web Interface

A Flask-based interface allows users to:

1. Enter Python code.
2. Submit the code for analysis.
3. View static analysis findings.
4. View runtime results.
5. Read explanations.
6. Review AI-generated fixes.

---

## 🏗️ System Architecture

```text
                  ┌──────────────────────┐
                  │     User / Browser   │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │     Flask Web App    │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │    BugLens Analyzer  │
                  └──────────┬───────────┘
                             │
             ┌───────────────┼────────────────┐
             │               │                │
             ▼               ▼                ▼
      ┌────────────┐  ┌─────────────┐  ┌──────────────┐
      │   Syntax   │  │ Static / AST│  │   Runtime    │
      │  Analysis  │  │   Analysis  │  │   Analysis   │
      └────────────┘  └─────────────┘  └──────────────┘
             │               │                │
             └───────────────┼────────────────┘
                             ▼
                  ┌──────────────────────┐
                  │  Explanation Engine  │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │   Local AI Analysis  │
                  │ Ollama + Qwen Coder  │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │   Results Dashboard  │
                  └──────────────────────┘

Technology Stack
Category	Technology
Programming Language	Python
Web Framework	Flask
Static Analysis	Python AST
Runtime Analysis	Python subprocess
AI Model Runtime	Ollama
AI Model	Qwen2.5-Coder 7B
Frontend	HTML, CSS, JavaScript
Testing	Pytest
Version Control	Git & GitHub
📂 Project Structure
BugLens/
│
├── analyzers/
│   ├── ai_analyzer.py
│   ├── ast_analyzer.py
│   ├── bug_analyzer.py
│   ├── explanation_engine.py
│   ├── runtime_analyzer.py
│   ├── static_analyzer.py
│   ├── syntax_analyzer.py
│   └── __init__.py
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── tests/
│   ├── test_app.py
│   ├── test_ast.py
│   ├── test_bug_analyzer.py
│   ├── test_explanation.py
│   ├── test_runtime.py
│   ├── test_static.py
│   └── test_syntax.py
│
├── app.py
├── requirements.txt
└── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/Nitheesha-Gundloor/BugLens.git
cd BugLens
2. Create a virtual environment
python -m venv venv
3. Activate the virtual environment

For Windows:

venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
🤖 Configure Local AI

BugLens uses Ollama for local AI-assisted code analysis.

Install Ollama and download the required model:

ollama pull qwen2.5-coder:7b

Make sure the Ollama service is running before using the AI analysis feature.

The application communicates with the local Ollama API at:

http://localhost:11434
▶️ Run the Application

Activate the virtual environment:

venv\Scripts\activate

Start the Flask application:

python app.py

Open the local Flask URL displayed in the terminal, usually:

http://127.0.0.1:5000
🧪 Running Tests

BugLens uses Pytest for automated testing.

Run the complete test suite:

python -m pytest -q

The current test suite contains:

46 passing tests

The tests cover different components including:

Flask application
Syntax analysis
AST analysis
Static analysis
Runtime analysis
Explanation engine
Bug analyzer integration
🔎 Example
Input
x = 10
y = 0

print(x / y)
BugLens Analysis
Static Analysis
→ Debug Print Statement

Runtime Analysis
→ ZeroDivisionError

BugLens then provides an explanation of the detected issues and suggested solutions.

When local AI analysis is available, the AI can additionally provide:

AI Explanation
→ Explanation of the issue

Why It Happens
→ Reason for the error

Suggested Fix
→ Recommended correction

Corrected Code
→ Modified version of the code

Changes Made
→ Summary of corrections
🔐 Local AI and Privacy

The AI analysis component uses a locally hosted Ollama model.

Python source code submitted for AI analysis is sent to the local Ollama service running on the user's machine rather than requiring a cloud-based AI API.

This allows AI-assisted code analysis without requiring an external AI API key.

🧩 Analysis Workflow

The general analysis workflow is:

Python Code
     │
     ▼
Syntax Check
     │
     ├── Syntax Error → Return Error
     │
     ▼
Static Analysis
     │
     ▼
AST Analysis
     │
     ▼
Runtime Analysis
     │
     ▼
Issue Detection
     │
     ▼
Rule-Based Explanation
     │
     ▼
Local AI Analysis
     │
     ▼
Results
📈 Future Enhancements

Potential future improvements include:

Additional static analysis rules
Support for more Python runtime exceptions
Code quality metrics
Downloadable analysis reports
User authentication
Analysis history
Support for additional programming languages
Improved AI-generated explanations
Integration with GitHub repositories
CI/CD integration
👥 Project

BugLens was developed as a Python full-stack project combining:

Python development
Flask web development
Static code analysis
AST-based analysis
Runtime debugging
Automated testing
Local AI integration
Git and GitHub

The project demonstrates how multiple analysis techniques can be combined into a single developer-focused debugging platform.

📄 License

This project is intended for educational and demonstration purposes.


### After replacing the README

Save it, then from your existing BugLens folder run:

```cmd
venv\Scripts\python.exe -m pytest -q

You should still get:

46 passed

Then:

git status

If only README.md is modified, commit it:

git add README.md
git commit -m "Add project documentation"
git push origin main

Finally:

git status