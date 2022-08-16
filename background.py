import requests
db = input("Enter UniProt Database : (UniProtKB/UniRef/UniParc)\n")
qu = input("Enter UniProtID : ")
tp = input("Enter file type : (Text/fasta/xml)")
#url = "https://rest.uniprot.org/uniprotkb/P12345.txt"
r = requests.get("https://rest.uniprot.org/"+db.lower()+"/"+qu+"."+tp.lower())
f = open("scrap2out.txt","w")
f.write(r.text)
f.close


