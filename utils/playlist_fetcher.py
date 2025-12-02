PLAYLISTS = {
    "happy": {
        "name": "Golden Hour Glow ✨",
        "url": "https://open.spotify.com/playlist/4RKOpn4egd37fxakJSchF0",
        "cover": "https://i.scdn.co/image/ab67616d0000b273f9da4ad6a79a3fd7c5f3e34d",
        "tracks": [
            "Good Days – SZA",
            "Levitating – Dua Lipa",
            "Sunflower – Post Malone",
        ]
    },

    "sad": {
        "name": "Midnight in My Mind 🌙",
        "url": "https://open.spotify.com/playlist/3yWQSi1Io43q26w57Sza0o",
        "cover": "https://i.scdn.co/image/ab67616d0000b2735a71df52439f0c1b15f8f8d8",
        "tracks": [
            "Ivy – Frank Ocean",
            "Like Real People Do – Hozier",
            "Heather – Conan Gray",
        ]
    },

    "calm": {
        "name": "Pastel Peace 🍃",
        "url": "https://open.spotify.com/playlist/0EedJsRbtKmRKeRoodUpHX",
        "cover": "https://i.scdn.co/image/ab67616d0000b273b6bc447ddb5a0e67e0c9383c",
        "tracks": [
            "Moon – Kanye West",
            "I Know – Djo",
            "Malibu Nights – LANY",
        ]
    },

    "angry": {
        "name": "R3V3NG3 L00P 🔥",
        "url": "https://open.spotify.com/playlist/0x3nOzZ7axAdryQxxujPjd",
        "cover": "https://i.scdn.co/image/ab67616d0000b2730ce4e3d0f5c1a7109a2c8e9b",
        "tracks": [
            "Stop Breathing – Carti",
            "Sdp Interlude – Travis Scott",
            "Teen X – Ken Carson",
        ]
    },

    "fear": {
        "name": "Velvet Fear 🩸",
        "url": "https://open.spotify.com/playlist/3QNuYmHA8rtvgGPETPvUZo",
        "cover": "https://i.scdn.co/image/ab67616d0000b273cd8f438db089d1dcef2fdf42",
        "tracks": [
            "Numb – Portishead",
            "Nightmare – Halsey",
            "Control – Halsey",
        ]
    },

    "surprise": {
        "name": "Fairy Dust ✨",
        "url": "https://open.spotify.com/playlist/2dhd7H9WG5z0MqN4dw98UU",
        "cover": "https://i.scdn.co/image/ab67616d0000b2734cbc2f1521f1d7a60f7f8012",
        "tracks": [
            "Electric Love – BØRNS",
            "Sunflower – Rex Orange County",
            "Magic – Kylie Minogue",
        ]
    },

    "neutral": {
        "name": "Vanilla Mornings ☀️",
        "url": "https://open.spotify.com/playlist/4B3NYLiLXe9iA1x2qBeB5v",
        "cover": "https://i.scdn.co/image/ab67616d0000b2737f9326b6c4b6f0b8e9cd2dba",
        "tracks": [
            "Coffee – beabadoobee",
            "Quality Time – Cautious Clay",
            "Lover Is A Day – Cuco",
        ]
    }
}


def get_playlist_for_emotion(emotion):
    return PLAYLISTS.get(emotion.lower(), PLAYLISTS["neutral"])

