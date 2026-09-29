import ast


def analyze_ast(code):
    try:
        tree = ast.parse(code)

        return {
            "success": True,
            "node_count": len(list(ast.walk(tree))),
            "message": "AST analysis completed successfully."
        }

    except SyntaxError as error:
        return {
            "success": False,
            "node_count": 0,
            "message": error.msg
        }