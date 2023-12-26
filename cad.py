import ezdxf
import svgwrite

# 打开DXF文件
doc =ezdxf.readfile("教堂.dxf")

# 获取模型空间
msp = doc.modelspace()

#创建SVG图像
dwg = svgwrite.Drawing("output.svg", profile='tiny')

# 遍历DXF文件中的所有实体
# for entity in msp:
#     # 将实体转换成SVG路径
#     path = entity.dxftype()
#     # 将路径添加到SVG图像中
#     dwg.add(path)

# for entity in msp:
#     cmd ={
#         'LINE':'|',
#         'CIRCLE':'m',
#         'ARC':'a',
#         'POLYLINE':'|'
#     }.get(entity.dxftype())
#     if cmd is None:
#         continue
#     x, y = [float(v) for v in entity.dxf.get('start', (0, 0))]
#     x,y = [x / 100, -y / 100]
#     dwg.add(dwg.line((0, 0), (x, y), stroke=svgwrite.rgb(1, 1, 1, '%')))

dwg.add(dwg.line((68.573650919997, 798.9345598756424), (518.573650919997, 798.9345598756424), stroke=svgwrite.rgb(10, 10, 16, '%'))) 
dwg.add(dwg.text('Test', insert=(2,20), fill='red'))  
# control_points = [(210, 705), (210, 705), (210, 705), 
#     (210, 676), (210, 676), (210, 676), 
#     (210, 660), (197, 648), (182, 648), 
#     (182, 648), (166, 648), (154, 660), 
#     (154, 676)]
# path_data = "M210,705 C210,705 210,705 210,676 210,676 210,676 210,660 197,648 182,648 S182,648 166,648 154,660 154,676"
# path_data = "M100,200 C100,100 250,100 250,200 S400,300 400,200"
# path_data = "M50,50 L50,150 L200,150 L200,50 Q125,25 50,50 "
path_data = "M275 212 C285 228, Q295 238 305 248"
# path_data = f"M {control_points[0][0]} {control_points[0][1]}"
# for i in range(1, len(control_points)-2, 3):
#             # print(f"Len={len(control_points)}, i={i}")
#         p1 = control_points[i] + control_points[i-1]
#         p2 = control_points[i+1] + control_points[i]
#         p3 = control_points[i+2]
#         path_data += f" C {p1[0]} {p1[1]}, {p2[0]} {p2[1]}, {p3[0]} {p3[1]}" 
# print(path_data)   
        # 添加 SVG 路径到 SVG 对象
dwg.add(dwg.path(d=path_data, stroke='black', fill='none'))
# path_data1 = "M100,200 C100,100 250,100 250,200 S400,300 400,200"
# dwg.add(dwg.path(d=path_data1, stroke='black', fill='none'))
    

# for entity in msp:
#    if entity.dxftype() == "LINE":
#         print(entity)


#保存SVG文件
dwg.save()

# import ezdxf

# def convert_to_pdf(dwg_file_path, pdf_file_path):
#     doc = ezdxf.readfile(dwg_file_path)
#     msp = doc.modelspace()
#     doc.saveas(pdf_file_path, "pdf")

# convert_to_pdf("D:/Desktop/test/torus.dxf", "D:/Desktop/test/output.pdf")
