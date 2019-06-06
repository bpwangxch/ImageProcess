# -*- coding:cp936 -*-
import arcpy
from arcpy import env
import ConversionUtils
import os
import sys
import shutil
import time

'''
批量栅格数据大小统一
批量处理影像四角灰度值也统一
author：wangxch
2017年1月1日
'''



def readjiehebiao():
    fname = "%s\\rs\\jiehebiao\\extent.txt" % rsfolder
    satellite_name = ((input_raster.split("\\"))[-1]).split("_")[0]
    latlon = ((input_raster.split("\\"))[-1]).split("_")[1]
    f = open(fname,"r")
    lines_list = f.readlines()
    for i in xrange(len(lines_list)):
        if ((lines_list[i].split("\n"))[0]).split("_")[0] == satellite_name and ((lines_list[i].split("\n"))[0]).split("_")[1] == latlon:
            filename = (lines_list[i].split("\n"))[0]
            extent_all = (lines_list[i+1].split("\n"))[0]
            #f.write("%s %s %s %s\n" % ((extent.lowerRight),(extent.lowerRight),(extent.upperLeft),(extent.upperRight)))
            print "lowerLeft",extent_all.split(" ")[0],extent_all.split(" ")[1]
            print "lowerRight",extent_all.split(" ")[4],extent_all.split(" ")[5]
            print "upperLeft",extent_all.split(" ")[8],extent_all.split(" ")[9]
            print "upperRight",extent_all.split(" ")[12],extent_all.split(" ")[13]
            print filename
    try:
        print extent_all
        return extent_all.split(" ")[0],extent_all.split(" ")[1],extent_all.split(" ")[4],extent_all.split(" ")[5],extent_all.split(" ")[8],extent_all.split(" ")[9],extent_all.split(" ")[12],extent_all.split(" ")[13]
    except:
        arcpy.AddMessage("影像范围不在结合表内，请检查结合表和影像范围")
