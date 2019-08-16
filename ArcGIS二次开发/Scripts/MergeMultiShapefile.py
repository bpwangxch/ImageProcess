# coding: cp936

import os
import arcpy

mirrorFolder = arcpy.GetParameterAsText(0)
arcpy.AddMessage("输入的文件夹为：{0}".format(mirrorFolder))

addfieldname = arcpy.GetParameterAsText(1)
field_length = arcpy.GetParameterAsText(2)
outputShapeFile = arcpy.GetParameterAsText(3)

print(mirrorFolder)
filelist = []

for files in os.walk(mirrorFolder):
    for onefile in  files[2]:
        if onefile.endswith(".shp"):
            inputfile = files[0] + "\\" + onefile
            print(onefile[:-4], inputfile)
            filelist.append(inputfile)
            arcpy.AddMessage(u"当前文件：{0}".format(inputfile))
            
            try:
                arcpy.DeleteField_management(inputfile, addfieldname)
                print("删除已有字段")
                arcpy.AddMessage(u"在{0}文件中删除了{1}字段：".format(inputfile, addfieldname))
            except:
                a = 0
                
            arcpy.AddField_management(inputfile, addfieldname, "TEXT", field_length = field_length)
            cursor = arcpy.UpdateCursor(inputfile)
            for row in cursor:
                row.setValue(addfieldname, onefile[:-4])
                cursor.updateRow(row)

arcpy.Merge_management(filelist, outputShapeFile)

arcpy.AddMessage(u"清理字段")
for inputfile in filelist:
    arcpy.DeleteField_management(inputfile, addfieldname)
    arcpy.AddMessage(u"在{0}文件中删除了{1}字段：".format(inputfile, addfieldname))


            
            
