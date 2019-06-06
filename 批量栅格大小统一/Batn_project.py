# -*- coding: utf-8 -*-

import arcpy
import os

Input_folder = "H:\\Original\\qhnu\\zx20170318\\MAP"
fileExtent = [".shp",".tif",".tiff",".img"]


for files in os.walk(Input_folder):
    for filename in files[2]:
        for Extent in fileExtent:
            if filename.endswith(Extent):
                inputData = files[0] + "\\" + filename
                oupPutData = files[0].replace("zx20170318","modif") + "\\r" + filename
                print inputData,oupPutData
                if os.path.exists(files[0].replace("zx20170318","modif")) == False:
                    os.mkdir(files[0].replace("zx20170318","modif"))
                if Extent == ".shp":
                    arcpy.Project_management(inputData, oupPutData, "PROJCS['WGS_1984_Albers',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',4000000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',96.5],PARAMETER['Standard_Parallel_1',34.0],PARAMETER['Standard_Parallel_2',37.0],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "", "PROJCS['WGS_1984_Albers',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',4000000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',105.0],PARAMETER['Standard_Parallel_1',25.0],PARAMETER['Standard_Parallel_2',47.0],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")
                else:
                    arcpy.ProjectRaster_management(inputData, oupPutData, "PROJCS['WGS_1984_Albers',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',4000000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',96.5],PARAMETER['Standard_Parallel_1',34.0],PARAMETER['Standard_Parallel_2',37.0],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "NEAREST", "1000 1000", "", "", "PROJCS['Albers_Conical_Equal_Area',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['false_easting',4000000.0],PARAMETER['false_northing',0.0],PARAMETER['central_meridian',105.0],PARAMETER['standard_parallel_1',25.0],PARAMETER['standard_parallel_2',47.0],PARAMETER['latitude_of_origin',0.0],UNIT['Meter',1.0]]")
