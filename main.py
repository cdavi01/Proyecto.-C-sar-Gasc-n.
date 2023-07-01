
from Customer import *
from Products import *
from Sale import *
from Payment import *
from Factura import *
from Shipment import *
import datetime



import requests
import json

def obtener_info_apis():
    response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json').text
    info_apis = json.loads(response)
    return info_apis

#Esta funcion crea los objetos de tipo products con la informacion de la API.
def objetos_apis(info_apis, products):
    
    for producto in info_apis:
        product_name=producto["name"]
        description=producto["description"]
        price= float(producto["price"])
        category=producto["category"]
        availability= int(producto["quantity"])

        product=Products(product_name, description, price, category, availability, 0)
        products.append(product)

            
#Este es el menú principal, es lo primero que aparece al iniciar el programa. Aquí se podrán seleccionar las gestiones que desea revisar; al seleccionar una, se abrira un submenu específico de la gestión.(Al seleccionar la opción 8, se guarda todo en un archivo txt).
def main_menu(products, sales, customers, facturas, payments, shipments, creditos): 
        print("¡BIENVENIDO A NUESTRA TIENDA DE PRODUCTOS NATURALES!")

        options=["Gestión de Productos", "Gestión de Ventas", "Gestión de Clientes", "Gestión de Pagos", "Gestión de Envíos", "Indicadores de Gestión", "Factura", "Salir"]
        while True:
            print("¿Qué acción desea realizar?")
            print("")
            for i in range(len(options)):
                print(f"{i+1}. {options[i]}")
            option=input('Ingrese opción: ')
            while not option.isnumeric() or int(option) -1 not in range(len(options)):
                option=input('ERROR! Ingrese de nuevo: ')
            
            if int(option)==1:
                gestion_producto(products)
            elif int(option)==2:
                gestion_venta(sales, products, customers, facturas, payments, shipments, creditos)
            elif int(option)==3:
                gestion_cliente(customers)
            elif int(option)==4:
                gestion_pago(payments)
            elif int(option)==5:
                gestion_envio(shipments)
            elif int(option)==6:
                gestion_estadisticas(creditos, sales, products, customers, shipments)
            elif int(option)==7:
                gestion_facturas()
            elif int(option)==8:
                print("¡Vuelva pronto!")
               
                with open("/Users/Usuario/OneDrive/Escritorio/Python/PROYECTO/txt/customers.txt","a") as a:
                    for customer1 in customers:
                        name = customer1.name
                        last_name = customer1.last_name
                        type = customer1.type
                        identification_card = customer1.identification_card
                        email = customer1.email
                        address = customer1.address
                        phone_number = customer1.phone_number
                        buy_amount = customer1.buy_amount
                    #Escribimos en el archivo
                    a.write(f"{name}///{last_name}///{type}///{identification_card}///{email}///{address}///{phone_number}///{buy_amount}///\n")
                
                with open("/Users/Usuario/OneDrive/Escritorio/Python/PROYECTO/txt/products.txt","a") as a:
                    for product1 in products:
                        product_name = product1.product_name
                        description = product1.description
                        price = product1.price
                        category = product1.category
                        availability = product1.availability
                        total_sales = product1.total_sales
                    #Escribimos en el archivo
                    a.write(f"{product_name}///{description}///{price}///{category}///{availability}///{total_sales}///\n")

                with open("/Users/Usuario/OneDrive/Escritorio/Python/PROYECTO/txt/sales.txt","a") as a:
                    for sale1 in sales:
                        customer = sale1.customer
                        product = sale1.product
                        total = sale1.total
                        payment = sale1.payment
                        shipment = sale1.shipment
                    #Escribimos en el archivo
                    a.write(f"{customer}///{product}///{total}///{payment}///{shipment}///\n")
                
                with open("/Users/Usuario/OneDrive/Escritorio/Python/PROYECTO/txt/payments.txt","a") as a:
                    for payment1 in sales:
                        customer=payment1.customer
                        total=payment1.total
                        currency=payment1.currency
                        payment_type=payment1.payment_type
                        date=payment1.date
                    #Escribimos en el archivo
                    a.write(f"{customer}///{total}///{currency}///{payment_type}///{date}///\n")
                
                with open("/Users/Usuario/OneDrive/Escritorio/Python/PROYECTO/txt/shipments.txt","a") as a:
                    for shipment1 in sales:
                        purchase_order=shipment1.purchase_order
                        shipping_service =shipment1.shipping_service 
                        cost=shipment1.cost 
                        shipment_amount=shipment1.shipment_amount 
                    #Escribimos en el archivo
                    a.write(f"{purchase_order}///{shipping_service}///{cost}///{shipment_amount}///\n")
                break
            

