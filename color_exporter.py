import os
import fileinput

#authored by Damien Gilliams of DamosDesigns.com on 10/15/2018

print "\n\n~~~Start of Program~~~\n"

originalColor = "ed2027"
newColors = ["000000", "4E3521", "8C3B28", "B28E28", "F4EA6E", "F0E6FF", "4D22D2", "8E2ABE", "3596EC", "0ECF7C", "ED2027"]

# for the files in the dir
for root, dirs, files in os.walk("."):
    for filename in files:

        # if file ext ends in .svg
        if (os.path.splitext(filename)[1] == ".svg"):
            svgFile = open(filename, 'r')
            svgData = svgFile.read()
            svgFile.close()

            # make sure color exists in file
            if svgData.find(originalColor) == -1:
                print "ERROR: Change fill color of " + filename + " to #ED2027 for script to work"
                break

            for newColor in newColors:

                newSvgFileData = svgData.replace(originalColor, newColor)

                newFileName = os.path.splitext(filename)[0] + "_" + newColor
                newFile = open(newFileName + ".svg", 'w')
                newFile.write(newSvgFileData)
                newFile.close

                print newFileName

        # output replaced results to new file

print "\n\n~~~Done!~~~\n"
