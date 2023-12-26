import ezdxf
import matplotlib.pyplot as plt

def dwg_to_pdf_with_matplotlib(dwg_file, pdf_file):
    doc = ezdxf.readfile(dwg_file)
    modelspace = doc.modelspace()
    fig, ax = plt.subplots()

    for entity in modelspace:
        # 处理实体并将其绘制到 matplotlib 图形中
        ax.add_entity(entity)

    plt.savefig(pdf_file)
    plt.close()

# 读取 DWG 文件并转换为 PDF（使用 matplotlib）
dwg_to_pdf_with_matplotlib("教堂.dxf", "output20.pdf")