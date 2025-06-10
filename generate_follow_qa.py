def generate_follow_qa(context): # call LLM to generate follow questions

  prompt = """ Generate one follow up question using this context:{context}. Answer Template: ///follow up question///.
 """.format(context = context)
  stream = False  # or False
  max_tokens = 512
  completion_res = client.completions.create(
    model=large_model,
    prompt=prompt,
    stream=stream,
    max_tokens=max_tokens,

  )

  content = completion_res.choices[0].text
  context = content.split("///follow up question///")
  if len(context) > 1:
    return context[1]
  else:
    return context
