data = json.load(open("d.json"))
data["men"] = menPref
data["women"] = womenPref
with open("d.json", "w") as f:
    json.dump(data, f, indent=4)