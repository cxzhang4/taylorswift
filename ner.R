library(spacyr)
library(tidyverse)

spacy_initialize()
setwd("~/taylorswift")
fps_lyrics_tif = read_csv("data/female_pop_star_lyrics.csv") %>% 
  tibble::rowid_to_column() %>% 
  mutate(doc_id = rowid, text = lyric) %>%
  select(doc_id, text)

spacy_parse(fps_lyrics_tif)
