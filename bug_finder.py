import subprocess

def run_flake8():
    """Runs flake8 linter and saves output to lint_report.txt."""
    result = subprocess.run(["flake8", "--max-line-length=100"], capture_output=True, text=True)

    if result.stdout:
        print("🔍 Linting Issues Found:\n", result.stdout)
        with open("lint_report.txt", "w") as f:
            f.write(result.stdout)
    else:
        print("✅ No linting issues found.")

if __name__ == "__main__":
    run_flake8()
