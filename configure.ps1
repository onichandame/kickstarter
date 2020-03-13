#install scoop
$Version = ($PSVersionTable.PSVersion)
If ($Version.Major -lt 5) {
  Write-Output PowerShell 5 or above is required
  exit
}
if ( -NOT (Get-Command scoop -errorAction SilentlyContinue)) {
  Set-ExecutionPolicy RemoteSigned -scope CurrentUser
  Invoke-WebRequest -useb get.scoop.sh | Invoke-Expression | Out-Null
}

#install deps
Get-Content .\prequirements.txt | ForEach-Object {
  scoop install $_ | Out-Null
}

#pass the rest of the work to python scipt
invoke-expression "python configure.py $args"
