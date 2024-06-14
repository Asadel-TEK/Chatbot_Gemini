import google.generativeai as genai

genai.configure(api_key="")

# Set up the model
generation_config = {
  "temperature": 0.5,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
    "dinas: layanan",
    "penjelasan dinas perdangan: Perindustrian Verifikasi Ijin pada OSS, Validasi Cek Lokasi Usaha Industri, Surat Keterangan Pelaku Industri, Surat Pengantar Pengiriman Asal Barang, Pendaftaran Akun SIINas, Sertifikat TKDN. Perdagangan Perdagangan Luar Negeri & Perdagangan Dalam Negeri.Metrologi perizinan Alat - Alat Ukur, Takar, Timbang dan Perlengkapannya (UTTP)",
   "dinas: tentang kami",
    "penjelasan dinas perdangan: Website Resmi Dinas Perdagangan dan Perindustrian Kabupaten Kotawaringin Timur. Kantor Jalan Jenderal Sudirman 6,7 Sampit, Kalimantan Tengah Kode Pos 74322",
    "dinas: informasi publik",
    "penjelasan dinas perdangan: belom ada isi",
    "dinas: harga daging",
    "penjelasan dinas perdangan: harga sapi bahan dalam pada tanggal 25 oktober tahun 2023 per kilo adalah 160000",
    "dinas: kepala dinas ",
    "penjelasan dinas perdangan:pemimpin dinas perdagangan kabupaten kotawaringin timur, Dr.Drs.H.zulhaidir,M.si. pembina  tingkat 1(IV/b). NIP 191611161994031006",
    "dinas: sekretaris",
    "penjelasan dinas perdangan: mohhammad ikhwan,s.t.,mm. pembina (IV/a). NIP 198006082009041001",
    "dinas: kepala sub bagian umum dan pelaporan",
    "penjelasan dinas perdangan: kamtini,s.e. penata tingkat I(III/d) NIP 197207221999022001",
    "dinas: kepala sub bagian keuangan dan perencanaan",
    "penjelasan dinas perdangan: Aulia rahman, S,psi., M.A.P penata tingkat 1(III/d) NIP 198508132008041002",
    "dinas: kepala bidang perdagangan",
    "penjelasan dinas perdangan:KASIYAN, SE.,MM pembina(IV/a) NIP 197309201993031004",
    "dinas: kepala bidang metrologi legal",
    "penjelasan dinas perdangan: TAUBA s,sos.,msi pembina(IV/a) NIP 196811151995121004",
    "dinas: kepala bidang perindustrian",
    "penjelasan dinas perdangan:rodi hartono, s.e.,m.t pembina (IV/a) NIP 196901122000031008",
]

while True:
    inputan = input("Anda: ")
    if inputan.lower() in ["keluar", "exit"]:
        break
    if not inputan.strip():
        print("Silakan masukkan pertanyaan yang valid.")
        continue

    # Deteksi salam
    if inputan.lower() in ["halo", "hai", "selamat pagi", "selamat siang", "selamat sore", "selamat malam"]:
        print("Disdagrin: Selamat datang! Ada yang bisa saya bantu?")
        continue

    try:
        response = model.generate_content(prompt_parts + [inputan])
        print("\nDisdagrin:", response.text)
    except Exception as e:
        print("Maaf, terjadi kesalahan:", e)