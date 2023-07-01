class Products:
    def __init__(self, product_name, description, price, category, availability, total_sales):
        self.product_name=product_name
        self.description=description
        self.price=price
        self.category=category
        self.availability=availability
        self.total_sales=total_sales


#Aquí se muestran los atributos del producto.
    def show_atributes(self):
        print(  f"""Nombre del Producto: {self.product_name}
            Descripción: {self.description}
            Precio: {self.price}
            Categoría: {self.category}
            Disponibilidad: {self.availability}
              """)

#Se hace herencia para que el desarrollo del código sea más claro.    
class ProductManagement(Products):
    def __init__(self, product_name, description, price, category, availability, total_sales):
        super().__init__(product_name, description, price, category, availability, total_sales)
    
#Función hecha para registrar y crear al producto. Se le pide nombre del producto, descripción, precio, categoría y disponibilidad.
    def add_product(products):
        print("\nBIENVENIDO. AQUÍ PODRÁ AÑADIR PRODUCTOS.")

        product_name=input("Ingrese el nombre del producto: ").title()
        while not product_name.isalpha():
            product_name=input("Error! Ingrese un nombre válido: ").title()
        
        description=input("Ingrese la descripción: ").capitalize()
        while not (description.replace(" ", "")).isalpha():
            description=input("Error! Ingrese una descripción válida: ").capitalize()

        price=input("Ingrese el precio: ")
        while not price.isnumeric():
            price=input("Error! Ingrese un precio válido: ")

        category=input("Ingrese la categoría: ").capitalize()
        while not category.isalpha():
            category=input("Error! Ingrese una categoría válida: ").capitalize()

        availability=input("Ingrese la cantidad de productos que desea registrar: ")
        while not availability.isnumeric():
            availability=input("Error! Ingrese una cantidad válida: ")



        product=Products(product_name, description, price, category, availability, 0)
        products.append(product)
        
        print("Este producto ha sido registrado")

#Función hecha para buscar al producto por su categoría. 
    def search_product_category(products):
        categories = []
        for i in products:
            if not i.category in categories: #Esto es para que no se impriman categorías repetidas.
                categories.append(i.category)
        
        for i, category in enumerate(categories):
            print(f"{i+1}. {category}")
        
        option=input("¿A qué categoría pertenece el producto que busca? ")
        while not option.isnumeric() or not int(option) in range(1, len(categories)+1):
            print("Error")
            option=input("¿A qué categoría pertenece el producto que busca? ")
        
        category = categories[int(option)-1]

        found=0
        for product in products:
            if product.category==category:
                found+=1
                print("\nDatos encontrados: ")
                print(f"""
                Nombre: {product.product_name}
                Descripción: {product.description}
                Precio: {product.price}
                Categoría: {product.category}
                Cantidad: {product.availability}
                """)
        
        if found==0:         
            print("Este producto no existe dentro de la base de datos.") 


#Función hecha para buscar al producto por su precio.
    def search_product_price(products):
        option=input("Ingrese el precio del producto deseado: ")
        while not option.isnumeric():
            option=input("Error! Intente de nuevo: ")
        
        found=0
        for product in products:
            if product.price==float(option):
                found+=1
                print("\nDatos encontrados: ")
                print(f"""
                Nombre: {product.product_name}
                Descripción: {product.description}
                Precio: {product.price}
                Categoría: {product.category}
                Cantidad: {product.availability}
                """)
        
        if found==0:         
            print("Este producto no existe dentro de la base de datos.") 
    

#Función hecha para buscar al producto por su nombre.
    def search_product_name(products):
        option=input("Ingrese el nombre del producto deseado: ").title()
        while not (option.replace(" ", "")).isalpha():
            option=input("Error! Intente de nuevo: ").title()
        
        found=0
        for product in products:
            if product.product_name==option:
                found+=1
                print("\nDatos encontrados: ")
                print(f"""
                Nombre: {product.product_name}
                Descripción: {product.description}
                Precio: {product.price}
                Categoría: {product.category}
                Cantidad: {product.availability}
                """)
        
        if found==0:         
            print("Este producto no existe dentro de la base de datos.") 
    

#Función hecha para buscar al producto por su disponibilidad.
    def search_product_availability(products):
        option=input("Ingresa el número o cantidad de productos disponibles: ")
        while not option.isnumeric():
            option=input("Error! Intente de nuevo: ")
        
        found=0
        for product in products:
            if product.availability==int(option):
                found+=1
                print("\nDatos encontrados: ")
                print(f"""
                Nombre: {product.product_name}
                Descripción: {product.description}
                Precio: {product.price}
                Categoría: {product.category}
                Cantidad: {product.availability}
                """)

        if found==0:         
            print("Este producto no existe dentro de la base de datos.") 


#Función hecha para modificar la información registrada anteriormente. Se muestran los productos registrados y el usuario decide cuál modificar.
    def modify_product_information(products):
        print("PRODUCTOS")
        print("")
        for i, product in enumerate(products):
            print(f"{i+1}. Nombre del Producto: {product.product_name}, Categoría: {product.category}")
        

        modify_product=input("¿Cuál producto desea modificar? (Marque con números) ")
        while not modify_product.isnumeric() or int(modify_product) not in range(1, len(products)+1):
            modify_product=input("Error! Ingrese un dato válido: ")
        
        modify_product=int(modify_product)-1

        producto_a_modificar=products[modify_product]


        print("""1. Nombre del producto.
                 2. Descripción.
                 3. Precio.
                 4. Categoría.
                 """)
        
        options=input("¿Qué desea modificar? ")
        while not options.isnumeric() or int(options) not in range(1, 5):
            options=input("Error! Intente de nuevo: ")

        if int(options)==1:
            product_name=input("Ingrese el nuevo nombre: ").title()
            while not product_name.isalpha():
                product_name=input("Error! Ingrese un nombre válido: ").title()
            producto_a_modificar.product_name = product_name 
        elif int(options)==2:
            description=input("Ingrese la nueva descripción: ").capitalize()
            while not (description.replace(" ", "")).isalpha():
                description=input("Error! Ingrese una descripción válida: ").capitalize()
            producto_a_modificar.description = description 
        elif int(options)==3:
            price=input("Ingrese el nuevo precio: ")
            while not price.isnumeric():
                price=input("Error! Ingrese un precio válido: ")
            producto_a_modificar.price = price 
        elif int(options)==4:
            category=input("Ingrese la nueva categoría: ").capitalize()
            while not category.isalpha():
                category=input("Error! Ingrese una categoría válida: ").capitalize()
            producto_a_modificar.category = category 


#Función hecha para eliminar a un objeto producto por el nombre.
    def delete_product(products):
        for i, product in enumerate(products):
            print(f"{i+1}. {product.product_name}")

        delete_product=input("¿Qué producto desea eliminar? ")
        while not delete_product.isnumeric() or int(delete_product) not in range(len(products)+1):
            delete_product=input("ERROR! Intente de nuevo: ")
        

        for product in products:
            if product.product_name == products[int(delete_product)-1].product_name:
                products.remove(product)
                print("\nProducto eliminado con éxito.")