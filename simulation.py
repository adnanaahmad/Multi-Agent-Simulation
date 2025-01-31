from graph import app

# Define the customer query
query = "I have an issue with my invoice. Can you help?"

# Run the workflow with a properly formatted state
response = app.invoke({"query": query})

# Print the result
print("Final Response:", response)