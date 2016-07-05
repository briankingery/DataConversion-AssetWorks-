# Extract_9_3_Data.py
# B. Gates
# 7/21/15

# Copy data from production database into a 9.3 file geodatabase.

import arcgisscripting
import os

Path = r'\\Missouri\GIS_Data\GIS_Private\DataResources\AssetworksDataConversion'
SourceFeatureClass = os.path.join(Path, r'Interfaces\Missouri_sdeVector_sdeViewer.sde\sdeVector.SDEDATAOWNER.WaterUtility\sdeVector.SDEDATAOWNER.wServiceLocation')
DestinationGDB = os.path.join(Path, r'Data\9_3_Data.gdb')
DestinationFeatureClassName = 'wServiceLocation'
DestinationFeatureClass = os.path.join(DestinationGDB, DestinationFeatureClassName)

gp = arcgisscripting.create()

if gp.Exists(DestinationFeatureClass):
    gp.Delete(DestinationFeatureClass)
    
gp.FeatureClassToFeatureClass_conversion(SourceFeatureClass, DestinationGDB, DestinationFeatureClassName)
