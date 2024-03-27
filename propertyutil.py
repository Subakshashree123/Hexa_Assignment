class PropertyUtil:
    @staticmethod
    def getPropertyString():
        server_name = "SUBAKSHATHIRU\SQLEXPRESS02"
        database_name = "Techshops"
        trusted_connection = "yes"
        return f"Driver={{SQL Server}};Server={server_name};Database={database_name};Trusted_Connection={trusted_connection};"