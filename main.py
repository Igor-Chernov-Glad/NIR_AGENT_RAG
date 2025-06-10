def main(user_question,num_subqa):
  stream = False

  IsValidQA = check_theme(user_question)
  IsValidQA = True
  if IsValidQA == False:
    answer = "The user's question is not relevant to that Corpus"
    sumcontext = ' '
    context = []
  else:

    subQAlist = generate_subQA(user_question,num_subqa)

    context = multi_process(user_question,subQAlist,history)

    sumcontext = ''
    for chunk in context :
      sumcontext = sumcontext + " " + chunk
    answer = final_model(user_question,sumcontext,stream)
    history['answer'] = answer
    history['question'] = user_question
    history['context'] = sumcontext

    res_dict = {'answer':[answer],'revelance_context':context,'final_context':[sumcontext]}

    return res_dict

def start():
  global history
  history = { 'answer': [],'question': [],'context': []}
  global IsStarted
  IsStarted = True
 
  
def end():
  global history
  history = { 'answer': [],'question': [],'context': []}
  global IsStarted
  IsStarted = False