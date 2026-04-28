import pyopenms as oms
import os
from tqdm import tqdm
import sys


def center(file_name: str, output_dir: str)->None:
    """Centroid the given mzML file.

    Args:
        file_name (str): The path to the .mzML file to centroid.
        output_dir (str): The directory to save centroided files to.
    """
    exp = oms.MSExperiment()
    oms.MzMLFile().load(file_name, exp)
    exp.sortSpectra(True)
    exp.setMetaValue("mzML_path", file_name)
    centroided_spectra = oms.MSExperiment()
    
    oms.PeakPickerHiRes().pickExperiment(exp, centroided_spectra, True)
    base_name = os.path.splitext(os.path.basename(file_name))[0]
    
    output_path = os.path.join(output_dir, f"{base_name}_centroided.mzML")
    oms.MzMLFile().store(output_path, centroided_spectra)
    del exp

if __name__ == "__main__":
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define paths relative to the script location
    original_dir = os.path.join(script_dir, "Original")
    centroided_dir = os.path.join(script_dir, "Centroided")
    
    os.makedirs(centroided_dir, exist_ok=True)
    print("Looking for spectra")
    
    mzML_files = []
    
    for root, dirs, files in os.walk(original_dir):
        for name in files:
            if os.path.splitext(name)[1].lower() == '.mzml':
                mzML_files.append(os.path.join(root, name))
    
    print(f"{len(mzML_files)} spectra found\nBegin centroiding")
    
    for file in tqdm(mzML_files):
        center(file, centroided_dir)
        
    print(f"Successfully centroided {len(mzML_files)} spectra!")
    sys.exit(0)