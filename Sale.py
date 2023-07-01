from Products import *
from Customer import *
from Payment import *
from Shipment import *
from Factura import *

class Sale:
    def __init__(self, customer, product, total, payment, shipment):
        self.customer=customer
        self.product=product
        self.total = total
        self.payment= payment
        self.shipment= shipment


#Aquí se muestran los atributos de la venta.
    def show_atributes(self):
        print(  f"""
        Cliente: {self.customer}
        Producto: {self.product}
        Cantidad: {self.total}
        Método de Pago: {self.payment}
        Método de Envío: {self.shipment}
            """)
        
#Se hace herencia para que el desarrollo del código sea más claro.  
class SaleManagement(Sale):
    def __init__(self, customer, product, total, payment, shipment):
        super().__init__(customer, product, total, payment, shipment)


#Función hecha para registrar y crear la venta. Se le pide nombre del producto deseado, la cantidad, si desea continuar, calcula el total...
    def register_sale(sales, products, customers, facturas, payments, shipments, creditos):
        if len(customers)!=0 and len(products)!=0:
            option=input("\nIngrese la cédula o RIF: ")
            customer=""
            for client in customers:
                if int(option)==client.identification_card:
                    customer=client
            if customer=="":
                print("Para realizar una venta, debe haber al menos un cliente registrado.")
            else:
                products_to_buy=[]
                while True:
                    if len(products)==0:
                            print('No hay productos registrados, registre alguno para poder realizar la compra.')
                    else:
                        
                        names=[]
                        for product in products:
                            print(f"{product.product_name}. Disponibilidad: {product.availability}. Precio {product.price}")
                            names.append(product.product_name)
                      
                        print("")

                        selection_1=input("Escriba el nombre del producto que desea: ").title()
                        while not (selection_1.replace(" ", "")).isalpha() or not selection_1 in names:
                            selection_1=input("Error! Ingrese un nombre válido: ").title()

                        amount=input("Escriba la cantidad del producto que desea: ")
                        while not amount.isnumeric() or not int(amount)<=product.availability:
                            amount=input("Error! Ingrese una cantidad válida: ")
                        products_to_buy.append([selection_1, amount, float(amount)*product.price])

                        #products[int(selection_1)-1].total_sales+=amount
                        #products[int(selection_1)-1].shipment_amount+=amount

                    
                    continues=input("¿Desea incluir otro producto? (1.SI 2.NO) ")
                    while not continues.isnumeric() or int(continues) not in range(1, 3):
                        continues=input("Error! Ingrese un dato válido: ")
                    if int(continues)==2:
                        break
                
                subtotal=0
                for i, buy in enumerate(products_to_buy):
                    subtotal += buy[2]

                payment =PaymentManagement.register_payment(payments, subtotal, customer) #Si aquí "PaymentManagement" sale como indefinido, ignorar, es un bug del programa y no interfiere al correrlo.
                shipment=ShipmentManagement.register_shipment(shipments, payments) #Si aquí "ShipmentManagement" sale como indefinido, ignorar, es un bug del programa y no interfiere al correrlo.

                discount=0
                if customer.type=="Jurídico" and payment.payment_type=="Cash":
                    discount=0.05
                    subtotal-=discount*subtotal
                iva=0.16*subtotal
                if payment.currency=="Dólares":
                    igtf=subtotal*0.03
                total=subtotal+iva+igtf
                print(f"El total es: {total}")

                
                if customer.type=="Jurídico":
                    ask=input("¿Desea hacer la compra a crédito o normal? (1.Crédito 2.Normal)")
                    while not ask.isnumeric() or int(ask) not in range(1, 3):
                        ask=input("Error! Ingrese un dato válido: ")

                    if int(ask)==1:
                        print("Su compra ha sido agregada a la lista de créditos")
                        
                        sale=Sale(customer, product, float(total), payment, shipment)
                        creditos.append(sale)

                    if int(ask)==2:
                        factura=Factura(customer.name, products_to_buy, subtotal, discount, iva, igtf, total) #Si aquí "Factura" sale como indefinido, ignorar, es un bug del programa y no interfiere al correrlo.
                        factura.show()
                        facturas.append(factura)

                        sale=Sale(customer, product, float(total), payment, shipment)
                        sales.append(sale)
                else:
                    factura=Factura(customer.name, products_to_buy, subtotal, discount, iva, igtf, total) #Si aquí "Factura" sale como indefinido, ignorar, es un bug del programa y no interfiere al correrlo.
                    factura.show()
                    facturas.append(factura)

                    sale=Sale(customer, product, float(total), payment, shipment)
                    sales.append(sale)

                    customer.buy_amount+=1

#Función hecha para buscar la venta por el cliente, al encontrala, muestra los datos de la venta.
    def search_customer_sale(sales):
        id_type = input("El cliente es natural (1) o jurídico (2): ")
        while not id_type.isnumeric() or int(id_type) not in range(1, 3):
            id_type=input("Error! Ingrese un dato válido: ")
        if id_type=="1":
            option=input("Ingrese su cédula: ")
            while not option.isnumeric() or (len(option))<7 and (len(option))>8:  
                option=input("Error! Ingrese una cédula válida: ")
        elif id_type=="2":
            option=input("Ingrese su RIF: ")
            while not option.isnumeric() or (len(option))!=10:  
                option=input("Error! Ingrese un RIF válido: ")

        found=0
        for customer2 in sales:
            if (customer2.customer).identification_card==int(option):
                found+=1
                print("\nDatos encontrados: ")
                print(f"""
                Cliente: {(customer2.customer).name}
                Producto: {customer2.product}
                Monto: {customer2.total}
                Método de Pago:{customer2.payment}
                Envío: {customer2.shipment}
                
                """)
        
        if found==0:         
            print("Esta venta no existe dentro de la base de datos.")


#Función hecha para buscar la venta por la fecha, al encontrala, muestra los datos de la venta.
    def search_date_sale(sales):
        option=input("Coloque la fecha de su venta según este formato:(YYYY-MM-DD) ")
        while not option.isnumeric() and not "/" in option:
            option=input("Error! Ingrese un dato válido: ")
        

        found=0
        for sale in sales:
            if (sale.payment).date==option:
                found+=1
                print("\nDatos encontrados: ")
                print(f"""
                Cliente: {sale.customer}
                Producto: {sale.product}
                Monto: {sale.total}
                Método de Pago:{sale.payment}
                Envío: {sale.shipment}
                
                """)
        
        if found==0:         
            print("Esta venta no existe dentro de la base de datos.") 
    

#Función hecha para buscar la venta por el total, al encontrala, muestra los datos de la venta.
    def search_total_sale(sales):
        option=input("Coloque el monto total: ")
        while not option.isnumeric():
            option=input("Error! Ingrese un dato válido: ")
        

        found=0
        for total in sales:
            if total.total== float(option):
                found+=1
                print("\nDatos encontrados: ")
                print(f"""Cliente: {total.customer}
                        Producto: {total.product}
                        Monto: {total.total}
                        Método de Pago:{total.payment}
                        Envío: {total.shipment}
                        
                        """)
        
        if found==0:         
            print("Esta venta no existe dentro de la base de datos.") 