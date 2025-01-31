import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("GEMINI_API_KEY")

# Setup
llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=api_key)

# Receptionist Agent: Routes the query
def receptionist_agent(state):
    query = state["query"]
    #print("received query at reception agent", query)
    prompt = ChatPromptTemplate.from_messages([
        ("human", "You are a receptionist. Your job is to route the query to the correct department (Sales, Support, or Billing).\n\nQuery: {query}")
    ])
    chain = prompt | llm
    response = chain.invoke({"query": query})
       # Parse the response to determine the department
    if "sales" in response.content.lower():
        department = "sales"
    elif "support" in response.content.lower():
        department = "support"
    elif "billing" in response.content.lower():
        department = "billing"
    else:
        department = "end"
    
    # Return a structured state
    return {"query": query, "department": department, "response": response.content}

# Sales Agent: Handles product inquiries
def sales_agent(state):
    #print("received query at sales agent", query)
    query = state["query"]
    prompt = ChatPromptTemplate.from_messages([
        ("human", "You are a sales agent. Answer questions about products and pricing. \n\nQuery: {query}")
    ])
    chain = prompt | llm
    response = chain.invoke({"query": query})
    return {"query": query, "department": "sales", "response": response.content}

# Support Agent: Resolves technical issues
def support_agent(state):
    #print("received query at support agent", query)
    query = state["query"]
    prompt = ChatPromptTemplate.from_messages([
        ("human", "You are a support agent. Help resolve technical issues. \n\nQuery: {query}")
    ])
    chain = prompt | llm
    response = chain.invoke({"query": query})
    return {"query": query, "department": "support", "response": response.content}

# Billing Agent: Manages payment and invoices
def billing_agent(state):
    #print("received query at billing agent", query)
    query = state["query"]
    prompt = ChatPromptTemplate.from_messages([
        ("human", "You are a billing agent. Handle payment and invoice-related queries. \n\nQuery: {query}")
    ])
    chain = prompt | llm
    response = chain.invoke({"query": query})
    return {"query": query, "department": "billing", "response": response.content}