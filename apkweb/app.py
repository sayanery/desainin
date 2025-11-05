import streamlit as st
from utils.api import get_dribbble_designs, get_figma_templates, chat_with_glm
from utils.favorite import load_favorites, save_favorite
import json

# ========== KONFIGURASI ==========
DRIBBBLE_TOKEN = "YOUR_DRIBBBLE_TOKEN"
FIGMA_TOKEN = "YOUR_FIGMA_TOKEN"
FIGMA_FILE_ID = "YOUR_FIGMA_FILE_ID"
GLM_API_KEY = "YOUR_GLM_API_KEY"

# ========== SIDEBAR NAVIGATION ==========
st.sidebar.title("🎨 Design Chatbot Navigation")
menu = st.sidebar.radio("Pilih Halaman:", ["💬 Chatbot", "🔥 Tren Desain", "⭐ Favorite"])

# ========== HALAMAN CHATBOT ==========
if menu == "💬 Chatbot":
    st.title("🤖 Design Assistant Chatbot")
    query = st.text_input("Masukkan ide desainmu:")
    if st.button("Cari & Generate"):
        with st.spinner("Mencari inspirasi desain..."):
            nlp_response = chat_with_glm(f"Buatkan deskripsi desain {query}", GLM_API_KEY)
            st.markdown(f"**AI Insight:** {nlp_response}")

            drib_results = get_dribbble_designs(query, DRIBBBLE_TOKEN)
            if drib_results:
                st.subheader("🎨 Hasil dari Dribbble:")
                for d in drib_results[:3]:
                    st.image(d["images"]["normal"], caption=d["title"])
                    if st.button(f"❤️ Favorite: {d['title']}"):
                        save_favorite(d["title"])

            figma_results = get_figma_templates(query, FIGMA_TOKEN, FIGMA_FILE_ID)
            if figma_results:
                st.subheader("📐 Template dari Figma:")
                for f in figma_results[:3]:
                    st.write(f"- {f.get('name')}")

# ========== HALAMAN TREN DESAIN ==========
elif menu == "🔥 Tren Desain":
    st.title("🔥 Tren Desain Terbaru")
    try:
        with open("assets/trend.json", "r") as f:
            data = json.load(f)
            for item in data["trends"]:
                st.image(item["image"], caption=item["title"])
    except:
        st.error("File trend.json tidak ditemukan!")

# ========== HALAMAN FAVORITE ==========
elif menu == "⭐ Favorite":
    st.title("⭐ Desain Favorit Kamu")
    favorites = load_favorites()
    if favorites:
        for f in favorites:
            st.write(f"❤️ {f}")
    else:
        st.info("Belum ada desain favorit disimpan.")
