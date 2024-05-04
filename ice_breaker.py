from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

if __name__ == '__main__':
    print("Hello Langchain")
    print(os.environ['OPENAI_API_KEY'])

    summary_template="""
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them


    """

    summary_prompt_template=PromptTemplate(input_variables=["information"],template=summary_template)

    llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")


