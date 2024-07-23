# YouTube-Video-Player-with-Speech-Recognition

## Overview

This project allows users to search for YouTube videos using voice commands and plays the selected video. The project utilizes speech recognition to capture voice commands, performs a YouTube search, and uses web scraping to fetch video titles and links. It also attempts to play the video using Celluloid.

## Features

- List available microphones and select one for input.
- Capture voice input for searching YouTube.
- Perform a YouTube search based on voice input.
- Extract video titles and links from search results.
- Play the selected video.

## Prerequisites

- Python 3.x
- Internet connection for fetching YouTube data and playing videos.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/voice-controlled-youtube-search.git
   cd YouTube-Video-Player-with-Speech-Recognition

2. **Install required libraries:**

   ```bash
   pip install SpeechRecognition webbrowser pafy requests beautifulsoup4 celluloid
Note: pafy may require additional dependencies for video playback. Refer to pafy documentation for more information.

## Usage
1. **Run the script:**

   ```bash
   python3 project.py

2. **Select the microphone index:**

The script will list available microphones. Enter the index of the microphone you want to use.

3. **Voice Command:**

Speak a command to search for YouTube videos. For example, say "Mr.Beast Search".

4.**Search and Playback:**

The script will perform a YouTube search based on your voice input, list the video titles and links, and attempt to play the best match video using Celluloid.

## Notes

The celluloid library is used for video playback, which may require additional setup or alternative libraries depending on your environment.
Make sure your microphone and audio settings are properly configured for speech recognition to work effectively.

(Initially I planned to use VLC and was almost over but it was not compatible with my Linux Machine so I had o switch to celluloid. WIll develop it in future for VLC too...) 

## Troubleshooting

1. **Speech Recognition Issues:** Ensure your microphone is working correctly and the audio is clear.
2. **YouTube Search Issues:** The web scraping part might fail if YouTube changes its page structure. Adjust the BeautifulSoup selectors as needed.
3. **Video Playback Issues:** Ensure you have the necessary video playback libraries installed. Celluloid may require configuration based on your system. 
