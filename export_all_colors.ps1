$colorToReplace = 'ED2027'
$colors = @("000000","4E3521","8C3B28","B28E28","F4EA6E","F0E6FF","4D22D2","8E2ABE","3596EC","0ECF7C","ED2027")

$files = Get-ChildItem -Path $PSScriptRoot

Write-Output $files

foreach($file in $files) {
  if(-NOT ($file.BaseName -eq 'export_all_colors')) {
    foreach ($color in $colors) {

    $newFileName = $file.Basename + "_" + $color + ".svg"
    Write-Output $newFileName
    powershell -Command "(gc *.svg) -replace '$colorToReplace', '$color' | Out-File $newFileName.svg"
    }
  }
}
