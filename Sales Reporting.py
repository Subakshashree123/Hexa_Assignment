def SalesReport(self, choice):
        def RetrieveSalesData():
            try:
                conn = Exception.getDBConn()
                cursor = conn.cursor()
                query = """WITH ProductSales AS(
                            SELECT OD.ProductID, SUM(OD.Quantity) Quantity FROM OrderDetails OD
                            GROUP BY OD.ProductID
                        )
                        SELECT P.ProductID, P.ProductName, PS.Quantity AS TotalQuantity
                        FROM Products P
                        JOIN ProductSales PS ON PS.ProductID = P.ProductID"""
                cursor.execute(query)
                rows = cursor.fetchall()

                print("Sales Report:")
                print("Product ID | Product Name | Total Quantity Sold")
                for row in rows:
                    print(f"{row.ProductID} | {row.ProductName} | {row.TotalQuantity}")
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        def GenerateSalesReport():
            try:
                conn = Exception.getDBConn()
                cursor = conn.cursor()
                query = """WITH ProductSales AS(
                            SELECT OD.ProductID, SUM(OD.Quantity) Quantity 
                            FROM OrderDetails OD
                            GROUP BY OD.ProductID
                        )
                        SELECT P.ProductID, P.ProductName, PS.Quantity AS TotalQuantity FROM Products P
                        JOIN ProductSales PS ON PS.ProductID = P.ProductID
                        WHERE PS.Quantity = (SELECT MAX(Quantity) FROM ProductSales) OR 
                        PS.Quantity = (SELECT MIN(Quantity) FROM ProductSales)
                        """
                cursor.execute(query)
                rows = cursor.fetchall()

                print("Sales Report:")
                print("Product ID | Product Name | Total Quantity Sold")
                for row in rows:
                    print(f"{row.ProductID} | {row.ProductName} | {row.TotalQuantity}")
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        if choice == 1:
            RetrieveSalesData()
        elif choice == 2:
            GenerateSalesReport()
        else:
            print('Invalid choice. Try again')
            return
