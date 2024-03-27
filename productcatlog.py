def ProductCatalog(self, choice):
        # Your implementation for ProductCatalog
        def check_product_exists(product_id):
                conn = Exception.getDBConn()
                cursor = conn.cursor()
                cursor.execute("""SELECT COUNT(*) FROM Products 
                               WHERE ProductID = ? """, (product_id,))
                count = cursor.fetchone()[0]
                cursor.close()
                return count>0

        def update_product_info():
                product_id = int(input('Enter product ID: '))
                if check_product_exists(product_id):
                    price = float(input('Enter New Price: '))
                    desc = input('Enter new description: ')
                    conn = Exception.getDBConn()
                    cursor = conn.cursor()
                    cursor.execute(""" UPDATE Products SET Price = ?, Description = ?
                                   WHERE ProductID = ?""",
                                   (price, desc, product_id))
                    conn.commit()
                    cursor.close()
                    print('Product information updated successfully')
                else:
                    print('Product Not found')
        def show_all_products():
            conn = Exception.getDBConn()
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM Products")
                print("Product details:")
                for row in cursor.fetchall():
                    print(row)
            finally:
                cursor.close()
                conn.close()

        def product_in_stock():
            product_id = int(input('Enter product ID: '))
            conn = Exception.getDBConn()
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = ?", (product_id,))
                quantity = cursor.fetchone()[0]
                if quantity>0:
                    print(f'Product in stock: {quantity}')
                else:
                    print('Product not in stock')
            finally:
                cursor.close()
                conn.close()

        if choice == 1:
            update_product_info()
        elif choice == 2:
            show_all_products()
        elif choice == 3:
            product_in_stock()
        else:
            print('Invalid choice. Please Try again')



