import ezdxf
from PIL import Image

def dxf_to_png(input_file, output_file):
    # 加载DXF文件
    doc = ezdxf.readfile(input_file)
    msp = doc.modelspace()

    # 计算输出图像的大小（以像素为单位）
    width = int(msp.limits[1][0] - msp.limits[0][0])
    height = int(msp.limits[1][1] - msp.limits[0][1])

    # 创建输出图像
    image = Image.new('RGBA', (width, height), (255, 255, 255, 0))

    # 将DXF文件中的所有实体直接写入PNG文件
    for entity in msp:
        entity_image = entity.get_raster_image()
        if entity_image:
            position = (
                int(entity.dxf.insert[0] - msp.limits[0][0]),
                int(height - (entity.dxf.insert[1] - msp.limits[0][1] + entity.dxf.height))
            )
            image.paste(entity_image, position)

    # 保存PNG文件
    image.save(output_file, 'PNG')
    print("DXF/DWG文件已成功转换为PNG！")

# 调用函数将DXF文件转换为PNG
dxf_to_png("教堂.dxf", "output22.png")