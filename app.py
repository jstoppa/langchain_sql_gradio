import os
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain.schema import AIMessage, HumanMessage
from operator import itemgetter
import gradio as gr
from langchain.agents import create_sql_agent
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


api_key = os.environ.get("OPENAI_API_KEY")

connection_string = "<connection string>"
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()

db = SQLDatabase(engine, include_tables=["Table"]) 

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=api_key, streaming=True)
chain = create_sql_query_chain(llm, db)

execute_query = QuerySQLDataBaseTool(db=db)
write_query = create_sql_query_chain(llm, db)
chain = write_query | execute_query

answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, and SQL result, answer the user question.

Question: {question}
SQL Query: {query}
SQL Result: {result}
Answer: """
)

answer = answer_prompt | llm | StrOutputParser()
chain = (
    RunnablePassthrough.assign(query=write_query).assign(
        result=itemgetter("query") | execute_query
    )
    | answer
)

def stream_response(input_text, history):
    history = history or []
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))

    if input_text is not None:
        history_langchain_format.append(HumanMessage(content=input_text))
        partial_message = ""
        for response in chain.stream({"question": input_text}):
            if (response != ""):
                partial_message += response
            
            yield partial_message

iface = gr.ChatInterface(
    stream_response,
    textbox=gr.Textbox(placeholder="Ask a question about the database...", container=False, scale=7),
)

iface.launch(share=True)