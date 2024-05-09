from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties import scrape_linkedin_profile

load_dotenv()
information= """
    Ever wondered about your role in #ImmersiveExperiences?

    In #Dubai,
    visitors personalize animals,
    enriching a communal jungle.
    While #AI aids walking models, the essence lies in visitor interaction,
    Explore Dibulo app for at-home engagement. Reminiscent of teamLab Inc.'s Sketch Aquarium at The Newark Museum of Art of Art, 
    where drawn sea creatures swam in a virtual aquarium. Immersion goes beyond observation; 
    it's about active participation shaping our #DigitalLandscapes. How can your creativity transform the spaces you encounter? Join the conversation.

    """

if __name__ == '__main__':
    print("Hello Langchain")
 
#print(os.environ['OPENAI_API_KEY'])

    summary_template="""
        given the information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them


    """

    summary_prompt_template=PromptTemplate(input_variables=["information"],template=summary_template)

    llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    
    chain = LLMChain(llm=llm , prompt=summary_prompt_template)
    res = chain.invoke(input={"information":information})

    print(res)

linkedin_data=scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/farzad-shojaei/')
print(linkedin_data.json())
print(chain.run(information=linkedin_data))

