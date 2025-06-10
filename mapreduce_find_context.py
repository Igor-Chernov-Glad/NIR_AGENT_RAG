def mapreduce_find_context(question,subqestion,history): #Use MapReduce to summarize best information from each found chunk




  found_qa = vector_search(subqestion,3) # find most n releveant docs
  answer_list = []
  question_list = []
  chunk_list = []
  for qa in found_qa:
    ques = AfricaCorpus.loc[lambda x: (x['question'] == qa) ].reset_index()
    if len(ques) != 0:
      context = ques['Context'][0]

      data = AfricaCorpus.loc[lambda x: (x['Context'] == context) ].reset_index()
    else:
      ques1 = CovidCorpus.loc[lambda x: (x['question'] == qa) ].reset_index()
      context = ques1['context'][0]
      data = CovidCorpus.loc[lambda x: (x['context'] == context) ].reset_index()

    for q in range(len(data)):

      answer_list.append(data['answer'][q])
      question_list.append(data['question'][q])
      chunk_list.append(data['BestChunk'][q])

  if len(history['answer']) != 0:
    answer_list.append(history['answer'])
    question_list.append(history['question'])
    chunk_list.append(history['context'])
  d = {'Context': chunk_list,'question':question_list,'answer':answer_list}
  dataset1 = pd.DataFrame(data = d)
  dataset =  dataset1.drop_duplicates().reset_index()


  cont_list = []
  for con in range(len(dataset)):
    cont = dataset['Context'][con]
    qu = dataset['question'][con]
    ans = dataset['answer'][con]
    temp = """"Question:{question}
    Answer:{answer}
    Context:{context}
    """.format(question = qu,answer = ans,context = cont)
    cont_list.append(temp)
  d = {'Pairs':cont_list}
  dataset2 = pd.DataFrame(data = d)
  doccontext = dataset2['Pairs'].iloc[0:]
  context = [Document(page_content=t) for t in doccontext]


  addmr =""" ```
    {Pairs}
    ```
    """
  addr= """

    ```
    {best information selected}
    ```
    <//>
    """



  map_template = """The following is a set of question-answer pairs with relevant context for them, pairs are delimeted by ``` . Select the pairs that will help answer the user's question.
  Then summarize them so that they are better suited to answer the user's question and сreate a list of the best information selected.


    """.format(question = question)
  map_template = map_template + addmr

  llm = ChatLiteLLM(model=map_model)


  map_prompt = PromptTemplate.from_template(map_template)
  map_chain = LLMChain(llm=llm,prompt=map_prompt)


  reduce_template = """The following is a set of best information found,which are delimeted by ``` .
    Look at the set of best information found and summarize the information found according to relevance to the user's question:'{question}'.



    """.format(question = question)
  reduce_template = reduce_template +  addr


  reduce_prompt = PromptTemplate(template=reduce_template,
    input_variables=["best information selected"]

    )
  reduce_chain=LLMChain(llm=llm,prompt=reduce_prompt)


  combine_documents_chain = StuffDocumentsChain(
      llm_chain=reduce_chain, document_variable_name="best information selected"
  )
  reduce_documents_chain = ReduceDocumentsChain(
        combine_documents_chain=combine_documents_chain,
        collapse_documents_chain=combine_documents_chain,
        token_max=40000)
  map_reduce_chain = MapReduceDocumentsChain(
        llm_chain=map_chain,
        reduce_documents_chain=reduce_documents_chain,
        document_variable_name="Pairs",
        return_intermediate_steps=False)

  output = map_reduce_chain.run(context)

  isEnoug = Is_enough(question,output)

  if isEnoug == True:
    final_context.append(output)

  else:
    ad_const1 = generate_follow_qa(output)
    ad_conts = vector_search(ad_const1,1)
    ques = AfricaCorpus.loc[lambda x: (x['question'] == ad_conts[0]) ].reset_index()
    if len(ques) != 0:
      
      context = ques['Context'][0]
      data = AfricaCorpus.loc[lambda x: (x['Context'] == context) ].reset_index()
    else:
      ques1 = CovidCorpus.loc[lambda x: (x['question'] == ad_conts[0]) ].reset_index()
      context = ques1['context'][0]
      data = CovidCorpus.loc[lambda x: (x['context'] == context) ].reset_index()
    answer_list = []
    question_list = []
    chunk_list = []
    for q in range(len(data)):

      answer_list.append(data['answer'][q])
      question_list.append(data['question'][q])
      chunk_list.append(data['BestChunk'][q])
    d = {'Context': chunk_list,'question':question_list,'answer':answer_list}
    dataset3 = pd.DataFrame(data = d)
    dataset4 =  dataset3.drop_duplicates().reset_index()


    cont_list = []
    for con in range(len(dataset4)):
      cont = dataset4['Context'][con]
      qu = dataset4['question'][con]
      ans = dataset4['answer'][con]
      temp = """"Question:{question}
      Answer:{answer}
      Context:{context}
      """.format(question = qu,answer = ans,context = cont)
      cont_list.append(temp)
    d = {'Pairs':cont_list}
    dataset5 = pd.DataFrame(data = d)
    doccontext = dataset5['Pairs'].iloc[0:]
    context = [Document(page_content=t) for t in doccontext]

    addmr =""" ```
    {Pairs}
    ```
    """
    addr= """

      ```
      {best information selected}
      ```
      <//>
      """



    map_template = """The following is a set of question-answer pairs with relevant context for them, pairs are delimeted by ``` . Select the pairs that will help answer the user's question.
    Then summarize them so that they are better suited to answer the user's question and сreate a list of the best information selected.


      """.format(question = question)
    map_template = map_template + addmr




    map_prompt = PromptTemplate.from_template(map_template)
    map_chain = LLMChain(llm=llm,prompt=map_prompt)


    reduce_template = """The following is a set of best information found,which are delimeted by ``` .
      Look at the set of best information found and summarize the information found according to relevance to the user's question:'{question}'.



      """.format(question = question)
    reduce_template = reduce_template +  addr


    reduce_prompt = PromptTemplate(template=reduce_template,
      input_variables=["best information selected"]

      )
    reduce_chain=LLMChain(llm=llm,prompt=reduce_prompt)


    combine_documents_chain = StuffDocumentsChain(
        llm_chain=reduce_chain, document_variable_name="best information selected"
    )
    reduce_documents_chain = ReduceDocumentsChain(
          combine_documents_chain=combine_documents_chain,
          collapse_documents_chain=combine_documents_chain,
          token_max=40000)
    map_reduce_chain = MapReduceDocumentsChain(
          llm_chain=map_chain,
          reduce_documents_chain=reduce_documents_chain,
          document_variable_name="Pairs",
          return_intermediate_steps=False)

    output1 = map_reduce_chain.run(context)


    output = output + " " + output1
    final_context.append(output)