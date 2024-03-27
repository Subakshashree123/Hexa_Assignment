def PaymentProcess(self, choice):

        def ProcessPayment():
            order_id = int(input('Enter order ID: '))
            try:
                conn = Exception.getDBConn()
                cursor = conn.cursor()
                query = """SELECT OD.OrderID, OD.ProductID, OD.Quantity, SUM(P.Price * OD.Quantity) TotalAmount FROM OrderDetails OD
                        JOIN Products P ON P.ProductID = OD.ProductID
                        WHERE OrderID = ?
                        GROUP BY OD.OrderID, OD.ProductID, OD.Quantity"""
                cursor.execute(query, (order_id,))
                rows = cursor.fetchall()
                if not rows:
                    print("No order details found for the given order ID.")
                else:
                    print("OrderID | ProductID | Quantity | TotalAmount")
                    print("-" * 40)
                    for row in rows:
                        order_id, product_id, quantity, total_amount = row
                        print(f"{order_id:^8} | {product_id:^9} | {quantity:^8} | {total_amount:^12}")
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        def AddDiscount():
            order_id = int(input('Enter order id: '))
            try:
                conn = Exception.getDBConn()
                cursor = conn.cursor()
                query = """SELECT OD.OrderID, SUM(P.Price * OD.Quantity) TotalAmount FROM OrderDetails OD
                            JOIN Products P ON P.ProductID = OD.ProductID
                            WHERE OrderID = ?
                            GROUP BY OD.OrderID"""
                cursor.execute(query, (order_id,))
                total_amount = cursor.fetchone()[1]
                print("Total Amount: $",total_amount)
                discounted_amount = total_amount - total_amount*0.10
                print("Discount of 10 percent will be added...")
                print("Total Amount: $", discounted_amount)
            except Exception as e:
                conn.commit()
                raise e
            finally:
                cursor.close()
                conn.close()
        if choice == 1:
            ProcessPayment()
        elif choice == 2:
            AddDiscount()
        else:
            print('Invalid choice. Try again')
            return

