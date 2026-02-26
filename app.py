from agent.insights import generate_insight

print("📊 Business Overview")

question = input("Ask your business question: ")
insight = generate_insight(question)

print(insight)