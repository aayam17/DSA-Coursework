import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import time
import concurrent.futures

class FileConversionApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("File Conversion App")
        self.geometry("600x400")

        # Initialize components
        self.create_widgets()
        
        self.selected_files = []
        self.executor = None
        self.futures = []

    def create_widgets(self):
        self.select_files_button = tk.Button(self, text="Select Files", command=self.select_files)
        self.select_files_button.pack(pady=10)

        self.conversion_options = ttk.Combobox(self, values=["PDF to Docx", "Image Resize"])
        self.conversion_options.pack(pady=10)

        self.start_button = tk.Button(self, text="Start Conversion", command=self.start_conversion)
        self.start_button.pack(pady=10)

        self.cancel_button = tk.Button(self, text="Cancel", command=self.cancel_conversion)
        self.cancel_button.pack(pady=10)

        self.progress_bar = ttk.Progressbar(self, length=500, mode='determinate')
        self.progress_bar.pack(pady=10)

        self.status_text = tk.Text(self, height=10, width=70)
        self.status_text.pack(pady=10)
        self.status_text.config(state=tk.DISABLED)

    def select_files(self):
        files = filedialog.askopenfilenames()
        self.selected_files = self.tk.splitlist(files)
        self.update_status(f"Selected files:\n{', '.join(self.selected_files)}")

    def update_status(self, message):
        self.status_text.config(state=tk.NORMAL)
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.config(state=tk.DISABLED)
        self.status_text.yview(tk.END)

    def conversion_task(self, file, conversion_type):
        try:
            for i in range(11):
                time.sleep(0.5)
                self.update_status(f"Processing {file}: {i * 10}% complete")
                self.progress_bar.step(10)
            self.update_status(f"Finished processing {file}")
        except Exception as e:
            self.update_status(f"Error processing {file}: {str(e)}")

    def start_conversion(self):
        if not self.selected_files:
            messagebox.showerror("Error", "No files selected!")
            return

        conversion_type = self.conversion_options.get()
        if not conversion_type:
            messagebox.showerror("Error", "No conversion type selected!")
            return

        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=len(self.selected_files))
        self.futures = [self.executor.submit(self.conversion_task, file, conversion_type) for file in self.selected_files]
        self.update_status("Conversion started...")

    def cancel_conversion(self):
        if self.executor:
            self.executor.shutdown(wait=False)
            for future in self.futures:
                future.cancel()
            self.update_status("Conversion cancelled.")

if __name__ == "__main__":
    app = FileConversionApp()
    app.mainloop()