#Este es el menú de gestión de producto; aquí se podrán seleccionar las acciones mostradas en pantalla en relación a los productos.
def gestion_producto(products): 
    options=["Agregar Producto", "Buscar Producto por Categoría", "Buscar Producto por Precio", "Buscar Producto por Nombre", "Buscar Producto por Disponibilidad",  "Modificar Producto", "Eliminar Producto", "Salir"]
    while True:
        print("\nBIENVENIDOS A LA GESTION DE PRODUCTOS")
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")
        option=input('Ingrese opción: ')
        while not option.isnumeric() or int(option) -1 not in range(len(options)):
            option=input('ERROR! Ingrese de nuevo: ')
        
        if int(option) == 1:
            ProductManagement.add_product(products)
        elif int(option)==2:
            ProductManagement.search_product_category(products)
        elif int(option)==3:
            ProductManagement.search_product_price(products)
        elif int(option)==4:
            ProductManagement.search_product_name(products)
        elif int(option)==5:
            ProductManagement.search_product_availability(products)
        elif int(option)==6:
            ProductManagement.modify_product_information(products)
        elif int(option)==7:
            ProductManagement.delete_product(products)
        elif int(option)==8:
            break

#Este es el menú de gestión de cliente; aquí se podrán seleccionar las acciones mostradas en pantalla en relación a los clientes.
def gestion_cliente(customers):
    options=["Registrar Clientes", "Modificar Información", "Eliminar Clientes", "Buscar cliente por cédula", "Buscar cliente por correo", "Salir"]
    while True:
        print("\nBIENVENIDOS A LA GESTION DE CLIENTES")
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")
        option=input('Ingrese opción: ')
        while not option.isnumeric() or int(option) -1 not in range(len(options)):
            option=input('ERROR! Ingrese de nuevo: ')
        
        if int(option)==1:
            CustomerManagement.register_customer(customers)
        elif int(option)==2:
            CustomerManagement.modify_customer_information(customers)
        elif int(option)==3:
            CustomerManagement.delete_customer(customers)
        elif int(option)==4:
            CustomerManagement.search_customer_identification_card(customers)
        elif int(option)==5:
           CustomerManagement.search_customer_email(customers)
        elif int(option)==6:
            break

#Este es el menú de gestión de venta; aquí se podrán seleccionar las acciones mostradas en pantalla en relación a las ventas.
def gestion_venta(sales, products, customers, facturas, payments, shipments, creditos):
    options=["Registrar Ventas", "Buscar venta por cliente", "Buscar venta por fecha", "Buscar venta por total", "Salir"]
    while True:
        print("\nBIENVENIDOS A LA GESTION DE VENTAS")
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")
        option=input('Ingrese opción: ')
        while not option.isnumeric() or int(option) -1 not in range(len(options)):
            option=input('ERROR! Ingrese de nuevo: ')
        
        if int(option)==1:
            SaleManagement.register_sale(sales, products, customers, facturas, payments, shipments, creditos)
        elif int(option)==2:
            SaleManagement.search_customer_sale(sales)
        elif int(option)==3:
            SaleManagement.search_date_sale(sales)
        elif int(option)==4:
            SaleManagement.search_total_sale(sales, payments)
        elif int(option)==5:
            break

