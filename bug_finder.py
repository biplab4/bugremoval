import subprocess


def run_flake8():
    """Runs flake8 linter and saves output to lint_report.txt."""
    try:
        result = subprocess.run(["flake8", "--max-line-length=100"], capture_output=True, text=True)

        # Always create lint_report.txt
        with open("lint_report.txt", "w") as f:
            if result.stdout:
                print("🔍 Linting Issues Found:\n", result.stdout)
                f.write(result.stdout)
            else:
                print("✅ No linting issues found.")
                f.write("No linting issues found.")

    except Exception as e:
        print(f"❌ ERROR: Flake8 failed to run: {e}")


if __name__ == "__main__":
    run_flake8()
