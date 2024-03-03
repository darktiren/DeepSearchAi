ReadMe
-Project Title:  DeepSearchAi
-TL-DR: A unique web browsing agent that leverages LLMs to analyze and synthesize comprehensive answers from multiple websites.
-What Does it Do?
	*Takes a user-provided query.
	*Uses an LLM (powered by the Google AI API) to generate a diverse list of relevant 	search queries.
	*Employs search libraries to find credible websites for each query.
	*Captures website content visually and converts images to text using LLMs.
	*Processes each website individually with an LLM, producing answers to the original 	query.
	*Combines individual answers for a final, comprehensive response, refined with the 	LLM for clarity.
Key Features:
	*In-depth Web Exploration: Goes beyond superficial search results to provide deep 	insights gleaned from entire websites.
	*LLM-Powered Throughout: Leverages LLMs for query generation, image-to-text 	conversion, and answer synthesis.
	*Free to Use: Relies on the free tier of the Google AI API (60 requests/minute limit 	applies).
Getting Started:
	*Clone Repository
	*Obtain Google AI API Key: [https://ai.google.dev/]
	*Install Dependencies: [install.py]
	*Run the Agent: DeepSearchAi.exe
Notes:
	*Designed for in-depth research and analysis - processing time can vary (20-40 	minutes typical).
	*Best suited for queries where a single website cannot provide a complete 	understanding.
Contribute:
We welcome contributions! This is a novel AI project, and areas for improvement or exploration include:
	*Batch requests for optimizing processing speed
	*Enhancing site selection criteria
	*Experimenting with alternative LLMs
	*Enable Multiple Searches at once
	*Improved error handling for blocked responses
License:
	Copyright (C) 2024 Christopher Garner
	GNU General Public License v3.0: https://www.gnu.org/licenses/Disclaimer

Disclaimer:
	This project is an experimental exploration of LLM capabilities. The final responses 	may contain inaccuracies or reflect biases present in the data used to train the
 	underlying language models. Use the results with critical judgment.