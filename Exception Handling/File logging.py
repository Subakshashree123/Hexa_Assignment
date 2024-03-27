class FileIOException(Exception):
    pass

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log_error(self, message):
        try:
            with open(self.log_file, 'a') as file:
                file.write(f"Error: {message}\n")
                print("Error logged successfully")
        except IOError as e:
            raise FileIOException(f"Error logging to file: {str(e)}")
logger = Logger("error.log")