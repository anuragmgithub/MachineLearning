# llm/llm.py

import openai

class LLM:
    """
    Simple wrapper for OpenAI GPT LLM for RAG.
    """

    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        """
        Initialize the LLM wrapper.
        :param api_key: OpenAI API key
        :param model: OpenAI model to use
        """
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key

    def generate_answer(self, query: str, retrieved_chunks: list, max_tokens: int = 500) -> str:
        """
        Generate an answer using LLM based on retrieved chunks.
        :param query: User query
        :param retrieved_chunks: List of TextChunk objects retrieved by retriever
        :param max_tokens: Maximum tokens in the answer
        :return: Generated answer string
        """
        # Combine retrieved chunks into context
        context = "\n\n".join([chunk.text for chunk in retrieved_chunks])

        # Prepare prompt for LLM
        prompt = (
            f"You are a financial expert assistant. Use the following context to answer the query.\n\n"
            f"Context:\n{context}\n\n"
            f"Query: {query}\n\n"
            f"Answer in a clear and concise manner."
        )

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=0.2
            )

            answer = response.choices[0].message.content.strip()
            return answer

        except Exception as e:
            print("Error generating answer:", e)
            return "Could not generate answer at this time."
