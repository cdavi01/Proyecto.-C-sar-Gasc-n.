class Customer:
    def __init__(self, name, last_name, type, identification_card, email, address, phone_number, buy_amount):
        self.name=name
        self.last_name=last_name
        self.type=type
        self.identification_card=identification_card
        self.email=email
        self.address=address
        self.phone_number=phone_number
        self.buy_amount=buy_amount

#Aquí se muestran los atributos del cliente.
    def show_atributes(self):
        print(  f"""Nombre: {self.name}
            Apellido: {self.last_name}
            Tipo: {self.type}
            Cédula: {self.identification_card}
            Email: {self.email}
            Dirección: {self.address}
            Telefono: {self.phone_number}
              """)

#Se hace herencia para que el desarrollo del código sea más claro.
class CustomerManagement(Customer):
    
    def __init__ (self, name, last_name, type, identification_card, email, address, phone_number, buy_amount):
        super().__init__(self, name, last_name, type, identification_card, email, address, phone_number, buy_amount)

#Función hecha para registrar y crear al cliente. Se le pide nombre, apellido, tipo de cliente, email, dirección y teléfono.
    def register_customer(customers):
        print("BIENVENIDO AL REGISTRO DE CLIENTES")

        name=input("Ingrese su nombre: ")
        while not name.isalpha():
            name=input("Error! Ingrese un nombre válido: ")
        
        last_name=input("Ingrese su apellido: ")
        while not last_name.isalpha():
            last_name=input("Error! Ingrese un apellido válido: ")

        type=input("Elija qué tipo de cliente es usted:(1.Natural 2.Jurídico) ")
        while not type.isnumeric() or int(type) not in range(1, 3):
            type=input("Error! Ingrese un dato válido: ")
        
        if int(type)==1:
            type="Natural"
            identification_card=input("Ingrese su cédula: ")
            while not identification_card.isnumeric() or (len(identification_card))<7 or (len(identification_card))>8: 
                identification_card=input("Error! Ingrese una cédula válida: ")
            
        elif int(type)==2:
            type="Jurídico"
            identification_card=input("Ingrese su RIF: ")
            while not identification_card.isnumeric() or (len(identification_card))!=10: 
                identification_card=input("Error! Ingrese un RIF válido: ")


        email= input("Ingrese su correo electrónico: ")
        while not "@" in email or not "." in email:
            email=input("Error! Ingrese un correo electrónico válido: ")

        address=input("Ingrese su dirección: ").capitalize()

        phone_number=input("Ingrese su número telefónico: ")
        while not phone_number.isnumeric() or (len(phone_number))!=11:
            phone_number=input("Error ingrese un número válido: ")

        customer=Customer(name, last_name, type, int(identification_card), email, address, phone_number, 0)
        customers.append(customer)

        print("\nCliente registrado con éxito.")


