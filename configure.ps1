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

#install python
scoop install python@3.6.1 | Out-Null

#install packages according to arguments
invoke-expression "python configure.py $args"
