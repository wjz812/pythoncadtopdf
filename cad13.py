import ezdxf
import svgwrite

# 读取 DXF 文件
doc = ezdxf.readfile("教堂.dxf")

# 创建 SVG 对象
dwg = svgwrite.Drawing("output13.svg", profile='tiny')

# 获取模型空间
msp = doc.modelspace()

# 遍历模型空间中的实体
for entity in msp:
    print(entity.dxftype())
    if entity.dxftype() == 'SPLINE':        
       # 处理 SPLINE 实体
        control_points = entity.fit_points()

        # 将贝塞尔曲线转换为 SVG 路径
        path_data = f"M {control_points[0][0]} {control_points[0][1]}"
        for i in range(1, len(control_points), 3):
            p1 = control_points[i]
            p2 = control_points[i+1]
            p3 = control_points[i+2]
            path_data += f" C {p1[0]} {p1[1]}, {p2[0]} {p2[1]}, {p3[0]} {p3[1]}"
        
        # 添加 SVG 路径到 SVG 对象
        dwg.add(dwg.path(d=path_data, stroke='black', fill='none'))
    else:
        # 处理其他类型的实体
        if entity.dxftype() == 'LINE':
            # 处理线段实体
            try:
                start, end = entity.dxf.start, entity.dxf.end
                #dwg.add(dwg.line(start=start, end=end, stroke='black'))
            except AttributeError:
                print('Ignoring line entity without start and end points')
        elif entity.dxftype() == 'CIRCLE':
            # 处理圆实体
            center = entity.dxf.center
            radius = entity.dxf.radius
            dwg.add(dwg.circle(center=center, r=radius, stroke='black', fill='none'))
        else:
            # 忽略不支持的实体类型
            print(f"Ignoring entity of type: {entity.dxftype()}")

# 保存 SVG 文件
dwg.save()