# Jervice Mobile Documentation

A mobile-friendly web interface for Jervice.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set the Jervice API key environment variable:
   - Windows PowerShell:
     ```powershell
     $env:JERVICE_API_KEY = "your_api_key_here"
     ```
   - macOS / Linux:
     ```bash
     export JERVICE_API_KEY="your_api_key_here"
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
- This backend proxies requests to Jervice securely from your machine.

## Styled Docs Page

Open `docs/index.html` in your browser to view the styled documentation.
