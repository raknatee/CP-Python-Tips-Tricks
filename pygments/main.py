from pygments import highlight #type:ignore
from pygments.lexers import PythonLexer #type:ignore
from pygments.formatters import HtmlFormatter #type:ignore
import os

code:str

for code_filename in os.listdir("./code"):
    with open(os.path.join("./code",code_filename),"r") as code_file:
        code = code_file.read()

    with open(f"./output/{code_filename}.html","w") as html_file:
        html_file.write(highlight(code, PythonLexer(), HtmlFormatter())) 

with open("./output/css.css","w") as css_file:
    css_file.write(HtmlFormatter().get_style_defs('.highlight'))