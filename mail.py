import bulkmail

mail = bulkmail.Email("example@gmail.com", "rogue-geek")

mail_list = [
    ['Georgette Lampron', 'example+user0@gmail.com', 'SCTCE', '2021/CMKR/TST000'],
    ['Luanna Hoose', 'example+user1@gmail.com', 'SCTCE', '2021/CMKR/TST001'],
    ['Madison Tarbell', 'example+user2@gmail.com', 'SCTCE', '2021/CMKR/TST002'],
    ['Rayna Usrey', 'example+user3@gmail.com', 'SCTCE', '2021/CMKR/TST003'],
    ['Jamison Napoles', 'example+user4@gmail.com', 'SCTCE', '2021/CMKR/TST004'],
    ['Alpha Auvil', 'example+user5@gmail.com', 'SCTCE', '2021/CMKR/TST005'],
    ['Lovie Abbott', 'example+user6@gmail.com', 'SCTCE', '2021/CMKR/TST006'],
    ['Denyse Trapani', 'example+user7@gmail.com', 'SCTCE', '2021/CMKR/TST007'],
    ['Dominica Zawacki', 'example+user8@gmail.com', 'SCTCE', '2021/CMKR/TST008'],
    ['Claire Hedlund', 'example+user9@gmail.com', 'SCTCE', '2021/CMKR/TST009'],
]

for person in mail_list:
    subject = f"TestMail | {person[0]}"
    message = f"""
    <html>
    <body>
        Dear {person[0]},<br>
        This is a test Email with an attachment.<br>
        <br>
        Thanks<br>
        rogue-geek
    </body>
    </html>
    """
    mail.newMail(person[1], person[0], subject, message)
    mail.attach(f"{person[0]}.jpg", "cert.jpg")
    mail.send()