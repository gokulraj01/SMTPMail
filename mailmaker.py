f = open("ids.txt", 'w+')

uname = "example"
udomain = "gmail.com"

fake_names = ["Georgette Lampron","Luanna Hoose","Madison Tarbell","Rayna Usrey","Jamison Napoles","Alpha Auvil","Lovie Abbott","Denyse Trapani","Dominica Zawacki","Claire Hedlund","Tyrell Besecker","Damon Brownlow","Billye Salvetti","Kristy Folkers","Brad Leclair","Minnie Suydam","Elva Schumann","Raven Tenner","Illa Kowalewski","Brandi Mcfall","Antony Marcantel","Celestine Sykes","Marx Pascal","Laticia Tome","Vanna Welker","Ezekiel Portwood","Bryanna Gillett","Laureen Difilippo","Many Dibella","Christeen Fong","Suzanne Crider","Tyler Pawlak","June Scogin","Garth Ho","Melynda Raff","Tegan Castaldo","Yon Claw","Luvenia Varnes","Ronna Brook","Maurine Ketchum","Giovanni Masden","Kelly Albin","Maud Dauenhauer","Tanisha Sievert","Sherita Pucci","Deana Tremaine","Mervin Santillo","Talia Bent","Marilyn Kivi","Edyth Deras"]

f.write("[")
for i in range(10):
    f.write(f"['{fake_names[i]}', '{uname}+user{i}@{udomain}', 'MyCollege', '2021/CMKR/TST{i:03}'],\n")
f.write("]")
f.close()