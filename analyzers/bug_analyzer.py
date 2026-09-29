from analyzers.syntax_analyzer import analyze_syntax
from analyzers.ast_analyzer import analyze_ast
from analyzers.static_analyzer import (
    find_unused_variables,
    find_unused_imports,
    find_mutable_defaults,
    find_bare_except,
    find_undefined_variables,
    find_dangerous_eval,
    find_division_by_zero,
    find_unreachable_code
)
from analyzers.runtime_analyzer import analyze_runtime
from analyzers.explanation_engine import get_explanation


def analyze_code(code):

    result = {
        "syntax": analyze_syntax(code),
        "ast": analyze_ast(code),
        "static": {},
        "runtime": None,
        "summary": {
            "total_static_issues": 0
        }
    }

    # Stop analysis if syntax is invalid
    if result["syntax"]["has_error"]:
        return result

    # Run all static analysis rules
    static_results = {
        "unused_variables": find_unused_variables(code),
        "unused_imports": find_unused_imports(code),
        "mutable_defaults": find_mutable_defaults(code),
        "bare_except": find_bare_except(code),
        "undefined_variables": find_undefined_variables(code),
        "dangerous_eval": find_dangerous_eval(code),
        "division_by_zero": find_division_by_zero(code),
        "unreachable_code": find_unreachable_code(code)
    }

    # Add findings and explanations
    for issue_type, findings in static_results.items():
        result["static"][issue_type] = {
            "findings": findings,
            "explanation": get_explanation(issue_type)
        }

    # Calculate total number of static issues
    total_static_issues = sum(
        len(issue["findings"])
        for issue in result["static"].values()
    )

    result["summary"]["total_static_issues"] = total_static_issues

    # Run code for runtime analysis
    result["runtime"] = analyze_runtime(code)

    return result