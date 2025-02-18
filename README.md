# 🚀 AI-Powered Bug Fixer (BugRemoval)  

This project is an **automated AI bug-fixing tool** that:  
✅ **Scans** Python code for linting errors and bugs.  
✅ **Uses AI (GPT-3.5-Turbo)** to suggest fixes for detected issues.  
✅ **Commits & pushes** the fixes to GitHub **automatically**.  

---

## ✨ How It Works  
1️⃣ **Linting** – The tool runs `flake8`, a Python linter, to detect errors in your repository.  
2️⃣ **AI Bug Fixing** – If issues are found, **GPT-3.5-Turbo suggests fixes** based on the `lint_report.txt` file.  
3️⃣ **Auto-Commit** – The fixed code is **automatically committed and pushed** to GitHub via GitHub Actions.  
4️⃣ **Daily Execution** – The process repeats **every day** using **GitHub Actions**.  

---

## 🎯 Why Use This?  
✅ **Keeps Your Code Clean** – Fixes linting issues **automatically**.  
✅ **Automates Code Reviews** – AI suggests fixes for **common mistakes**.  
✅ **Daily Improvements** – Your repository gets **better over time** without manual effort.  

---

## 🛠 Setup Instructions  

### **1️⃣ Install Dependencies**  
Make sure you have the necessary dependencies installed:  
```sh
pip install flake8 openai python-dotenv
