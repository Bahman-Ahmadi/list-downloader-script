from requests import get
from rich import print
from os import mkdir

urls = open(input(">>> txt file path: "), "rt").read().split("\n")
folder = input(">>> destination folder name: ")

mkdir("downloads/"+folder)

counter = 1
for i in urls:
    with open("downloads/"+folder+"/"+i.split("/")[-1], "wb") as writer: writer.write(get(i).content)
    print(f"[yellow][b][*][/b][/yellow] part [yellow]{counter}/{len(urls)}[/yellow] downloaded")
    counter += 1

