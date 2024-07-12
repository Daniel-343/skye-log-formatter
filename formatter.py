import tkinter as tk
from tkinter import scrolledtext
from tkinter import font

def format_text():
    content = text_field.get("1.0", tk.END)
    formatted_content = format_sentences(content)
    text_field.delete("1.0", tk.END)
    text_field.insert(tk.END, formatted_content)

def format_sentences(text):
    formatted_text = text.replace("[NEW_LINE]", "\n")
    return formatted_text

root = tk.Tk()
root.title("Skye log formatter")

custom_font = font.Font(family="Helvetica", size=12)

text_field = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=25, font=custom_font)
text_field.pack(padx=10, pady=10)

format_button = tk.Button(root, text="Format Text", command=format_text, font=custom_font)
format_button.pack(pady=10)

root.mainloop()
