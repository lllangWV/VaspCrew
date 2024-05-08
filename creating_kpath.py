
from pymatgen.core import Structure
from pymatgen.io.vasp.inputs import Poscar
from pymatgen.symmetry.kpath import KPathLatimerMunro, KPathSeek

poscar=Poscar.from_str(""" Sr V O
1.0
   3.8465199999999999   0.0000000000000000   0.0000000000000000
   0.0000000000000000   3.8465199999999999   0.0000000000000000
   0.0000000000000000   0.0000000000000000   3.8465199999999999
 Sr V O
 1 1 3
Direct
   0.0000000000000000   0.0000000000000000   0.0000000000000000
   0.5000000000000000   0.5000000000000000   0.5000000000000000
   0.5000000000000000   0.5000000000000000   0.0000000000000000
   0.5000000000000000   0.0000000000000000   0.5000000000000000
   0.0000000000000000   0.5000000000000000   0.5000000000000000
""")
structure = poscar.structure

# from pymatgen.symmetry.kpath import KPathLatimerMunro, KPathSeek
# kpath=KPathLatimerMunro(structure)

# # print(kpath.get_kpoints(line_density=10,coords_are_cartesian=False))
# kpoints=kpath.get_kpoints(line_density=10,coords_are_cartesian=False)

# for kpoint in kpoints:
    # print(kpoint)



kpath_seek=KPathSeek(structure)

kpath=kpath_seek.kpath
kpoints=kpath['kpoints']
paths=kpath['path']

kpoints_str="generate KPOINTS by seekpath\n"
kpoints_str+="50 ! Grid points\n"
kpoints_str+="Line_points\n"
kpoints_str+="reciprocal\n"
for path in paths:
    for i,kpoint_name in enumerate(path):
        if i == len(path)-1:
            break
        current_kpoint_name=path[i]
        current_kpoint=str(kpoints[current_kpoint_name]).replace('[','').replace(']','').replace(',','')
        
        next_kpoint_name=path[i+1]
        next_kpoint=str(kpoints[next_kpoint_name]).replace('[','').replace(']','').replace(',','')

        kpoints_str+= current_kpoint + f" ! {current_kpoint_name}\n"
        kpoints_str+= next_kpoint + f" ! {next_kpoint_name}\n"
        kpoints_str+="\n"

print(kpoints_str)
# print(kpath_seek.get_kpoints())