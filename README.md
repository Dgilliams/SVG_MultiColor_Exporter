# SVG_MultiColor_Exporter
A small yet useful PowerShell script built for saving time exporting the same SVG into multiple appropriately named color files. 

This was made specifically for exporting assets for the [Gitcoin Avatar Generator](https://github.com/gitcoinco/web) but it can be used to quickly make copies of any .svg into appropriately named color files. 

(Watch it in action!) [https://www.youtube.com/watch?v=dfM_2emAa_Y&feature=youtu.be]

## How to use:
1. make an incredible SVG hair asset and make it Ginger Red! (#ED2027) 
  - you can change the value of the `$colorToReplace` variable to any start color on line 1
  - you can change the colors the script will output by changing the hexidecimal numbers in the `$colors` array on line 2
  
2. install windows powershell if you dont have it
  - common powershell commands you will use
    - `dir` - "current directory" shows you all the files in the current directory
    - `cd <newDirectory>` - "change directory" to newDirectory

3. download "export_all_colors.ps1" script and place in an empty folder

4. open powershell using "Run as Administrator"

5. set the execution policy to allow unsigned scripts with the Command (we will revert the settings when we are done)
  - run this command in the Powershell
  ```Set-ExecutionPolicy -ExecutionPolicy Unrestricted```
  - (read more) [https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-6&viewFallbackFrom=powershell-Microsoft.PowerShell.Core]
  
  
6. navigate to the empty directory you want your assets in. Use the dir and cd commands explained above.
  -  ex: ```"cd C:\_DamosDesignsLLC\Gitcoin\temp_asset_folder"```

7. drag and drop the .svg you want to use into this directory using the file explorer

8. run this command in Powershell
- ```.\export_all_colors.ps1```

9. MAGIC!!!!

10. move your new color changed and renamed file to another directory! This script currently only supports changing one svg asset at a time. If you put more than one svg in the directory before running the script, you'll end up with the same asset repeated. 

11. When you're done, don't forget to change your security policy back to the default!
  ```Set-ExecutionPolicy -ExecutionPolicy Restricted```
