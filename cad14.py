import ezdxf
import svgwrite

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
dwg = svgwrite.Drawing("output14.svg", profile='tiny', size= (viewbox_width, viewbox_height), viewBox=viewbox,  transform=f"translate(0, {viewbox_height}) scale(1, -1)")

for entity in msp:
    # print(entity.dxf_to_svg)
    if entity.dxftype() == 'LINE':
        start = (entity.dxf.start[0], entity.dxf.start[1])
        end = (entity.dxf.end[0], entity.dxf.end[1])

        dwg.add(dwg.line(start, end, stroke=svgwrite.rgb(10, 10, 16, '%')))
        # print(f"LINE: Start={start}, End={end}")
    elif entity.dxftype() == 'SPLINE':
        control_points = entity.get_control_points()   #获取曲线控制点  
        color = 'black'
        if entity.dxf.color == 242 :
            color = 'red'
        path_data = f"M {control_points[0][0]} {control_points[0][1]}"  # 使用 "M" 指令指定起始点
        for point in control_points[1:]:
            path_data += f" L {point[0]},{point[1]}"  # 使用 "L" 指令连接其他点
        print(path_data)
        dwg.add(dwg.path(d=path_data, stroke=color, fill='none'))
        # control_points = entity.get_control_points()   #获取曲线控制点       
        # # print(f"SPLINE: Len={len(control_points)}")
        # if len(control_points) == 4:    
        #     # print(f"SPLINE: Len={len(control_points)}, Control Points={control_points}")
            
        #     color = 'black'
        #     if entity.dxf.color == 242 :
        #         color = 'red'
        #         print(f"SPLINE: Len={len(control_points)}, Control Points={control_points}")
        #     path_data = f"M {control_points[0][0]} {control_points[0][1]} C "
        #     for i in range(1, len(control_points)-2, 3):
        #         print(f"Len={len(control_points)}, i={i}")                
        #         p1 = control_points[i] + control_points[i-1]
        #         p2 = control_points[i+1] + control_points[i]
        #         p3 = control_points[i+2]
        #         path_data += f" {p1[0]} {p1[1]}, {p2[0]} {p2[1]}, {p3[0]} {p3[1]}"
            
        #     # path_data = "M {},{} ".format(control_points[0][0], control_points[0][1])  # 将起始点添加到路径数据中
        #     # path_data += "C "  # 使用贝塞尔曲线命令
        #     # for point in control_points[1:]:  # 添加剩余的控制点 
        #     #     path_data += "{},{}, ".format(point[0], point[1])
        #     # 添加 SVG 路径到 SVG 对象
        #     print(path_data)
        #     dwg.add(dwg.path(d=path_data, stroke=color, fill='none'))
        # # print(f"SPLINE: Control Points={control_points}")
dwg.save()
