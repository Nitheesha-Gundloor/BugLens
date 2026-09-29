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


def analyze_code(code):

    result = {
        "syntax": analyze_syntax(code),
        "ast": analyze_ast(code),
        "static": {},
        "runtime": None
    }

    # Stop here if syntax is invalid
    if result["syntax"]["has_error"]:
        return result

    result["static"] = {
        "unused_variables": find_unused_variables(code),
        "unused_imports": find_unused_imports(code),
        "mutable_defaults": find_mutable_defaults(code),
        "bare_except": find_bare_except(code),
        "undefined_variables": find_undefined_variables(code),
        "dangerous_eval": find_dangerous_eval(code),
        "division_by_zero": find_division_by_zero(code),
        "unreachable_code": find_unreachable_code(code)
    }

    result["runtime"] = analyze_runtime(code)

    return result