from os import rename, listdir

fnames = listdir("./pngs/")

count = 1
for fname in fnames:
    if fname.endswith(".png"):
        print("./pngs/"+fname)
        #rename("./pngs/"+fname, "./pngs/"+fname.replace(str(idx).zfill(5), str(3036-idx).zfill(5)))
        count += 1
        
print(count)

idx = 1
for fname in fnames:
    if fname.endswith(".png"):
        print("./pngs/"+fname.replace(str(idx).zfill(5), str(count-idx).zfill(5)).replace(".png", "_rev.png"))
        reverse_fname = "./pngs/"+fname.replace(str(idx).zfill(5), str(count-idx).zfill(5)).replace(".png", "_rev.png")
        rename("./pngs/"+fname, reverse_fname)
        idx += 1

fnames = listdir("./pngs/")
for fname in fnames:
    if fname.endswith(".png"):
        rename("./pngs/"+fname, "./pngs/"+fname.replace("_rev.png", ".png"))


