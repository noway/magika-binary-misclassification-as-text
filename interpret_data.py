import os
import shutil

data = open("magika_misclassifications.txt", "r").read()

lines = data.strip().split("\n")

file_dict = {}
for line in lines:
    file, filetype = line.split(": ")
    file_dict[file] = filetype


sorted_dict = dict(sorted(file_dict.items(), key=lambda item: item[1]))

i = 1
last_value = ""
for key, value in sorted_dict.items():
    if not ("(code)" in value) and not ("(text)" in value):
        continue
    slug_value = value.replace("(code)", "").replace("(text)", "").strip()
    slug_value = slug_value.replace(" ", "_").lower()
    slug_value = slug_value.replace("(", "").replace(")", "")

    if last_value != value:
        i = 1

    print(f"{slug_value}: {key}")

    if not os.path.exists(f"result/{slug_value}"):
        os.makedirs(f"result/{slug_value}")
    shutil.copy(key, f"result/{slug_value}/sample_{i}")
    i += 1
    last_value = value

print("Written to result/ folder successfully")
