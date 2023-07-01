from Products import *
from Customer import *
from Shipment import *
from Sale import *
import datetime

class Payment:
    def __init__(self, customer, total, currency, payment_type, date):
        self.customer=customer
        self.total=total
        self.currency=currency
        self.payment_type=payment_type
        self.date=date

#Aquí se muestran los atributos del pago.
    def show_atributes(self):
        print(  f"""
        Cliente: {self.customer}
        Total: {self.total}
        Moneda: {self.currency}
        Método de Pago: {self.payment_type}
        Fecha: {self.date}
            """)
        

#Se hace herencia para que el desarrollo del código sea más claro.
class PaymentManagement(Payment):
    def __init__(self, customer, total, currency, payment_type, date):
        super().__init__(customer, total, currency, payment_type, date)


#Función hecha para registrar y crear el pago. Se le pide moneda de pago, tipo de pago y el tiempo.
#(No se muestra en el menú de gestión de pago, ya que se hace el registro automáticamente en la clase de ventas).
    def register_payment(payments, total, customer):
            currency=input("Ingrese la moneda de pago: (1.Dólares 2.Bolívares)")
            while not currency.isnumeric() or int(currency) not in range(1, 3):
                currency=input("Error! Ingrese un dato válido: ")
            
            if int(currency)==1:
                currency="Dólares"
            elif int(currency)==2:
                currency="Bolívares"

            payment_type = ["PdV", "PM", "Zelle", "Cash"]
            for i, type in enumerate(payment_type):
                print(f"{i+1}. {type}")
            option=input("¿Qué tipo de pago desea realizar? ")
            while not option.isnumeric() or not int(option) in range(1, len(payment_type)+1):
                print("Error")
                option=input("¿Qué tipo de pago desea realizar? ")

            if int(option)==1:
                payment_type="Pdv"
            elif int(option)==2:
                payment_type="PM"
            elif int(option)==3:
                payment_type="Zelle"
            elif int(option)==4:
                payment_type="Cash"
            
            
            date=datetime.datetime.now().date()
            
            
            payment=Payment(customer, total, currency, payment_type, date)
            payments.append(payment)
            return payment                
    

#Función hecha para buscar el pago por el cliente, al encontralo, muestra los datos del pago.
    def search_customer_payment(payments, customer):
        if customer.type=="Natural":
            option=input("Ingrese su cédula: ")
            while not option.isnumeric() or (len(option))<7 and (len(option))>8:  
                option=input("Error! Ingrese una cédula válida: ")
        elif customer.type=="Jurídico":
            option=input("Ingrese su RIF: ")
            while not option.isnumeric() or (len(option))!=10:  
                option=input("Error! Ingrese un RIF válido: ")

        found=0
        for customer2 in payments:
            if customer2.identification_card==option:
                found+=1
                print("\nDatos encontrados: ")
                print(f"""Cliente: {customer2.customer}
                        Total: {customer2.total}
                        Moneda del Pago: {customer2.currency}
                        Tipo de Pago:{customer2.payment_type}
                        Fecha: {customer2.date}
                        
                        """)
        
        if found==0:         
            print("Este pago no existe dentro de la base de datos.") 
    

#Función hecha para buscar el pago por la fecha, al encontralo, muestra los datos del pago.
    def search_date_payment(payments):
        option=input("Coloque la fecha de su pago según este formato:(YYYY-MM-DD) ")
        while not option.isnumeric() and not "/" in option:
            option=input("Error! Ingrese un dato válido: ")

        found=0
        for date1 in payments:
            if date1.date==option:
                found+=1
                print("\nDatos encontrados: ")
                print(f"""Cliente: {date1.customer}
                        Total: {date1.total}
                        Moneda del Pago: {date1.currency}
                        Tipo de Pago:{date1.payment_type}
                        Fecha: {date1.date}
                        
                        """)
        
        if found==0:         
            print("Este pago no existe dentro de la base de datos.") 

#Función hecha para buscar el pago por el tipo de pago, al encontralo, muestra los datos del pago.
    def search_type_payment(payments):
        option=input("¿Qué tipo de pago realizó? (PdV, PM, Zelle, Cash) Escríbalo igual. ").capitalize()
        while not option.isalpha():
            option=input("Error! ¿Qué tipo de pago realizó? ").capitalize()

        found=0
        for tipo in payments:
            if tipo.payment_type==option:
                found+=1
                print("\nDatos encontrados: ")
                print(f"""Cliente: {tipo.customer}
                        Total: {tipo.total}
                        Moneda del Pago: {tipo.currency}
                        Tipo de Pago:{tipo.payment_type}
                        Fecha: {tipo.date}
                        
                        """)
        
        if found==0:         
            print("Este pago no existe dentro de la base de datos.") 
    

#Función hecha para buscar el pago por el tipo de moneda, al encontralo, muestra los datos del pago.
    def search_currency_payment(payments):
        option=input("¿Qué moneda de pago utilizó? (Dólares, Bolívares) Escríbalo igual. ").capitalize()
        while not option.isalpha():
            option=input("Error! ¿Qué tipo de pago realizó? ").capitalize()

        found=0
        for currency1 in payments:
            if currency1.currency==option:
                found+=1
                print("\nDatos encontrados: ")
                print(f"""Cliente: {currency1.customer}
                        Total: {currency1.total}
                        Moneda del Pago: {currency1.currency}
                        Tipo de Pago:{currency1.payment_type}
                        Fecha: {currency1.date}
                        
                        """)
        
        if found==0:         
            print("Este pago no existe dentro de la base de datos.") 