if __name__=="__main__":
    
    script_path = sys.path[0]
    input_raster = ConversionUtils.gp.GetParameterAsText(0)
    
    ##input_raster = "C:\\Users\\Administrator\\Desktop\\test\\rs\\data\\ZY3_038132_20160315_023226_17_M.TIF"
    elevSTDResult = arcpy.GetRasterProperties_management(input_raster,"BOTTOM")
    BOTTOM = elevSTDResult.getOutput(0)
    print BOTTOM
    elevSTDResult = arcpy.GetRasterProperties_management(input_raster,"RIGHT")
    RIGHT = elevSTDResult.getOutput(0)
    print RIGHT
    elevSTDResult = arcpy.GetRasterProperties_management(input_raster,"LEFT")
    LEFT = elevSTDResult.getOutput(0)
    print LEFT
    elevSTDResult = arcpy.GetRasterProperties_management(input_raster,"TOP")
    TOP = elevSTDResult.getOutput(0)
    print TOP
    elevSTDResult = arcpy.GetRasterProperties_management(input_raster,"CELLSIZEX")
    CELLSIZEX = elevSTDResult.getOutput(0)
    print CELLSIZEX
    elevSTDResult = arcpy.GetRasterProperties_management(input_raster,"CELLSIZEY")
    CELLSIZEY = elevSTDResult.getOutput(0)
    print CELLSIZEY
    elevSTDResult = arcpy.GetRasterProperties_management(input_raster,"COLUMNCOUNT")
    COLUMNCOUNT = elevSTDResult.getOutput(0)
    print COLUMNCOUNT  #列
    elevSTDResult = arcpy.GetRasterProperties_management(input_raster,"ROWCOUNT")
    ROWCOUNT = elevSTDResult.getOutput(0)
    print ROWCOUNT  #行
    elevSTDResult = arcpy.GetRasterProperties_management(input_raster,"BANDCOUNT")
    MultiBandNum = elevSTDResult.getOutput(0)
    print MultiBandNum  #波段数
    
    xml_filepath = "\\".join(input_raster.split("\\")[:-1]) + "\\" + (input_raster.split("\\")[-1])+".xml"
    print script_path
    env.workspace = script_path
    rsfolder = "\\".join((env.workspace.split("\\"))[:-1])
    print rsfolder
    result_savefolder = "\\".join(input_raster.split("\\")[:-1])

    #########################2016-05-09 modify begin######################################

    #新修改内容：多个参数直接从xml获取
    arcpy.AddMessage(script_path+"\\rs\\ZY303313720150216Y.XML")
    f = open(rsfolder+"\\rs\\ZY303313720150216Y.XML","r")
    num = 0
    for tmp in f.readlines():
        num = num + 1
        if num==4:
            ProductName = (tmp.split("\n")[0]).split(">")[1]
            print (tmp.split("\n")[0]).split(">")[1]
        if num==6:
            Owner = tmp.split("\n")[0].split(">")[1]
            print tmp.split("\n")[0].split(">")[1]
        if num==8:
            Producer = (tmp.split("\n")[0].split(">")[1]).split("<")[0]
            print (tmp.split("\n")[0].split(">")[1]).split("<")[0]
        if num==9:
            Publisher = tmp.split("\n")[0].split(">")[1]
            print tmp.split("\n")[0].split(">")[1]
        if num==12:
            print tmp.split("\n")[0].split(">")[1].split("<")[0]
        if num==29:
            LongerRadius = tmp.split("\n")[0].split(">")[1]
            print tmp.split("\n")[0].split(">")[1]
        if num==31:
            OblatusRatio = tmp.split("\n")[0].split(">")[1]
            print tmp.split("\n")[0].split(">")[1]
        if num==33:
            GeodeticDatum = tmp.split("\n")[0].split(">")[1]
            print tmp.split("\n")[0].split(">")[1]
        if num==35:
            MapProjection = tmp.split("\n")[0].split(">")[1]
            print tmp.split("\n")[0].split(">")[1]
        if num==41:
            CoordinationUnit = tmp.split("\n")[0].split(">")[1]
            print tmp.split("\n")[0].split(">")[1]
        if num==43:
            HeightSystem = tmp.split("\n")[0].split(">")[1]
            print tmp.split("\n")[0].split(">")[1]
        if num==45:
            HeightDatum = tmp.split("\n")[0].split(">")[1]
            print tmp.split("\n")[0].split(">")[1]
        if num==82:
            ManufactureType = (tmp.split("\n")[0].split(">")[1]).split("<")[0]
            print (tmp.split("\n")[0].split(">")[1]).split("<")[0]
        if num==85:
            OrthoRectifySoftWare = (tmp.split("\n")[0].split(">")[1]).split("<")[0]
            print (tmp.split("\n")[0].split(">")[1]).split("<")[0]
        if num==86:
            ResampleMethod = (tmp.split("\n")[0].split(">")[1]).split("<")[0]
            print (tmp.split("\n")[0].split(">")[1]).split("<")[0]
        if num==109:
            InstituteCheckUnit = (tmp.split("\n")[0].split(">")[1]).split("<")[0]
            print (tmp.split("\n")[0].split(">")[1]).split("<")[0]
        if num==113:
            BureauCheckUnit = (tmp.split("\n")[0].split(">")[1]).split("<")[0]
            print (tmp.split("\n")[0].split(">")[1]).split("<")[0]
    
    #########################2016-05-31 modify end######################################
    coordinate_ = readjiehebiao()
    #解析四角坐标
    
    #print "lowerLeft",extent_all.split(" ")[0],extent_all.split(" ")[1]
    #print "lowerRight",extent_all.split(" ")[4],extent_all.split(" ")[5]
    #print "upperLeft",extent_all.split(" ")[8],extent_all.split(" ")[9]
    #print "upperRight",extent_all.split(" ")[12],extent_all.split(" ")[13]
    #东南西北east South west north
    SouthWestOrd = coordinate_[2]  #
    SouthWestAbs = coordinate_[3]
    NorthWestOrd = coordinate_[4]
    NorthWestAbs = coordinate_[5]
    NorthEastOrd = coordinate_[6]
    NorthEastAbs = coordinate_[7]
    SouthEastOrd = coordinate_[0]
    SouthEastAbs = coordinate_[1]

    #四角坐标计算完毕，开始基本参数的录入
    
    #创建临时文件夹，如果存在则不创建，直接使用
    if os.path.exists(env.workspace + "\\tmp") == False:
        os.mkdir(env.workspace + "\\tmp")
    shutil.copy(rsfolder + "\\rs\\GF2_odl_M.MDB",env.workspace + "\\tmp")
    new_file_name = input_raster.split("\\")[-1]
    os.rename(env.workspace + "\\tmp\\GF2_odl_M.MDB", env.workspace + "\\tmp\\%s.MDB" % new_file_name[:-4])

    newtable_name = str((new_file_name[:-4]).split("_")[1] + "_" + (new_file_name[:-4]).split("_")[-3])
    print new_file_name[:-4],type(newtable_name),newtable_name
    print env.workspace + "\\tmp\\%s.MDB\\010123_E0893N358" % new_file_name[:-4]
    print env.workspace + "\\tmp\\%s.MDB\\010123_E0893N358" % new_file_name[:-4],
    print env.workspace + "\\tmp\\%s.MDB\\%s" % (new_file_name[:-4],newtable_name)
