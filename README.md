# Blender2Front
The overall scene synthesis dataset is not compatible with the popular 3D graphics program such as blender. 
This repository contains code to convert .blend files to .json files for use with 3D-FRONT.
<H2>
  Installation
</H2>
Our code requires the following dependencies.

+ Blender 4.0
+ pyyaml
+ json
+ numpy

<H2>
  Executing the program
</H2>
<H3>
  convert a Blender File to a Front File
</H3>
Our program consists of both Blender and Python scripts. The Blender script extracts information from 3D scenes (`blender_script.txt`), generating several files that contain data about meshes, furniture, extensions, scenes.
The python script(`blender_to_front.py`) then generates a .json file according to the 3D-FRONT specifications.

To use the program:
1. First, run the Blender script to generate .txt files containing scene information
2. Then, execute the Python script. When running the Python script, make sure to specify the paths to the Blender output files in the Python project's config file.

+ Blender script
  
  You can run the Blender script by copying the code into the scripting tab within the Blender program and executing it, or by following the appropriate method for running Blender scripts.

+ Python script
  
  When running the Python script to convert Blender files to 3D-FRONT files, you need to pass the config file path as an argument:
  ```
  python blender_to_front.py --config_file CONFIG_FILE_PATH
  ```
<H3>
  Update the model_info file
</H3>  
Scene synthesis models based on ATISS use a `model_info.json` file, which contains information about furnitures, such as model ID, category, style, theme, material, and more.
Manually updating the model info each time new scene data is added is inefficient, so we provide a script to automate this process.


+ Python script
  
  To update the `model_info.json`, run the provided Python script, passing the config file path as an argument:
  ```
  python update_model_info.py --config_file CONFIG_FILE_PATH
  ```
