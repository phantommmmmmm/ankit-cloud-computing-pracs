import logging
from flask import Flask

app = Flask(__name__)

# Enable debug logging
app.logger.setLevel(logging.DEBUG)

@app.route('/')
def home():
    app.logger.debug("Home route accessed")
    return "Hello, World!"

# Catch all exceptions to log them
@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error("Exception occurred", exc_info=e)
    return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


