import ezdxf

def convert_dxf_to_svg(input_file, output_file):
    doc = ezdxf.readfile(input_file)
    modelspace = doc.modelspace()

    doc.saveas(output_file)

if __name__ == '__main__':
    input_file = "教堂.dxf"
    output_file = "output15.svg"
    convert_dxf_to_svg(input_file, output_file)