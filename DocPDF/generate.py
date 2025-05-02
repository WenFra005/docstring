import inspect
from fpdf import FPDF
from DocPDF.config import PDF_CONFIG

class CustomPDF(FPDF):
    def __init__(self, cover_info):
        super().__init__()
        self.cover_info = cover_info

    def header(self):
        self.set_y(10)
        self.set_font(PDF_CONFIG["font"], "B", PDF_CONFIG["font_size"])
        self.cell(0, 10, self.cover_info["title"], 0, 1, "C")
        self.set_font(PDF_CONFIG["font"], "", PDF_CONFIG["font_size"] - 2)
        self.cell(0, 10, f"Autor: {self.cover_info['author']}", 0, 1, "C")
        self.cell(0, 10, f"Local: {self.cover_info['city']} - {self.cover_info['state']} | Ano: {self.cover_info['year']}", 0, 1, "C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font(PDF_CONFIG["font"], "", PDF_CONFIG["font_size"] - 2)
        self.cell(0, 10, f"{self.page_no()}", 0, 0, "R")

def extract_docstrings(module):
    module_counter = 1
    docstrings = [f"{module_counter}. {module.__name__}\n"]  
    function_counter = 1 

    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            class_counter = function_counter 
            docstrings.append(f"{module_counter}.{class_counter} {name}\n")
            method_counter = 1
            for method_name, method in inspect.getmembers(obj, inspect.isfunction):
                docstring = inspect.getdoc(method)
                if docstring:
                    docstrings.append(f"{module_counter}.{class_counter}.{method_counter} {method_name}\n{docstring}\n")
                    method_counter += 1
            function_counter += 1
        elif inspect.isfunction(obj):
            docstring = inspect.getdoc(obj)
            if docstring:
                docstrings.append(f"{module_counter}.{function_counter} {name}\n{docstring}\n")
                function_counter += 1

    return "".join(docstrings)

def convert_docstring_to_pdf(docstrings, cover_info ,output_file):
    pdf = CustomPDF(cover_info)

    pdf.set_left_margin(PDF_CONFIG["margin_left"])
    pdf.set_top_margin(PDF_CONFIG["margin_top"])
    pdf.set_right_margin(PDF_CONFIG["margin_right"])
    pdf.set_auto_page_break(auto=True, margin=PDF_CONFIG["margin_bottom"])

    pdf.add_page()

    for line in docstrings.split("\n"):
        if line.startswith("1.     "):
            pdf.set_font(PDF_CONFIG["font"], PDF_CONFIG["title_format"]["level_1"]["style"],
                         PDF_CONFIG["title_format"]["level_1"]["size"])
        elif line.startswith("1.1   "):
            pdf.set_font(PDF_CONFIG["font"], PDF_CONFIG["title_format"]["level_2"]["style"],
                         PDF_CONFIG["title_format"]["level_2"]["size"])
        elif line.startswith("1.1.1 "):
            pdf.set_font(PDF_CONFIG["font"], PDF_CONFIG["title_format"]["level_3"]["style"],
                         PDF_CONFIG["title_format"]["level_3"]["size"])
        else:
            pdf.set_font(PDF_CONFIG["font"], "", PDF_CONFIG["font_size"])
        pdf.multi_cell(0, 10, line)

    pdf.output(f"{output_file}.pdf")

