def Is_enough(question,context): # Call LLM to determine if there is enough information in the chunk

  prompt = """Is this context:{context} sufficient to fully answer the question:{question}?
  Answer Template: If sufficient, the answer is <yes>, if not sufficient, the answer is <no>.
 """.format(question = question,context = context)
 
  max_tokens = 512
  completion_res = client.completions.create(
    model=large_model,
    prompt=prompt,
    stream=False,
    max_tokens=max_tokens,
  )


  content = completion_res.choices[0].text
  res = False

  if ('yes' in  content ) == True or ('Yes' in  content )  == True or ('YES' in  content )  == True:
    res = True
  else:
    res = False

  return res