import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3

def open_pdf_with_file_explorer():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.geometry("400x300")  # Set width=400 and height=300

    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    while file_path:
        pdfFileObj = open(file_path, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        page_count = len(pdfReader.pages)
        input_page = 0
        
        while True:
            input_page = int(input(f"Enter the page number (0 to {page_count - 1}) from the selected PDF: "))
            
            if 0 <= input_page < page_count:
                break
            else:
                print(f"Invalid page number. Please enter a number between 0 and {page_count - 1}.")
        
        pagObj = pdfReader.pages[input_page]
        extracted_text = pagObj.extract_text()
        print("Text from selected page:")
        print(extracted_text)
        
        # Initialize text-to-speech engine
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')  # Get available voices
        # Set the voice to the desired one (you can change '0' to another index if you want a different voice)
        engine.setProperty('voice', voices[1].id)
        engine.say(extracted_text)
        engine.runAndWait()
        
    else:
        messagebox.showinfo("Info", "No file selected.")

if __name__ == "__main__":
    open_pdf_with_file_explorer()
