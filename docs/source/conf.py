project = "sphinx-demo"
copyright = "2020, Dmitriy Ponomar"
author = "Dmitriy Ponomar"

release = "1.0.0"

extensions = ["rst2pdf.pdfbuilder"]

templates_path = ["_templates"]

exclude_patterns = []

html_theme = "alabaster"

html_static_path = ["_static"]

pdf_documents = [
    ("index", u"sphinx-demo", u"Sphinx demo project", u"Dmitriy Ponomar"),
]
