import gmsh
import math
import os
import sys

gmsh.initialize()


path = os.path.dirname(os.path.abspath(__file__))
gmsh.merge(os.path.join(path, 'task2.stl'))


angle = 2

forceParametrizablePatches = True

includeBoundary = False

curveAngle = 180

gmsh.model.mesh.classifySurfaces(angle * math.pi / 180., includeBoundary,
forceParametrizablePatches,
curveAngle * math.pi / 180.)

gmsh.model.mesh.createGeometry()


s = gmsh.model.getEntities(2)
l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()

f = gmsh.model.mesh.field.add("MathEval")

gmsh.model.mesh.field.setString(f, "F", "8")
gmsh.model.mesh.field.setAsBackgroundMesh(f)

gmsh.model.mesh.generate(3)
gmsh.write('task2.msh')

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()