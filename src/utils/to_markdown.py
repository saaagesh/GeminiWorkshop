import textwrap
from IPython.display import Markdown


##
## Convert a text to markdown format
##
def to_markdown(text: str):
    text = text.replace("•", "  *")

    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))
