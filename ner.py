import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

fps_lyrics = pd.read_csv('data/fps_lyrics_tif.csv')

# print(fps_lyrics)
# fps_lyrics['text_as_spacy_objects'] = fps_lyrics['text'].apply(nlp)

ts_lyrics = fps_lyrics[fps_lyrics.artist == 'Taylor Swift']

ts_songs = ts_lyrics.track_title.unique()

ts_spacy = {}

print(ts_songs)
i = 1
for song in ts_songs:
    print(i)
    print(song)
    song_lyrics = ts_lyrics[ts_lyrics.track_title == song]
    print(song_lyrics.text)
    # print(song_lyrics.text.str.join(' '))
    # ts_spacy[song] = nlp(song_lyrics.text.str.join())
    i = i + 1

# print(len(ts_songs.index))

# ts_songs['spacy_obj'] = ts_songs['text'].apply(nlp)
#
# for doc in ts_songs['spacy_obj']:
#     for ent in doc.ents:
#         print(ent.text, ent.start_char, ent.end_char, ent.label_)

# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)

# i = 1
# for doc in fps_lyrics['text_as_spacy_objects']:
#     # print(i)
#     for ent in doc.ents:
#         print(ent.text, ent.start_char, ent.end_char, ent.label_)
#     # i = i + 1
