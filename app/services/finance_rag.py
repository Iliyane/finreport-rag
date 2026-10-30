from __future__ import annotations

import os

from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.multi_modal_llms.openai import OpenAIMultiModal

load_dotenv()


def build_multimodal_llm():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing. Set it in the environment or .env file.")
    return OpenAIMultiModal(model="gpt-4o", api_key=api_key, max_new_tokens=300)


def query_table_images(table_dir: str, prompt: str):
    if not os.path.exists(table_dir) or not os.listdir(table_dir):
        raise FileNotFoundError("No table images were found in the target directory.")

    llm = build_multimodal_llm()
    image_documents = SimpleDirectoryReader(table_dir).load_data()

    chat_message = ChatMessage(
        role=MessageRole.USER,
        content=prompt,
        additional_kwargs={"image_documents": image_documents},
    )

    response = llm.chat([chat_message])
    return response.message.content