##    arcpy.Rename_management(env.workspace + "\\tmp\\%s.MDB\\010123_E0893N358" % new_file_name[:-4],
##                            env.workspace + "\\tmp\\%s.MDB\\%s" % (new_file_name[:-4],newtable_name),
##                            "Table")
    arcpy.Rename_management(env.workspace + "\\tmp\\%s.MDB\\010123_E0893N358" % new_file_name[:-4],
                            env.workspace + "\\tmp\\%s.MDB\\%s" % (new_file_name[:-4],new_file_name[:-4]),
                            "Table")
    MetaDataFileName = ConversionUtils.gp.GetParameterAsText(0).split("\\")[-1][:-4] + "MDB"
    arcpy.AddMessage(MetaDataFileName)
    if ConversionUtils.gp.GetParameterAsText(21) == "":
        ConHorizontalPrecision = ""
    else:
        ConHorizontalPrecision = ConversionUtils.gp.GetParameterAsText(21)
    if ConversionUtils.gp.GetParameterAsText(29) == "":
        ConclusionInstitute = ""
    else:
        ConclusionInstitute = ConversionUtils.gp.GetParameterAsText(29)

    if ConversionUtils.gp.GetParameterAsText(30) == "":
        InstituteCheckName = ""
    else:
        InstituteCheckName = ConversionUtils.gp.GetParameterAsText(30)

    if ConversionUtils.gp.GetParameterAsText(31) == "":
        InstituteCheckDate = ""
    else:
        InstituteCheckDate = "-".join(ConversionUtils.gp.GetParameterAsText(31).split(" ")[0].split("/"))
    if ConversionUtils.gp.GetParameterAsText(32) == "":
        BureauCheckName = ""
    else:
        BureauCheckName = ConversionUtils.gp.GetParameterAsText(32)

    if ConversionUtils.gp.GetParameterAsText(33) == "":
        ConclusionBureau = ""
    else:
        ConclusionBureau = ConversionUtils.gp.GetParameterAsText(33)

    if ConversionUtils.gp.GetParameterAsText(34) == "":
        BureauCheckDate = ""
    else:
        BureauCheckDate = "-".join(ConversionUtils.gp.GetParameterAsText(34).split(" ")[0].split("/"))
    GetParameterAsText_list = [MetaDataFileName,ProductName,Owner,
                               Producer,Publisher,"-".join(ConversionUtils.gp.GetParameterAsText(1).split(" ")[0].split("/")),
                               ConversionUtils.gp.GetParameterAsText(2),ConversionUtils.gp.GetParameterAsText(3),ConversionUtils.gp.GetParameterAsText(4),
                               ConversionUtils.gp.GetParameterAsText(5),ConversionUtils.gp.GetParameterAsText(6),ConversionUtils.gp.GetParameterAsText(7),
                               LongerRadius,OblatusRatio,GeodeticDatum,MapProjection,ConversionUtils.gp.GetParameterAsText(8),ConversionUtils.gp.GetParameterAsText(9),
                               ConversionUtils.gp.GetParameterAsText(10),CoordinationUnit,HeightSystem,HeightDatum,
                               ConversionUtils.gp.GetParameterAsText(11),ConversionUtils.gp.GetParameterAsText(12),MultiBandNum,ConversionUtils.gp.GetParameterAsText(13),
                               ConversionUtils.gp.GetParameterAsText(14),
                               ConversionUtils.gp.GetParameterAsText(15),"-".join(ConversionUtils.gp.GetParameterAsText(16).split(" ")[0].split("/")),ConversionUtils.gp.GetParameterAsText(17),
                               ConversionUtils.gp.GetParameterAsText(18),ConversionUtils.gp.GetParameterAsText(19),ConversionUtils.gp.GetParameterAsText(20),
                               ConHorizontalPrecision,ConversionUtils.gp.GetParameterAsText(22),
                               ConversionUtils.gp.GetParameterAsText(23),ManufactureType,
                               ConversionUtils.gp.GetParameterAsText(24),ConversionUtils.gp.GetParameterAsText(25),OrthoRectifySoftWare,ResampleMethod,ConversionUtils.gp.GetParameterAsText(27),
                               ConversionUtils.gp.GetParameterAsText(27),ConversionUtils.gp.GetParameterAsText(28),
                               ConversionUtils.gp.GetParameterAsText(29),InstituteCheckUnit,InstituteCheckName,InstituteCheckDate,
                               BureauCheckName,BureauCheckUnit,ConclusionBureau,BureauCheckDate,
                               SouthWestOrd,SouthWestAbs,NorthWestOrd,NorthWestAbs,NorthEastOrd,NorthEastAbs,SouthEastOrd,SouthEastAbs]
    arcpy.AddMessage("成功录入数据%s条" % len(GetParameterAsText_list))
    field_list = ['MetaDataFileName', 'ProductName', 'Owner', 'Producer', 'Publisher', 'ProduceDate', 'ConfidentialLevel', 'GroundResolution', 'ImgColorModel', 'PixelBits', 'ImgSize',
                  'DataFormat', 'LongerRadius','OblatusRatio', 'GeodeticDatum', 'MapProjection', 'CentralMederian', 'ZoneDivisionMode', 'GaussKrugerZoneNo', 'CoordinationUnit',
                  'HeightSystem', 'HeightDatum','SateName', 'MultiBandSensorType', "MultiBandNum", 'MultiBandName', 'MultiBandResolution',
                  'MultiBandOrbitCode', 'MultiBandDate', 'SateImgQuality', 'GridInterval', 'DEMPrecision', 'ControlSource', 'ConHorizontalPrecision',
                  'ATProducerName', 'ATCheckerName', 'ManufactureType', 'MultiBRectifyXRMS', 'MultiBRectifyYRMS',
                  'OrthoRectifySoftWare', 'ResampleMethod', 'OrthoRectifyQulity', 'OrthoRectifyName', 'OrthoCheckName', 'ConclusionInstitute', 'InstituteCheckUnit', 'InstituteCheckName',
                  'InstituteCheckDate', 'BureauCheckName', 'BureauCheckUnit', 'ConclusionBureau','BureauCheckDate',
                  'SouthWestOrd','SouthWestAbs','NorthWestOrd','NorthWestAbs','NorthEastOrd','NorthEastAbs','SouthEastOrd','SouthEastAbs']
    arcpy.AddMessage("成功导入数据库共%s条数据" % len(GetParameterAsText_list))
    
    fc = env.workspace + "\\tmp\\%s.mdb\\%s" % (new_file_name[:-4],new_file_name[:-4])
    with arcpy.da.UpdateCursor(fc,field_list) as cursor:
        for row in cursor:
            for i in xrange(len(GetParameterAsText_list)):
                row[i] = GetParameterAsText_list[i]
            print row
            cursor.updateRow(row)
    del cursor
    print fc
##    with arcpy.da.UpdateCursor(env.workspace + "\\GF2_odl_M.MDB\\010123_E0893N358",field_list) as cursor:
##        print "success"
    time.sleep(5)
    shutil.copy(env.workspace + "\\tmp\\%s.mdb" % new_file_name[:-4],result_savefolder + "\\%s.mdb" % new_file_name[:-4])

    #清除缓存
    shutil.rmtree(env.workspace + "\\tmp")
    
    
    
    
