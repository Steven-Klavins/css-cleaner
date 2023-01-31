import os


class CssCleaner:
    def __init__(self, project_path, templating_engine="html", css_processor="css"):
        self.project_path = project_path
        self.templating_engine = templating_engine
        self.css_processor = css_processor

    # Scan for and gather all CSS/SASS/SCSS document paths.
    def gather_css_document_paths(self):
        print(f"Gathering .{self.css_processor} documents...")

    # Scan for and gather all HTML/.erb document paths.
    def gather_html_template_paths(self):
        print(f"Gathering all .{self.templating_engine} documents...")

    def merge_document(self, document):
        pass

    def run(self):
        print("CSS Cleaner has begun...")
        self.gather_css_document_paths()
        self.gather_html_template_paths()

