# -*- coding: utf-8 -*-
 
import os,shutil
Input_folder = "G:\\basedata\\qinghai\\dem"
oupPut_folder = "G:\\basedata\\qinghai\\modif"
print(Input_folder)

fileExtent = ["_dem.tif"]
 
import os
for files in os.walk(Input_folder):
    for filename in files[2]:
        for Extent in fileExtent:
            if filename.endswith(Extent):
                inputData = files[0] + "\\" + filename
                oupPutData = oupPut_folder + "\\r" + filename
                if os.path.exists(oupPut_folder) == False:
                    os.makedirs(oupPut_folder)
                shutil.copyfile(inputData,oupPutData)
                print("move %s -> %s" % (inputData,oupPutData))
            
