# Quickstart #
## Load Corpus ##

    !git clone https://github.com/Igor-Chernov-Glad/Corpus.git

Load Data from Git

      AfricaCorpus1=pd.read_csv('..../AfricaCorpus1.csv')
      AfricaCorpus2=pd.read_csv('..../AfricaCorpus2.csv')
      CovidCorpus1=pd.read_csv('..../CovidCorpus1.csv')
      CovidCorpus2=pd.read_csv('..../CovidCorpus2.csv')

Load topics

       Corpus_Themes=pd.read_csv('..../Corpus_Themes.csv')

Set api_keys

    openai_key = "your key"                        "sk_2RUu0AuaSK_TlZVu8RU07Nh_0ZdsuE_tH1ZPf3AyovQ"
    os.environ["NOVITA_API_KEY"] = "your key"      "sk_06MM_hE9k5pCtt3XuNWInDLoWk7KjlA3VrWyaHVq1xw"
    weaviate_api = "your key"                       "T0dMcUQwN1N2NTJZZU80dF9STzBNUWV1eXJsaTE4cHBOSk9vYVhvaFgzcXNqRU52ZGVzVC9wb25ubXdNPV92MjAw"
    url = "your ulr for weaviate cluster"           "yis9umodqbkdmxbxbwuhwg.c0.europe-west3.gcp.weaviate.cloud"

    
