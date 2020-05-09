import mysql.connector

class UseDatabase:
    
    # Method that initializes the attribute with the settings
    def __init__(self, config:dict) -> None:
        self.configuration = config 

    # Includes configuration file and returns cursor
    def __enter__(self) -> 'cusor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor 

    # To close everything, the method that includes any destruction code
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

        
        

    
