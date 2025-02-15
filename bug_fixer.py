import openai
import os

# Load OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client (NEW API FORMAT)
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def read_lint_report():
    """Reads the lint report and returns the error text."""
    if not os.path.exists("lint_report.txt"):
        print("❌ ERROR: lint_report.txt file NOT found!")
        return None

    with open("lint_report.txt", "r") as f:
        errors = f.read().strip()

    if not errors:
        print("✅ No linting issues found in lint_report.txt.")
        return None

    print("🔍 Linting Issues Detected:\n", errors)
    return errors

def generate_fix(lint_errors):
    """Uses GPT-4 to generate a fix for the linting errors."""
    if lint_errors is None:
        print("❌ No lint errors found. Skipping AI Fix.")
        return None

    if not OPENAI_API_KEY:
        print("❌ ERROR: OpenAI API Key is missing!")
        return None

    print("⏳ Sending request to OpenAI for a fix...")
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert Python developer."},
                {"role": "user", "content": f"Here are some Python linting errors:\n\n{lint_errors}\n\nPlease provide the corrected code."}
            ]
        )
        fixed_code = response.choices[0].message.content
        print("✅ AI generated a fix!")
        return fixed_code
    except Exception as e:
        print(f"❌ OpenAI API Error: {e}")
        return None

def save_fixed_code(fixed_code):
    """Saves the AI-fixed code into a new file."""
    if fixed_code:
        with open("fixed_code.py", "w") as f:
            f.write(fixed_code)
        print("✅ Fixed code saved to fixed_code.py!")
    else:
        print("❌ No fixes were generated.")

if __name__ == "__main__":
    print("🚀 Running AI Bug Fixer...")
    lint_errors = read_lint_report()

    if lint_errors:
        fixed_code = generate_fix(lint_errors)
        save_fixed_code(fixed_code)
    else:
        print("🛑 No issues to fix.")
