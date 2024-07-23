import speech_recognition as sr
import webbrowser as wb
import pafy
import requests
from bs4 import BeautifulSoup
import celluloid

# List available microphones
microphones = sr.Microphone.list_microphone_names()
for i, mic_name in enumerate(microphones):
    print(f"{i}: {mic_name}")

# Prompt the user to select the microphone index
mic_index = int(input("Enter the microphone index to use: "))

# Create Recognizer() class objects called recog1 and recog2
recog1 = sr.Recognizer()
recog2 = sr.Recognizer()

# Create microphone instance with the selected device index
mc = sr.Microphone(device_index=mic_index)

# Capture voice
with mc as source:
    print("Search YouTube video to play")
    print("----------------------------")
    print("You can speak now")
    audio = recog1.listen(source)

try:
    if 'search' in recog1.recognize_google(audio):
        recog1 = sr.Recognizer()
        with mc as source:
            print('Searching for the video(s)...')
            audio = recog2.listen(source)

            get_keyword = recog1.recognize_google(audio)
            print(f"Keyword: {get_keyword}")

            search_url = f"https://www.youtube.com/results?search_query={get_keyword}"
            wb.open_new_tab(search_url)

            # Fetch HTML content
            response = requests.get(search_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            with open("file.txt","w") as f:
                f.write(soup)
                f.write('\n')
            # Extract video titles and links
            video_links = []
            for vid in soup.find_all(attrs={'class': 'yt-uix-tile-link'}, limit=10):
                video_title = vid['title']
                video_link = 'https://www.youtube.com' + vid['href']
                video_links.append((video_title, video_link))

            print(video_links)

            # Play the video using Celluloid
            player = celluloid.Celluloid()
            player.play_video(best_stream.url)

            # Optionally wait to ensure the media is playing
            input("Press Enter to stop playback...")
            player.stop()

except sr.RequestError as e:
    print(f"Unable to provide required output: {e}")
except Exception as e:
    print(f"Error occurred: {e}")