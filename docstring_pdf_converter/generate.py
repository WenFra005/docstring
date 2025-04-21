import inspect
from fpdf import FPDF
from docstring_pdf_converter.config import PDF_CONFIG

class CustomPDF(FPDF):
    def __init__(self, cover_info):
        super().__init__()
        self.cover_info = cover_info

    def header(self):
        self.set_font(PDF_CONFIG["font"], "B", PDF_CONFIG["font_size"])
        self.cell(0, 10, self.cover_info["title"], 0, 1, "C")
        self.set_font(PDF_CONFIG["font"], "", PDF_CONFIG["font_size"] - 2)
        self.cell(0, 10, f"Autor: {self.cover_info['author']} | Instituição: {self.cover_info}", 0, 1, "C")
        self.cell(0, 10, f"Local: {self.cover_info['city']} - {self.cover_info['state']} | Ano: {self.cover_info['year']}", 0, 1, "C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font(PDF_CONFIG["font"], "", PDF_CONFIG["font_size"] - 2)
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

def extract_docstrings(module):
    module_counter = 1
    docstrings = [f"{module_counter}.   {module.__name__}\n"]
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            class_counter = 1
            docstrings.append(f"{module_counter}.{class_counter}    {name}\n")
            for method_name, method in inspect.getmembers(obj, inspect.isfunction):
                method_counter = 1
                docstring = inspect.getdoc(method)
                if docstring:
                    docstrings.append(f"{module_counter}.{class_counter}.{method_counter}   "
                                      f"{method_name}\n{docstring}\n")
                    method_counter += 1
            class_counter +=1
        elif inspect.isfunction(obj):
            function_counter = 1
            docstring = inspect.getdoc(obj)
            if docstring:
                docstrings.append(f"{module_counter}.{function_counter}     {name}\n{docstring}\n")
                function_counter += 1
    return "\n".join(docstrings)

def add_header(pdf, cover_info):
    pdf.set_y(PDF_CONFIG["margin_top"])
    pdf.set_font(PDF_CONFIG["font"], "B", PDF_CONFIG["font_size"])

    pdf.cell(0, 10, f"Autor: {cover_info['author']}", ln=0, align="L")
    pdf.set_x(pdf.w - PDF_CONFIG["margin_right"] - 100)
    pdf.cell(0, 10, f"Instituição: {cover_info['institution']}", ln=1, align="R")

    pdf.cell(0, 10, f"Local: {cover_info['city']} - {cover_info['state']}", ln=0, align="L")
    pdf.set_x(pdf.w - PDF_CONFIG["margin_right"] - 100)
    pdf.cell(0, 10, f"Ano: {cover_info['year']}", ln=1, align="R")

def add_page_number(pdf):
    pdf.set_y(10)
    pdf.set_x(pdf.w - PDF_CONFIG["margin_right"] - 20)
    pdf.set_font(PDF_CONFIG["font"], "", PDF_CONFIG["font_size"])
    pdf.cell(0, 10, f"{pdf.page_no()}", 0, 0, "R")

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

    