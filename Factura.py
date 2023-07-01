from Sale import *
from Payment import *
from Shipment import *


class Factura:
    def __init__(self, customer, products_to_buy, subtotal, discount, iva, igtf, total):
        self.customer=customer
        self.products_to_buy=products_to_buy
        self.subtotal=subtotal
        self.discount=discount
        self.iva=iva
        self.igtf=igtf
        self.total=total

    
#Función para mostrar la factura con sus atributos.
    def show(self):
        
        print(f""" ---FACTURA---
        Cliente: {self.customer}
        Producto:{self.products_to_buy}
        Subtotal: {self.subtotal}
        Descuento: {self.discount}
        IVA: {self.iva}
        IGTF: {self.igtf}
        Total: {self. total}""")
