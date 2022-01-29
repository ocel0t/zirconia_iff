# zirconia_iff
Heinz team, Boulder CO, USA, 2021-2022

# iff_bonds_NTM.py
The iff_bonds_NTM.py script generates missing quadratic bonded term entries.

Input (file): user defined filename+extension with the missing bonded terms. 

Example input file (from Materials Studio error output):
'''
Error: Energy expression: cannot find parameters for torsion: O8(ozr1)-Zr4(zr2)-O3(ozr7)-Zr3(zr4)
Error: Energy expression: cannot find parameters for torsion: O3(ozr7)-Zr4(zr2)-O8(ozr1)-Zr1(zr1)
Error: Energy expression: cannot find parameters for torsion: O3(ozr7)-Zr4(zr2)-O8(ozr1)-Zr3(zr4)
'''

Input (data): user defined version, reference and bond constant)
Output: bonded terms on the screen.

Usage: execute iff_bonds_NTM.py and follow screen instructions.

# iff_dihedrals_NTM.py

The iff_dihedrals_NTM.py script generates missing dihedral term entries.

Input (file): user defined filename+extension with the missing dihedral terms 

Example input file (from Materials Studio error output):
'''
Error: Energy expression: cannot find parameters for torsion: O8(ozr1)-Zr4(zr2)-O3(ozr7)-Zr3(zr4)
Error: Energy expression: cannot find parameters for torsion: O3(ozr7)-Zr4(zr2)-O8(ozr1)-Zr1(zr1)
Error: Energy expression: cannot find parameters for torsion: O3(ozr7)-Zr4(zr2)-O8(ozr1)-Zr3(zr4)
'''

Input (data): user defined version, reference, but dihedral parameters are all set to 0.

Output: bonded terms on the screen.

Usage: execute iff_dihedrals_NTM.py and follow screen instructions.
