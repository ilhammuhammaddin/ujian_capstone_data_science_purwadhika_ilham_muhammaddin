listBuku = [
    {
        'judul buku': 'Buku X',
        'stock': 20,
        'biaya sewa': 5000
    },
    {
        'judul buku': 'Buku Y',
        'stock': 15,
        'biaya sewa': 6000
    },
    {
        'judul buku': 'Buku Z',
        'stock': 25,
        'biaya sewa': 5000
    }
]

def menampilkanDaftarBuku() :
    def keseluruhanstock():
        if listBuku == []:
            print('--Tidak ada buku yang tersedia--')
            return menampilkanDaftarBuku()
        else:
            print ('--Berikut data keseluruhan stock buku--')
            print('Index\t| Judul Buku  \t| Stock\t| Biaya sewa')
            for i in range(len(listBuku)) :
                print('{}\t| {}  \t| {}\t| {}'.format(i,listBuku[i]['judul buku'],listBuku[i]['stock'],listBuku[i]['biaya sewa']))
            return menampilkanDaftarBuku()

    def mencaribukuberdasarkanindex():
        if listBuku == []:
            print('--Tidak ada buku yang tersedia--')
            return menampilkanDaftarBuku()
            
        caribuku = int(input ('Masukkan Index Buku :'))
        indexing = caribuku

        if caribuku >= len(listBuku):
            print('--Buku yang anda cari tidak ada, berikut daftar buku yang tersedia: --')
            print('Index\t| Judul Buku  \t| Stock\t| Biaya sewa')
            for i in range(len(listBuku)) :
                print('{}\t| {}  \t| {}\t| {}'.format(i,listBuku[i]['judul buku'],listBuku[i]['stock'],listBuku[i]['biaya sewa']))
            return menampilkanDaftarBuku()

        caribuku = listBuku[caribuku]
        for i in listBuku:
            if caribuku == i :
                print ('--Berikut data buku yang anda cari--')
                print('Index\t| Judul Buku  \t| Stock\t| Biaya sewa')
                print('{}\t| {}  \t| {}\t| {}'.format(indexing,listBuku[indexing]['judul buku'],listBuku[indexing]['stock'],listBuku[indexing]['biaya sewa']))
                return menampilkanDaftarBuku()

    while True :
        pilihanreaddata = input('''
        #List Menu Menampilkan Daftar Buku :
        1. Keseluruhan Stock buku
        2. Mencari buku berdasarkan index
        3. Kembali ke menu utama

        Masukkan angka Menu yang ingin dijalankan : ''')
            
        if (pilihanreaddata == '1'):
            keseluruhanstock()
            break
            
        elif (pilihanreaddata == '2'):
            mencaribukuberdasarkanindex()
            break
            
        elif (pilihanreaddata == '3') :
            kembaliutama = input ('Apakah anda ingin kembali ke menu utama ? (YA/TIDAK) =')
            if (kembaliutama == 'YA') :
                break
        else :
            print('--Pilihan yang anda masukkan salah, Silahkan input ulang--')

def menambahBuku() :
    def tambahstockbuku():
        iBuku = int(input('Masukkan Index Buku : '))
        indxing = iBuku

        if iBuku >= len(listBuku) :
            namaBuku = str(input('Masukkan Nama Buku :'))
            stockBuku = int(input('Masukkan Stock Buku : '))
            biayasewa = int(input('Masukkan Biaya Sewa Buku : '))
            listBuku.append({
            'judul buku': namaBuku,
            'stock': stockBuku,
            'biaya sewa': biayasewa})
            print ('--Tambahan buku telah tersimpan--')
            return menambahBuku()
        
        iBuku = listBuku[iBuku]
        for i in listBuku:
            if iBuku == i:
                print('--Buku dengan index tersebut sudah ada, berikut datanya :--')
                print('Index\t| Judul Buku  \t| Stock\t| Biaya sewa')
                print('{}\t| {}  \t| {}\t| {}'.format(indxing,listBuku[indxing]['judul buku'],listBuku[indxing]['stock'],listBuku[indxing]['biaya sewa']))
                return menambahBuku()
    
    while True :
        pilihantambahbuku = input ('''
        #List Menu Tambah Buku :
        1. Tambah stock buku
        2. Kembali ke menu utama
        
        Masukkan angka Menu yang ingin dijalankan : ''')
        if (pilihantambahbuku == '1'):
            tambahstockbuku()
            break
        elif (pilihantambahbuku == '2'):
            kembaliutama = input ('Apakah anda ingin kembali ke menu utama ? (YA/TIDAK) =')
            if (kembaliutama == 'YA') :
                break
        else :
            print('--Menu yang anda masukkan salah, silahkan input ulang--')

