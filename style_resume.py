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
  >{\raggedright\arraybackslash}p{(\columnwidth - 8\tabcolsep) * \real{0.0663}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 8\tabcolsep) * \real{0.0843}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 8\tabcolsep) * \real{0.0964}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 8\tabcolsep) * \real{0.3373}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 8\tabcolsep) * \real{0.4157}}@{}}
\toprule\noalign{}
\endhead
\bottomrule\noalign{}
\endlastfoot
Norwalk, CT & (203)-278-1760 & toj320@gmail.com &
\href{https://thomasjamesfrancis.com}{thomasjamesfrancis.com} &
\href{https://www.linkedin.com/in/thomas-james-libiano-francis/}{LinkedIn} \\
\end{longtable}
""",
    r"""
\begin{longtable}[]{@{}
  >{\centering\arraybackslash}p{0.2\textwidth}
  >{\centering\arraybackslash}p{0.2\textwidth}
  >{\centering\arraybackslash}p{0.2\textwidth}
  >{\centering\arraybackslash}p{0.2\textwidth}
  >{\centering\arraybackslash}p{0.2\textwidth}@{}}
\toprule\noalign{}
\centering Norwalk, CT & \centering (203)-278-1760 & \centering toj320@gmail.com &
\centering\href{https://thomasjamesfrancis.com}{thomasjamesfrancis.com} &
\centering\href{https://www.linkedin.com/in/thomas-james-libiano-francis/}{LinkedIn} \\
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
