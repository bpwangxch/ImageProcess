# -*- coding: utf-8 -*-


import arcpy
import os

inputfolder = arcpy.GetParameterAsText(0)

def extool(csv,filename):

    # Process: Make XY Event Layer
    print("MakeXYEventLayer_management")
    arcpy.MakeXYEventLayer_management(csv, "lon", "lat", tmpfolder + "\\" + filename + "_Layer", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;.001;.001;IsHighPrecision", "")

    # Process: Kriging
    print("Kriging_sa")
    arcpy.gp.Kriging_sa(tmpfolder + "\\_Layer", "value", tmpfolder + "\\" + filename + "Kriging_2", "Spherical #", "", "VARIABLE 12", tmpfolder + "\\" + filename + "Output_variance_of_prediction_raster")

    # Process: Reclassify
    print("Reclassify_sa")
    arcpy.gp.Reclassify_sa(tmpfolder + "\\" + filename + "Output_variance_of_prediction_raster", "VALUE", "0.020690 2.094484 1;2.094484 3.797958 2;3.797958 5.427368 3;5.427368 6.686457 4;6.686457 7.649290 5;7.649290 8.538059 6;8.538059 9.426828 7;9.426828 10.537789 8;10.537789 11.870943 9;11.870943 13.426288 10;13.426288 14.907570 11;14.907570 16.611044 12;16.611044 18.981094 13", tmpfolder + "\\" + filename + "Reclass_Krig2", "DATA")

tmpfolder = arcpy.GetParameterAsText(1)
arcpy.gp.overwriteOutput=1

for files in os.walk(inputfolder):
    for filename in files[2]:
        if filename.endswith(".csv"):
            inputfile = files[0] + "\\" + filename
            extool(inputfile, filename)
print("finished")
            


