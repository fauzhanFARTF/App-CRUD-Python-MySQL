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
    print("CRUD DATA MAHASISWA")
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
        mycursor.execute("SELECT nim, nama, jurusan FROM user")
        myresult = mycursor.fetchall()
        print("====== ANDA BERADA DI MENU LIHAT SELURUH MAHASISWA ========")
        print("(nim,nama,jurusan)")
        for x in myresult:
            print(x)
    elif(p == 2):
        print("========== ANDA BERADA DI MENU TAMBAH USER ============")
        nim = input("MASUKAN NIM : ")
        nama = input("MASUKAN NAMA : ")
        jurusan = input("MASUKAN JURUSAN : ")
        sql = "INSERT INTO user (nim, nama,jurusan) VALUES (%s, %s,%s)"
        val = (nim, nama,jurusan)
        mycursor.execute(sql, val)
        koneksi.commit()
        print(mycursor.rowcount, "data user berhasil di tambah")
    elif(p == 3):
        print("=========== ANDA BERADA DI MENU EDIT MAHASISWA ==============")
        nim = input("MASUKAN NIM : ")
        mycursor.execute("SELECT nim, nama, jurusan FROM user where nim ='%s'"%(nim)+" LIMIT 1")
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x
        if(user != None):
            nama = input("NAMA AWAL ("+user[1]+") AKAN DIGANTI MENJADI : ") or user[1]
            jurusan = input("JURUSAN AWAL ("+user[2]+") AKAN DIGANTI MENJADI : ") or user[2]
            sql = "UPDATE user SET nama=%s,jurusan=%s WHERE nim=%s"
            val = (nama, jurusan,nim)
            mycursor.execute(sql, val)
            koneksi.commit()
            print(mycursor.rowcount, "data user berhasil di update")
        else:
            print("data tidak ditemukan")
    elif(p == 4):
        print("=========== ANDA BERADA DI MENU HAPUS MAHASISWA ==============")
        nim = input("MASUKAN NIM : ")
        mycursor.execute("SELECT nim, nama, jurusan FROM user where nim ='%s'"%(nim))
        myresult = mycursor.fetchall()
        user = None
        for x in myresult:
            user = x
        if(user != None):
            print("MENGHAPUS DATA : ",user)
            sql = "DELETE FROM user WHERE nim ='%s'"%(nim)
            mycursor.execute(sql)
            koneksi.commit()
            print(mycursor.rowcount, "data user berhasil di hapus")
        else:
            print("data tidak ditemukan")
    elif(p == 5):
        print("=========== ANDA BERADA DI MENU CARI MAHASISWA ==============")
        nim = input("MASUKAN NIM : ")
        mycursor.execute("SELECT nim, nama, jurusan FROM user where nim ='%s'"%(nim))
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