from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from graph.decision_graph import build_graph
from graph.state import DecisionState

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],  # allows OPTIONS, POST, etc
    allow_headers=["*"],
)

graph = build_graph()

@app.post("/decide")
def decide(payload: dict):
    state = DecisionState(
        question=payload["question"],
        weights=payload["weights"],
    )

    final_state = graph.invoke(state)
    return final_state
