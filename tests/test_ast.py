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


def test_detect_functions():
    code = """
def greet(name):
    print(name)
"""

    result = analyze_ast(code)

    assert result["success"] is True
    assert "greet" in result["functions"]


def test_detect_classes():
    code = """
class Person:
    pass
"""

    result = analyze_ast(code)

    assert result["success"] is True
    assert "Person" in result["classes"]


def test_detect_imports():
    code = """
import os
from math import sqrt
"""

    result = analyze_ast(code)

    assert result["success"] is True
    assert "os" in result["imports"]
    assert "sqrt" in result["imports"]


def test_detect_variables():
    code = """
x = 10
y = 20
"""

    result = analyze_ast(code)

    assert result["success"] is True
    assert "x" in result["variables"]
    assert "y" in result["variables"]