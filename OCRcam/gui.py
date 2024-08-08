import tkinter as tk
from tkinter import ttk
from .scanner import Scanner
from .ocr import OCRProcessor
from .image_processing import ImageProcessor

class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCRcam - Escaneo de Libros")
        self.root.geometry("800x600")
        
        self.scanner = Scanner()
        self.ocr_processor = OCRProcessor()
        self.image_processor = ImageProcessor()
        
        self.create_widgets()
        
    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')
        
        self.setup_tab = ttk.Frame(self.notebook)
        self.preview_tab = ttk.Frame(self.notebook)
        self.results_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.setup_tab, text="Configuración")
        self.notebook.add(self.preview_tab, text="Vista Previa")
        self.notebook.add(self.results_tab, text="Resultados")
        
        self.create_setup_tab()
        self.create_preview_tab()
        self.create_results_tab()
        
    def create_setup_tab(self):
        ttk.Label(self.setup_tab, text="Seleccione la cámara:").pack(pady=10)
        self.camera_combo = ttk.Combobox(self.setup_tab, values=self.scanner.get_camera_list())
        self.camera_combo.pack(pady=5)
        
        ttk.Label(self.setup_tab, text="Número de páginas:").pack(pady=10)
        self.pages_entry = ttk.Entry(self.setup_tab)
        self.pages_entry.pack(pady=5)
        
        ttk.Button(self.setup_tab, text="Iniciar Escaneo", command=self.start_scanning).pack(pady=20)
        
    def create_preview_tab(self):
        self.preview_canvas = tk.Canvas(self.preview_tab, width=600, height=400)
        self.preview_canvas.pack(pady=10)
        
        self.progress_bar = ttk.Progressbar(self.preview_tab, length=500, mode='determinate')
        self.progress_bar.pack(pady=10)
        
    def create_results_tab(self):
        self.results_text = tk.Text(self.results_tab, wrap=tk.WORD, width=70, height=30)
        self.results_text.pack(pady=10, padx=10, expand=True, fill='both')
        
    def start_scanning(self):
        camera_index = self.camera_combo.current()
        total_pages = int(self.pages_entry.get())
        
        self.scanner.start(camera_index, total_pages, self.update_preview, self.update_progress, self.process_page)
        
    def update_preview(self, frame):
        # Actualizar canvas con el frame
        pass
        
    def update_progress(self, value):
        self.progress_bar['value'] = value
        
    def process_page(self, image):
        processed_image = self.image_processor.process(image)
        text = self.ocr_processor.extract_text(processed_image)
        self.results_text.insert(tk.END, text + "\n\n")

def main():
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()