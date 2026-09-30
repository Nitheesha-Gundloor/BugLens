import subprocess
import sys
import tempfile
import os
import re


RUNTIME_ERROR_MAPPING = {
    "ZeroDivisionError": "zero_division_error",
    "NameError": "name_error",
    "TypeError": "type_error"
}


def analyze_runtime(code):
    temp_file = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8"
        ) as file:
            file.write(code)
            temp_file = file.name

        result = subprocess.run(
            [sys.executable, temp_file],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            return {
                "has_error": False,
                "error_type": None,
                "issue_type": None,
                "message": "Code executed successfully.",
                "output": result.stdout,
                "line_number": None,
                "source_line": None
            }

        error_message = result.stderr.strip()

        # Extract the line number from the traceback
        line_number = None

        match = re.search(r'line (\d+)', error_message)

        if match:
            line_number = int(match.group(1))

        # Extract the actual error type
        error_type = "RuntimeError"

        error_lines = error_message.splitlines()

        if error_lines:
            last_line = error_lines[-1]
            error_type = last_line.split(":")[0]

        # Map Python error type to BugLens issue type
        issue_type = RUNTIME_ERROR_MAPPING.get(
            error_type,
            "runtime_error"
        )

        # Get the source line that caused the error
        source_line = None

        if line_number is not None:
            code_lines = code.splitlines()

            if 1 <= line_number <= len(code_lines):
                source_line = code_lines[line_number - 1].strip()

        return {
            "has_error": True,
            "error_type": error_type,
            "issue_type": issue_type,
            "message": error_message,
            "output": result.stdout,
            "line_number": line_number,
            "source_line": source_line
        }

    except subprocess.TimeoutExpired:
        return {
            "has_error": True,
            "error_type": "TimeoutError",
            "issue_type": "timeout_error",
            "message": "Code execution exceeded the 5-second limit.",
            "output": "",
            "line_number": None,
            "source_line": None
        }

    finally:
        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)