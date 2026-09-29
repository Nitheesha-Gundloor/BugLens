import ast


def analyze_ast(code):
    try:
        tree = ast.parse(code)

        functions = []
        classes = []
        imports = []
        variables = []

        for node in ast.walk(tree):

            # Detect functions
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                functions.append(node.name)

            # Detect classes
            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)

            # Detect imports
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(
                        alias.asname if alias.asname else alias.name
                    )

            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    imports.append(
                        alias.asname if alias.asname else alias.name
                    )

            # Detect variables
            elif isinstance(node, ast.Name):
                if isinstance(node.ctx, ast.Store):
                    variables.append(node.id)

        return {
            "success": True,
            "node_count": len(list(ast.walk(tree))),
            "functions": functions,
            "classes": classes,
            "imports": imports,
            "variables": variables,
            "message": "AST analysis completed successfully."
        }

    except SyntaxError as error:
        return {
            "success": False,
            "node_count": 0,
            "functions": [],
            "classes": [],
            "imports": [],
            "variables": [],
            "message": error.msg
        }