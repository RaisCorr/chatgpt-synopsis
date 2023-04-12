from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


def overall_chain(theme):
    """
    Generate a story synopsis based on a given theme using a LangChain model.

    :param theme: a string representing the theme of the story
    :return: a dictionary containing the generated prompt and synopsis
    """
    # Instantiate a ChatOpenAI model for generating language
    llm = ChatOpenAI(temperature=0.9)

    # Create an LLMChain for generating a prompt based on the given theme
    template = """
    As a professional scenario writer, please list 50 English words separated by commas that vividly and precisely describe a cute girl's illustration based on the given theme and the following criteria with an imaginative and extravagant idea.

    Criteria: Imagine and express an illustration that includes the following information with an imaginative and extravagant idea.
    Infomation: Action, clothing, eye color, gaze, hair color, hairstyle, hair length, expression, clothing, top, bottom, accessory, posture, worldview, composition, location, three things in the surroundings, time, three fantasy-cute worldviews.
    Theme: {theme}
    English words:
    """
    prompt_template = PromptTemplate(input_variables=["theme"], template=template)
    sd_prompt_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="sd_prompt")

    # Create an LLMChain for generating a story synopsis based on the prompt
    template = """
    As a professional scenario writer, please write a 100 WORD synopsis of the first story that is both metaphorical and poetic without using the English words given as sd_prompt.

    sd_prompt: {sd_prompt}
    synopsis:
    lang:ja
    """
    prompt_template = PromptTemplate(input_variables=["sd_prompt"], template=template)
    synopsis_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="synopsis")

    # Create a SequentialChain
    overall_chain = SequentialChain(
        chains=[sd_prompt_chain, synopsis_chain],
        input_variables=["theme"],
        output_variables=["sd_prompt", "synopsis"],
        verbose=True,
    )

    # Run the overall_chain
    results = overall_chain({"theme": theme})

    return results
