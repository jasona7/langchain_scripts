# Langchain AI Python Scripts Repository

This repository hosts a collection of Python scripts that showcases the growing end-to-end language model application capabilities of the Langchain Project.  There are too many applications and use caes to list but some represented here are #hiring, #devSecOps, and #CyberSecurity.

https://github.com/hwchase17/langchain

## 🎯Repository Contents 

### bash_oneliners_langchain.py

This script uses the `Flask` framework to create a web application that generates a Bash one-liner command based on user input IN ANY LANGUAGE! :fire: 

The program uses the Langchain Library, specifically the `LLMBashChain` class, to process user input and generate the output. This script also demonstrates the handling of web requests and serving static content in a Flask application.

[Link to the file](bash_oneliners_langchain.py)

### chat_cve.py 

This script leverages the SQL_Database Libraries in the Langchain project to interact with a SQLite3 database seeded with Syft and Grype Software Bill Of Materials (SBOM) and Common Vulnerabilities and Exposures (CVE) findings from the National Vulnerability Database (NVD). This script shows an example of creating an agent that interacts with a SQL database and executes user-specified commands.

[Link to the file](chat_cve.py)

### dol_h1b_cases.py 

This script reads, sanitizes, and analyzes the US Department of Labor's public dataset showing H1B case activity for Q1 2022. It leverages the Langchain's DataFrame Libraries to facilitate conversational interaction with the dataset. It includes a demonstration of sanitizing dataframe data, creating a conversational agent, and processing user input.

[Link to the file](dol_h1b_cases.py)

## 📖 Installation

The scripts in this repository require minimum Python 3.6 or higher and the Langchain Library.  Pandas and Flask are also  required for certain functionality.
