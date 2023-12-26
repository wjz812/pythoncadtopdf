import aspose.threed as a3d

scene = a3d.Scene.from_file("教堂.dxf")
scene.save("output8.dwg")
# scene.save("Output2.html")