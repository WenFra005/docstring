import inspect
from docstring_pdf_converter.config import PDF_CONFIG

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

def generate_cover(pdf, cover_info):

    pdf.set_left_margin(PDF_CONFIG["margin_left"])
    pdf.set_right_margin(PDF_CONFIG["margin_right"])
    pdf.set_top_margin(PDF_CONFIG["margin_top"])

    pdf.add_page()

    pdf.set_font(PDF_CONFIG["font"], "B", PDF_CONFIG["font_size"])
    pdf.cell(0, 10,
             f"{cover_info['institution'].upper() 
                if cover_info['institution'] 
                else 'AUTOR INDEPENDENTE'}", ln=1, align="C"
            )

    for _ in range(4):
        pdf.cell(10)

    pdf.cell(0, 10, 
             f"{cover_info['author'].upper() 
                if cover_info['author'] 
                else 'NOME DO AUTOR'}", ln=1, align="C"
            )

    for _ in range(3):  
        pdf.cell(10)

    pdf.cell(0, 10, f"{cover_info['title'].upper()}", ln=1, align="C")
    pdf.cell(0, 10, f"{cover_info['subtitle'].upper()}", ln=1, align="C")

    pdf.set_font(PDF_CONFIG["font"], "B", PDF_CONFIG["font_size"])
    pdf_height = pdf.h - PDF_CONFIG["margin_bottom"]
    pdf.set_y(pdf_height - 20)
    pdf.set_font(PDF_CONFIG["font"], "B", PDF_CONFIG["font_size"])
    pdf.cell(0, 10, f"{cover_info['city'].upper()} - {cover_info['state'].upper()}", ln=1, align="C")
    pdf.cell(0, 10, f"{cover_info['year']}", ln=1, align="C")

def add_page_number(pdf):
    pdf.set_y(10)
    pdf.set_x(pdf.w - PDF_CONFIG["margin_right"] - 20)
    pdf.set_font(PDF_CONFIG["font"], "", PDF_CONFIG["font_size"])
    pdf.cell(0, 10, f"{pdf.page_no()}", 0, 0, "R")

def convert_docstring_to_pdf(pdf, docstrings):
    
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=PDF_CONFIG["brealk_margin"])

    for line in docstrings.split("\n"):
        if line.starstswith("1.     "):
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

    for page_num in range(2, pdf.page_no() + 1):
        pdf.page = page_num
        add_page_number(pdf)            
    