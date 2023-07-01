from Payment import *
from Customer import *
from Sale import *

class Shipment:
    def __init__(self, purchase_order, shipping_service, cost, shipment_amount):
        self.purchase_order=purchase_order
        self.shipping_service =shipping_service 
        self.cost=cost 
        self.shipment_amount=shipment_amount 


#Aquí se muestran los atributos del envío.
    def show_atributes(self):
        print(  f"""Orden de Compra: {self.purchase_order}
            Servicio de envío: {self.shipping_service}
            Costo: {self.cost}
              """)
        
#Se hace herencia para que el desarrollo del código sea más claro. 
class ShipmentManagement(Shipment):
    def __init__(self, purchase_order, shipping_service, cost, shipment_amount):
        super().__init__(purchase_order, shipping_service, cost, shipment_amount)

#Función hecha para registrar y crear el envío. Se le pide el orden de compra, el servicio de envío (si es Delivery, pide los datos del motorizado) y el costo.
#(No se muestra en el menú de gestión de envíos, ya que se hace el registro automáticamente en la clase de ventas).
    def register_shipment(shipments, payments):
        if len(payments)==0:
            print("No se ha hecho la compra de ningún producto.")
        else:
            purchase_order=input("Ingrese el orden de su compra: ")#Este ítem no pude comprenderlo. Mis disculpas.
            while not purchase_order.isnumeric():
                purchase_order=input("Error! Intente de nuevo: ")

            shipping_service = ["MRW", "Zoom", "Delivery"]
            for i, service in enumerate(shipping_service):
                print(f"{i+1}. {service}")
        
            option=input("¿Qué servicio de envío desea? ")
            while not option.isnumeric() or not int(option) in range(1, len(shipping_service)+1):
                print("Error")
                option=input("¿Qué servicio de envío desea? ")
            
            if int(option)==3:
                print("Ingrese datos de motorizado:")
                print("")

                moto_name=input("Ingrese el nombre del motorizado: ")
                while not moto_name.isalpha():
                    moto_name=input("Error! Ingrese un nombre válido: ")
                moto_identification_card=input("Ingrese la cédula del motorizado: ")
                while not moto_identification_card.isnumeric() or (len(moto_identification_card))<7 and (len(moto_identification_card))>8: 
                    moto_identification_card=input("Error! Ingrese una cédula válida: ")
                moto_phone_number=input("Ingrese el número telefónico del motorizado: ")
                while not moto_phone_number.isnumeric() or (len(moto_phone_number))!=11:
                    moto_phone_number=input("Error ingrese un número válido: ")
                

            cost=input("Costo del servicio: ")
            while not cost.isnumeric():
                cost=input("Error! Intente de nuevo: ")
            
            shipment=Shipment(purchase_order, shipping_service, cost, 0)
            shipments.append(shipment)
            return shipment
        

#Función hecha para buscar el envío por el cliente, al encontralo, muestra los datos del envío.
    def search_customer_shipment(shipments):
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
        for customer2 in shipments:
            if (customer2.customer).identification_card==int(option):
                found+=1
                print("\nDatos encontrados: ")
                print(f"""
                Cliente: {(customer2.customer).name}
                Orden de Compra: {customer2.purchase_order}
                Servicio de envío: {customer2.shipping_service}
                Costo: {customer2.cost}
                
                """)
        
        if found==0:         
            print("Esta venta no existe dentro de la base de datos.")
    

#Función hecha para buscar el envío por la fecha, al encontralo, muestra los datos del envío.
    def search_date_shipment(shipments):
        option=input("Coloque la fecha de su envío según este formato:(YYYY-MM-DD) ")
        while not option.isnumeric() and not "/" in option:
            option=input("Error! Ingrese un dato válido: ")

        found=0
        for date1 in shipments:
            if date1.date==option:
                found+=1
                print("\nDatos encontrados: ")
                print(f"""Orden de Compra: {date1.purchase_order}
                        Servicio de envío: {date1.shipping_service}
                        Costo: {date1.cost}
                        
                        """)
        
        if found==0:         
            print("Este pago no existe dentro de la base de datos.") 