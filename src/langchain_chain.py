from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from retriever import retriever

# openai_api_key (REMOVE THIS BECAUSE IT IS NOT SECURE)
chatgpt_api_key = "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"


# Initialize the OpenAI language model
llm = OpenAI(temperature=0.7, openai_api_key=chatgpt_api_key)

# Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["institution", "results"],
    template="Here is the information I found about {institution}: {results}"
)

# Combine the retriever with the LLM in a chain
class RAGChain(LLMChain):
    def __init__(self, retriever, llm, prompt_template):
        super().__init__(llm=llm, prompt=prompt_template)
        self.retriever = retriever

    def run(self, institution):
        results = self.retriever.retrieve(institution)
        return super().run(institution=institution, results=results.to_dict(orient='records'))

rag_chain = RAGChain(retriever=retriever, llm=llm, prompt_template=prompt_template)

# Example usage
query = "Harvard"
response = rag_chain.run(query)
print(response)