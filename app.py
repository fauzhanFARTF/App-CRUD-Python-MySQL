import mysql.connector
 
 
koneksi = mysql.connector.connect(
  host="localhost",
  user="root",
  password="m4suk4j4h",
  database="dbpython_first"
)
 
 
mycursor = koneksi.cursor()
 
lanjut = True
while lanjut:
    print("")
    print("")
    print("")
    print("CRUD User")
    print("1.LIHAT USER")
    print("2.TAMBAH USER")
    print("3.UBAH USER")
    print("4.HAPUS USER")
    print("5.SEARCH")
    print("6.KELUAR")
    print("")
     
 
    p = int(input("SILAHKAN PILIH MENU : "))
    print("")
    print("")
    if(p == 1):
        mycursor.execute("SELECT * FROM user")
        myresult = mycursor.fetchall()
        print("====== ANDA BERADA DI MENU LIHAT SELURUH USER ========")
        print("(id,nama,email,no hp)")
        for x in myresult:
            print(x)
    elif(p == 2):
        print("========== ANDA BERADA DI MENU TAMBAH USER ============")
        nama = input("MASUKAN NAMA : ")
        email = input("MASUKAN EMAIL : ")
        no_hp = input("MASUKAN NO HP : ")
        sql = "INSERT INTO user (nama, email,no_hp) VALUES (%s, %s,%s)"
        val = (nama, email,no_hp)
        mycursor.execute(sql, val)
        koneksi.commit()
        print(mycursor.rowcount, "data user berhasil di tambah")
    elif(p == 3):
        print("=========== ANDA BERADA DI MENU EDIT USER ==============")
        id = input("MASUKAN ID USER :")
        mycursor.execute("SELECT * FROM user where id ="+id+" LIMIT 1")
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x
        if(user != None):
            nama = input("NAMA AWAL ("+user[1]+") AKAN DIGANTI MENJADI : ") or user[1]
            email = input("EMAIL AWAL ("+user[2]+") AKAN DIGANTI MENJADI : ") or user[2]
            no_hp = input("NO HP AWAL ("+user[3]+") :AKAN DIGANTI MENJADI  ") or user[3]
            sql = "UPDATE user SET nama=%s,email=%s,no_hp=%s WHERE id=%s"
            val = (nama, email,no_hp,id)
            mycursor.execute(sql, val)
            koneksi.commit()
            print(mycursor.rowcount, "data user berhasil di simpan")
        else:
            print("data tidak ditemukan")
    elif(p == 4):
        print("=========== ANDA BERADA DI MENU HAPUS USER ==============")
        id = input("MASUKAN ID USER :")
        mycursor.execute("SELECT * FROM user where id ="+id+" LIMIT 1")
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x
        if(user != None):
            print("MENGHAPUS DATA :",user)
            sql = "DELETE FROM user WHERE id="+id
            mycursor.execute(sql)
            koneksi.commit()
            print(mycursor.rowcount, "data user berhasil di hapus")
        else:
            print("data tidak ditemukan")
    elif(p == 5):
        print("=========== ANDA BERADA DI MENU CARI USER ==============")
        id = input("MASUKAN ID USER :")
        mycursor.execute("SELECT * FROM user where id ="+id+" LIMIT 1")
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x
             
        if(user != None):
            print(user)

        else:
            print("data tidak ditemukan")
    elif(p == 6):
        lanjut = False