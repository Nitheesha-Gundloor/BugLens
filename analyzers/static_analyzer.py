import ast


def find_unused_variables(code):
    tree = ast.parse(code)

    assigned_variables = set()
    used_variables = set()

    for node in ast.walk(tree):

        # Find variables that receive values
        if isinstance(node, ast.Name):
            if isinstance(node.ctx, ast.Store):
                assigned_variables.add(node.id)

            elif isinstance(node.ctx, ast.Load):
                used_variables.add(node.id)

    unused_variables = assigned_variables - used_variables

    return list(unused_variables)
def find_unused_imports(code):
    tree = ast.parse(code)

    imported_names = set()
    used_names = set()

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):
            for alias in node.names:
                name = alias.asname if alias.asname else alias.name.split(".")[0]
                imported_names.add(name)

        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                name = alias.asname if alias.asname else alias.name
                imported_names.add(name)

        elif isinstance(node, ast.Name):
            if isinstance(node.ctx, ast.Load):
                used_names.add(node.id)

    unused_imports = imported_names - used_names

    return list(unused_imports)
def find_mutable_defaults(code):
    tree = ast.parse(code)

    mutable_defaults = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

            for default in node.args.defaults:
                if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                    mutable_defaults.append({
                        "function": node.name,
                        "line": node.lineno
                    })

    return mutable_defaults
def find_bare_except(code):
    tree = ast.parse(code)

    bare_excepts = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ExceptHandler):
            if node.type is None:
                bare_excepts.append({
                    "line": node.lineno
                })

    return bare_excepts