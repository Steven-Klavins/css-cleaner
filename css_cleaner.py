import os


class CssCleaner:
    def __init__(self, project_path, templating_engine, css_processor="css"):
        self.project_path = project_path
        self.templating_engine = templating_engine
        self.css_processor = css_processor

    # Scan an HTML document for all it's used CSS classes
    def gather_css(self):
        print(f"Gathering {self.css_processor} documents...")
