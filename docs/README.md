# Jervice Mobile

A mobile-friendly web interface for Jervice using Gemini.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your Gemini API key in the server environment:
   - Windows PowerShell:
     ```powershell
     $env:GEMINI_API_KEY = "your_api_key_here"
     ```
   - macOS / Linux:
     ```bash
     export GEMINI_API_KEY="your_api_key_here"
     ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open the mobile interface from your phone using your PC's local IP:
   ```
   http://YOUR-PC-IP:5000
   ```

## Notes

- The page is designed for mobile screens.
- Keep your API key secret; do not embed it directly in the browser.
- This backend proxies requests to Gemini securely from your machine.

## Documentation

For more detailed instructions, see `docs/README.md`.
