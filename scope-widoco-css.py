import os
import re
import sys

lessc_installed = os.system("lessc --version > /dev/null")
if lessc_installed != 0:
    sys.exit("lessc is not installed! Install with 'npm i -g less' and try again!")

print()
css_files = os.listdir("./public/resources")
css_files = list(filter(lambda _file: re.search("\\.css$", _file), css_files))


def scope_css_file(file_path):
    print("\tCreating scoped .less file... ", end='')
    less_content = None
    with open(file_path, "r") as _css:
        css_content = _css.read()
        old_lines = css_content.split("\n")
        lines = []
        lines.append(".widoco {")
        for line in old_lines:
            lines.append("    "+line)
        lines.append("}")
        less_content = "\n".join(lines)
    new_file_path = file_path.replace(".css", ".less")
    with open(new_file_path, "w") as less_file:
        less_file.write(less_content)
    print("Done!\n\tRe-compiling .css file... ", end='')
    os.system("lessc %s %s" % (new_file_path, file_path))
    print("Done!\n\tRemoving .less file... ", end='')
    os.remove(new_file_path)
    print("Done!")


for _file in css_files:
    file_path = os.path.join("./public/resources", _file)
    print("Scoping %s... " % file_path)
    scope_css_file(file_path)
    print("Done!")
