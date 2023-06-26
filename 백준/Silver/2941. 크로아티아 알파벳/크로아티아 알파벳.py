word = input()

croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for item in croatia:
    word= word.replace(item,"#")

print(len(word))