import ezdxf
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.figure import Figure



def dxf_to_pdf(input_file, out_file):
    doc =ezdxf.readfile(input_dxf_file)
    msp = doc.modelspace()

    fig = Figure()
    ax = fig.add_subplot(111)

    for entity in msp.query('LINE,CIRCLE,ARC,LWPOLYLINE'):
        entity.RenderContext(ax)

    pdf.pages = PdfPages(output_pdf_file)
    pdf.pages.savefig(fig)
    pdf.pages.close()

# Usage
input_dxf_file = "torus.dxf"
output_pdf_file = "output2.pdf"

dxf_to_pdf(input_dxf_file, output_pdf_file)