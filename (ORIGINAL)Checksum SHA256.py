import hashlib
import sys
import os
import platform
from tkinter import filedialog
import tkinter as tk

# from progress.bar import Bar

message = ''

hashTypes = ['sha256', 'md5', 'sha1']

sysPath = sys.path[0]

root = tk.Tk()
root.attributes('-topmost', 1)
root.geometry("500x150")
root.withdraw()

system = platform.system()

if system != 'Windows':
    filePath = filedialog.askopenfilename(initialdir="~/", title="Select File")
else:
    filePath = filedialog.askopenfilename(initialdir="C:\\Users\\", title="Select File")

root.update()

fileSize = os.path.getsize(filePath)
print("File selected: " + filePath)
print("\nfile is: " + str(fileSize) + " bytes\n")


def SHA256(filePath):
    """"This function returns the SHA-1 hash
    of the file passed into it"""
    print("Processing SHA256...")

    # make a hash object
    h = hashlib.sha256()

    # open file for reading in binary mode
    with open(filePath, 'rb') as file:

        # loop till the end of the file
        chunk = 0
        iteration = 0
        onePercent = fileSize / 100
        while chunk != b'':
            if iteration == onePercent:
                print(iteration)
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            # every 1024 bytes
            iteration += 1024
            h.update(chunk)
    # return the hex representation of digest
    return h.hexdigest()


def MD5(filePath):
    print("processing MD5...")

    h = hashlib.md5()

    with open(filePath, 'rb') as file:
        chunk = 0

        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)

        return h.hexdigest()


def SHA1(filePath):
    print("processing SHA1...")

    h = hashlib.sha1()

    with open(filePath, 'rb') as file:
        chunk = 0

        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)

        return h.hexdigest()


def filetypesha256():
    message = SHA256(filePath)
    check_sum_text.delete('1.0', tk.END)
    check_sum_text.insert(tk.END, message)


def filetypesha1():
    message = SHA1(filePath)
    check_sum_text.delete('1.0', tk.END)
    check_sum_text.insert(tk.END, message)


def filetypemd5():
    message = MD5(filePath)
    check_sum_text.delete('1.0', tk.END)
    check_sum_text.insert(tk.END, message)


def exit():
    sys.exit()


root.deiconify()
root.after_idle(root.attributes, '-topmost', 0)
root.lift()

root.update()

check_sum_text = tk.Text(root, height=2, width=64)
check_sum_text.pack()

sha256 = tk.Button(root, text="SHA256", command=filetypesha256)
sha256.pack()

sha1 = tk.Button(root, text="SHA1", command=filetypesha1)
sha1.pack()

md5 = tk.Button(root, text="MD5", command=filetypemd5)
md5.pack()

exitprogram = tk.Button(root, text="EXIT", command=exit)
exitprogram.pack()

root.mainloop()
