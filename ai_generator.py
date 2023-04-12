from abc import abstractmethod
import openai

class AIGenerator:

    @abstractmethod
    def generate(self, system_prompt, user_prompt):
        pass


class OpenAI(AIGenerator):

    def generate(self, system_prompt, user_prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
        )
        return response.choices[0].message['content']
