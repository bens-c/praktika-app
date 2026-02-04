import smtplib, time
from email.message import EmailMessage
from firmen import firmen

EMAIL = "b9848411@gmail.com"
PASSWORT = "kfrp odjm skkm wmrc"

BETREFF = "Schülerpraktikum Game-/App-Entwicklung (16.03.–02.04.)"

TEXT = """Liebes Entwicklerteam,

mein Name ist Benjamin Schroeder und ich besuche derzeit die 8. Klasse der Stadtteilschule Oldenfelde in Hamburg.
Hiermit bewerbe ich mich um ein Schülerpraktikum im Zeitraum vom 16. März bis 2. April im Bereich Game-, App- oder Webentwicklung.

Ich interessiere mich sehr für Programmierung, Spieleentwicklung und Webdesign und entwickle in meiner Freizeit eigene kleine Spiele, Webseiten und Apps.

Über eine Rückmeldung würde ich mich sehr freuen.

Mit freundlichen Grüßen
Benjamin Schroeder
"""

msg_template = EmailMessage()
msg_template["From"] = EMAIL
msg_template["Subject"] = BETREFF
msg_template.set_content(TEXT)

# PDF anhängen
with open("Benjamin_Schroeder_Lebenslauf.pdf", "rb") as f:
    pdf_data = f.read()

msg_template.add_attachment(
    pdf_data,
    maintype="application",
    subtype="pdf",
    filename="Benjamin_Schroeder_Lebenslauf.pdf"
)

with open("zeugnis_Benjamin_7Klasse_2HJ.pdf", "rb") as f:
    pdf_data = f.read()

msg_template.add_attachment(
    pdf_data,
    maintype="application",
    subtype="pdf",
    filename="Zeugnis_Benjamin_7Klasse_2HJ.pdf"
)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, PASSWORT)

for firma, mail in firmen:
    msg = msg_template.clone()
    msg["To"] = mail
    server.send_message(msg)
    print(f"📨 Gesendet an {firma}")
    time.sleep(15)

server.quit()
print("✅ Alle Bewerbungen wurden verschickt.")
