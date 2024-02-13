class Contact:
    def __init__(self, name, phone, email, is_favorite = False) -> None:
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__is_favorite = is_favorite
    
    def set_name(self, name):
        self.__name = name
        return 
    
    def set_phone(self, phone):
        self.__phone = phone
        return 
    
    def set_email(self, email):
        self.__email = email
        return 
    
    def set_is_favorite(self):
        self.__is_favorite = not bool(self.__is_favorite)
        return 
    
    def get_name(self):
        return self.__name
    
    def get_phone(self):
        return self.__phone
    
    def get_email(self):
        return self.__email
    
    def get_is_favorite(self):
        return self.__is_favorite
        
    def to_dict(self):
        return {
            "name": self.__name,
            "phone": self.__phone,
            "email": self.__email,
            "is_favorite": self.__is_favorite
        }
    
    def to_string(self):
        is_favotire = '★' if self.__is_favorite else ''
        return f'[{is_favotire}] {self.__name} - {self.__phone} - {self.__email}'

def create_contact():
    name = input("Digite o nome do contato que deseja adicionar: ")
    phone = input("Digite o telefone do contato que deseja adicionar: ")
    email = input("Digite o e-mail do contato que deseja adicionar: ")
    contact = Contact(name=name, phone=phone, email=email)
    contacts.append(contact)
    print(f"\nContato {contact.get_name()} foi cadastrado com sucesso!")
    return

def get_all_contacts(filter_favorite = False):
    for index, contact in enumerate(contacts, start=1):
        if filter_favorite and not contact.get_is_favorite():
            continue
        print(f'\n{index}.{contact.to_string()}')

def update_contact():
    index_contact = input("Digite o numero do contato que deseja atualizar: ")
    index_contact = int(index_contact) - 1
    if index_contact >= 0 and index_contact < len(contacts) :
        contact = contacts[index_contact]
        print(f'\nContato {contact.to_string()} selecionado:')
        while True: 
            is_changed = input("\nDeseja alterar o nome do contato? (s/n)")
            if is_changed.lower() != 'n' and is_changed.lower() != 's':
                print('Valor digitado incorreto, digite S para alterar e N para prosseguir!')
                continue
            elif is_changed.lower() == 's':
                new_name = input(f"Digite o novo nome do contato :")
                contact.set_name(new_name)
            break

        while True: 
            is_changed = input("\nDeseja alterar o telefone do contato? (s/n)")
            if is_changed.lower() != 'n' and is_changed.lower() != 's':
                print('Valor digitado incorreto, digite S para alterar e N para prosseguir!')
                continue
            elif is_changed.lower() == 's':
                new_phone = input(f"Digite o novo telefone do contato :")
                contact.set_phone(new_phone)
            break
            
        while True: 
            is_changed = input("\nDeseja alterar o email do contato? (s/n)")
            if is_changed.lower() != 'n' and is_changed.lower() != 's':
                print('Valor digitado incorreto, digite S para alterar e N para prosseguir!')
                continue
            elif is_changed.lower() == 's':
                new_email = input(f"Digite o novo email do contato :")
                contact.set_email(new_email)
            break

        print(f"Contato alterador : {contact.to_string()}")
    else :
        print(f"Indice de contato invalido.")
    return
    
def checked_favorite():
    index_contact = input("Digite o numero do contato que deseja marcado/desmarcar como favorito: ")
    index_contact = int(index_contact) - 1
    if index_contact >= 0 and index_contact < len(contacts) :
        contact = contacts[index_contact]
        print(f'\nContato {contact.to_string()} selecionado:')
        while True: 
            string_checked = 'marcar' if contact.get_is_favorite else 'desmarcar'
            is_changed = input(f"\nTem certeza que deseja {string_checked} como favorito? (s/n)")
            if is_changed.lower() != 'n' and is_changed.lower() != 's':
                print('Valor digitado incorreto, digite S para alterar e N para prosseguir!')
                continue
            elif is_changed.lower() == 's':
                contact.set_is_favorite()
                string_checked = 'marcar' if not contact.get_is_favorite else 'desmarcar'
                print(f"Contato {string_checked} como favorito!")
            else:
                print(f"Ação cancelada !")
            break
    
    else :
        print(f"Indice de contato invalido.")
    return

def delete_contact():
    index_contact = input("Digite o numero do contato que deseja deletar: ")
    index_contact = int(index_contact) - 1
    if index_contact >= 0 and index_contact < len(contacts) :
        contact = contacts[index_contact]
        print(f'\nContato {contact.to_string()} selecionado:')
        while True:
            is_deleted = input(f"\nTem certeza que deseja deletar o contato? (s/n)")
            if is_deleted.lower() != 'n' and is_deleted.lower() != 's':
                print('Valor digitado incorreto, digite S para alterar e N para prosseguir!')
                continue
            elif is_deleted.lower() == 's':
                contacts.remove(contact)
                print(f"Contato deletado com sucesso!")
            else:
                print(f"Ação cancelada !")
            break
    else :
        print(f"Indice de contato invalido.")
    return

contacts = []
print("\nControle de contatos")
while True:
    print("\nMenu do gerenciador de contatos:")
    print("1. Adicionar contato")
    print("2. Ver os contatos favoritos")
    print("3. Ver todos os contatos")
    print("4. Editar um contato")
    print("5. Marcar/desmarcar contato como favorito")
    print("6. Deletar contatos")
    print("7. Sair")

    escolha = input("Digite a sua escolha: ")

    if(escolha == "1"):
        print("\nCadastrar novo contato:")
        create_contact()
    elif escolha == "2" :
        print("\nListar todo os contatos favoritos:")
        get_all_contacts(True)
    elif escolha == "3" :
        print("\nListar todo os contatos:")
        get_all_contacts()
    elif escolha == "4" :
        print("\nEditar um contato:")
        get_all_contacts()
        update_contact()
    elif escolha == "5" :
        print("\nMarcar/desmarcar um contato como favorito:")
        get_all_contacts()
        checked_favorite()
    elif escolha == "6" :
        print("\nDeletar um contato:")
        get_all_contacts()
        delete_contact()
    elif escolha == "6" :
        break
print("Programa finalizado")