from bs4 import BeautifulSoup


class CssScanner:
    def __init__(self):
        self.document_format = "html"

    # Scan an HTML document for all it's used CSS classes
    def scan_html(self, document_path):
        print(f"Scanning {document_path} for CSS...")

    # Scan an .erb (Ruby on Rails template/view) document for all it's used CSS classes
    def scan_erb(self, document_path):
        print(f"Scanning {document_path} for CSS...")