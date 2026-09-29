from analyzers.static_analyzer import find_unused_variables
from analyzers.static_analyzer import find_unused_imports
from analyzers.static_analyzer import find_mutable_defaults
from analyzers.static_analyzer import find_bare_except
from analyzers.static_analyzer import find_undefined_variables
from analyzers.static_analyzer import find_dangerous_eval
from analyzers.static_analyzer import find_division_by_zero
from analyzers.static_analyzer import find_unreachable_code

def test_unused_variable():
    code = """
x = 10
y = 20
print(x)
"""

    result = find_unused_variables(code)

    assert "y" in result
    assert "x" not in result


def test_no_unused_variable():
    code = """
x = 10
print(x)
"""

    result = find_unused_variables(code)

    assert result == []
def test_unused_import():
    code = """
import os
import math

print(math.sqrt(16))
"""

    result = find_unused_imports(code)

    assert "os" in result
    assert "math" not in result


def test_no_unused_import():
    code = """
import math

print(math.sqrt(16))
"""

    result = find_unused_imports(code)

    assert result == []
def test_mutable_default_argument():
    code = """
def add_item(item, items=[]):
    items.append(item)
    return items
"""

    result = find_mutable_defaults(code)

    assert len(result) == 1
    assert result[0]["function"] == "add_item"


def test_no_mutable_default_argument():
    code = """
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
"""

    result = find_mutable_defaults(code)

    assert result == []
def test_bare_except():
    code = """
try:
    x = 10 / 0
except:
    print("Error")
"""

    result = find_bare_except(code)

    assert len(result) == 1
    assert result[0]["line"] == 4


def test_specific_except():
    code = """
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error")
"""

    result = find_bare_except(code)

    assert result == []
def test_undefined_variable():
    code = """
x = 10
print(x)
print(y)
"""

    result = find_undefined_variables(code)

    assert "y" in result
    assert "x" not in result


def test_defined_variable_and_builtin():
    code = """
x = 10
print(x)
"""

    result = find_undefined_variables(code)

    assert result == []
def test_dangerous_eval():
    code = """
user_input = input("Enter expression: ")
result = eval(user_input)
"""

    result = find_dangerous_eval(code)

    assert len(result) == 1
    assert result[0]["line"] == 3


def test_no_eval():
    code = """
x = 10
result = x + 5
"""

    result = find_dangerous_eval(code)

    assert result == []
def test_division_by_zero():
    code = """
result = 10 / 0
"""

    result = find_division_by_zero(code)

    assert len(result) == 1
    assert result[0]["line"] == 2


def test_valid_division():
    code = """
x = 10
result = x / 2
"""

    result = find_division_by_zero(code)

    assert result == []
def test_unreachable_code():
    code = """
def calculate():
    return 10
    print("unreachable")
"""

    result = find_unreachable_code(code)

    assert len(result) == 1
    assert result[0]["line"] == 4


def test_reachable_code():
    code = """
def calculate():
    x = 10
    return x
"""

    result = find_unreachable_code(code)

    assert result == []