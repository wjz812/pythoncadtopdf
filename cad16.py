import ezdxf
from svgwrite import Drawing

# 打开DXF文件
doc =ezdxf.readfile("教堂.dxf")

# 获取模型空间
msp = doc.modelspace()

# 创建 SVG 对象
dwg = Drawing("output16.svg", profile='tiny')

for entity in msp:
    path = entity.svg()
    dwg.add(path)

dwg.save()