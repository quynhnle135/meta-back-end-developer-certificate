# with open('newfile.txt', mode='w') as file:
#     file.writelines(["I am having the biggest crush on Johnathan",
#                     "\nHere is another line for this file", "\nThe third one because why not"])

# with open('newfile.txt', 'r') as file:
#     data = file.readlines()
# for line in data:
#     print(line)
# file.close()

# with open('test.txt', 'r') as file:
#     lines = file.readlines()
# print(lines)

content = []
with open('sampletext.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        content.append(line)
print(content)
