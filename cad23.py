# 以下代码示例演示了如何使用 Python 将 DWG 文件转换为 PDF 文档。
import aspose.cad as cad
from aspose.cad import Color

# 加载现有 DWG 文件
image = cad.Image.load("test.dwg")
# image = cad.Image.load("教堂.dxf")

# 获取图像内容的边界框
bounds = image.bounds
print(bounds, image.size, image.container, image.unit_type)

# 计算内容的大小
# content_width = bounds.max_x - bounds.min_x
# content_height = bounds.max_y - bounds.min_y

# print("内容的宽度：", content_width)
# print("内容的高度：", content_height)

# 设置输出尺寸
output_width = 595
output_height = 842

# 获取内容宽度和高度
content_width = image.width
content_height = image.height
# content_width = output_width
# content_height = output_width * image.height / image.width
print(content_width, content_height)



# 初始化并指定 CAD 选项
rasterizationOptions = cad.imageoptions.CadRasterizationOptions()
rasterizationOptions.page_width = float(content_width)
rasterizationOptions.page_height = float(content_height)
rasterizationOptions.layouts = ["Model"]
rasterizationOptions.background_color  = Color.from_argb(255, 0, 0, 0)
rasterizationOptions.draw_color  = Color.from_argb(255, 255, 255, 255)

# # 指定 PDF 选项
pdfOptions = cad.imageoptions.PdfOptions()
pdfOptions.vector_rasterization_options = rasterizationOptions

# 添加水印
# pdfOptions.user_watermark_text = "1111"

# pdfOptions.core_pdf_options = cad.imageoptions.PdfDocumentOptions()
# pdfOptions.core_pdf_options.compliance = cad.imageoptions.PdfCompliance.PDF_A1B

# 另存为 PDF
image.save("dwg-output23.pdf", pdfOptions)
# image.save("dxf-output23.pdf", pdfOptions)

