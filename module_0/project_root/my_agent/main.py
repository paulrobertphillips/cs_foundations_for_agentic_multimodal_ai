import asyncio
from .config import AgentConfig
from .agent import run_agent

def main():
    cfg = AgentConfig(dataset_path="data.csv")
    result = asyncio.run(run_agent(cfg))
    # Pydantic model → plain dict
    print(result.model_dump())

if __name__ == "__main__":
    main()
