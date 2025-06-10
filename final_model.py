def final_model(question,context): #call llm to final answer

  enable_thinking = False
  chat_completion_res = client.chat.completions.create(
    model=large_model,
    messages=[
          {
              "role": "system",
              "content": "Answer the user's question using this context:{context}".format(context = context),
          },
          {
              "role": "user",
              "content": question,
          }
      ],
      stream=False,
      max_tokens=10000,

  )



  return chat_completion_res.choices[0].message.content