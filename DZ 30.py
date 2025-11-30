import codecs
import re


def delete_html_tags(html_file, result_file="cleaned.txt"):
    with codecs.open(html_file, "r", "utf-8") as file:
        html = file.read()
    text = re.sub(r"<[^>]*>", "", html)
    lines = text.split("\n")
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    with codecs.open(result_file, "w", "utf-8") as file:
        file.write("\n".join(cleaned_lines))


delete_html_tags("draft.html")
