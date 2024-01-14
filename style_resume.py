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
    r"""
\begin{longtable}[]{@{}
  >{\raggedright\arraybackslash}p{(\columnwidth - 10\tabcolsep) * \real{0.0550}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 10\tabcolsep) * \real{0.0700}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 10\tabcolsep) * \real{0.0800}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 10\tabcolsep) * \real{0.2800}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 10\tabcolsep) * \real{0.3450}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 10\tabcolsep) * \real{0.1700}}@{}}
\toprule\noalign{}
\endhead
\bottomrule\noalign{}
\endlastfoot
Norwalk, CT & (203)-278-1760 & toj320@gmail.com &
\href{https://thomasjamesfrancis.com}{thomasjamesfrancis.com} &
\href{https://www.linkedin.com/in/thomas-james-libiano-francis/}{LinkedIn}
& \href{https://github.com/tieje}{Github} \\
\end{longtable}
""",
    r"""
\begin{longtable}[]{@{}
  >{\centering\arraybackslash}p{0.15\textwidth}
  >{\centering\arraybackslash}p{0.15\textwidth}
  >{\centering\arraybackslash}p{0.20\textwidth}
  >{\centering\arraybackslash}p{0.20\textwidth}
  >{\centering\arraybackslash}p{0.15\textwidth}
  >{\centering\arraybackslash}p{0.15\textwidth}@{}}
\toprule\noalign{}
\centering Norwalk, CT & \centering (203)-278-1760 & \centering toj320@gmail.com &
\centering\href{https://thomasjamesfrancis.com}{thomasjamesfrancis.com} &
\centering\href{https://www.linkedin.com/in/thomas-james-libiano-francis/}{LinkedIn} &
\centering\href{https://github.com/tieje}{Github} \\
\end{longtable}
""",
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
