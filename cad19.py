import pyautocad
from svgwrite import Drawing

def dxf_to_svg(input_file, output_file):
    acad = pyautocad.Autocad()
    doc = acad.Application.Documents.Open(input_file)

    drawing = Drawing(output_file)

    for entity in acad.Model:
        if entity.EntityName == 'Line':
            start_point = entity.StartPoint
            end_point = entity.EndPoint
            line = drawing.add(drawing.line(start=start_point, end=end_point))
            line['stroke'] = 'black'
    drawing.save()

if __name__ == '__main__':
    input_file = '教堂.dxf'
    output_file = 'example.svg'

    dxf_to_svg(input_file, output_file)