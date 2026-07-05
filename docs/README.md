# Jervice Mobile Documentation

This documentation explains how to install, configure, run, and use the mobile version of Jervice.

## Project Overview

`cssbasic10` contains a mobile-ready web interface for Jervice.

- `index.html` - the mobile chat UI.
- `app.py` - Flask backend that forwards chat prompts to Gemini using `google-genai`.
- `requirements.txt` - required Python packages.
- `README.md` - quick start guide.
- `docs/README.md` - this detailed documentation.

## Features

- Mobile-optimized chat interface
- Same API key flow as your desktop Jervice assistant
- Backend proxy to keep the Gemini key secret
- Simple install and run process

## Installation

1. Open a terminal in `d:\Css 3\cssbasic10`.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

> If you use a virtual environment, activate it first.

## Configuration

Set the Gemini API key before running the server.

- Windows PowerShell:

```powershell
$env:GEMINI_API_KEY = "your_api_key_here"
```

- macOS / Linux:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

## Running Jervice Mobile

Start the mobile server:

```bash
python app.py
```

Then open the page from your phone using your PC's local IP address:

```text
http://YOUR-PC-IP:5000
```

## How to Find Your PC IP

On Windows, run:

```powershell
ipconfig
```

Look for the IPv4 address under your active network adapter.

Example:

```text
192.168.1.50
```

Then open this in your phone browser:

```text
http://192.168.1.50:5000
```

## Using the Mobile UI

1. Type a question into the text box.
2. Tap `Send`.
3. Jervice responds in the chat window.
4. Tap `Clear` to reset the chat.

## Troubleshooting

### Server does not start

- Ensure `google-genai` is installed.
- Ensure `GEMINI_API_KEY` is set.
- Check port `5000` is not blocked by firewall.

### Mobile page says network error

- Confirm phone and PC are on the same Wi-Fi network.
- Confirm the server is running on the PC.
- Use the PC IP address, not `localhost`.

### `Gemini client not configured` error

- Confirm the API key environment variable is present when running `python app.py`.
- Example:

```powershell
$env:GEMINI_API_KEY = "your_api_key_here"
python app.py
```

## Optional: Use Outside Your Local Network

To access Jervice from outside your home network, use a tunneling service like `ngrok`.

Example:

```bash
ngrok http 5000
```

Then use the generated public URL on your phone.

## Notes

- The API key is never sent to the browser directly.
- All requests are handled by the backend server.
- Keep your key private.
