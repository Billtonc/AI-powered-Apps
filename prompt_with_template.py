import gradio as gr
from langchain.prompts import PromptTemplate
import os
from langchain_community.llms import HuggingFaceEndpoint

hfkey = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = hfkey

# Mendefinisikan model AI
llm = HuggingFaceEndpoint(
    repo_id="google/flan-ul2",
    hfkey= hfkey
)

# Mendefinisikan PromptTemplate sebagai format prompt untuk input dari user
def chatbot(user_input):
    # defining a template
    template = """Question: {question}
     please provide step by step Answer:
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])
    formated_prompt =prompt.format(question=str(user_input))
    return llm.invoke(formated_prompt)



# Launch the Gradio interface
gr.Interface(fn=chatbot, inputs="text", outputs="text").launch(server_name="0.0.0.0", server_port= 7860, share=True)