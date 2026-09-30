from analyzers.runtime_analyzer import analyze_runtime


def test_successful_execution():
    code = """
x = 10
print(x)
"""

    result = analyze_runtime(code)

    assert result["has_error"] is False
    assert result["error_type"] is None
    assert result["issue_type"] is None
    assert "10" in result["output"]


def test_runtime_error():
    code = """
x = 10
y = 0
print(x / y)
"""

    result = analyze_runtime(code)

    assert result["has_error"] is True
    assert result["error_type"] == "ZeroDivisionError"
    assert result["issue_type"] == "zero_division_error"


def test_runtime_error_location():
    code = """
x = 10
y = 0
print(x / y)
"""

    result = analyze_runtime(code)

    assert result["has_error"] is True
    assert result["error_type"] == "ZeroDivisionError"
    assert result["issue_type"] == "zero_division_error"
    assert result["line_number"] == 4
    assert result["source_line"] == "print(x / y)"


def test_timeout():
    code = """
while True:
    pass
"""

    result = analyze_runtime(code)

    assert result["has_error"] is True
    assert result["error_type"] == "TimeoutError"
    assert result["issue_type"] == "timeout_error"