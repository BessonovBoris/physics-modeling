import os

for root, dirs, files in os.walk("."):
    for filename in files:
        new_name = filename.replace("_", "-")

        print(filename, new_name)

        os.rename(os.path.join(root, filename), os.path.join(root, new_name))

        # if filename.split("_")[-1].split(".")[0] == "compressed":
        #     # new_name_arr = filename.split("_")[:-1] + [filename.split(".")[-1]]
        #     # new_name = ""
        #     #
        #     # for i in range(len(new_name_arr)):
        #     #     new_name += new_name_arr[i]
        #     #     if i == len(new_name_arr) - 2:
        #     #         new_name += "."
        #     #     elif i < len(new_name_arr) - 2:
        #     #         new_name += "_"
        #
        #     os.rename(os.path.join(root, filename), os.path.join(root, new_name))
