class TechShopProcessor(ITechShopRepository):
    def CustomerRegistration(self, customer):
        try:
            conn = TechShopProcessor.getDBConn()
            cursor = conn.cursor()
            if '@' not in customer.get_email():
                raise Exception.InvalidDataException('Invalid Email')
            cursor.execute("SELECT TOP 1 CustomerID FROM Customers ORDER BY CustomerID DESC")
            customer_id = cursor.fetchone()[0]+1
            cursor.execute("""INSERT INTO Customers (FirstName, LastName,                 Email, Phone, Address)
                           VALUES ( ?, ?, ?, ?, ?)""", ( customer.get_first_name(), 
customer.get_last_name(), customer.get_email(), 
customer.get_phone(), customer.get_address()))
            conn.commit()
            print('Customer created successfully.\n')
        except Exception.InvalidDataException as e:
            conn.rollback()
            print(e)
        finally:
            cursor.close()
            conn.close()


