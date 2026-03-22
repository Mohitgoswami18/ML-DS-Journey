from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "TeichAI/Qwen3-14B-Claude-4.5-Opus-High-Reasoning-Distill-GGUF",
    task= "text-generation"
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("What is the capital of France?")

print(result)