import os

from dotenv import load_dotenv

load_dotenv()

USER_CREDENTIAL = str(os.getenv("USER_CREDENTIAL"))
PASS_CREDENTIAL = str(os.getenv("PASS_CREDENTIAL"))
