# Raspberry-Pi-Streaming

# Table Of Contents:
- [About](https://github.com/Cooldude1259/Raspberry-Pi-Streaming?tab=readme-ov-file#about)

- [Keep in mind](https://github.com/Cooldude1259/Raspberry-Pi-Streaming?tab=readme-ov-file#keep-in-mind)

- [Downloading](https://github.com/Cooldude1259/Raspberry-Pi-Streaming?tab=readme-ov-file#downloading)

  - [Step 1: Downloading the Files](https://github.com/Cooldude1259/Raspberry-Pi-Streaming?tab=readme-ov-file#step-1-downloading-the-files)

    - [Method 1](https://github.com/Cooldude1259/Raspberry-Pi-Streaming?tab=readme-ov-file#method-1)

    - [Method 2](https://github.com/Cooldude1259/Raspberry-Pi-Streaming?tab=readme-ov-file#method-2)

  - [Step 2: File Preperation](https://github.com/Cooldude1259/Raspberry-Pi-Streaming?tab=readme-ov-file#step-2-file-preperation)
 
  - [Step 3: Downloading the Web Server](https://github.com/Cooldude1259/Raspberry-Pi-Streaming?tab=readme-ov-file#step-3-downloading-the-web-server)
 
  - [Step 4: Find Videos](https://github.com/Cooldude1259/Raspberry-Pi-Streaming?tab=readme-ov-file#step-4-find-videos)
 
  - [Step 5: Running the Program](https://github.com/Cooldude1259/Raspberry-Pi-Streaming?tab=readme-ov-file#step-5-running-the-program)

- [Visiting the Site](https://github.com/Cooldude1259/Raspberry-Pi-Streaming?tab=readme-ov-file#visiting-the-site)


## About
Raspberry Pi Streaming is a project I pursued to make. I wanted a streaming service type program to run on my new Raspberry Pi 5. The program doesn't require any new Python packages. The GUI is a website containing blocks with Thumbnails of the videos and their titles.

## Keep in mind
Please keep in mind that this code was created on and for a Raspberry Pi 5. Other Raspberry Pi's may work but maybe not. This code is pretty much supported for Linux.

# Downloading
## Step 1: Downloading the Files
When downloading the files, there are multiple methods.
### Method 1
For this method, you are going to download the ZIP file. Above all of the code, click the green dropdown button that says code. At the bottom of the Dropdown, click Download ZIP. Find where the ZIP was downloaded and move it to where you want the program to be. Then unzip the file. Now proceed to step 2.
### Method 2
for this method, you are going to use the git command in your terminal. In the terminal, navigate into the directory that you want the program to be in. Then enter the command: git clone https://github.com/Cooldude1259/Raspberry-Pi-Streaming.git.
Now, proceed onto step 2.

## Step 2: File Preperation
You may notice that the files Videos.zip and VidInfo.zip are currently ZIP files. Unzip them and remove any files inside.

## Step 3: Downloading the Web Server
You now need to get into the terminal and run some commands. The following are the commands you need to run:
sudo apt update
sudo apt install apache2 -y

Run the command: sudo systemctl status apache2
to check that the server is running.

## Step 4: Find Videos
The program does not come with its own videos. You will therefore need to find your own videos for the program. I am giving no suggestions on where to find the videos.

The Videos and thumbnails go into the Videos folder. The names don't matter as long as you remember them. The videos are to be in the MP4 format and the thumbnails are to be in the jpg or png format.

In VidInfo, for every video, you are going to need to make a json file. The name of these files don't matter either, as long as it ends in .json. Only whats in them matters. The format is as follows:
{
  "title": "Example Video",
  "path": "example_video.mp4",
  "thumbnail": "example_thumbnail.jpg",
  "description": "This is a sample video."
}

## Step 5: Running the Program
Now to run the program, you need to run the videos-api.py file. An easy way I have is to open the terminal in the directory of the file and enter the command: python3 videos-api.py

# Visiting the Site
When you run the code in the terminal, there is a message on it saying:
127.0.0.1:5000
<raspberry-pi-ip>:5000

Where there is <raspberry-pi-ip> will be your raspberry pi's ip. to visit the site, just visit either of those two links. If you are not visiting the site on your pi, go to the link with your pi's ip.
