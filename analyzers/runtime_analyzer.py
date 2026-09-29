import subprocess
import sys
import tempfile
import os


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
                "message": "Code executed successfully.",
                "output": result.stdout
            }

        error_lines = result.stderr.strip().splitlines()

        error_type = "RuntimeError"

        if error_lines:
            last_line = error_lines[-1]
            error_type = last_line.split(":")[0]

        return {
            "has_error": True,
            "error_type": error_type,
            "message": result.stderr.strip(),
            "output": result.stdout
        }

    except subprocess.TimeoutExpired:
        return {
            "has_error": True,
            "error_type": "TimeoutError",
            "message": "Code execution exceeded the 5-second limit.",
            "output": ""
        }

    finally:
        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)