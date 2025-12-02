import streamlit as st
import cv2
import numpy as np
import time
import random

from utils.camera_emotion import detect_emotion_from_frame
from utils.playlist_fetcher import get_playlist_for_emotion

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="Pink Polaroid",
    page_icon="🎀",
    layout="centered"
)

# ----------------------------------
# LOAD CUSTOM CSS
# ----------------------------------
with open("static/style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----------------------------------
# HERO SECTION (like your first Canva page)
# ----------------------------------
st.markdown(
    """
    <section class="hero">
      <div class="hero-inner">
        <p class="hero-line">
          Ready to capture your vibe and turn it into a playlist?
        </p>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------
# CAMERA SECTION (like your second Canva page)
# ----------------------------------
st.markdown(
    """
    <section class="camera-section">
      <div class="camera-inner">
        <div class="camera-text">
          <h2>Take a photo and<br/>I'll detect your mood,</h2>
          <h2>then match it with the<br/>perfect playlist &lt;3</h2>
        </div>
        <div class="camera-polaroid-wrapper">
          <div class="camera-polaroid">
            <div class="camera-top"></div>
    """,
    unsafe_allow_html=True,
)

# camera widget – Streamlit will drop it right here
camera_photo = st.camera_input(" ", key="pink_polaroid_camera")

# close the polaroid wrapper
st.markdown(
    """
            <div class="camera-bottom">
              <p class="camera-caption">Pink Polaroid</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------
# RESULT SECTION (like your third Canva page)
# We'll only show this AFTER a photo is taken + emotion found
# ----------------------------------

if camera_photo:
    with st.spinner("✨ Scanning your vibe and picking a playlist…"):
        time.sleep(1.4)

    file_bytes = np.asarray(bytearray(camera_photo.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    emotion = detect_emotion_from_frame(img)

    if not emotion:
        st.warning("Face not detected properly 😭 Try again in better lighting!")
    else:
        emotion = emotion.lower()
        playlist_meta = get_playlist_for_emotion(emotion)

        if not playlist_meta:
            st.error("No playlist found for this mood 😢")
        else:
            # pick tilt for fun if you ever use it
            _ = random.choice(["tilt-1", "tilt-2", "tilt-3", "tilt-4"])

            playlist_url = playlist_meta["url"]
            playlist_id = playlist_url.split("/")[-1].split("?")[0]

            # cover handling (URL vs local file vs missing)
            raw_cover = playlist_meta.get("cover")
            cover_url = None

            if raw_cover:
                if raw_cover.startswith("http://") or raw_cover.startswith("https://"):
                    cover_url = raw_cover
                else:
                    cover_url = f"static/{raw_cover.lstrip('/')}"

            if cover_url:
                cover_block = f"""
                    <img src="{cover_url}" alt="Playlist cover" class="result-cover"/>
                """
            else:
                cover_block = """
                    <div class="result-cover placeholder"></div>
                """

            tracks_html = "".join(
                [f"<li>🎧 {t}</li>" for t in playlist_meta.get("tracks", [])]
            )

            result_html = f"""
            <section class="result-section">
              <div class="result-header">
                <p class="result-sub">YOUR PLAYLIST IS READY! HOPE YOU ENJOY IT 🎀</p>
                <h2 class="result-title">
                  Detected mood:
                  <span class="result-mood">{emotion.upper()}</span>
                </h2>
              </div>

              <div class="result-layout">
                <div class="result-left">
                  {cover_block}
                </div>

                <div class="result-right">
                  <h3 class="playlist-title">{playlist_meta['name']}</h3>

                  <div class="playlist-scroll">
                    <ul class="track-list">
                      {tracks_html}
                    </ul>

                    <div class="spotify-embed">
                      <iframe 
                        style="border-radius:12px"
                        src="https://open.spotify.com/embed/playlist/{playlist_id}"
                        width="100%"
                        height="320"
                        frameborder="0"
                        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                        loading="lazy">
                      </iframe>
                    </div>
                  </div>

                  <div class="playlist-button-row">
                    <a href="{playlist_url}" target="_blank" rel="noopener noreferrer" class="spotify-link-btn">
                      Take me to the playlist on Spotify ↗
                    </a>
                  </div>
                </div>
              </div>
            </section>
            """

            st.markdown(result_html, unsafe_allow_html=True)
else:
    # if no photo yet, show a faint hint result section (optional) or nothing
    pass
