import argparse
from crypto_ai_baseline import run_trading_for_coin_timeframe  # aparte functie aanmaken

parser = argparse.ArgumentParser()
parser.add_argument("--coin")
parser.add_argument("--timeframe")
parser.add_argument("--mode", choices=["live", "test"], default="test")
args = parser.parse_args()

run_trading_for_coin_timeframe(args.coin, args.timeframe, args.mode)
