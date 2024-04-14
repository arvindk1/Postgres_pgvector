import os
import openai

# Set your OpenAI API key as an environment variable (replace with your actual key)
openai.api_key = os.getenv("OPENAI_API_KEY")

def list_embedding_models():
    """ Lists all available embedding models from the OpenAI API. """

    try:
        response = openai.Engine.list()
        embedding_models = [engine for engine in response.data if engine.id.startswith('text-embedding')]

        if embedding_models:
            print("Available embedding models:")
            for model in embedding_models:
                print(f"- {model.id} ({model.owner})")
        else:
            print("No embedding models found.")

    except openai.error.APIError as e:
        print(f"An API error occurred: {e}")

if __name__ == "__main__":
    list_embedding_models()
