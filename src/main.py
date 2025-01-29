from datetime import datetime

currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# next part is taken from deepseek as I don't know how to create md files within another
with open("../docs/version.md", "w") as file:
    file.write(f"Last updated: {currentTime}")

