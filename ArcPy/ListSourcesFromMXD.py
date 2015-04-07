########################################
# ListSourcesFromMXD.py
# 2014-10-30
# janek@nijn.nu
#
# Find all the data sources added
# to an MXD.
########################################

import os.path, arcpy


######## USER-DEFINED VARIABLES ########

working_dir = r""
output_file = 'sources.txt'
mxd = arcpy.mapping.MapDocument(r"map.mxd")


######## MAIN ##########################

output = open(os.path.join(working_dir,output_file), 'w')

# Iterate through data frames
for df in arcpy.mapping.ListDataFrames(mxd):
    s = df.name
    s += "\n"

    output.write(s)

    # Iterate through layers and group layers
    for fl in arcpy.mapping.ListLayers(mxd, "", df):

        s = "\t" + fl.longName

        if fl.supports("VISIBLE"):
            s += "\tV"
        else:
            s += "\t"

        if fl.isGroupLayer is False:
            if fl.supports("DATASOURCE"):
                s += "\t" + fl.dataSource

            elif fl.supports("WORKSPACEPATH"):
                s += "\t" + fl.workspacePath

        s += "\n"
        output.write(s)

    #endfor

    s += "\n"

#endfor

# release all resources
output.close()
del mxd

print '\n============='
print 'Exported.'
