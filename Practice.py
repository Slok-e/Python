import logging

logging.basicConfig(logging.warning
    filename="run_py.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s"
)
logging.warning("This will get logged to hangman.py file")