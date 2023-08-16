from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
llm = ChatOpenAI()
current_player = f"X"
board_layout = f"first row:['1', '2', '3'] second row:['4' ,'5' ,'6']third row:['7', '8', '9']"
board_state = f"first row:['', '', ''] second row:['' ,'' , '']third row:['', '', '']"

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

lang_model = OpenAI(temperature=0.9)

text = "What would be a good company name for a company that makes colorful socks?"
# print(llm("What's a good name for a guitar company that makes pink guitars"))


prompt_llm = PromptTemplate(
    input_variables=["input"],
    template="answer the human in a business style of writing {input}?",
)


chain = LLMChain(llm=lang_model, prompt=prompt_llm, verbose=True)

# print(chain.run(input="what is todays date"))


print(chain.run("what is the largest dog breed?"))










prompt_template = PromptTemplate.from_template(
    "You are a master tic tac toe player. the board is laid out in this \
    fasion: {board_layout} and the current player is: {current_player} \
      what is your move based on the current board state of: {board_state}."
)
prompt_template.format(current_player=current_player, board_layout=board_layout, board_state=board_state)
# chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)
response = llm.predict(prompt_template)
print(response)