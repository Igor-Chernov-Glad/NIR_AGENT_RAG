def check_theme(qa): #chech user question on theme identification

  res = False
  stemmer = PorterStemmer()
  themes = ThemeModel(qa)
  themes = themes [0]
  themes  = themes ['generated_text']
  themes  = themes.split(';')
  for theme in themes:
    theme = theme.lower()
    stemmed_word = stemmer.stem(theme) 
    if (stemmed_word in Corpus_Themes["topic"]) == True:

      res = True

  return res
