# SVG_MultiColor_Exporter

Two scripts built for saving time exporting SVG into multiple appropriately named color files. 

They parse the SVG files in the script's directory and replace all instances of the specified color. 

This was made specifically for exporting assets for the [Gitcoin Avatar Generator](https://github.com/gitcoinco/web) but it can be used to quickly make copies of any .svg into appropriately named color files. 

# Python Version 
## How to use
1. Make a SVG with the color you want to change set to #ED2027
1. download color_exporter.py
2. put color_exporter.py in a new empty directory
3. place all SVG to export in the same directory
4. open terminal and navigate to that same directory
    terminal navigation commands
    - `ls` : list files in current directory
    - `cd <newDirectory>` : "change directory" to the newDirectory
5. run command ```python color_exporter.py```
6. Magic! All of your colored SVG files should be generated alongside the original in the directory

## Python and Windows
- If this is your first python script, you'll need to install python and add an environment variable
    - https://www.python.org/downloads/
    - https://docs.python.org/3/using/windows.html
        - >To permanently modify the default environment variables, click Start and search for ‘edit environment variables’, or open System properties, Advanced system settings and click the Environment Variables button. In this dialog, you can add or modify User and System variables. To change System variables, you need non-restricted access to your machine (i.e. Administrator rights).```

# Powershell Version (Windows only)
[Watch it in action!](https://www.youtube.com/watch?v=dfM_2emAa_Y&feature=youtu.be)

## How to use:
1. make an incredible SVG asset and make it Ginger Red! (#ED2027) 
    - you can change the value of the `$colorToReplace` variable to any hexadecimal start color on line 1
    - you can change the SVG color output by changing the hexadecimal numbers in the `$colors` array on line 2
  
2. install windows powershell if you dont have it
    - common powershell commands you will use
      - `dir` : "current directory" shows you all the files in the current directory
      - `cd <newDirectory>` - "change directory" to the newDirectory

3. download "export_all_colors.ps1" script and place in an empty folder

4. open powershell using "Run as Administrator"

5. set the execution policy to allow unsigned scripts with the Command (we will revert the settings when we are done)
    - run this command in the Powershell
    ```Set-ExecutionPolicy -ExecutionPolicy Unrestricted```
    - [read more](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-6&viewFallbackFrom=powershell-Microsoft.PowerShell.Core)  

6. navigate to the empty directory you want your assets in. Use the dir and cd commands explained above.
    -  ex: ```"cd C:\_DamosDesignsLLC\Gitcoin\temp_asset_folder"```

7. drag and drop the .svg you want to use into this directory using the file explorer

8. run this command in Powershell
    - ```.\export_all_colors.ps1```

9. MAGIC!!!!

10. move your new color changed and renamed file to another directory! This script currently only supports changing one svg asset at a time. If you put more than one svg in the directory before running the script, you'll end up with the same asset repeated. 

11. When you're done, don't forget to change your security policy back to the default!

    - ```Set-ExecutionPolicy -ExecutionPolicy Restricted```
