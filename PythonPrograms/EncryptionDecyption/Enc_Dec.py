from tkinter import messagebox, simpledialog, Tk, Entry, Text, Button

def is_even(number):
  """Checks if a number is even using the modulo operator."""
  return number % 2 == 0

def caesar_cipher(message, shift_value, mode):
  """Encrypts or decrypts a message using Caesar Cipher with a shift value.

  Args:
      message: The message to encrypt or decrypt.
      shift_value: The number of positions to shift letters (positive for encryption, negative for decryption).
      mode: "encrypt" or "decrypt" depending on the operation.

  Returns:
      The encrypted or decrypted message.
  """
  ciphered_message = ""
  for char in message:
    if char.isalpha():  # Check for alphabetic characters only
      base = ord('a') if char.islower() else ord('A')
      new_ord = ord(char) - base + shift_value
      new_ord = (new_ord - 26) % 26 if mode == "encrypt" else (new_ord + 26) % 26  # Handle wrap-around
      ciphered_message += chr(new_ord + base)
    else:
      ciphered_message += char  # Preserve non-alphabetic characters
  return ciphered_message

def get_task():
  """Prompts the user for encryption or decryption task using a dialog box."""
  task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
  return task.lower()  # Convert to lowercase for easier comparison

def get_message():
  """Prompts the user for a message using a text entry widget."""
  root = Tk()
  root.withdraw()  # Hide the root window
  message = simpledialog.askstring('Message', 'Enter the message:')
  root.destroy()  # Destroy the hidden window
  return message

def main():
  """Main program loop for user interaction and encryption/decryption."""
  root = Tk()
  root.title("Text Encryption/Decryption Tool")

  message_entry = Entry(root, width=50)
  message_entry.pack()

  result_text = Text(root, height=10, width=50)
  result_text.pack()

  def encrypt_click():
    """Encrypts the message entered in the entry widget and displays the result."""
    message = message_entry.get()
    if not message:
      messagebox.showerror("Error", "Please enter a message to encrypt.")
      return
    shift_value = simpledialog.askinteger("Shift Value", "Enter a shift value for Caesar Cipher (1-25):")
    if not 1 <= shift_value <= 25:
      messagebox.showerror("Error", "Shift value must be between 1 and 25.")
      return
    encrypted_message = caesar_cipher(message, shift_value, "encrypt")
    result_text.delete(1.0, 'end')  # Clear the result text box
    result_text.insert(1.0, encrypted_message)

  def decrypt_click():
    """Decrypts the message entered in the entry widget and displays the result."""
    message = message_entry.get()
    if not message:
      messagebox.showerror("Error", "Please enter a message to decrypt.")
      return
    shift_value = simpledialog.askinteger("Shift Value", "Enter a shift value for Caesar Cipher (1-25):")
    if not 1 <= shift_value <= 25:
      messagebox.showerror("Error", "Shift value must be between 1 and 25.")
      return
    decrypted_message = caesar_cipher(message, shift_value, "decrypt")
    result_text.delete(1.0, 'end')  # Clear the result text box
    result_text.insert(1.0, decrypted_message)

  encrypt_button = Button(root, text="Encrypt", command=encrypt_click)
  encrypt_button.pack()

  decrypt_button = Button(root, text="Decrypt", command=decrypt_click)
  decrypt_button.pack()

  root.mainloop()

if __name__ == "__main__":
  main()
