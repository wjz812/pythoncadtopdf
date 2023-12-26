from ezdxf.addons import odafc

# dwg = odafc.readfile("input_file.dxf")

odafc.convert('input.dwg', 'out.dxf', version='R2018', replace=True)