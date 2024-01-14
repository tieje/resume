import os
import pyperclip

# Specify the file path
file_path = "resume.tex"

# Read the contents of the file
with open(file_path, "r") as file:
    content = file.read()

# Perform the replacements
content = content.replace(
    r"""\documentclass[
]{article}""",
    r"""\documentclass[letterpaper]{article}
\usepackage[margin=1in]{geometry} % Set 1 inch margins on all sides
\usepackage{fancyhdr} % For customizing headers and footers""",
)

content = content.replace(
    r"""\hypertarget{thomas-james-l.-francis}{%
\section{Thomas James L. Francis}\label{thomas-james-l.-francis}}""",
    r"""\hypertarget{thomas-james-l.-francis}{%
\begin{center}
\section{Thomas James L. Francis}
\end{center}
\label{thomas-james-l.-francis}}""",
)

content = content.replace(
    r">{\raggedright\arraybackslash}p{(\columnwidth - 2\tabcolsep) * \real{0.0957}}",
    r">{\raggedright\arraybackslash}p{(\columnwidth - 2\tabcolsep) * \real{0.1057}}",
)

content = content.replace(
    r">{\raggedright\arraybackslash}p{(\columnwidth - 2\tabcolsep) * \real{0.0293}}",
    r">{\raggedright\arraybackslash}p{(\columnwidth - 2\tabcolsep) * \real{0.0793}}",
)
content = content.replace(
    r">{\raggedright\arraybackslash}p{(\columnwidth - 2\tabcolsep) * \real{0.0720}}",
    r">{\raggedright\arraybackslash}p{(\columnwidth - 2\tabcolsep) * \real{0.1020}}",
)

# Write the modified content back to the file
with open(file_path, "w") as file:
    file.write(content)

pyperclip.copy(content)

print("Replacements completed successfully!")
