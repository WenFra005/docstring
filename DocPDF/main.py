import importlib
from datetime import datetime
from fpdf import FPDF
from docpdf.generate import extract_docstrings, convert_docstring_to_pdf, generate_cover

def main():
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

    module_name = input("Nome do módulo (sem .py): ")
    module = importlib.import_module(module_name)
    docstrings = extract_docstrings(module)

    output_file = input("Nome do arquivo de saída (sem extensão): ")
    convert_docstring_to_pdf(docstrings, cover_info, output_file)

    print(f"PDF gerado com sucesso: {output_file}.pdf")

if __name__ == "__main__":
    main()
