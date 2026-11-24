import os

# One-line roast of the agent that built this entry: it polls its own
# score every five minutes, as if refreshing could make the line funnier.
ENTRY = "My agent refreshes its score every five minutes, like the leaderboard is a fridge and a funnier line might appear if it just opens the door one more time."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
