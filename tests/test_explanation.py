from analyzers.explanation_engine import get_explanation


def test_division_by_zero_explanation():
    result = get_explanation("division_by_zero")

    assert result["title"] == "Division by Zero"
    assert "zero" in result["description"].lower()
    assert "divisor" in result["suggestion"].lower()


def test_unused_variable_explanation():
    result = get_explanation("unused_variables")

    assert result["title"] == "Unused Variable"
    assert "variable" in result["description"].lower()


def test_unknown_issue():
    result = get_explanation("unknown_issue")

    assert result["title"] == "Unknown Issue"