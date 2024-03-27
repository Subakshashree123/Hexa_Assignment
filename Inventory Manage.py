def InventoryManagement(self, choice):

        def AddProduct():
            conn = Exception.getDBConn()
            cursor = conn.cursor()
            cursor.execute('SELECT TOP 1 ProductID FROM Products ORDER BY ProductID DESC')
            product_id = cursor.fetchone()[0]+1
            cursor.execute('SELECT TOP 1 InventoryID FROM Inventory ORDER BY InventoryID DESC')
            inventory_id = cursor.fetchone()[0]+1
            try:
                product_name = input('Enter product name: ')
                desc = input('Enter product description: ')
                price = float(input('Enter product price: '))
                category = "Electronics"
                quantity = int(input('Enter quantity in stock: '))
                last_stock_date = date.today()
                cursor.execute("INSERT INTO Products VALUES (?,?,?,?,?)",
                               (product_id, product_name, desc, price, category))
                cursor.execute("INSERT INTO Inventory VALUES (?,?,?,?)",
                                (inventory_id, product_id, quantity, last_stock_date))
                conn.commit()
                print('Product Added Succesfully')
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        def UpdateProductStock():
            product_id = int(input('Enter product id: '))
            new_quantity = int(input('Enter quantity to be added: '))
            try:
                conn = Exception.getDBConn()
                cursor = conn.cursor()
                cursor.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = ?", (product_id,))
                quantity_in_stock = cursor.fetchone()[0]
                print('Quantity in stock: ', quantity_in_stock)
                quantity = quantity_in_stock + new_quantity
                cursor.execute("UPDATE Inventory SET QuantityInStock = ? WHERE ProductID = ?", (quantity, product_id))
                print(f'Quantity updated for Product ID {product_id}: {quantity}')
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        def RemoveDiscontinuedItems():
            item = int(input('Enter product you want to discontinue (product ID): '))
            try:
                conn = Exception.getDBConn()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Inventory WHERE ProductID = ?",(item))
                cursor.execute("DELETE FROM Products WHERE ProductID = ?",(item))
                conn.commit()
                print('Removed items successfully')
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()
        if choice == 1:
            AddProduct()
        elif choice == 2:
            UpdateProductStock()
        elif choice == 3:
            RemoveDiscontinuedItems()
        else:
            print('Invalid choice. Please Try again')
