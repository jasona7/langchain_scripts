
# The script will Sanitize and Analyze the US Department of Laor Public Dataset showing H1B Case activity for Q1 2022
# engaging the user through a conversational session with the dataset.


from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import pandas as pd
class ConversationChain:
    def __init__(self):
        self.conversation = []

    def add_user_input(self, user_input):
        self.conversation.append(('user', user_input))

    def add_agent_response(self, agent_response):
        self.conversation.append(('agent', agent_response))

    def get_last_response(self):
        if not self.conversation:
            return ''
        _, last_response = self.conversation[-1]
        return last_response

def sanitize_dataframe(df):
    date_columns = ['RECEIVED_DATE', 'DECISION_DATE', 'ORIGINAL_CERT_DATE', 'BEGIN_DATE', 'END_DATE']
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    
    df['EMPLOYER_POC_MIDDLE_NAME'] = df['EMPLOYER_POC_MIDDLE_NAME'].fillna('')
    df = df.drop_duplicates()
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    df['employer_name'] = df['employer_name'].str.strip()
    df['naics_code'] = df['naics_code'].astype(str)
    
    return df

# Read the CSV file(s)
df2022_q4 = pd.read_csv('/home/ec2-user/llm/dol/h1b/LCA_Disclosure_Data_FY2022_Q4.csv')

# Sanitize the dataframes
df2022_q4 = sanitize_dataframe(df2022_q4)

agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df2022_q4, verbose=True)
conversation = ConversationChain()

def run_agent_and_print_token_count():
    while True:
        user_input = input("Enter a question or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            break

        conversation.add_user_input(user_input)
        response = agent.run(conversation.get_last_response())

        # Add the agent's response to the conversation
        conversation.add_agent_response(response)

        # Calculate token count manually
        token_count = len(response.split())

        # Print the result and token count
        print(response)
        print(f'Tokens used: {token_count}')

run_agent_and_print_token_count()
