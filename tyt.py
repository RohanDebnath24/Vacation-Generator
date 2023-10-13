from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os
os.environ['OPENAI_API_KEY']="(Place your OpenAI API key here)"  
llm=OpenAI(temperature=0.7)

def get_country_city_places(continent):
    prompt_template_country=PromptTemplate(
        input_variables=['continent'],
        template="I want to visit {continent}. give me a random country to visit."
    )
    country_chain=LLMChain(llm=llm,prompt=prompt_template_country,output_key="country_name")
    prompt_template_places=PromptTemplate(
        input_variables=['country_name'],
        template="I want to visit{country_name}.Suggest me places to visit there. Give the places in a comma seperated strin"

    )
    places_chain=LLMChain(llm=llm,prompt=prompt_template_places,output_key="place_to_visit")
    chain=SequentialChain(
       chains=[country_chain,places_chain],
        input_variables=['continent'],
        output_variables=["country_name", "place_to_visit"]
    )
    response=chain({'continent':continent})
    return response
    

