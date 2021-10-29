from pygments import highlight #type:ignore
from pygments.lexers import PythonLexer #type:ignore
from pygments.formatters import HtmlFormatter #type:ignore


code:str
with open("code.py","r") as code_file:
    code = code_file.read()

with open("./output/html.html","w") as html_file:
    html_file.write(highlight(code, PythonLexer(), HtmlFormatter())) 

with open("./output/css.css","w") as css_file:
    css_file.write(HtmlFormatter().get_style_defs('.highlight'))