#Este es el menú de gestión de pago; aquí se podrán seleccionar las acciones mostradas en pantalla en relación a los pagos.
def gestion_pago(payments):
    options=["Buscar Pago por cliente", "Buscar Pago por fecha", "Buscar Pago por tipo de pago", "Buscar Pago por moneda de pago", "Salir"]
    while True:
        print("\nBIENVENIDOS A LA GESTION DE PAGOS")
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")
        option=input('Ingrese opción: ')
        while not option.isnumeric() or int(option) -1 not in range(len(options)):
            option=input('ERROR! Ingrese de nuevo: ')
        
        if int(option)==1:
            PaymentManagement.search_customer_payment(payments)
        elif int(option)==2:
            PaymentManagement.search_date_payment(payments)
        elif int(option)==3:
            PaymentManagement.search_type_payment(payments)
        elif int(option)==4:
            PaymentManagement.search_currency_payment(payments)
        elif int(option)==5:
            break

#Este es el menú de gestión de envío; aquí se podrán seleccionar las acciones mostradas en pantalla en relación a los envíos.
def gestion_envio(shipments):
    options=["Buscar Envio por cliente", "Buscar Envio por fecha" "Salir"]
    while True:
        print("\nBIENVENIDOS A LA GESTION DE ENVÍOS")
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")
        option=input('Ingrese opción: ')
        while not option.isnumeric() or int(option) -1 not in range(len(options)):
            option=input('ERROR! Ingrese de nuevo: ')
        
        if int(option)==1:
            ShipmentManagement.search_customer_shipment(shipments)
        elif int(option)==2:
            ShipmentManagement.search_date_shipment(shipments)
        elif int(option)==3:
            break
       
#Este es el menú de gestión de factura; aquí se podrán seleccionar las acciones mostradas en pantalla en relación a las facturas.
def gestion_facturas():
    options=["Mostrar Factura", "Salir"]
    while True:
        print("\nBIENVENIDOs A LA FACTURA")
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")
        option=input('Ingrese opción: ')
        while not option.isnumeric() or int(option) -1 not in range(len(options)):
            option=input('ERROR! Ingrese de nuevo: ')
        
        if int(option)==1:
            Factura.show()
        elif int(option)==2:
            break

#Este es el menú de gestión de estadísticas; aquí se podrán seleccionar las acciones mostradas en pantalla en relación a las estadísticas.
def gestion_estadisticas(creditos, sales, products, customers, shipments):
    options=["Generar informes de Ventas", "Generar informes de Pagos", "Generar informes de envíos", "Salir"]
    while True:
        print("\nBIENVENIDOS A ESTADÍSTICAS")
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")
        option=input('Ingrese opción: ')
        while not option.isnumeric() or int(option) -1 not in range(len(options)):
            option=input('ERROR! Ingrese de nuevo: ')
        

        if int(option)==1:
            generar_informe_venta(sales, products, customers)
        elif int(option)==2:
            generar_informe_pago(creditos, sales)
        elif int(option)==3:
            generar_informes_envios(shipments, creditos)
        elif int(option)==4:
            break

#Esta función esta relacionada con las estadísticas de las ventas.
def generar_informe_venta(sales, products, customers):
    date = datetime.datetime.now().date()

#Ventas totales por día, semana, mes y año:
#En el índice 1(0) esta la cantidad de ventas y en el índice 2(1) esta el monto total.
    venta_total_dia=[0, 0]
    venta_total_semana=[0, 0] #Este ítem no pude comprenderlo. Mis disculpas.
    venta_total_mes=[0, 0]
    venta_total_año=[0, 0]

    for venta in sales:
        if venta.date.day == date.day:
            venta_total_dia[1]+=venta.total
            venta_total_dia[0]+=1
        if venta.date.month==date.month:
            venta_total_mes[1]+=venta.total
            venta_total_mes[0]+=1
        if venta.date.year==date.year:
            venta_total_año[1]+=venta.total
            venta_total_año[0]+=1

    print("Ventas totales por día, semana, mes y año")
    print(f"""
        En el día {date.day} se hicieron {venta_total_dia[0]} ventas con un monto total de {venta_total_dia[1]}
        En el mes {date.month} se hicieron {venta_total_mes[0]} ventas con un monto total de {venta_total_mes[1]}
        En el año {date.year} se hicieron {venta_total_año[0]} ventas con un monto total de {venta_total_año[1]}
          """)

