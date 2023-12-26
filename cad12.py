import ezdxf
from svgwrite import Drawing

def calculate_bounding_box(entities):
    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')

    for entity in entities:
        if entity.dxftype() == "LINE":
            start = entity.dxf.start
            end = entity.dxf.end
            min_x = min(min_x, start[0], end[0])
            min_y = min(min_y, start[1], end[1])
            max_x = max(max_x, start[0], end[0])
            max_y = max(max_y, start[1], end[1])
        elif entity.dxftype() == "CIRCLE":
            center = entity.dxf.center
            radius = entity.dxf.radius
            min_x = min(min_x, center[0] - radius)
            min_y = min(min_y, center[1] - radius)
            max_x = max(max_x, center[0] + radius)
            max_y = max(max_y, center[1] + radius)

    return min_x, min_y, max_x, max_y

def dxf_to_svg(input_file, output_file):
    # 从DXF文件加载图形
    doc = ezdxf.readfile(input_file)
    modelspace = doc.modelspace()

    # 计算图形的边界框
    min_x, min_y, max_x, max_y = calculate_bounding_box(modelspace)

    # 计算图形的宽度和高度
    width = max_x - min_x
    height = max_y - min_y

    # 创建一个SVG绘图对象
    dwg = Drawing(output_file, size=(f"{width}mm", f"{height}mm"))

    # 遍历DXF中的实体，并将其添加到SVG中
    for entity in modelspace:
        path = entity.svg()
        dwg.add(path)
        if entity.dxftype() == "LINE":
            start = (entity.dxf.start[0], entity.dxf.start[1])
            end = (entity.dxf.end[0], entity.dxf.end[1])
            dwg.add(dwg.line(start, end))
        elif entity.dxftype() == "CIRCLE":
            center = (entity.dxf.center[0], entity.dxf.center[1])
            radius = entity.dxf.radius
            dwg.add(dwg.circle(center, radius))
        elif entity.dxftype() == "LWPOLYLINE":
            points = [(point[0], point[1]) for point in entity.get_points()]
            dwg.add(dwg.polyline(points))
        elif entity.dxftype() == "TEXT":
            insert = (entity.dxf.insert[0], entity.dxf.insert[1])
            text = entity.dxf.text
            dwg.add(dwg.text(text, insert))

    # 保存SVG文件
    dwg.save()

# 调用函数进行转换
dxf_to_svg("教堂.dxf", "output.svg")