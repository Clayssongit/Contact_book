class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"Nome: {self.name} \nFone: {self.phone} \nEmail: {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def seach_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def get_all_contacts(self):
        return self.contacts
