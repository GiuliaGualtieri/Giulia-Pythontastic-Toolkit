import fitz
import urllib3


def pdf_to_images(pdf_file: str) -> str:
    """
    Convert a PDF file to a series of PNG images.

    This function takes a PDF file, opens it using PyMuPDF (fitz), and converts each page
    into a PNG image. The resulting image filenames are in the format "pageX.png", where
    X is the page number.

    Parameters:
        pdf_file (str): The path to the PDF file.

    Returns:
        str: The filename of the first generated PNG image.

    Note:
        The function only returns the filename of the first page's image.
        The images are saved in the current working directory.
    """
    doc = fitz.open(pdf_file)
    for p in doc:
        pix = p.get_pixmap()
        output = f"page{p.number}.png"
        pix.writePNG(output)
        return output


def get_response(url: str) -> tuple:
    """
    Get the HTTP response status code and data from a URL.

    This function performs an HTTP GET request to the specified URL using the urllib3
    library and returns a tuple containing the response status code and data.

    Parameters:
        url (str): The URL to send the GET request to.

    Returns:
        tuple: A tuple containing the response status code (int) and the response data (bytes).
    """
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    return response.status, response.data
