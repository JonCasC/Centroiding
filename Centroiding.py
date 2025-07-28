import pyopenms as oms
import os
import fnmatch
from tqdm import tqdm
import sys


def center(file_name: str)->None:
    exp = oms.MSExperiment()
    oms.MzMLFile().load(file_name, exp)
    exp.sortSpectra(True)
    exp.setMetaValue("mzML_path", file_name)
    centroided_spectra = oms.MSExperiment()
    oms.PeakPickerHiRes().pickExperiment(exp, centroided_spectra, True)
    oms.MzMLFile().store("./Centroided/" + file_name[11:-5] + "_centroided.mzML", centroided_spectra)
    del exp

if __name__ == "__main__":
    print("Looking for sepcta")
    
    mzML_files=[]
    pattern = '*.mzML'
    
    for root, dirs, files in os.walk("./Original"):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                mzML_files.append(os.path.join(root, name))
    
    print(f"{len(mzML_files)} spectra found\nBegin centroiding")
    
    for file in tqdm(mzML_files):
        center(file)
        
    print(f"Succesfully centroided {len(mzML_files)} specrta!")
    sys.exit(1)