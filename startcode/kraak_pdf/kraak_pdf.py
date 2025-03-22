import pikepdf
from tqdm import tqdm

passwords = []
for wachtwoord in open("woorden.txt"):
    passwords.append(wachtwoord.strip())

for wachtwoord in tqdm(passwords):
    try:
        pikepdf.open("hacking.pdf", password=wachtwoord)
        print("Het gevonden wachtwoord is:", wachtwoord)
        break
    except:
        pass
        #print("fout wachtwoord")