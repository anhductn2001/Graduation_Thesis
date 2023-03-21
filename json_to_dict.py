import random
import json

files = [
         "summary.json",
    ]

fps = {file: open(file, "wt") for file in files}

num_rows = dataset['test'].num_rows
num_test = 0

for i in range(num_rows):
    text = dataset['test'][i]['document']
    text_length = len(text.split(" "))
    if text_length > 1000:
        group = "test"
        num_test += 1
        summary = dataset['test'][i]['summary']
        summary_size = len(summary.split(" "))

        json_obj = {"text": text, "summary": summary}

        json.dump(
            json_obj["text"],
            fps["text" + ".json"],
            sort_keys=False,
            indent=None,
            ensure_ascii=False,
        )
        fps["text" + ".json"].write("\n")
        json.dump(
            json_obj["summary"],
            fps["summary" + ".json"],
            sort_keys=False,
            indent=None,
            ensure_ascii=False,
        )
        fps["summary" + ".json"].write("\n")

for fp in fps.values():
    fp.close()