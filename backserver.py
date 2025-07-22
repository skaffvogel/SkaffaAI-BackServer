from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
import subprocess
import os

app = FastAPI()

class TrainRequest(BaseModel):
    coin: str
    timeframe: str
    epochs: int = 20
    model: str = "LSTM"

class TradeRequest(BaseModel):
    coin: str
    timeframe: str
    live: bool = False

@app.post("/train")
def train_model(req: TrainRequest):
    # Notebook script aanroepen met parameters
    cmd = f"python3 notebook_train_wrapper.py --coin {req.coin} --timeframe {req.timeframe} --epochs {req.epochs} --model {req.model}"
    subprocess.Popen(cmd, shell=True)
    return {"status": "started", "message": f"Training gestart voor {req.coin} [{req.timeframe}]"}

@app.post("/trade")
def trade(req: TradeRequest):
    mode = "live" if req.live else "test"
    cmd = f"python3 notebook_trade_wrapper.py --coin {req.coin} --timeframe {req.timeframe} --mode {mode}"
    subprocess.Popen(cmd, shell=True)
    return {"status": "started", "message": f"Trading gestart ({mode}) voor {req.coin} [{req.timeframe}]"}

@app.get("/metrics")
def get_metrics():
    if os.path.exists("metrics/metrics.csv"):
        with open("metrics/metrics.csv") as f:
            return {"metrics": f.read()}
    return {"error": "Metrics not found"}

@app.get("/status")
def status():
    return {"status": "ready"}

if __name__ == "__main__":
    port = int(os.environ.get("SERVER_PORT", 7860))
    uvicorn.run("backserver:app", host="0.0.0.0", port=port, reload=True)
