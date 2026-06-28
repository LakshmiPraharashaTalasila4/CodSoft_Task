import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "":
        messagebox.showwarning("Warning", "Enter Name")
        return

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    messagebox.showinfo("Success", "Contact Added")
    clear_entries()
    show_contacts()

def search_contact():
    name = name_entry.get()

    if name in contacts:
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

        phone_entry.insert(0, contacts[name]["Phone"])
        email_entry.insert(0, contacts[name]["Email"])
        address_entry.insert(0, contacts[name]["Address"])
    else:
        messagebox.showerror("Error", "Contact Not Found")

def update_contact():
    name = name_entry.get()

    if name in contacts:
        contacts[name]["Phone"] = phone_entry.get()
        contacts[name]["Email"] = email_entry.get()
        contacts[name]["Address"] = address_entry.get()

        messagebox.showinfo("Success", "Contact Updated")
        show_contacts()
    else:
        messagebox.showerror("Error", "Contact Not Found")

def delete_contact():
    name = name_entry.get()

    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact Deleted")
        clear_entries()
        show_contacts()
    else:
        messagebox.showerror("Error", "Contact Not Found")

def show_contacts():
    listbox.delete(0, tk.END)

    for name, details in contacts.items():
        listbox.insert(
            tk.END,
            f"{name} | {details['Phone']} | {details['Email']}"
        )

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Book")
root.geometry("600x500")

tk.Label(root, text="Contact Book", font=("Arial",18,"bold")).pack(pady=10)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Add", width=10, command=add_contact).grid(row=0,column=0,padx=5)

tk.Button(frame, text="Search", width=10, command=search_contact).grid(row=0,column=1,padx=5)

tk.Button(frame, text="Update", width=10, command=update_contact).grid(row=0,column=2,padx=5)

tk.Button(frame, text="Delete", width=10, command=delete_contact).grid(row=0,column=3,padx=5)

listbox = tk.Listbox(root, width=80, height=12)
listbox.pack(pady=10)

root.mainloop()
