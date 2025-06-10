# Quickstart #

## Preparing the environment ##

            from openai import OpenAI
            import os
            import pandas as pd
            import nltk
            from nltk.tokenize import word_tokenize
            nltk.download('punkt_tab')
            import tensorflow as tf
            from langchain.text_splitter import CharacterTextSplitter
            from datasets import load_dataset
            from transformers import T5ForConditionalGeneration,T5Tokenizer
            from transformers import AutoModelForCausalLM, AutoTokenizer
            from abc import ABC
            from langchain.llms.base import LLM
            from typing import Any, List, Mapping, Optional
            from langchain.callbacks.manager import CallbackManagerForLLMRun
            from langchain.llms import HuggingFacePipeline
            import torch
            import weaviate
            from weaviate.classes.init import Auth
            from weaviate.classes.config import Configure
            from transformers import pipeline
            from langchain.text_splitter import CharacterTextSplitter
            from langchain_community.document_loaders import WebBaseLoader
            from transformers import AutoModel
            from numpy.linalg import norm
            from nltk.stem import PorterStemmer
            from nltk.tokenize import word_tokenize
            from langchain_core.documents import Document
            from langchain.chains import LLMChain
            from typing import Any, Dict, List
            from transformers import pipeline
            from langchain_core.pydantic_v1 import BaseModel, Field
            from langchain_core.runnables import RunnableLambda
            from langchain_core.output_parsers import CommaSeparatedListOutputParser
            from langchain.chains import StuffDocumentsChain
            from langchain.chains import ReduceDocumentsChain
            from langchain.chains import MapReduceDocumentsChain
            from langchain.prompts import PromptTemplate
            from langchain.agents import AgentExecutor, create_react_agent
            output_parser = CommaSeparatedListOutputParser()
            from langchain_community.chat_models import ChatLiteLLM
            from langchain_core.prompts import (
                ChatPromptTemplate,
                SystemMessagePromptTemplate,
                AIMessagePromptTemplate,
                HumanMessagePromptTemplate,
            )
            from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
            import threading
            import weaviate
            
            import main
            import check_theme
            import final_model
            import generate_follow_qa
            import generate_subQA
            import Is_enough
            import mapreduce_find_context
            import multi_process
            import vector_search


## Load Corpus ##

    !git clone https://github.com/Igor-Chernov-Glad/NIR_AGENT_RAG.git

Load Data from Git

      AfricaCorpus1=pd.read_csv('..../AfricaCorpus1.csv')
      AfricaCorpus2=pd.read_csv('..../AfricaCorpus2.csv')
      CovidCorpus1=pd.read_csv('..../CovidCorpus1.csv')
      CovidCorpus2=pd.read_csv('..../CovidCorpus2.csv')
      CovidCorpus = pd.concat([CovidCorpus1, CovidCorpus2])
      AfricaCorpus = pd.concat([AfricaCorpus1, AfricaCorpus2])



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
                
    
