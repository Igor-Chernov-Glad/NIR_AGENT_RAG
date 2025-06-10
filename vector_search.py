
def vector_search(question,n): # search in database top n docs
  res = []
  response = collection.query.near_text(
    query=question,
    limit=n
  )

  for obj in response.objects:
      qa = obj.properties["question"]
      res.append(qa)
  return res
