import autopep8


c = autopep8
# Read the code from test.py
with open("test.py", "r", encoding="utf-8") as file:
    code = file.read()

# Automatically fix the code
fixed_code = c.fix_code(code)

# Save the fixed code back to test.py
with open("test.py", "w", encoding="utf-8") as file:
    file.write(fixed_code)

print("✅ Code formatting fixed using autopep8!")
