import streamlit as st
import pytube as py
from pytube import YouTube
import os

#st.markdown(custom_css, unsafe_allow_html=True)
#st.image("logo.png")
# Get the YouTube link from the user
# st.text("Enter The Youtube Video link: ")
youtube_link = st.text_input("Insira a url do vídeo para baixar:", placeholder="Somente vídeos do youtube",key="youtubelink")

# Get the video resolution from the user
# st.text("Select Video Resolution: ")
video_resolution = st.selectbox("Selecione a resolução para download:", ["360p", "720p","1080"], key="resolution")

# Button to process the YouTube link
if st.button("Buscar Vídeo"):
    if youtube_link:
        # Create a YouTube object
        video_instance = py.YouTube(youtube_link)

        # Get the stream with the selected resolution
        stream = video_instance.streams.filter(res=video_resolution).first()

        if stream is None:
            #st.write(f"O vídeo não está disponível com essa resolução {video_resolution}")
            st.warning(f"O vídeo não está disponível com essa resolução {video_resolution}")
        else:
            # Download the video (this will download the video to the server running Streamlit)
            filename = stream.download()

            # Check if the file exists (download was successful)
            if os.path.isfile(filename):
                # Get the actual name of the file without OS path
                actual_filename = os.path.basename(filename)

                # Read file data
                with open(filename, "rb") as f:
                    bytes = f.read()

                # Provide a button for the user to download the video file
                st.download_button(
                    label="Download Vídeo",
                    data=bytes,
                    file_name=actual_filename,
                    mime='video/mp4'
                    
                    
        
                )
            

            st.video(youtube_link)