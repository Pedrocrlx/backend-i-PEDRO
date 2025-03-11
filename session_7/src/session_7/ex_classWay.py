import time
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format="[%(filename)s] - [%(funcName)s] - [%(asctime)s] ")
logging.getLogger(__name__)


class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        logging.info(f"started {time.process_time()}")
        print(f"Opening file {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file {self.filename}")
        if self.file:
            self.file.close()
            logging.info(f"finished {time.process_time()}")
        # Do not suppress exceptions
        return False


# Usage example:
if __name__ == "__main__":
    with FileOpener("example_Class.txt", "w") as f:
        f.write("\nhello ---- joreg " * 10)
        f.write("\nhello ---- predo " * 10)
        f.write("\nhello ---- driogo " * 10)
        f.write("\nhello ---- lrucas " * 10)
