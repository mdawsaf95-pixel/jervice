import os
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

MODEL_NAME = 'models/gemini-2.5-flash'
JERVICE_API_KEY = os.environ.get('JERVICE_API_KEY')

try:
    from google import genai
    client = genai.Client(api_key=JERVICE_API_KEY) if JERVICE_API_KEY else genai.Client()
except Exception as exc:
    client = None
    genai_error = str(exc)
else:
    genai_error = None


def ask_jervice(prompt):
    if not client:
        raise RuntimeError('Jervice client is not configured. Install google-genai and set JERVICE_API_KEY.')

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=f"Jervice: Respond as a short, friendly mobile assistant. User asked: {prompt}",
    )
    answer = getattr(response, 'text', None)
    if not answer and hasattr(response, 'output'):
        answer = response.output[0].content[0].text
    return answer or 'No response from Jervice.'


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    if not client:
        return jsonify(error='Jervice client not configured. Install google-genai and set JERVICE_API_KEY.'), 500

    data = request.get_json(silent=True) or {}
    prompt = data.get('prompt', '').strip()
    if not prompt:
        return jsonify(error='Prompt is required.'), 400

    try:
        return jsonify(text=ask_jervice(prompt))
    except Exception as exc:
        return jsonify(error=f'Jervice request failed: {exc}'), 500


@app.route('/status')
def status():
    if client:
        return jsonify(status='ok', model=MODEL_NAME)
    return jsonify(status='error', error=genai_error or 'Client unavailable'), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
