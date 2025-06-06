import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import pikepdf

def merge_pdfs():
    files = filedialog.askopenfilenames(title="Select PDFs to Merge", filetypes=[("PDF Files", "*.pdf")])
    if not files:
        return
    merger = PdfMerger()
    for file in files:
        merger.append(file)
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Save Merged PDF")
    if save_path:
        merger.write(save_path)
        merger.close()
        messagebox.showinfo("Success", "PDFs merged successfully!")

def split_pdf():
    file = filedialog.askopenfilename(title="Select PDF to Split", filetypes=[("PDF Files", "*.pdf")])
    if not file:
        return
    reader = PdfReader(file)
    total_pages = len(reader.pages)

    start = simple_input("Start Page (1-based index):")
    end = simple_input("End Page:")

    if not start or not end:
        messagebox.showerror("Error", "Page numbers required!")
        return

    try:
        start_page = int(start)
        end_page = int(end)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
        return

    if start_page < 1 or end_page > total_pages or start_page > end_page:
        messagebox.showerror("Error", "Invalid page range!")
        return

    writer = PdfWriter()
    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])

    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Save Split PDF")
    if save_path:
        with open(save_path, 'wb') as f:
            writer.write(f)
        messagebox.showinfo("Success", "PDF split successfully!")

def compress_pdf():
    file = filedialog.askopenfilename(title="Select PDF to Compress", filetypes=[("PDF Files", "*.pdf")])
    if not file:
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Save Compressed PDF")
    if save_path:
        try:
            pdf = pikepdf.open(file)
            pdf.save(save_path, optimize_pdf=True, compression=pikepdf.CompressionLevel.default)
            pdf.close()
            messagebox.showinfo("Success", "PDF compressed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Compression failed: {e}")

def simple_input(prompt_text):
    popup = tk.Toplevel(root)
    popup.title("Input Required")
    popup.geometry("300x100")
    tk.Label(popup, text=prompt_text).pack(padx=10, pady=5)
    entry = tk.Entry(popup)
    entry.pack(pady=5)
    result = []

    def submit():
        result.append(entry.get())
        popup.destroy()

    tk.Button(popup, text="Submit", command=submit).pack(pady=5)
    popup.grab_set()
    root.wait_window(popup)
    return result[0] if result else None

# GUI Setup
root = tk.Tk()
root.title("PDF Tools by TechYatri")
root.geometry("320x320")

tk.Label(root, text="📄 PDF Tools", font=("Arial", 18)).pack(pady=15)
tk.Button(root, text="Merge PDFs", width=30, command=merge_pdfs).pack(pady=10)
tk.Button(root, text="Split PDF", width=30, command=split_pdf).pack(pady=10)
tk.Button(root, text="Compress PDF", width=30, command=compress_pdf).pack(pady=10)

tk.Label(root, text="Made with ❤️ by TechYatri", font=("Arial", 10)).pack(side="bottom", pady=15)

root.mainloop()
