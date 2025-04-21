import importlib
from datetime import datetime
from fpdf import FPDF
from docstring_pdf_converter.generate import add_header, extract_docstrings, convert_docstring_to_pdf

def main():
    pdf = FPDF()

    print("Bem-vindo ao conversor de docstrings para PDF!")
    print("Por favor, preencha as informações a seguir:")

    title = input("Título do PDF: ")
    subtitle = input("Subtítulo do PDF: ")
    author = input("Autor do PDF: ")
    institution = input("Instituição/Empresa vinculado ao autor: ")
    city = input("Cidade: ")
    state = input("Estado: ")

    cover_info = {
        "title": title,
        "subtitle": subtitle,
        "author": author,
        "institution": institution,
        "city": city,
        "state": state,
        "year": datetime.now().year
    }
    pdf.add_page()
    add_header(pdf, cover_info)

    module_name = input("Nome do módulo (sem .py): ")
    module_name = importlib.import_module(module_name)
    docstrings = extract_docstrings(module_name)

    output_file = input("Nome do arquivo de saída (sem extensão): ")
    convert_docstring_to_pdf(docstrings, cover_info, output_file)

    print(f"PDF gerado com sucesso: {output_file}.pdf")

if __name__ == "__main__":
    main()
    