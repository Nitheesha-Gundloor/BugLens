import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5-coder:7b"


def analyze_with_ai(code, detected_issues):
    """
    Send BugLens findings and source code to the local Ollama model
    and return an AI-generated explanation and corrected code.
    """

    prompt = f"""
You are BugLens AI, a Python code analysis assistant.

Analyze the following Python code and the issues detected by BugLens.

SOURCE CODE:
{code}

DETECTED ISSUES:
{detected_issues}

Provide:
1. A clear explanation of the detected problems.
2. Why the problems occur.
3. Suggested fixes.
4. Corrected Python code.
5. A short list of changes made.

Return ONLY valid JSON in exactly this structure:

{{
    "explanation": "Explain the problems clearly.",
    "why_it_happens": "Explain why the problems occur.",
    "suggested_fix": "Explain how to fix them.",
    "corrected_code": "Provide the complete corrected Python code.",
    "changes_made": [
        "Change 1",
        "Change 2"
    ]
}}

Do not use Markdown code fences.
Do not add any text before or after the JSON.
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        request = urllib.request.Request(
            OLLAMA_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json"
            },
            method="POST"
        )

        with urllib.request.urlopen(request, timeout=120) as response:
            response_data = json.loads(
                response.read().decode("utf-8")
            )

        ai_response = response_data.get("response", "").strip()

        if not ai_response:
            return {
                "success": False,
                "error": "AI returned an empty response."
            }

        try:
            result = json.loads(ai_response)

            return {
                "success": True,
                "explanation": result.get("explanation", ""),
                "why_it_happens": result.get("why_it_happens", ""),
                "suggested_fix": result.get("suggested_fix", ""),
                "corrected_code": result.get("corrected_code", ""),
                "changes_made": result.get("changes_made", [])
            }

        except json.JSONDecodeError:
            return {
                "success": False,
                "error": "AI returned an invalid JSON response.",
                "raw_response": ai_response
            }

    except Exception as error:
        return {
            "success": False,
            "error": str(error)
        }