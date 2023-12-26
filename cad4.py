import ezdxf  
from fpdf import FPDF  
  
# 打开DXF文件  
doc = ezdxf.readfile("教堂.dxf")  
  
# 获取模型空间  
msp = doc.modelspace()  
  
# 创建一个PDF对象  
pdf = FPDF()  
  
# 遍历DXF文件中的每个实体并将其添加到PDF中  
for entity in msp:  
    # pdf.add_page()  
    # pdf.set_font("Arial", size=12)  
    pdf.set_fill_color(0, 0, 0) # 设置填充颜色为黑色  
    pdf.set_draw_color(0, 0, 0) # 设置线条颜色为黑色  
    pdf.set_line_width(2)
    # pdf.begin_shape() # 开始绘制形状  
    # for point in entity.points():  
    #     pdf.vertex(x=point[0], y=point[1]) # 添加顶点  
    # pdf.end_shape(fill=True) # 结束绘制形状并填充颜色  
  
# 保存PDF文件  
pdf.output("output.pdf")