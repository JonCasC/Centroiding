import pyopenms as oms
import os
import fnmatch
mzML_files=[]
pattern = '*.mzML'
for root, dirs, files in os.walk("./Original"):
    for name in files:
        if fnmatch.fnmatch(name, pattern):
            mzML_files.append(os.path.join(root, name))

for file in mzML_files:
    exp = oms.MSExperiment()
    oms.MzMLFile().load(file, exp)
    exp.sortSpectra(True)
    exp.setMetaValue("mzML_path", file)
    centroided_spectra = oms.MSExperiment()
    oms.PeakPickerHiRes().pickExperiment(exp, centroided_spectra, True)
    oms.MzMLFile().store("./Centroided/" + file[11:-5] + "_centroided.mzML", centroided_spectra)
    del exp