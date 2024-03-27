def SearchOrRecommendProduct(self, choice):
        
        def SearchProduct():
            product_id = input('Enter a product id: ')
            try:
                conn = Exception.getDBConn()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Products WHERE ProductID = ?", (product_id,))
                rows = cursor.fetchone()
                if rows:
                    print('Product Found!\n')
                    print('Product ID: ', rows[0])
                    print('Product Name: ', rows[1])
                    print('Product Description: ', rows[2])
                    print('Product Price: ', rows[3])
                    print('Product Category: ', rows[4])
                else:
                    print('Product Not Found\n')
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()
        
        def RecommendProduct():
            product_id = input('Enter a product id: ')
            try:
                conn = Exception.getDBConn()
                cursor = conn.cursor()
                cursor.execute("SELECT Category FROM Products WHERE ProductID = ?",(product_id,))
                category = cursor.fetchone()[0]
                cursor.execute("SELECT * FROM Products WHERE Category = ?",(category,))
                recommended_products = cursor.fetchall()

                if recommended_products:
                    print('Here are the recommeded products: \n')
                    for product in recommended_products:
                        print(product[1])
                else:
                    print('No recommendations')
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        if choice == 1:
            SearchProduct()
        elif choice == 2:
            RecommendProduct()
        else:
            print('Invalid choice. try again')
            return


