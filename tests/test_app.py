from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"BugLens" in response.data


def test_code_analysis():
    client = app.test_client()

    code = """
x = 10
print(x)
"""

    response = client.post(
        "/",
        data={"code": code}
    )

    assert response.status_code == 200
    assert b"No syntax errors found" in response.data
    assert b"AST analysis completed successfully" in response.data