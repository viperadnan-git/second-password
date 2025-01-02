from os import getenv

from src import app


app.run(
    host=getenv("HOST", "0.0.0.0"),
    port=int(getenv("PORT", 8000)),
    load_dotenv=True,
    debug=False,
)
