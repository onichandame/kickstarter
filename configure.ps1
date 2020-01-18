#install scoop
$Version = ($PSVersionTable.PSVersion)
If ($Version.Major -lt 5) {
  echo PowerShell 5 or above is required
  exit
}
if ( -NOT (Get-Command scoop -errorAction SilentlyContinue)) {
  Set-ExecutionPolicy RemoteSigned -scope CurrentUser
  iwr -useb get.scoop.sh | iex | Out-Null
}

#install python
scoop install python | Out-Null

#install packages according to arguments
python configure.py $args | Out-Null
