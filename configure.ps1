#install scoop
$Version = ($PSVersionTable.PSVersion)
If ($Version.Major -lt 5) {
  echo PowerShell 5 or above is required
  exit
}
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
start powershell {Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')}

#install python
scoop install python

#install packages according to arguments
start powershell { python configure.py $args }