def mengubahdatabuku ():
    def updatebuku():
        if listBuku == []:
            print('--Tidak ada buku yang tersedia--')
            return mengubahdatabuku()
        else :
            ubahbuku = int(input('Masukkan index buku yang datanya ingin dirubah :'))
            indexubah = ubahbuku

            if ubahbuku >= len(listBuku):
                print('--Buku yang anda cari tidak ada, berikut daftar buku yang tersedia--')
                print('Index\t| Judul Buku  \t| Stock\t| Biaya sewa')
                for i in range(len(listBuku)) :
                    print('{}\t| {}  \t| {}\t| {}'.format(i,listBuku[i]['judul buku'],listBuku[i]['stock'],listBuku[i]['biaya sewa']))
                return mengubahdatabuku ()
    
            ubahbuku = listBuku [ubahbuku]
            for i in listBuku:
                if ubahbuku == i:
                    print('Index\t| Judul Buku  \t| Stock\t| Biaya sewa')
                    print('{}\t| {}  \t| {}\t| {}'.format(indexubah,listBuku[indexubah]['judul buku'],listBuku[indexubah]['stock'],listBuku[indexubah]['biaya sewa']))
                    pastiubah = input('Apakah anda yakin ingin mengubah data buku ini? (YA/TIDAK) =')
                    if (pastiubah == 'TIDAK'):
                        return mengubahdatabuku()
                    namabuku = str(input('Masukkan Nama Baru Buku :'))
                    stockbuku = int(input('Masukkan Stock Baru Buku : '))
                    biayasewa = int(input('Masukkan Biaya Sewa Baru Buku : '))
                    listBuku[indexubah] =({
                    'judul buku': namabuku,
                    'stock': stockbuku,
                    'biaya sewa': biayasewa})
                    print ('--Update buku telah tersimpan--')
                    return mengubahdatabuku()

    while True :
        pilihanupdate = input ('''
        #List Menu Update Buku :
        1. Update data buku
        2. Kembali ke menu utama
        
        Masukkan angka Menu yang ingin dijalankan : ''')
        if(pilihanupdate == '1'):
            updatebuku()
            break
        elif(pilihanupdate == '2'):
            kembaliutama = input ('Apakah anda ingin kembali ke menu utama ? (YA/TIDAK) =')
            if (kembaliutama == 'YA') :
                break
        else :
            print('--Menu yang anda masukkan salah, silahkan input ulang--')

def menghapusbuku():
    def kurangstockbuku():
        if listBuku == []:
            print('--Tidak ada buku yang tersedia--')
            return menghapusbuku()
        else :
            kBuku = int(input('Masukkan Index Buku : '))
            indxin = kBuku

            if kBuku >= len(listBuku) :
                print('--Buku yang anda cari tidak ada, berikut daftar buku yang tersedia: --')
                print('Index\t| Judul Buku  \t| Stock\t| Biaya sewa')
                for i in range(len(listBuku)) :
                    print('{}\t| {}  \t| {}\t| {}'.format(i,listBuku[i]['judul buku'],listBuku[i]['stock'],listBuku[i]['biaya sewa']))
                return menghapusbuku()
        
            kBuku = listBuku[kBuku]
            for i in listBuku:
                if kBuku == i:
                    print('Index\t| Judul Buku  \t| Stock\t| Biaya sewa')
                    print('{}\t| {}  \t| {}\t| {}'.format(indxin,listBuku[indxin]['judul buku'],listBuku[indxin]['stock'],listBuku[indxin]['biaya sewa']))
                    pastiubah = input('Apakah anda yakin ingin menghapus data buku ini? (YA/TIDAK) =')
                    if (pastiubah == 'TIDAK'):
                        return menghapusbuku()
                    del listBuku [indxin]
                    print ('--Buku yang anda pilih sudah terhapus--')
                    return menghapusbuku()
    
    while True :
        pilihankurangbuku = input ('''
        #List Menu Hapus Buku :
        1. Hapus stock buku
        2. Kembali ke menu utama
        
        Masukkan angka Menu yang ingin dijalankan : ''')
        if (pilihankurangbuku == '1'):
            kurangstockbuku()
            break
        elif (pilihankurangbuku == '2'):
            kembaliutama = input ('Apakah anda ingin kembali ke menu utama ? (YA/TIDAK) =')
            if (kembaliutama == 'YA') :
                break
        else :
            print('--Menu yang anda masukkan salah, silahkan input ulang--')
          
while True :
    pilihanMenu = input('''
        ===Selamat Datang di Perpustakaan Qwerty===

        #List Menu :
        1. Menu Daftar Buku
        2. Menambah Buku
        3. Mengubah Data Buku
        4. Menghapus Buku
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        menampilkanDaftarBuku()
    elif(pilihanMenu == '2') :
        menambahBuku()
    elif(pilihanMenu == '3') :
        mengubahdatabuku()
    elif(pilihanMenu == '4') :
        menghapusbuku()
    elif(pilihanMenu == '5') :
        break
    else : 
        print('\n\t--Pilihan yang anda masukkan salah, Silahkan input ulang--')

    
