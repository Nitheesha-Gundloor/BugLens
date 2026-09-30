import ast
import builtins

def find_unused_variables(code):
    tree = ast.parse(code)

    assigned_variables = set()
    used_variables = set()

    for node in ast.walk(tree):

        if isinstance(node, ast.Name):

            if isinstance(node.ctx, ast.Store):
                assigned_variables.add(node.id)

            elif isinstance(node.ctx, ast.Load):
                used_variables.add(node.id)

    unused_variables = assigned_variables - used_variables

    # Ignore Python's conventional throwaway variable
    unused_variables.discard("_")

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
def find_undefined_variables(code):
    tree = ast.parse(code)

    builtin_names = set(dir(builtins))
    undefined_variables = set()

    class ScopeAnalyzer(ast.NodeVisitor):

        def __init__(self):
            self.defined = set()
            self.used = set()

        def visit_FunctionDef(self, node):
            # Function name is defined in the outer scope
            self.defined.add(node.name)

            # Analyze the function in its own local scope
            local_analyzer = ScopeAnalyzer()

            # Function parameters are already defined
            for arg in node.args.posonlyargs:
                local_analyzer.defined.add(arg.arg)

            for arg in node.args.args:
                local_analyzer.defined.add(arg.arg)

            for arg in node.args.kwonlyargs:
                local_analyzer.defined.add(arg.arg)

            if node.args.vararg:
                local_analyzer.defined.add(node.args.vararg.arg)

            if node.args.kwarg:
                local_analyzer.defined.add(node.args.kwarg.arg)

            # Analyze statements inside the function
            for statement in node.body:
                local_analyzer.visit(statement)

            # Check variables used inside the function
            for name in local_analyzer.used:
                if (
                    name not in local_analyzer.defined
                    and name not in self.defined
                    and name not in builtin_names
                ):
                    undefined_variables.add(name)

        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Store):
                self.defined.add(node.id)

            elif isinstance(node.ctx, ast.Load):
                self.used.add(node.id)

    analyzer = ScopeAnalyzer()

    # Analyze top-level code
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            analyzer.visit(node)

        else:
            analyzer.visit(node)

    for name in analyzer.used:
        if name not in analyzer.defined and name not in builtin_names:
            undefined_variables.add(name)

    return list(undefined_variables)
def find_dangerous_eval(code):
    tree = ast.parse(code)

    dangerous_calls = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "eval":
                dangerous_calls.append({
                    "line": node.lineno
                })

    return dangerous_calls
def find_division_by_zero(code):
    tree = ast.parse(code)

    division_errors = []

    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp):
            if isinstance(node.op, (ast.Div, ast.FloorDiv, ast.Mod)):
                if isinstance(node.right, ast.Constant) and node.right.value == 0:
                    division_errors.append({
                        "line": node.lineno
                    })

    return division_errors
def find_unreachable_code(code):
    tree = ast.parse(code)

    unreachable_lines = []

    for node in ast.walk(tree):
        statements = []

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            statements = node.body

        elif isinstance(node, (ast.For, ast.While)):
            statements = node.body

        elif isinstance(node, ast.If):
            statements = node.body

        for index, statement in enumerate(statements):
            if isinstance(
                statement,
                (ast.Return, ast.Raise, ast.Break, ast.Continue)
            ):
                for unreachable in statements[index + 1:]:
                    unreachable_lines.append({
                        "line": unreachable.lineno
                    })
                break

    return unreachable_lines
def find_none_comparison(code):
    tree = ast.parse(code)

    none_comparisons = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Compare):

            for operator, comparator in zip(
                node.ops,
                node.comparators
            ):

                if isinstance(operator, (ast.Eq, ast.NotEq)):
                    if (
                        isinstance(comparator, ast.Constant)
                        and comparator.value is None
                    ):
                        none_comparisons.append({
                            "line": node.lineno
                        })

    return none_comparisons
def find_none_comparison(code):
    tree = ast.parse(code)

    none_comparisons = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Compare):

            for operator, comparator in zip(
                node.ops,
                node.comparators
            ):

                if isinstance(operator, (ast.Eq, ast.NotEq)):
                    if (
                        isinstance(comparator, ast.Constant)
                        and comparator.value is None
                    ):
                        none_comparisons.append({
                            "line": node.lineno
                        })

    return none_comparisons
def find_debug_prints(code):
    tree = ast.parse(code)

    debug_prints = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if (
                isinstance(node.func, ast.Name)
                and node.func.id == "print"
            ):
                debug_prints.append({
                    "line": node.lineno
                })

    return debug_prints