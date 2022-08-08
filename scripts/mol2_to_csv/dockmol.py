class Dockmol:
    def __init__(self, name): #headers, atoms, bonds):
        self.name = name
        # self.headers = headers
        # self.atoms = atoms
        # self.bonds = bonds 

    def pr_name(self):
        return f"hello"
    # def atoms():
    #     return f"{self.atoms}" 

a = Dockmol("haha")
print(a.pr_name())
