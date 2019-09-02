import shutil

class Zipper():
    def __init__(self, input_folder, output_name, output_extension="zip"):
        self._ifolder = input_folder
        self._oname = output_name
        self._oext = output_extension
    
    def compressFolder(self):
        try:
            shutil.make_archive(self._oname, self._oext, self._ifolder)
            print(f"Succesfully created {self._oname}.{self._oext}")
        except:
           print("Oops, something went wrong!")