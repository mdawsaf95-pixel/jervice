import os

# Use the newer `google.genai` client wherever possible.
# Supports text-only testing without microphone installation issues.

GOOGLE_API_KEY = os.environ.get("JERVICE_API_KEY")
if not GOOGLE_API_KEY:
    try:
        GOOGLE_API_KEY = input('Enter your JERVICE API key (leave blank to skip): ').strip() or None
    except Exception:
        GOOGLE_API_KEY = None

HAS_GENAI = False
client = None
MODEL_NAME = "models/gemini-2.5-flash"

try:
    from google import genai
    client = genai.Client(api_key=GOOGLE_API_KEY) if GOOGLE_API_KEY else genai.Client()
    HAS_GENAI = True
except Exception as exc:
    print('Warning: google.genai client not available:', exc)
    HAS_GENAI = False


def ask_jervice(prompt):
    if not HAS_GENAI or not client:
        return "No Google GenAI client is available in this environment. Install google-genai."

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=f"Respond in a very short, crisp and friendly manner: {prompt}",
        )
        if hasattr(response, 'text') and response.text:
            return response.text
        if hasattr(response, 'output') and response.output:
            try:
                return response.output[0].content[0].text
            except Exception:
                pass
        return str(response)
    except Exception as exc:
        return f"Error contacting Jervice: {exc}"


if __name__ == '__main__':
    print("Text-mode AI assistant (type 'exit' to quit)")
    if not HAS_GENAI:
        print('No Google GenAI client installed. Install `google-genai` in your environment.')
    while True:
        user_input = input('You: ').strip()
        if not user_input:
            continue
        if user_input.lower() in ('exit', 'quit', 'stop'):
            print('Goodbye!')
            break
        ai_response = ask_jervice(user_input)
        print('AI:', ai_response)
