import tkinter as tk
from tkinter import ttk, messagebox
from contact import Contact, ContactBook

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Contatos")
        self.contact_book = ContactBook()

        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12))

        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.name_label = ttk.Label(self.main_frame, text="Nome:")
        self.name_label.grid(row=0, column=0, pady=5)
        self.name_entry = ttk.Entry(self.main_frame, width=40)
        self.name_entry.grid(row=0, column=1, pady=5)

        self.phone_label = ttk.Label(self.main_frame, text="Telefone:")
        self.phone_label.grid(row=1, column=0, pady=5)
        self.phone_entry = ttk.Entry(self.main_frame, width=40)
        self.phone_entry.grid(row=1, column=1, pady=5)

        self.email_label = ttk.Label(self.main_frame, text="Email:")
        self.email_label.grid(row=2, column=0, pady=5)
        self.email_entry = ttk.Entry(self.main_frame, width=40)
        self.email_entry.grid(row=2, column=1, pady=5)

        self.add_button = ttk.Button(self.main_frame, text="Adicionar Contato", command=self.add_contact)
        self.add_button.grid(row=3, column=0, pady=5)

        self.remove_button = ttk.Button(self.main_frame, text="Remover Contato", command=self.remove_contact)
        self.remove_button.grid(row=3, column=1, pady=5)

        self.display_button = ttk.Button(self.main_frame, text="Listar Contatos", command=self.display_contacts)
        self.display_button.grid(row=4, column=0, pady=5)

        self.search_button = ttk.Button(self.main_frame, text="Buscar Contato", command=self.search_contact)
        self.search_button.grid(row=4, column=1, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        contact = Contact(name, phone, email)
        self.contact_book.add_contact(contact)
        messagebox.showinfo("Sucesso", "Contato adicionado com sucesso.")
        self.clear_fields()

    def remove_contact(self):
        name = self.name_entry.get()
        contact = self.contact_book.seach_contact(name)
        if contact:
            self.contact_book.remove_contact(contact)
            messagebox.showinfo("Sucesso", "Contato removido com sucesso.")
        else:
            messagebox.showerror("Erro", "Contato não encontrado.")

    def display_contacts(self):
        contacts = self.contact_book.get_all_contacts()
        if contacts:
            contact_list = "\n".join(str(contact) for contact in contacts)
            messagebox.showinfo("Contatos", contact_list)
        else:
            messagebox.showinfo("Contatos", "Nenhum contato encontrado.")

    def search_contact(self):
        name = self.name_entry.get()
        contact = self.contact_book.seach_contact(name)
        if contact:
            messagebox.showinfo("Contato Encontrado", str(contact))
        else:
            messagebox.showerror("Erro", "Contato não encontrado.")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