#Productos más vendidos:
    producto_mas_vendido=[0, 0]

    for vendido in products:
        if vendido.total_sales>producto_mas_vendido[1]:
            producto_mas_vendido=[vendido.product_name, vendido.total_sales]
    print(f"El producto con mayores ventas fue: {producto_mas_vendido[0]}, con {producto_mas_vendido[1]} ventas.")

#Clientes más frecuentes:
    cliente_mas_frecuente=[0, 0, 0]

    for frecuente in customers:
        if frecuente.buy_amount>cliente_mas_frecuente[1]:
            cliente_mas_frecuente=[frecuente.identification_card, frecuente.buy_amount, frecuente.name]
    print(f"El cliente más frecuente fue: {cliente_mas_frecuente[2]} de cédula o RIF: {cliente_mas_frecuente[0]}, con {cliente_mas_frecuente[1]} compras.")



#Esta función esta relacionada con las estadísticas de los pagos.
def generar_informe_pago(creditos, sales):
    date = datetime.datetime.now().date()

#Pagos totales por día, semana, mes y año:
#En el índice 1(0) esta la cantidad de pagos y en el índice 2(1) esta el monto total.
    pago_total_dia=[0, 0]
    pago_total_semana=[0, 0] #Este ítem no pude comprenderlo. Mis disculpas.
    pago_total_mes=[0, 0]
    pago_total_año=[0, 0]

    for credito in creditos:
        if credito.date.day == date.day:
            pago_total_dia[1]+=credito.total
            pago_total_dia[0]+=1
        if credito.date.month==date.month:
            pago_total_mes[1]+=credito.total
            pago_total_mes[0]+=1
        if credito.date.year==date.year:
            pago_total_año[1]+=credito.total
            pago_total_año[0]+=1

    for venta in sales:
        if venta.date.day == date.day:
            pago_total_dia[1]+=credito.total
            pago_total_dia[0]+=1
        if venta.date.month==date.month:
            pago_total_mes[1]+=credito.total
            pago_total_mes[0]+=1
        if venta.date.year==date.year:
            pago_total_año[1]+=credito.total
            pago_total_año[0]+=1
    
    print("Pagos totales por día, semana, mes y año")
    print(f"""
        En el día {date.day} se hicieron {pago_total_dia[0]} ventas con un monto total de {pago_total_dia[1]}
        En el mes {date.month} se hicieron {pago_total_mes[0]} ventas con un monto total de {pago_total_mes[1]}
        En el año {date.year} se hicieron {pago_total_año[0]} ventas con un monto total de {pago_total_año[1]}
          """)
        
#Clientes con pagos pendientes:
    cliente_con_pago_pendiente= []
    for i in creditos:
        if not i.customer.identification_card in cliente_con_pago_pendiente:
            cliente_con_pago_pendiente.append(i.customer)
    print("Clientes con pagos pendientes:")
    for i, customer in enumerate(cliente_con_pago_pendiente):
        print(f"{i+1}. Nombre: {customer.name} Cédula o RIF: {customer.identification_card}")


#Esta función esta relacionada con las estadísticas de los envíos.
def generar_informes_envios(shipments, creditos):
    date = datetime.datetime.now().date()

#Envíos totales por día, semana, mes y año:
#En el índice 1(0) esta la cantidad de envíos y en el índice 2(1) esta el monto total.
    envio_total_dia=[0, 0]
    envio_total_semana=[0, 0] #Este ítem no pude comprenderlo. Mis disculpas.
    envio_total_mes=[0, 0]
    envio_total_año=[0, 0]

    for envio in shipments:
        if envio.date.day == date.day:
            envio_total_dia[1]+=envio.total
            envio_total_dia[0]+=1
        if envio.date.month==date.month:
            envio_total_mes[1]+=envio.total
            envio_total_mes[0]+=1
        if envio.date.year==date.year:
            envio_total_año[1]+=envio.total
            envio_total_año[0]+=1
    
    print("Envíos totales por día, semana, mes y año")
    print(f"""
        En el día {date.day} se hicieron {envio_total_dia[0]} envíos con un monto total de {envio_total_dia[1]}
        En el mes {date.month} se hicieron {envio_total_mes[0]} envíos con un monto total de {envio_total_mes[1]}
        En el año {date.year} se hicieron {envio_total_año[0]} envíos con un monto total de {envio_total_año[1]}
          """)

