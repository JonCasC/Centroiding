import pyopenms as oms
import os
import fnmatch
data_list=[]
pattern = '*.mzML'
for root, dirs, files in os.walk("./Original"):
    for name in files:
        if fnmatch.fnmatch(name, pattern):
            data_list.append(os.path.join(root, name))
mzML_files = data_list
mzML_files

for file in mzML_files:
    exp = oms.MSExperiment()
    oms.MzMLFile().load(file, exp)
    exp.sortSpectra(True)
    exp.setMetaValue("mzML_path", file)
    centroided_spectra = oms.MSExperiment()
    oms.PeakPickerHiRes().pickExperiment(exp, centroided_spectra, True)
    oms.MzMLFile().store("./Centroided/" + file[:-5] + "_centroided.mzML", centroided_spectra)