


print("**********Please Register First!**********")

sys_username = (input(" Please Enter The User Name: "))

sys_password = (input(" Please Enter The Password: "))

print("***Registration Successful!***")

print("Please Login")

print("**********User Login**********")



giris_hakki = 5

while True:
    username = input("User Name: ")
    password = input("Password: ")

    if username != sys_username and password == sys_password :
        print("Incorrect Username!")
        giris_hakki -=1
        
            

        
    elif username != sys_username and password != sys_password :
        print("Username and Password Incorrect!")
        giris_hakki -=1
        

        

        
    elif username == sys_username and password  != sys_password :
        print("Incorrect Password!")
        giris_hakki -=1
        
        
        
        
    else :
        print("Login Successful!")
        break
    
    if ( giris_hakki == 0 ) :
         
         print("Please Try Again!")
not_database = {}
while True :

    print("**********Please Select Transaction**********")

    print("0:Çıkış")
    print("1:Takdir Teşekkür Hesaplama")
    select = input("İşlem Giriniz")
    if select == "0" :
        print ("Başarılı Bir Şekilde Çıkış Yapıldı")
        break

    if select == "1" :
        print("*****Takdir Teşekkür Hesaplama*****")
    while True :
        m1 = float(input("Matematik Birinci Sınav Notunuzu Giriniz:"))
        if not (0 <= m1 <= 100):
            print("Hatalı Not Girişi: Lütfen 0 ile 100 arasında bir not girin.")
            continue

        m2 = float(input("Matematik İkinci Sınav Notunuzu Giriniz:"))
        if not (0 <= m2 <= 100):
            print("Hatalı Not Girişi: Lütfen 0 ile 100 arasında bir not girin.")
            continue

        m3 = float(input("Matematik Üçüncü Sınav Notunuzu Giriniz:"))
        if not (0 <= m3 <= 100):
            print("Hatalı Not Girişi: Lütfen 0 ile 100 arasında bir not girin.")
            continue

 
        mort = (m1 + m2 + m3) / 3

        s1 = float(input("Sosyal Birinci Sınav Notunuzu Giriniz: "))
        if not (0 <= s1 <= 100):
            print("Hatalı Not Girişi: Lütfen 0 ile 100 arasında bir not girin.")
            continue
        s2 = float(input("Sosyal İkinci Sınav Notunuzu Giriniz: "))
        if not (0 <= s2 <= 100):
            print("Hatalı Not Girişi: Lütfen 0 ile 100 arasında bir not girin.")
            continue
        s3 = float(input("Sosyal Üçüncü Sınav Notunuzu Giriniz: "))
        if not (0 <= s3 <= 100):
            print("Hatalı Not Girişi: Lütfen 0 ile 100 arasında bir not girin.")
            continue

        sort = (s1 + s2 + s3) / 3

        t1 = float(input("Türkçe Birinci Sınav Notunuzu Giriniz: "))
        if not (0 <= t1 <= 100):
            print("Hatalı Not Girişi: Lütfen 0 ile 100 arasında bir not girin.")
            continue
        
        t2 = float(input("Türkçe İkinci Sınav Notunuzu Giriniz: "))
        if not (0 <= t2 <= 100):
            print("Hatalı Not Girişi: Lütfen 0 ile 100 arasında bir not girin.")
            continue
        t3 = float(input("Türkçe Üçüncü Sınav Notunuzu Giriniz: "))
        if not (0 <= t3 <= 100):
            print("Hatalı Not Girişi: Lütfen 0 ile 100 arasında bir not girin.")
            continue
         
        tort = (t1 + t2 + t3) / 3

        f1 = float(input("Fen Birinci Sınav Notunuzu Giriniz: "))
        if not (0 <= f1 <= 100):
            print("Hatalı Not Girişi: Lütfen 0 ile 100 arasında bir not girin.")
            continue
        f2 = float(input("Fen İkinci Sınav Notunuzu Giriniz: "))
        if not (0 <= f2 <= 100):
            print("Hatalı Not Girişi: Lütfen 0 ile 100 arasında bir not girin.")
            continue
        f3 = float(input("Fen Üçüncü Sınav Notunuzu Giriniz: "))
        if not (0 <= f3 <= 100):
            print("Hatalı Not Girişi: Lütfen 0 ile 100 arasında bir not girin.")
            continue

        fort = (f1 + f2 + f3) / 3


        dönemort = (mort + sort + fort) / 3


        print("Dönem Ortalamanız:",round(dönemort, 3))

        if (dönemort >= 85 ):
            print("Tebrikler Takdir Belgesi Kazandınız!")
            break
        elif ( 70 <= dönemort < 85):
            print("Tebrikler Teşekkür Belgesi Kazandınız!")
            break
        else:
            print("Belge Kazanamadınız.")
            break

