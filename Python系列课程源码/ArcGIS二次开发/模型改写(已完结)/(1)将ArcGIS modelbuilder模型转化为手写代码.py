# -*- coding: utf-8 -*-

'''
本代码为将ArcGIS modelbuilder模型转化为手写代码
正常情况下不一定需要对model builder建的模型进行改写，本次改写的主要目的是理解ArcGIS Python二次开发
中间数据保存到一个gdb临时文件夹中
作者：太白野老
2019年6月9日
'''

import arcpy

input_data = "C:\\Users\\wangxch\\Desktop\\经纬点.csv"
tmpFolder = "C:\\Users\\wangxch\\Desktop\\ttt\\Habitat.gdb"
print(input_data)

arcpy.MakeXYEventLayer_management(input_data, "lon", "lat", tmpFolder + "\\_Layer", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;.001;.001;IsHighPrecision", "")
print("MakeXYEventLayer_management")
arcpy.gp.Kriging_sa(tmpFolder + "\\_Layer", "序号", tmpFolder + "\\Kriging", "Spherical #", "", "VARIABLE 12", tmpFolder + "\\Output_variance_of_prediction_raster")
print("Kriging_sa")
arcpy.CheckOutExtension("Spatial")
outReclassify = arcpy.gp.Reclassify_sa(tmpFolder + "\\Kriging", "VALUE", "0.020690 2.094484 1;2.094484 3.797958 2;3.797958 5.427368 3;5.427368 6.686457 4;6.686457 7.649290 5;7.649290 8.538059 6;8.538059 9.426828 7;9.426828 10.537789 8;10.537789 11.870943 9;11.870943 13.426288 10;13.426288 14.907570 11;14.907570 16.611044 12;16.611044 18.981094 13", tmpFolder +  "\\outreclass02", "DATA")
outReclassify.save(tmpFolder +  "\\outreclass02")
print("finish")
