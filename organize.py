##organize these laTex output.
import os

##ENTER THE DIRECTORY FOR LATEX DOCUMENTS HERE
path='/home/user/Latex Documents/'
myfiles=os.listdir(path)

##write to a python dictionary of the form {mathdoc:[mathdoc.tex, mathdoc.pdf,...]} 
##ignore it if there is no extension name to the file.

def make_dict(directory,newfiles={}):
    for file_ in directory:
        temp=file_.split('.')
        if len(temp)==1 or temp[1]=='py':
            pass
        else:
            if temp[0] not in newfiles:
                newfiles[temp[0]]=[file_]
            else:
                newfiles[temp[0]].append(file_)
    return newfiles
organized=make_dict(myfiles)
##for each elem in a dictionary, make a directory called path+mathdoc, and move
## .pdf,.tex garbage into this folder.
def organize():
    path='/home/andres/Latex Documents/'
    for texname in organized:
        name = path+texname
        os.mkdir(name)
        for texfile in organized[texname]:
            filename = path+texfile
            newname=name+'/'+texfile
            os.rename(filename, newname)
if __name__ == "__main__":
    organize()
            
