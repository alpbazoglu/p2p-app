
How the program Works

Run the first code then wite the name of the png name but the png file kb must be under 5.
Secondly, run the second code then run the third code then run the fourth code and write the png name again with ‘……………’.png. YOU MUST ADD THE .PNG 
This application allows users to share files with others on the local network. It consists of multiple components:

1. File Divider: `main`
   - Divides a file into multiple chunks to be shared.
   - Asks for user input to specify the file to be shared.
   - Starts broadcasting the chunks to the network.

2. Content Receiver: `2. bölüm`
   - Listens for incoming broadcasts and receives content information from other devices on the network.
   - Updates the content dictionary with the IP addresses of devices that have the shared chunks.
   - Saves the content dictionary to a file named `content_dictionary.txt`.

3. Content Uploader: `3. bölüm`
   - Periodically broadcasts the list of chunks available for sharing to other devices on the network.
   - Sends the list of chunks in JSON format to the broadcast IP and port.

4. File Downloader: `4. bolüm`
   - Allows users to download files shared by other devices on the network.
   - Prompts the user to enter the filename to download.
   - Downloads the specified file chunks from available IP addresses.
   - Merges the downloaded chunks into the original file.




Usage:
1. Run the File Divider (`main`) on the device that has the file to be shared. Enter the file path when prompted.
2. Run the Content Receiver (`2. bölüm`) on all devices that want to discover and download shared files.
3. Run the Content Broadcaster (`3. bölüm`) on all devices that want to share files.
4. Run the File Downloader (`4. bolm`) on the device that wants to download files from other devices.

Note: Make sure all devices are connected to the same local network. Suitable for files less than 5kb in size


Important Files:
- `content_dictionary.txt`: Stores the content information (IP addresses) for shared files.
- `downloaded/`: Directory where downloaded file chunks are stored.
- `download_log.txt`: Log file that records the download activities



