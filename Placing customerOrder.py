def Orders(self, customer_id, choice):

        def CreateOrder():
            try:
                conn = Exception.getDBConn()
                cursor = conn.cursor()

                product_id = int(input('Enter product ID: '))
                quantity = int(input('Enter quantity: '))
                order_date = date.today()
                if not product_id or not quantity:
                    raise custom_exceptions.IncompleteOrderException("Enter All the details")

                cursor.execute("SELECT Price FROM Products WHERE ProductID = ?", (product_id,))
                row = cursor.fetchone()
                if row:
                    price = row[0]
                    total_amount = price * quantity
                else:
                    raise custom_exceptions.ProductNotFoundException('Product Not Found')
                cursor.execute("SELECT TOP 1 OrderID FROM Orders ORDER BY OrderID DESC")
                order_id = cursor.fetchone()[0]
                order_id += 1

                cursor.execute("SELECT TOP 1 OrderDetailID FROM OrderDetails ORDER BY OrderDetailID DESC")
                order_detail_id = cursor.fetchone()[0]
                order_detail_id += 1

                #Insert order into Orders Table
                cursor.execute(""" INSERT INTO Orders(OrderID, CustomerId, OrderDate, TotalAmount, Status)
                               VALUES (?, ?, ?, ?, ?)""", (order_id, customer_id, order_date, total_amount, 'Pending'))
                # Insert order details into OrderDetails Table
                cursor.execute(""" INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity)
                               VALUES(?, ?, ?, ?)""", (order_detail_id, order_id, product_id, quantity))
                # Update quantity in stock in Inventory Table
                cursor.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = ?",(product_id,))
                current_quantity = cursor.fetchone()[0]
                if current_quantity:
                    new_quantity = current_quantity - quantity
                    cursor.execute(""" UPDATE Inventory SET QuantityInStock = ?
                                WHERE ProductID = ?""", (new_quantity, product_id))
                    
                    conn.commit()
                    print('Order Created Successfully')
                else:
                    raise custom_exceptions.InsufficientStockException('Insufficient Stock')
            except custom_exceptions.ProductNotFoundException as e:
                print(e)
            except custom_exceptions.InsufficientStockException as e:
                print(e)
            except custom_exceptions.IncompleteOrderException as e:
                print(e)
            except Exception as e:
                conn.rollback()
                print('Error creating Order', e)
            finally:
                cursor.close()
                conn.close()

        def GetOrderDetails():
            try:
                conn = Exception.getDBConn()
                cursor = conn.cursor()
                cursor.execute("""SELECT OD.OrderDetailID, OD.OrderID, OD.ProductID, OD.Quantity, O.OrderDate 
                               FROM OrderDetails OD
                               JOIN Orders O ON O.OrderID = OD.OrderID
                               WHERE O.CustomerID = ?""", (customer_id,))
                orders = cursor.fetchall()
                print(f"You've ordered {len(orders)} times, below are those order details:")
                for order in orders:
                    print()
                    print(f"Order Detail ID: {order[0]}")
                    print(f"Order ID: {order[1]}")
                    print(f"Product ID: {order[2]}")
                    print(f"Quantity: {order[3]}")
                    print(f"Order Date: {order[4]}")
                    print()
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        def CancelOrder():
            print('Here are your orders: \n')
            GetOrderDetails()
            order_id = int(input('Select an order to cancel: '))
            try:
                conn = Exception.getDBConn()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM OrderDetails WHERE OrderID = ?", (order_id,))
                cursor.execute("DELETE FROM Orders WHERE OrderID = ?", (order_id,))
                conn.commit()
                print('Order Canceled.')
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        if choice == 1:
            CreateOrder()
        elif choice == 2:
            GetOrderDetails()
        elif choice == 3:
            CancelOrder()
        else:
            print('Invalid Choice. Please Try again.')
            return
