import matplotlib.pyplot as plt
import ezdxf 
from ezdxf.addons.drawing import RenderContext, Frontend 
from ezdxf.addons.drawing.matplotlib_backend import MatplotlibBackend

doc = ezdxf.readfile(YOURFILE)
fig = plt.figure()
out = MatplotlibBackend(fig.add_axes([0, 0, 1, 1]))
Frontend(RenderContext(doc), out).draw_layout(doc.modelspace(), finalize=True)
#fig.savefig(os.path.join(temp_output_dir, outputfilebase + ".png"), dpi=300)
fig.savefig(os.path.join(temp_output_dir, outputfilebase + ".svg")) 