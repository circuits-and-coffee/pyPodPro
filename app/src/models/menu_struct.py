# Original method
# MENU_STRUCTURE = {
#     'Music': {
#         'Artists': None,
#         'Albums': None,
#         'Tracks': None
#     },
#     'Videos': {
#         'TV Shows': None,
#         'Movies': None,
#         'Music Videos': None
#     },
#     'Photos': None,
#     'Settings': {
#         'Jellyfin': {
#             'Find and Connect': "FIND_JELLYFIN_CONNECT"
#         },
#     },
#     'Shuffle Songs': None,
#     'Quit': "QUIT"
# }

MENU_STRUCTURE=[
    ("Local Music", [
        ("Artists", "show_artists"),
        ("Albums", "show_albums"),
        ("Tracks", "show_tracks")
        ]
     ), (
    "Online Music", [
        ("Top Charts", "show_top_charts"),
        ("New Releases", "show_new_releases"),
        ("Genres", "show_genres")
        ]
    ),(
    "Photos",[
        ("Albums", "show_photo_albums"),
        ("Favorites", "show_favorite_photos")
        ]
    ),(
    "Videos",[
        ("TV Shows", "show_tv_shows"),
        ("Movies", "show_movies"),
        ("Music Videos", "show_music_videos")
        ]
    ),(
    "Settings", [
        ("Theme", "show_theme"),
        ("Jellyfin", [
            ("Find and Connect", "find_jellyfin_connect")
            ])
        ]),(
    "Quit", "quit_app")
]