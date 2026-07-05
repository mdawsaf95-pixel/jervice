# Jervice Mobile

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

5. View live documentation from your phone:
   ```
   http://YOUR-PC-IP:5000/docs
   ```

## Notes

- The page is designed for mobile screens.
- Keep your API key secret; do not embed it directly in the browser.
- This backend proxies requests to Jervice securely from your machine.

## Deployment

You can deploy this app to a cloud host and share a public URL.

1. Host requirements:
   - `Flask`
   - `google-genai`
   - environment variable `JERVICE_API_KEY`

2. Recommended platforms:
   - Railway
   - Render
   - Heroku

3. Required files in `cssbasic10`:
   - `requirements.txt`
   - `Procfile`
   - `runtime.txt`

4. After deployment, use the public URL for the assistant and docs:
   - Assistant: `https://YOUR-HOST-NAME/`
   - Live docs: `https://YOUR-HOST-NAME/docs`

## Documentation

For more detailed instructions and a styled docs page, open `cssbasic10/docs/index.html` in your browser.
