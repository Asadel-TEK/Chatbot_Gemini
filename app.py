from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# ... (konfigurasi model Gemini dan prompt_parts sama seperti sebelumnya)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input.lower() in ["keluar", "exit"]:
            return "Chat berakhir. Refresh halaman untuk memulai lagi."
        if not user_input.strip():
            return render_template("index.html", error="Silakan masukkan pertanyaan yang valid.")

        # Deteksi salam
        if user_input.lower() in ["halo", "hai", "selamat pagi", "selamat siang", "selamat sore", "selamat malam"]:
            return render_template("index.html", response="Disdagrin: Selamat datang! Ada yang bisa saya bantu?")

        try:
            response = model.generate_content(prompt_parts + [user_input])
            return render_template("index.html", response=response.text)
        except Exception as e:
            return render_template("index.html", error="Maaf, terjadi kesalahan: {}".format(e))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
