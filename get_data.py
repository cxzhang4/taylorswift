import lyricsgenius

# number of Taylor Swift songs in dataset (use API to get the most recent album?)
n_songs = 94

# already did Beyonce and Britney Spears
artist_names = ["Nicki Minaj", "Adele", "Katy Perry", "Lady Gaga", "Mariah Carey", "Whitney Houston", "Celine Dion", "Madonna", "Rihanna"]

genius = lyricsgenius.Genius(client_access_token = "JCLqL8cnw-sE8cJbFS0rlX0TsnoNkhE78nk8ZIQEuQZCLVC6-skWWEPVoUyjIXQt",
  skip_non_songs = True,
  excluded_terms = ["(Remix)", "(Live)", "(Version)", "(Acoustic)", "(Demo)", "(Chart History)"])

for artist_name in artist_names:
    artist = genius.search_artist(artist_name, max_songs = n_songs)

    print(artist.songs)

    artist.save_lyrics()
