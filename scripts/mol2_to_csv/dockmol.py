class Dockmol:
    def __init__(self, name,headers): #, atoms, bonds):
        self.name = name
        self.headers = headers
        #self.atoms = atoms
        #self.bonds = bonds 
    #getting name of molecule
    def get_name(self):
        return f"{self.name}"
    #getting all headers of molecule
    def get_headers(self):
        return f"{self.headers}"
   
    #getting all atoms of molecules
    def get_atoms():
        return f"{self.atoms}" 

#a = Dockmol("haha",{'ESOL': '4.2','LOGP': '4.5'})
#print(a.pr_name())
#print(a.pr_headers())
