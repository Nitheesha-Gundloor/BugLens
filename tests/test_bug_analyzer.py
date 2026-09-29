from analyzers.bug_analyzer import analyze_code


def test_complete_analysis():
    code = """
import os

x = 10
y = 20

print(x)

def greet(name=[]):
    print(name)

try:
    print(x / 0)
except:
    pass
"""

    result = analyze_code(code)

    assert result["syntax"]["has_error"] is False
    assert result["ast"]["success"] is True

    assert "y" in result["static"]["unused_variables"]
    assert "os" in result["static"]["unused_imports"]
    assert len(result["static"]["mutable_defaults"]) > 0
    assert len(result["static"]["bare_except"]) > 0
    assert len(result["static"]["division_by_zero"]) > 0


def test_invalid_syntax_stops_analysis():
    code = """
x = 10
print(x
"""

    result = analyze_code(code)

    assert result["syntax"]["has_error"] is True
    assert result["static"] == {}
    assert result["runtime"] is None