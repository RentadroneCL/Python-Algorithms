import os
import argparse
import tkinter as tk
from tkinter import filedialog






def makedirs(path):
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise

def askdirectory(title = ""):
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askdirectory(title = title)

    return file_path

def _main_(args):

    measurefmt = args.measurefmt
    distance = args.distance
    humidity = args.humidity
    emissivity = args.emissivity
    reflection = args.reflection

    #print (input_path)
    #makedirs(output_path)
    input_path = askdirectory(title = "Select Input Folder") + "/"
    output_path = askdirectory(title =  "Select Output Folder") + "/"

    image_paths = []

    if os.path.isdir( r"%s" % input_path):
        for inp_file in os.listdir( r"%s" % input_path):
            image_paths += [input_path + inp_file]
    else:
        image_paths += [input_path]

    image_paths = [inp_file for inp_file in image_paths if (inp_file[-4:] in ['.jpg', '.png', '.JPEG', '.JPG'])]

    code_variable =  " --measurefmt " + measurefmt + " --distance " + distance + " --humidity " + humidity + " --emissivity " + emissivity +" --reflection " + reflection

    if image_paths == []:
        print('No image in path or directory')

    for image_path in image_paths:

        image_path = "\"" + image_path + "\""
        output_image = "\"" + output_path + image_path.split('/')[-1].split('.')[0] + ".raw \""
        os.system("dji_irp.exe -s" +  image_path + " -a measure -o " +  output_image  + code_variable)

    #print('Todo Ok')


if __name__ == '__main__':

    example = 'Example Code: python3 Measure.py --measurefmt \"float32\" --distance \"5.0\" --humidity \"80.0\" --emissivity \"1.0\" --reflection \"20.0\" '

    argparser = argparse.ArgumentParser(description='Extract Temperature DJI_THERMAL_SDK' + example)

    argparser.add_argument('-m', '--measurefmt', help='output format for temperature measurement, options = int16 or float 32 (default = "float32")', default="float32", type=str)
    argparser.add_argument('-d', '--distance', help='distance to the target argument range =[1.0, 25.0] (default = "5.0")', default="5.0", type=str)
    argparser.add_argument('-hu', '--humidity', help='relative humidity of the enviroment  argument range =[20.0, 100.0] (default = "70.0")' , default="70.0", type=str)
    argparser.add_argument('-e', '--emissivity', help='emissivity of the target  argument range =[0.10, 1.0] (default = "1.0")', default="1.0", type=str)
    argparser.add_argument('-r', '--reflection', help='reflection of the target  argument range =[-40.0, 500.0] (default = "23.0")', default="23.0", type=str)
    args = argparser.parse_args()
    _main_(args)
