EXPLANATIONS = {
    "unused_variables": {
        "title": "Unused Variable",
        "description": "A variable is assigned a value but is never used later in the code.",
        "suggestion": "Remove the variable if it is unnecessary, or use it where required."
    },

    "unused_imports": {
        "title": "Unused Import",
        "description": "An imported module or name is not used in the code.",
        "suggestion": "Remove the import if it is not required."
    },

    "mutable_defaults": {
        "title": "Mutable Default Argument",
        "description": "A function uses a mutable object such as a list, dictionary, or set as a default argument.",
        "suggestion": "Use None as the default value and create the mutable object inside the function."
    },

    "bare_except": {
        "title": "Bare Except",
        "description": "The code catches all exceptions without specifying an exception type.",
        "suggestion": "Catch a specific exception type such as ValueError or TypeError."
    },

    "undefined_variables": {
        "title": "Undefined Variable",
        "description": "A variable is used before it has been defined.",
        "suggestion": "Define the variable before using it and check for spelling mistakes."
    },

    "dangerous_eval": {
        "title": "Dangerous eval() Usage",
        "description": "eval() executes dynamically generated Python code and can introduce security risks.",
        "suggestion": "Avoid eval() when possible and use safer alternatives such as ast.literal_eval() for data parsing."
    },

    "division_by_zero": {
        "title": "Division by Zero",
        "description": "The code attempts to divide, floor-divide, or take modulo by zero.",
        "suggestion": "Check that the divisor is not zero before performing the operation."
    },

    "unreachable_code": {
        "title": "Unreachable Code",
        "description": "This code appears after a return, raise, break, or continue statement and may never execute.",
        "suggestion": "Remove the unreachable statements or move them before the control-flow statement."
    },
    "none_comparison": {
    "title": "None Comparison",
    "description": "The code compares a value with None using == or != instead of the identity operators is or is not.",
    "suggestion": "Use 'is None' or 'is not None' when checking whether a value is None."
    }
}


def get_explanation(issue_type):
    return EXPLANATIONS.get(
        issue_type,
        {
            "title": "Unknown Issue",
            "description": "No explanation is available for this issue.",
            "suggestion": "Review the reported code and check its behavior."
        }
    )