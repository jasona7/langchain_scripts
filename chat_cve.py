# This AI Prompt session demonstrates the capability of the Langchain SQL_Database Libraries
# https://github.com/hwchase17/langchain
# https://python.langchain.com/en/latest/modules/agents/toolkits/examples/sql_database.html
#
# The script requires a sqlite3 DB seeded with Syft and Grype SBOM and CVE findings from the 
# National Vulnerability Database (nvd).  The workflow for SBOMs is Syft > Grype > SQLite3:app_patrol,
# the workflow for CVE fetch is NVD REST API > local Vuln DB > sqllite3:nvd_cves
#
# sqlite3 - 'pip install sqlite3'
# define two tables: nvd_cves and app_patrol
#
# schemas: 
#
#   nvd-cves
#   CREATE TABLE nvd_cves (
#     cve_id TEXT PRIMARY KEY,
#     source_id TEXT,
#      published TEXT,
#      last_modified TEXT,
#      vuln_status TEXT,
#      description TEXT,
#      cvss_v30_vector_string TEXT,
#      cvss_v30_base_score REAL,
#      cvss_v30_base_severity TEXT,
#      cvss_v2_vector_string TEXT,
#      cvss_v2_base_score REAL,
#      cvss_v2_base_severity TEXT,
#      weakness TEXT,
#      ref_info TEXT
#  );
#
#   app_patrol:
#   CREATE TABLE app_patrol (
#    NAME TEXT,
#    INSTALLED TEXT,
#    FIXED_IN TEXT,
#    TYPE TEXT,
#    VULNERABILITY TEXT,
#    SEVERITY TEXT,
#    IMAGE_TAG TEXT
# DATE_ADDED TEXT)
#   
#
#

from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor

# Create a SQLDatabaseToolkit connection to the App_Patrol Database

db = SQLDatabase.from_uri("sqlite:////home/ec2-user/syft/app_patrol.db")
toolkit = SQLDatabaseToolkit(db=db)

agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True
)

#agent_executor.run("Describe nvd_cves table with a helpful summary abou the Severity column.")
#Take user input and gaurdrails and run the agent on it
while True:
    gaurdrails = ("Do not use sql LIMIT in the results. ")
    user_input = gaurdrails + input("Enter a question or type 'exit' to quit: ")
    if user_input.lower() == 'exit':
        break

    agent_executor.run(user_input)
