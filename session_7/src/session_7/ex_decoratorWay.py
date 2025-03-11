from contextlib import contextmanager
import logging
import time
import os

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format="[%(filename)s] - [%(funcName)s] - [%(asctime)s] ")

@contextmanager
def open_file(filename, mode):
    logging.info(f"started {time.process_time()}")
    print(f"Opening file {filename}")
    f = open(filename, mode)
    try:
        yield f
    finally:
        print(f"Closing file {filename}")
        f.close()
        logging.info(f"started {time.process_time()}")

# Usage example:
if __name__ == "__main__":
    with open_file("example_Decorator.txt", "a") as f:
        f.write("\nAppending with context manager using @contextmanager.")
