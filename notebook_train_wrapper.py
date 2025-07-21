import argparse
from crypto_ai_baseline import run_training_for_coin_timeframe  # hernoemde functie uit notebook

parser = argparse.ArgumentParser()
parser.add_argument("--coin")
parser.add_argument("--timeframe")
parser.add_argument("--epochs", type=int, default=20)
parser.add_argument("--model", default="LSTM")
args = parser.parse_args()

run_training_for_coin_timeframe(args.coin, args.timeframe, args.epochs, args.model)
