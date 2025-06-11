# Advanced Encryption Tool using AES (Fernet) with GUI
import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox

# Step 1: Generate a key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Key Generated", "Encryption key saved as 'secret.key'.")

# Step 2: Load the key from file
def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        messagebox.showerror("Key Not Found", "Please generate the key first.")
        return None

# Step 3: Encrypt the selected file
def encrypt_file():
    key = load_key()
    if key is None:
        return

    filepath = filedialog.askopenfilename(title="Select file to encrypt")
    if not filepath:
        return

    with open(filepath, "rb") as file:
        file_data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)

    encrypted_path = filepath + ".encrypted"
    with open(encrypted_path, "wb") as file:
        file.write(encrypted_data)

    messagebox.showinfo("Encryption Complete", f"File encrypted and saved as:\n{encrypted_path}")

# Step 4: Decrypt the selected file
def decrypt_file():
    key = load_key()
    if key is None:
        return

    filepath = filedialog.askopenfilename(title="Select file to decrypt")
    if not filepath:
        return

    with open(filepath, "rb") as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception:
        messagebox.showerror("Decryption Failed", "Wrong key or corrupted file.")
        return

    decrypted_path = filepath.replace(".encrypted", ".decrypted")
    with open(decrypted_path, "wb") as file:
        file.write(decrypted_data)

    messagebox.showinfo("Decryption Complete", f"File decrypted and saved as:\n{decrypted_path}")

# Step 5: Create a GUI window
def setup_gui():
    window = tk.Tk()
    window.title("Advanced Encryption Tool ")
    window.geometry("450x300")
    window.configure(bg="#f7f7f7")

    tk.Label(window, text="Advanced Encryption Tool", font=("Arial", 18, "bold"), bg="#f7f7f7").pack(pady=20)

    tk.Button(window, text="Generate Encryption Key", command=generate_key, bg="#007bff", fg="white",
              font=("Arial", 12), width=30).pack(pady=10)

    tk.Button(window, text="Encrypt a File", command=encrypt_file, bg="#28a745", fg="white",
              font=("Arial", 12), width=30).pack(pady=10)

    tk.Button(window, text="Decrypt a File", command=decrypt_file, bg="#dc3545", fg="white",
              font=("Arial", 12), width=30).pack(pady=10)

    tk.Label(window, text="Keep the key file safe!", font=("Arial", 10), bg="#f7f7f7", fg="gray").pack(pady=10)

    window.mainloop()

# Run the program
if __name__ == "__main__":
    setup_gui()
