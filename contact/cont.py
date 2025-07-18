import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

# CSV File
FILENAME = 'contacts.csv'

# Create file if not exists
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone', 'Email', 'Address'])

# Helper to load all contacts
def load_contacts():
    contacts = []
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append(row)
    return contacts

# Helper to save all contacts
def save_contacts(contacts):
    with open(FILENAME, 'w', newline='') as file:
        fieldnames = ['Name', 'Phone', 'Email', 'Address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

# Add Contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required!")
        return

    contacts = load_contacts()
    contacts.append({'Name': name, 'Phone': phone, 'Email': email, 'Address': address})
    save_contacts(contacts)

    messagebox.showinfo("Success", "Contact added successfully!")
    clear_fields()
    view_contacts()

# View Contacts
def view_contacts():
    listbox.delete(0, tk.END)
    contacts = load_contacts()
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Search Contact
def search_contact():
    query = entry_search.get().lower()
    listbox.delete(0, tk.END)
    contacts = load_contacts()
    found = False
    for contact in contacts:
        if query in contact['Name'].lower() or query in contact['Phone']:
            listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")
            found = True
    if not found:
        messagebox.showinfo("Not Found", "No matching contact found.")

# Select contact to update/delete
def select_contact(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        selected = listbox.get(index).split(" - ")[0]
        contacts = load_contacts()
        for contact in contacts:
            if contact['Name'] == selected:
                entry_name.delete(0, tk.END)
                entry_name.insert(0, contact['Name'])

                entry_phone.delete(0, tk.END)
                entry_phone.insert(0, contact['Phone'])

                entry_email.delete(0, tk.END)
                entry_email.insert(0, contact['Email'])

                entry_address.delete(0, tk.END)
                entry_address.insert(0, contact['Address'])

# Update Contact
def update_contact():
    selected = entry_name.get()
    contacts = load_contacts()
    for contact in contacts:
        if contact['Name'] == selected:
            contact['Phone'] = entry_phone.get()
            contact['Email'] = entry_email.get()
            contact['Address'] = entry_address.get()
            break
    else:
        messagebox.showwarning("Not Found", "Contact not found.")
        return

    save_contacts(contacts)
    messagebox.showinfo("Success", "Contact updated.")
    clear_fields()
    view_contacts()

# Delete Contact
def delete_contact():
    selected = entry_name.get()
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c['Name'] != selected]
    if len(contacts) == len(new_contacts):
        messagebox.showwarning("Not Found", "Contact not found.")
        return

    save_contacts(new_contacts)
    messagebox.showinfo("Deleted", "Contact deleted.")
    clear_fields()
    view_contacts()

# Clear Fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# --- UI Code ---
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")

# Entry Form
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Address").pack()
entry_address = tk.Entry(root)
entry_address.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack()
tk.Button(root, text="Delete Contact", command=delete_contact).pack()

tk.Label(root, text="Search").pack()
entry_search = tk.Entry(root)
entry_search.pack()
tk.Button(root, text="Search", command=search_contact).pack(pady=5)

tk.Button(root, text="View All Contacts", command=view_contacts).pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", select_contact)

view_contacts()

root.mainloop()
