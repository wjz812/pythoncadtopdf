import ezdxf
import svgwrite

# 读取DXF文件
doc = ezdxf.readfile("教堂.dxf")

extmin = doc.header.get('$EXTMIN')
extmax = doc.header.get('$EXTMAX')
# print(f"DXF文件的大小为：{extmin} x {extmax} ")

width = extmax[0] - extmin[0]
height = extmax[1] - extmin[1]

# 计算 DXF 文件的大小
padding = 20
viewbox_width = width + padding * 4
viewbox_height = height + padding * 2
viewbox = f'{extmin[0]-2 * padding} {extmin[1]-padding} {viewbox_width} {viewbox_height}'

# print(f"DXF文件的大小为：{width} x {height} （单位：图坐标）")
msp = doc.modelspace()

# 创建 SVG 对象
dwg = svgwrite.Drawing("output21.svg", profile='tiny', size= (viewbox_width, viewbox_height), viewBox=viewbox,  transform=f"translate(0, {viewbox_height}) scale(1, -1)")

for entity in msp:
    if entity.dxftype() == 'SPLINE':
        control_points = entity.get_control_points()
        fit_points = entity.get_fit_points()
        degree = entity.dxf.degree
        knots = entity.get_knot_values()
        weights = entity.get_weights()

        # 创建SVG路径对象并设置属性
        path = dwg.path(fill='none', stroke='black')

        # 添加样条曲线的起始点
        start_point = control_points[0]
        path.push('M', start_point[0], start_point[1])

        # 添加样条曲线的控制点和拟合点
        for point in zip(control_points, fit_points):
                path.push('C', point[0][0], point[0][1], point[1][0], point[1][1])

        # 将样条曲线添加到SVG绘图对象中
        dwg.add(path)

        # 创建描述元素(desc)并设置文本内容为节点和权重信息
        desc = svgwrite.base.Desc(text=f"Knots: {knots}\nWeights: {weights}")
        path.desc = desc

# 将DXF文件中的所有实体转换为SVG格式并添加到SVG绘图对象中
dwg.save()
print("DXF/DWG文件已成功转换为SVG！")