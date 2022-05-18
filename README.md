# RENTADRONE'S-PYTHON-ALGORITHMS
Some Python scripts that we have developed as parts of our technical services. You can use them too...

## Measure_GUI.py
This Script permits running the batch process of the [DJI Thermal SDK ](https://www.dji.com/downloads/softwares/dji-thermal-sdk) in order to convert R-JPG Thermal Images to .RAW format, maintaining the same original name of each file.
Instructions: 
1. Copy the file "Measure_GUI.py" inside the directory of the SDK in your PC, specifically in this folder: *../dji_thermal_sdk_v1.2_20211209/utility/bin/windows/release_x64/*

3. Run the script in the command line in a python environment, writing the args with theirs desired values (for details about the args, refer to the readme file in the SDK): 
  
  ```python Measure_GUI.py --measurefmt "int16" --distance "25.0" --humidity "59.0" --emissivity "0.85" --reflection "5.0"```
  
3. After running the code, a two windows will open. First select the input directory with your thermal images and, later, the output directory for the .raw files
