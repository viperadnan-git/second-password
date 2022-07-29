from os import getenv

from dotenv import load_dotenv

from web import app

load_dotenv()

app.run(
    host=getenv("HOST", "0.0.0.0"),
    port=int(getenv("PORT", 8000)),
    load_dotenv=True,
    debug=False,
)
