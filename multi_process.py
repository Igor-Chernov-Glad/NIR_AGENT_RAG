
def multi_process(question,subquestions,history): # Do parallel MapReduce for each generate subquestion
   global final_context
   final_context =  []



   threads = [threading.Thread(target=mapreduce_find_context,args=(question, subquestions,history)) for _ in range(len(subquestions))]

   for thread in threads:
        thread.start()

   for thread in threads:
        thread.join()

   return final_context