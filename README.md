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

## Set api_keys ##

    openai_key = "your key"                        "sk_2RUu0AuaSK_TlZVu8RU07Nh_0ZdsuE_tH1ZPf3AyovQ"
    os.environ["NOVITA_API_KEY"] = "your key"      "sk_06MM_hE9k5pCtt3XuNWInDLoWk7KjlA3VrWyaHVq1xw"
    weaviate_api = "your key"                       "T0dMcUQwN1N2NTJZZU80dF9STzBNUWV1eXJsaTE4cHBOSk9vYVhvaFgzcXNqRU52ZGVzVC9wb25ubXdNPV92MjAw"
    url = "your ulr for weaviate cluster"           "yis9umodqbkdmxbxbwuhwg.c0.europe-west3.gcp.weaviate.cloud"

## Load models ##

BART

         ThemeModel = pipeline("text2text-generation", model="ankur310794/bart-base-keyphrase-generation-kpTimes")

Novita_Qwen

        client = OpenAI(
            base_url="https://api.novita.ai/v3/openai",

            api_key=openai_key
            )

        large_model = "qwen/qwen3-32b-fp8"
        small_model = "qwen/qwen3-4b-fp8"
        map_model = "novita/qwen/qwen3-32b-fp8"


## Connect to weaviate ##


        Weaclient = weaviate.connect_to_weaviate_cloud(
            cluster_url=url,                     # Weaviate URL: "REST Endpoint" in Weaviate Cloud console
            auth_credentials=Auth.api_key(weaviate_api),  # Weaviate API key: "ADMIN" API key in Weaviate Cloud console
        )
        
        print(Weaclient.is_ready())  # Should print: `True`
        collection = Weaclient.collections.get("Corpus_QA")



## Agent RAG ##
Start session (This is to record the history of the conversation)

    start()

    user_question = "ask your question"
    n = "set the number of sub questions"


    result = main(user_question,n)


End session (Delete the history of the conversation)   

        end()        
                
    
