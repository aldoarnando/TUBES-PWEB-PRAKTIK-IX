from project.app import client

def getAnswerAI(umur_bulan:int, hasil_bb_u, hasil_tb_u, hasil_imt_u):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    'role': 'user',
                    'content': 
                        f"""
                        Berikan rekomendasi pola makan ataupun pola hidup pada anak berusia {umur_bulan} bulan jika:
                        1. hasil diagnosis berat badan: {hasil_bb_u}
                        2. hasil diagnosis stunting: {hasil_tb_u}
                        3. hasil diagnosis gizi: {hasil_imt_u}
                        jawablah dalam bentuk paragraf dan sertakan referensi anda dalam memberikan rekomendasi di akhir setelah anda membuat semua list rekomendasi, gunakan referensi yang kuat.
                        """
                } 
            ],
            model="llama-3.3-70b-versatile",
            stream=False
        )
        
        ai_answer = chat_completion.choices[0].message.content.replace("**", "").replace("*", "")
        return ai_answer.split("\n")
    except Exception:
        return "Maaf, saat ini AI tidak tersedia untuk memberikan rekomendasi. Silahkan coba lagi nanti".split()