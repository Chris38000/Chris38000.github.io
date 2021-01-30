f = open("email.html")
text = f.read()
f.close()

b = [{
	"pseudo": "007",
	"ip": "127",
	"css": "style1.css",
	"file": "email1.html"
},
{
	"pseudo": "Balthazar",
	"ip": "0",
	"css": "style.css",
	"file": "email2.html"
},
{
	"pseudo": "MrX",
	"ip": "0",
	"css": "style2.css",
	"file": "email3.html"
},
{
	"pseudo": "Luigi",
	"ip": "1",
	"css": "style3.css",
	"file": "email4.html"
}]

for a in b:
	f = open(a["file"], "w")
	f.write(text.replace("{pseudo}", a["pseudo"]).replace("{ip}", a["ip"]).replace("{css}", a["css"]))
	f.close()