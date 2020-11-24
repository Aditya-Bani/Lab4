# lab-4
## Latihan 1
![soal-latihan-1](assets/img/tugas-praktikum-4/latihan1/1.png)

**Code:**

![sc-latihan-1](assets/img/tugas-praktikum-4/latihan1/2.png)

**Penjelasan:**
* ``a = [1, 3, 5, 7, 9] `` list a dengan 5 elemen

Akses list
* ``print(a[2])`` menampilkan elemen ke - 3
* ``print(a[1:3])`` mengambil nilai elemen ke 2 sampai elemen ke 4
* ``print(a[4])`` mengambil elemen terakhir

ubah elemen list
* ``a[3] = 4`` mengubah elemen ke 4 dengan nilai lainnya
* ``a[3:5] = [8, 10]`` mengubah elemen ke 4 sampai dengan elemen terakhir

tambah elemen list
* ``b = a [0:2]`` mengambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
* ``b.append('halo')`` menambah list B dengan nilai string
* ``b.extend([10, 20, 30])`` menambah list B dengan 3 nilai
* ``x = a + b`` menggabungkan list B dengan list A

**Output:**

![output-latihan-1](assets/img/tugas-praktikum-4/latihan1/3.png)

## Tugas Praktikum 4
![soal-praktikum-1](assets/img/tugas-praktikum-4/tugas-praktikum/1.png)

**Code:**

![sc-praktikum-1](assets/img/tugas-praktikum-4/tugas-praktikum/2.png)

**Penjelasan:**
* ``data = []`` Membuat list kosong yang nanti akan di isi
* ``while ulangi =='y':`` Membuat perulangan dengan variabel ``ulangi``, dimana ketika memilih 'y' maka akan otomatis mengulang pengisian data
* ``nilai_akhir = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100`` Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)
* ``data.append([nama, nim, nilai_tugas, nilai_uts, nilai_uas, int(nilai_akhir)])`` Memasukkan variabel input ke dalam list data
* ``ulangi = (input('tambah data?(y/t)'))`` Ketika memilih 't' ``if ulangi == 't':`` maka cetaklah hasil

**Output:**

![output-praktikum-1](assets/img/tugas-praktikum-4/tugas-praktikum/3.png)

**Flowchart:**


<div align="center">
  <img alt="flowchart-praktikum-1" src="assets/img/tugas-praktikum-4/tugas-praktikum/4.png" />
</p>
