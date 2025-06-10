def generate_subQA(question,n): #split user questions on n subqestions
 
  prompt = "Generate {n} subqestions from that question '{question}'.   Answer Template: <1.subqestion> // <2.subqestion> // <n.subqestion> ...".format(question = question,n = n)

 
  max_tokens = 512
  completion_res = client.completions.create(
    model=small_model,
    prompt=prompt,
    stream=False,
    max_tokens=max_tokens,
  )


  res = completion_res.choices[0].text
  res_list = []

  res = res.split('subqestion')

  for st in res:
    if ("?" in st) == True:
      res_list.append(st)

  return res_list[:3]