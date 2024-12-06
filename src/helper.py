from src.prompt import system_instruction
from groq import Groq

client = Groq()

messages = [
    {"role": "system", "content": system_instruction}
]
def ask_order(messages, model='llama3-8b-8192', temperature=0):
    chat_completion = client.chat.completions.create(
        #
        # Required parameters
        #
        messages=messages,

        # The language model which will generate the completion.
        model=model,

        #
        # Optional parameters
        #

        # Controls randomness: lowering results in less random completions.
        # As the temperature approaches zero, the model will become deterministic
        # and repetitive.
        temperature=temperature,

        # The maximum number of tokens to generate. Requests can use up to
        # 2048 tokens shared between prompt and completion.
        max_tokens=1024,

        # Controls diversity via nucleus sampling: 0.5 means half of all
        # likelihood-weighted options are considered.
        top_p=1,

        # A stop sequence is a predefined or user-specified text string that
        # signals an AI to stop generating content, ensuring its responses
        # remain focused and concise. Examples include punctuation marks and
        # markers like "[end]".
        # For this example, we will use ", 6" so that the llm stops counting at 5.
        # If multiple stop values are needed, an array of string may be passed,
        # stop=[", 6", ", six", ", Six"]
        stop=", 6",

        # If set, partial message deltas will be sent.
        stream=False,
    )
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content
    # Print the completion returned by the LLM.
    