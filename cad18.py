import ezdxf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

doc =ezdxf.readfile("教堂.dxf")
msp = doc.modelspace()
paper_size = (210, 297)  # A4纸尺寸
layout_name = 'Model'  # 模型空间的布局名称
fig, ax = plt.subplots()
for entity in msp:
        # 处理每个实体并绘制到 matplotlib 图形中
        # 例如，对于直线：
        if entity.dxftype() == 'LINE':
            start_point = entity.dxf.start
            end_point = entity.dxf.end
            x_values = [start_point[0], end_point[0]]
            y_values = [start_point[1], end_point[1]]
            ax.plot(x_values, y_values)
with PdfPages("output18.pdf") as pdf:
    pdf.savefig()