def CustomerUpdate(self, customer_id, choice):
        def UpdateCustomerDetails():
            email = input('Enter new email: ')
            phone = input('Enter new phone number: ')
            address = input('Enter new address: ')
            try:
                conn = Exception.getDBConn()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (customer_id,))
                customer_details = cursor.fetchone()
                if customer_details:
                    customer = Customers(*customer_details)  # Assuming Customers class takes the details as arguments
                    customer.set_email(email)
                    customer.set_phone(phone)
                    customer.set_address(address)
                    cursor.execute("""UPDATE Customers SET Email = ?, Phone = ?, Address = ?
                                    WHERE CustomerID = ?""",
                                (customer.get_email(), customer.get_phone(), customer.get_address(), customer_id))
                    conn.commit()
                    print("Customer details updated")
                else:
                    print("Customer not found")
            except Exception as e:
                conn.rollback()
                raise e
            finally: 
                cursor.close()
                conn.close()

            
        def GetCustomerDetails():
            try:
                conn = Exception.getDBConn()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (customer_id, ))
                detail = cursor.fetchone()
                print('Customer ID: ', detail[0])
                print('First Name: ', detail[1])
                print('Last Name: ', detail[2])
                print('Email: ', detail[3])
                print('Phone: ', detail[4])
                print('Address: ', detail[5])
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()
                
        
        if choice == 1:
            UpdateCustomerDetails()
        elif choice == 2:
            GetCustomerDetails()
        else:
            print("Invalid choice. Try again\n")