#Función hecha para modificar la información registrada anteriormente. Se muestran los clientes registrados y el usuario decide cuál modificar.
    def modify_customer_information(customers):
        print("CLIENTES")
        print("")
        for i, customer in enumerate(customers):
            print(f"{i+1}. Nombre: {customer.name}, Cédula o RIF: {customer.identification_card}")


        modify_client=input("¿Cuál cliente desea modificar? (Marque con números) ")
        while not modify_client.isnumeric() or int(modify_client) not in range(1, len(customers)+1):
            modify_client=input("Error! Ingrese un dato válido: ")
        
        modify_client=int(modify_client)-1

        cliente_a_modificar=customers[modify_client]


        print("""
        1. Nombre.
        2. Apellido.
        3. Tipo de Cliente.
        4. Cédula o RIF.
        5. Email.
        6. Dirección.
        7. Teléfono.
        """)

        options=input("¿Qué desea modificar? ")
        while not options.isnumeric() or int(options) not in range(1, 8):
            options=input("Error! Intente de nuevo: ")
        
       
        if int(options)==1:
            name=input("Ingrese su nuevo nombre: ")
            while not name.isalpha():
                name=input("Error! Ingrese un nombre válido: ")
            cliente_a_modificar.name = name 

        elif int(options)==2:
            last_name=input("Ingrese su nuevo apellido: ")
            while not last_name.isalpha():
                last_name=input("Error! Ingrese un apellido válido: ")
            cliente_a_modificar.last_name = last_name

        elif int(options)==3:
            type=input("Elija nuevamente qué tipo de cliente es usted:(1.Natural 2.Jurídico) ") 
            while not type.isnumeric() or int(type) not in range(1, 3):
                type=input("Error! Ingrese un dato válido: ")
            cliente_a_modificar.type = type

        elif int(options)==4:
            ask=input("¿Qué tipo de cliente es usted? (1. Natural 2.Jurídico) ")
            while not ask.isnumeric() or int(ask) not in range(1, 3):
                ask=input("Error! Ingrese un dato válido: ")
            if int(ask)==1:
                identification_card=input("Ingrese su nueva cédula: ")
                while not identification_card.isnumeric() or (len(identification_card))<7 and (len(identification_card))>8: 
                    identification_card=input("Error! Ingrese una cédula válida: ")
                cliente_a_modificar.identification_card = identification_card
            elif int(ask)==2:
                identification_card=input("Ingrese su nuevo RIF: ")
                while not identification_card.isnumeric() or (len(identification_card))!=10: 
                    identification_card=input("Error! Ingrese un RIF válido: ")
                cliente_a_modificar.identification_card = identification_card

        elif int(options)==5:
            email= input("Ingrese su nuevo email: ")
            while not "@" in email or not "." in email:
                email=input("Error! Ingrese un email válido: ")
            cliente_a_modificar.email=email

        elif int(options)==6:
            address=input("Ingrese su nueva dirección: ").capitalize()
            cliente_a_modificar.address=address

        elif int(options)==7:
            phone_number=input("Ingrese su nuevo número telefónico: ")
            while not phone_number.isnumeric() or (len(phone_number))!=11:
                phone_number=input("Error ingrese un número válido: ")
            cliente_a_modificar.phone_number = phone_number


#Función hecha para eliminar a un objeto cliente por la cédula o RIF.
    def delete_customer(customers):
        id_type = input("El cliente es natural (1) o juridico (2): ")
        while not id_type.isnumeric() or int(id_type) not in range(1, 3):
            id_type=input("Error! Ingrese un dato válido: ")

        if id_type=="1":
            identification=input("Ingrese la cédula del cliente a eliminar:" )
            while not identification.isnumeric() or (len(identification))<7 and (len(identification))>8: 
                identification=input("Error! Ingrese una cédula válida: ")
        elif id_type=="2":
            identification=input("Ingrese el RIF del cliente a eliminar:" )
            while not identification.isnumeric() or (len(identification))!=10: 
                identification=input("Error! Ingrese un RIF válido: ")

        found=0
        for customer1 in customers:
            if customer1.identification_card==identification:
                customers.remove(customer1)
                print("Cliente eliminado con éxito")
                found+=1  
                break

        if found==0:         
            print("Este cliente no existe dentro de la base de datos.") 

    
#Función hecha para buscar al cliente por su cédula.
    def search_customer_identification_card(customers):
        id_type = input("El cliente es natural (1) o juridico (2): ")
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
        for customer2 in customers:
            if customer2.identification_card==option:
                found+=1
                print("\nDatos encontrados: ")
                print(f"""
                Nombre: {customer2.name}
                Apellido: {customer2.last_name}
                Tipo: {customer2.type}
                Cédula:{customer2.identification_card}
                Email: {customer2.email}
                Dirección: {customer2.address}
                Teléfono: {customer2.phone_number}
                """)
        
        if found==0:         
            print("Este cliente no existe dentro de la base de datos.")         

                    
#Función hecha para buscar al cliente por su email.
    def search_customer_email(customers):
        option=input("Ingrese su correo electrónico: ")
        while not "@" in option or not "." in option:
            option=input("Error! Ingrese un correo electrónico válido: ")

        found=0
        for customer2 in customers:
            if customer2.email==option:
                found+=1
                print("\nDatos encontrados: ")
                print(f"""Nombre: {customer2.name}
                        Apellido: {customer2.last_name}
                        Tipo: {customer2.type}
                        Cédula:{customer2.identification_card}
                        Email: {customer2.email}
                        Dirección: {customer2.address}
                        Teléfono: {customer2.phone_number}
                        """)
        
        if found==0:         
            print("Este cliente no existe dentro de la base de datos.") 