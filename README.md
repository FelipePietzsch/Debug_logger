# 🐛 DebugLogger – Simple and Flexible Debug Logging for Python

**DebugLogger** is a lightweight and easy-to-integrate Python module that enables structured error logging through decorators. It is designed to be added to existing projects with minimal effort, supporting both procedural and object-oriented code.

---

## 🚀 Features

- Minimal setup with a single decorator: `@DebugLog.printer` or `@DebugLog.raiser`
- Logs both caught and raised exceptions
- Saves detailed logs to a file
- Console output for quick debugging
- Does not interrupt the program (printer mode) or optionally raises exceptions (raiser mode)
- Configurable via `.env` file

---

## ⚙️ Usage

### Import and Apply the Decorator

```python
from src.debug_logger import DebugLog

@DebugLog.printer
def safe_function():
    # Will catch and log errors, then continue execution

@DebugLog.raiser
def critical_function():
    # Will catch, log, and raise errors to stop execution
```

## Logging Modes

### printer
	•	Catches errors
	•	Prints a short error message in the console
	•	Logs full traceback to a file
	•	Allows the program to continue

### raiser
	•	Catches errors
	•	Logs the error and raises it again
	•	Stops the program
	•	Console will show both the system exception and DebugLogger output

⚠️ Known issue: Both the system and DebugLogger print the error. This will be improved in a future update.

### 🔧 Custom Exceptions

By default, DebugLogger will handle the following built-in exceptions:

```python
EXCEPTIONS = (ValueError, TypeError, AttributeError, SyntaxError)
```

If you want to log other types of exceptions (e.g., from external libraries like SQLAlchemy or FastAPI), you can extend this tuple by importing the exception first and then adding it.

#### ➕ Example: Adding SQLAlchemy Exceptions
```
from sqlalchemy.exc import IntegrityError
from debug_logger import DebugLog

DebugLog.EXCEPTIONS += (IntegrityError,)
```

## 🧪 Implementation Examples

### Procedural Example

See prozedural_code.py for a full demo.
```python
@DebugLog.printer
def divide(a, b):
    return a / b

divide(5, 0)  # Error is logged and printed, program continues
```

### Object-Oriented Example

See oop_code.py for full implementation.
```python
class MathOperations:
    
    @DebugLog.raiser
    def divide(self, a, b):
        return a / b # Error is logged and printed, program continues
```

## 🛠️ Configuration

All environment-specific settings (such as log file path) are stored in a .env file.
A template file .env.template is provided as an example.
```
# .env
DEBUG_LOG_FILE_PATH = "example/path/debug.log"
```

## 📁 Project Structure
````
debug_logger/
├── src
    ├── debug_logger.py
    ├──implementation_code
        ├── prozedural_code.py
        ├── oop_code.py
├── .env.template
├── requirements.txt
````

## 📦 Installation
	1.	Clone the repository
	2.	Create a .env file based on .env.template
	3.	Install dependencies

````bash
pip install -r requirements.txt
````

## 📝 Log Output

Logged errors include:
	•	Timestamp
	•	Function/method name
	•	Full traceback
	•	Type of error

Example log entry:
```
[2025-05-21 13:14:22] ERROR in divide: division by zero
Traceback (most recent call last):
  File "prozedural_code.py", line 10, in divide
    return a / b
ZeroDivisionError: division by zero
```

## ❗ Known Limitations/Features ;)
	•	In raiser mode, error output appears twice (once from the system and once from DebugLogger)

## 📌 Notes
	•	This is a private project
	•	Intended for internal or personal use
	•	Feel free to adapt it to your needs!
