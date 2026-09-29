from analyzers.syntax_analyzer import analyze_syntax


def test_valid_code():
    code = """
x = 10
print(x)
"""

    result = analyze_syntax(code)

    assert result["has_error"] is False


def test_invalid_code():
    code = """
x = 10
print(x
"""

    result = analyze_syntax(code)

    assert result["has_error"] is True
    assert result["error_type"] == "SyntaxError"