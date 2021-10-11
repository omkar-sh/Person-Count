# import os

# image_files = []
# os.chdir(os.path.join("data", "person_detect"))
# for filename in os.listdir(os.getcwd()):
#     if filename.endswith(".PNG"):
#         image_files.append("data/person_detect/" + filename)
# os.chdir("..")
# with open("train.txt", "w") as outfile:
#     for image in image_files:
#         outfile.write(image)
#         outfile.write("\n")
#     outfile.close()
# os.chdir("..")
import os
dir = 'C:/Omkar.Uttarwar/Dataset/Bus_Poc/person_detect'
list = []
for filename in os.listdir(dir):
	if filename.endswith(".txt"):
		with open(dir +'/'+filename, "r") as file:
			lines = file.readlines()
		for line in lines:
			if line[0] not in list:
				list.append(line[0])
print(list)
			# if line[0] != str(0):
			# 	print(line[0])
			# 	print(filename)
        #image_files.append("data/person_detect/" + filename)