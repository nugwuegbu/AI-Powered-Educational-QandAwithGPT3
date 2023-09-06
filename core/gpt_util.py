import os
import openai

openai.api_key = os.environ.get('API_KEY')

class GPTUtil:

    @staticmethod
    def search_query(query_data):
        s_query = query_data['search_text']
        result = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = s_query,
            max_tokens = 256,
            temperature = 0.5,
            n = 1,
            stop = None
        )
        return result