import subprocess

# ODAFileConverter 可执行文件路径
oda_file_converter_exe = r'C:/Program Files/ODA/ODAFileConverter 24.11.0/ODAFileConverter.exe'

# 待转换的 DWG 文件路径
input_dwg_file = "test.dwg"

# 输出的 PDF 文件路径
output_pdf_file = "output5.pdf"

# 构建调用命令
cmd = [oda_file_converter_exe, '-pdf', '-plot', '-drawlayout', input_dwg_file, '-o', output_pdf_file]

# 调用 ODAFileConverter 进行格式转换
subprocess.run(cmd)