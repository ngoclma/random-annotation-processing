import os
import random
from datetime import datetime
from datetime import timedelta

time_format_str = "%Y%m%d-%H%M%S"

dir = ""
origins = os.listdir(dir)

# change raffle_city time (+8)
def change(inp):
    # string to datetime & plus 8
    time = inp[3:18]
    time_obj = datetime.strptime(time, time_format_str)
    time_add = time_obj + timedelta(hours=8)
    # final time to string
    time_final = datetime.strftime(time_add, time_format_str)
    # create replace string
    out = inp
    out = out.replace(time, time_final)
    # rename
    inp = dir + inp
    out = dir + out
    print(inp)
    print(out)
    print("---")
    os.rename(inp, out)


# change time format for Excel calculation
def format1(txt):
    txt = txt[12:21] + "000"
    dt = datetime.strptime(txt, "%H%M%S%f")
    dt_txt = datetime.strftime(dt, "%H:%M:%S.%f")
    dt_txt = dt_txt[0:12]
    print(dt_txt)


# list name to merge small videos to 2-hour video
def merge(inps):
    file_dir = "/videos.txt"
    f = open(file_dir, "w")
    for i in range(0, 13):
        # txt = "file 'xxx/{fname}'".format(fname = inps[i])
        txt = inps[i]
        print(txt[3:21])
        f.write(txt)
        f.write("\n")
    f.close()


# list timestamp of videos
def listName(inps):
    file_dir = dir + "/namelist.txt"
    f = open(file_dir, "w")
    for inp in inps:
        if inp.endswith(".mp4") or inp.endswith(".avi"):
            op = inp.find("2022") + 8
            ed = op + 6
            txt = inp + "," + inp[op:ed]
            f.write(txt)
            f.write("\n")


# split to train val test
def splitRandom(dir):
    f_all = dir + "/train_copy.txt"
    f_train = dir + "/train_.txt"
    f_val = dir + "/val_.txt"
    f_test = dir + "/test_.txt"

    # create random list
    f = open(f_all, "r")
    imgs = f.readlines()
    imgs_len = len(imgs)
    print(imgs_len)
    random.shuffle(imgs)
    f = open(f_all, "w")
    for img in imgs:
        f.write(img)

    # split to train
    train_len = int(imgs_len * 0.6)
    print(train_len)
    f = open(f_train, "w")
    for i in range(0, train_len):
        f.write(imgs[i])

    # split to val
    val_len = int(imgs_len * 0.2)
    print(val_len)
    f = open(f_val, "w")
    for i in range(train_len, train_len + val_len):
        f.write(imgs[i])

    # split to test
    test_len = imgs_len - train_len - val_len
    print(test_len)
    f = open(f_test, "w")
    for i in range(train_len + val_len, imgs_len):
        f.write(imgs[i])


# split to train val test but test is the first 20%
def splitTestFirst(dir):
    f_all = dir + "/train_copy.txt"
    f_train = dir + "/train_.txt"
    f_val = dir + "/val_.txt"
    f_test = dir + "/test_.txt"

    # read list
    f = open(f_all, "r")
    imgs = f.readlines()
    imgs_len = len(imgs)
    print(imgs_len)

    # split to test
    test_len = int(imgs_len * 0.2)
    print(test_len)
    f = open(f_test, "w")
    for i in range(0, test_len):
        f.write(imgs[i])

    # create random list
    imgs_new = imgs[test_len:imgs_len]
    random.shuffle(imgs_new)
    f = open(f_all, "w")
    for img in imgs_new:
        f.write(img)

    # split to train
    train_len = int(imgs_len * 0.6)
    print(train_len)
    f = open(f_train, "w")
    for i in range(0, train_len):
        f.write(imgs_new[i])

    # split to val
    val_len = imgs_len - train_len - test_len
    print(val_len)
    f = open(f_val, "w")
    for i in range(train_len, train_len + val_len):
        f.write(imgs_new[i])


if __name__ == "__main__":
    # RENAME
    for origin in origins:
        change(origin)

    # MERGE
    # print(len(origins))
    # origins.sort()
    # merge(origins)

    # SPLIT
    # splitRandom()
    # splitTestFirst(dir)

    # LIST NAME
    # origins.sort()
    # listName(origins)
