# Query your database with AI using LangChain and Gradio

Read the tutorial "[Query your database with AI using LangChain and Gradio](https://jstoppa.com/posts/artificial-intelligence/fundamentals/query-your-database-with-ai-using-langchain-and-gradio/post/)" that explains how this repo works

## Setup

1. Download Python and PIP in your local machine (see [this article](https://jstoppa.com/posts/getting_started_with_openai_in_python/post/) )
2. Install virtual environment

```bash
pip install virtualenv
```

3. Navigate to the folder where you want to create the VM and run the below
   NOTE: Run the command below from one level up where you installed the repo - e.g. if you downloaded the repo to C:\repo\langchain_sql_gradio, you need to run the command below from C:\repo

```bash
virtualenv langchain_sql_gradio
```

4. Activate the environment by using

```bash
.\langchain_sql_gradio\Scripts\activate
```

5. Inside the Virtual environment, install all required components

```bash
pip install -r requirements.txt
```

6. Create a the following environment variables (see [this example](https://jstoppa.com/posts/getting_started_with_openai_in_python/post/#5-creating-a-hello-world-app-with-openai) )

-   OPENAI_API_KEY -> used for connecting to OpenAI

7. After doing all the previous steps, you might need to restart your machine, I have noticed that the environment variables are not picked up by Python until a restart or the PIP install doesn't quite work

## Notes for using the repo

-   Install any new pip package inside the virtual environment command line
-   Run the command below to update the requirements.txt file that contains the packages needed to run the repo

```bash
pip freeze > requirements.txt
```
