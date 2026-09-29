from analyzers.ast_analyzer import analyze_ast


def test_valid_python_code():
    code = """
x = 10
print(x)
"""

    result = analyze_ast(code)

    assert result["success"] is True
    assert result["node_count"] > 0


def test_invalid_python_code():
    code = """
x = 10
print(x
"""

    result = analyze_ast(code)

    assert result["success"] is False
    assert result["node_count"] == 0