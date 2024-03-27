def OrderStatus(self, order_id, choice):
        def DisplayStatus():
            try:
                conn = Exception.getDBConn()
                cursor = conn.cursor()
                cursor.execute("SELECT Status FROM Orders WHERE OrderID = ?", (order_id,))
                status = cursor.fetchone()[0]
                print("Your order status: ", status)
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()
        def UpdateStatus():
            status = input('Enter status (Shipped/Pending): ')
            if status == 'Shipped'.lower() or 'Pending'.lower():
                try:
                    conn = Exception.getDBConn()
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Orders SET Status = ? WHERE OrderID = ?", (status, order_id))
                    print('Status Updated\n')
                    conn.commit()
                except Exception as e:
                    conn.rollback()
                    raise e
                finally:
                    cursor.close()
                    conn.close()
            else:
                print('Enter valid status. Try again')
                return
        if choice == 1:
            DisplayStatus()
        elif choice == 2:
            UpdateStatus()
        else:
            print('Invalid choice. Please Try again')

