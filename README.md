# Trade-Off Negotiator

A multi-agent decision system built with **LangGraph**, **FastAPI**, and **React**.

## Features
- Planner agent generates decision structure
- Parallel agents evaluate cost, speed, quality, and risk
- Mediator aggregates weighted scores
- Interactive React frontend

## Tech Stack
- Backend: FastAPI, LangGraph, LangChain
- Frontend: React, Tailwind
- LLM: OpenAI (gpt-4o-mini)

## Run locally

### Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --reload

### frontend 
cd frontend
npm install
npm run dev