#Productos más enviados:
    producto_mas_enviado=[0, 0]

    for enviado in shipments:
        if enviado.shipment_amount>producto_mas_enviado[1]:
            producto_mas_enviado=[enviado.product_name, enviado.shipment_amount]
    print(f"El producto con mayores envios fue: {producto_mas_enviado[0]}, con {producto_mas_enviado[1]} envíos.")

#Clientes con envíos pendientes:
    cliente_con_envío_pendiente= []
    for i in creditos:
        if not i.customer.identification_card in cliente_con_envío_pendiente:
            cliente_con_envío_pendiente.append(i.customer)
    print("Clientes con envíos pendientes:")
    for i, customer in enumerate(cliente_con_envío_pendiente):
        print(f"{i+1}. Nombre: {customer.name} Cédula o RIF: {customer.identification_card}")


#En esta función se encuentran todas las listas donde se agrega la información de cada clase, además del resto de código que permite guardar la información en un archivo txt.
def main():
    
    customers=[]
    leer= open("/Users/Usuario/OneDrive/Escritorio/Python/PROYECTO/txt/customers.txt","r")
    info_archivo = leer.readlines()
    leer.close()

    for i in range(0, len(info_archivo)):
        info_archivo[i] = info_archivo[i].split(sep='///')
        info_archivo[i].pop(len(info_archivo[i])-1)

    for cliente in info_archivo:
        customer=Customer(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5], cliente[6], cliente[7])
        customers.append(customer)


    products=[]
    leer= open("/Users/Usuario/OneDrive/Escritorio/Python/PROYECTO/txt/products.txt","r")
    info_archivo = leer.readlines()
    leer.close()

    for i in range(0, len(info_archivo)):
        info_archivo[i] = info_archivo[i].split(sep='///')
        info_archivo[i].pop(len(info_archivo[i])-1)

    for producto in info_archivo:
        product=Products(producto[0], producto[1], producto[2], producto[3], producto[4], producto[5])
        products.append(product)

    sales=[]
    leer= open("/Users/Usuario/OneDrive/Escritorio/Python/PROYECTO/txt/sales.txt","r")
    info_archivo = leer.readlines()
    leer.close()

    for i in range(0, len(info_archivo)):
        info_archivo[i] = info_archivo[i].split(sep='///')
        info_archivo[i].pop(len(info_archivo[i])-1)

    for venta in info_archivo:
        sale=Sale(venta[0], venta[1], venta[2], venta[3], venta[4])
        sales.append(sale)

    payments=[]
    leer= open("/Users/Usuario/OneDrive/Escritorio/Python/PROYECTO/txt/payments.txt","r")
    info_archivo = leer.readlines()
    leer.close()

    for i in range(0, len(info_archivo)):
        info_archivo[i] = info_archivo[i].split(sep='///')
        info_archivo[i].pop(len(info_archivo[i])-1)

    for pago in info_archivo:
        payment=Payment(pago[0], pago[1], pago[2], pago[3], pago[4])
        payments.append(payment)

    shipments=[]
    leer= open("/Users/Usuario/OneDrive/Escritorio/Python/PROYECTO/txt/shipments.txt","r")
    info_archivo = leer.readlines()
    leer.close()

    for i in range(0, len(info_archivo)):
        info_archivo[i] = info_archivo[i].split(sep='///')
        info_archivo[i].pop(len(info_archivo[i])-1)

    for envio in info_archivo:
        shipment=Shipment(envio[0], envio[1], envio[2])
        shipments.append(shipment)

    facturas=[]
     
    creditos = []
#Aquí se esta llamando a la función para cargar la API:
    info_apis = obtener_info_apis() 
    objetos_apis(info_apis, products)

#Aquí corre el menú principal, que da comienzo a todo:
    main_menu(products, sales, customers, facturas, payments, shipments, creditos)
    

main()
