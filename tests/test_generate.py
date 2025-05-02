from unittest.mock import patch, MagicMock
from DocPDF.generate import extract_docstrings, convert_docstring_to_pdf

def test_extract_docstrings():
    class MockClass:
        """Mock class docstring."""
        def mock_method(self):
            """Mock method docstring."""
            pass

    def mock_function():
        """Mock function docstring."""
        pass

    mock_module = MagicMock()
    mock_module.__name__ = "mock_module"
    mock_module.MockClass = MockClass
    mock_module.mock_function = mock_function

    result = extract_docstrings(mock_module)

    expected = (
        "1. mock_module\n"
        "1.1 MockClass\n"
        "1.1.1 mock_method\nMock method docstring.\n"
        "1.2 mock_function\nMock function docstring.\n"
    )

    assert result == expected

@patch("DocPDF.generate.CustomPDF")
def test_convert_docstring_to_pdf(mock_pdf_class):
    mock_pdf_instance = MagicMock()
    mock_pdf_class.return_value = mock_pdf_instance

    docstrings = "1.   mock_module\n1.1    MockClass\n1.1.1   mock_method\nMock method docstring.\n"
    cover_info = {
        "title": "Test Title",
        "subtitle": "Test Subtitle",
        "author": "Test Author",
        "institution": "Test Institution",
        "city": "Test City",
        "state": "Test State",
        "year": 2023
    }
    output_file = "test_output"

    convert_docstring_to_pdf(docstrings, cover_info, output_file)

    mock_pdf_class.assert_called_once_with(cover_info)
    mock_pdf_instance.set_left_margin.assert_called_once_with(30)
    mock_pdf_instance.set_top_margin.assert_called_once_with(30)
    mock_pdf_instance.set_right_margin.assert_called_once_with(20)
    mock_pdf_instance.set_auto_page_break.assert_called_once_with(auto=True, margin=20)
    mock_pdf_instance.add_page.assert_called()
    mock_pdf_instance.multi_cell.assert_any_call(0, 10, "1.   mock_module")
    mock_pdf_instance.output.assert_called_once_with("test_output.pdf")