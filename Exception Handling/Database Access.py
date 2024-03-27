import time

class DatabaseConnectionError(Exception):
    pass

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.max_connection_attempts = 3

    def connect(self):
        attempt = 0
        while attempt < self.max_connection_attempts:
            try:
                # Simulate database connection (replace with actual connection code)
                print("Attempting to connect to database...")
                # Simulate connection failure
                raise DatabaseConnectionError("Unable to connect to database")
            except DatabaseConnectionError as e:
                print(f"Database connection attempt {attempt + 1} failed: {str(e)}")
                attempt += 1
                if attempt < self.max_connection_attempts:
                    print("Retrying connection...")
                    time.sleep(2)
                else:
                    print("Maximum retry attempts reached.")
                    raise

    def execute_query(self, query):
        try:
            self.connect()  # Attempt to establish connection
            # Execute query (replace with actual query execution code)
            print("Query executed successfully")
        except DatabaseConnectionError as e:
            print(f"Error executing query: {str(e)}")


