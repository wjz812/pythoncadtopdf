import ezdxf
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import *
from reportlab.lib.pagesizes import letter

def dxf_to_pdf(input_file, output_file):
    # 加载DXF文件
    doc = ezdxf.readfile(input_file)
    msp = doc.modelspace()

    # 创建PDF绘图对象
    drawing = Drawing(0, 0, *letter)

    group = Group()

    # 将DXF文件中的所有样条实体直接写入PDF文件
    for entity in msp:
        if entity.dxftype() == 'SPLINE':
            control_points = entity.get_control_points()
            fit_points = entity.get_fit_points()
            degree = entity.dxf.degree
            knots = entity.get_knot_values()
            weights = entity.get_weights()

            # 创建PDF路径对象并设置属性
            path = Path()
            path.moveTo(*control_points[0])
            for point in zip(control_points, fit_points):
                path.curveTo(*point)

            # 添加样条曲线到PDF绘图对象中
            group.add(path)

            # 添加描述文本到PDF绘图对象中
            text = f"Knots: {knots}\nWeights: {weights}"
            string = String(10, 10, text)
            group.add(string)
    drawing.add(group)

    # 将PDF绘图对象保存为PDF文件
    renderPDF.drawToFile(drawing, output_file)
    print("DXF/DWG文件中的SPLINE已成功转换为PDF！")

# 调用函数将DXF文件转换为PDF
dxf_to_pdf("教堂.dxf", "output17.pdf")