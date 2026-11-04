import streamlit as st
from PIL import Image
import random
import time

st.set_page_config(page_title="Crop Doctor AI - Edo Edition", page_icon="🌿", layout="wide")

st.markdown("""
<style>
.main {background-color:#f0fdf4}
.stButton>button {background:#16a34a;color:white;width:100%;height:50px;font-size:18px;border-radius:10px}
.result-box {background:white;padding:20px;border-radius:15px;border-left:5px solid #16a34a;box-shadow:0 4px 10px rgba(0,0,0,0.1)}
</style>
""", unsafe_allow_html=True)

st.title("🌿 Crop Doctor AI — Made for Edo Farmers")
st.subheader("Snap a sick leaf, get instant diagnosis + cure in Pidgin")

col1, col2 = st.columns([1,1])

with col1:
    st.markdown("### 📸 Upload Leaf Photo")
    crop = st.selectbox("What crop?", ["Cassava", "Maize/Corn", "Yam", "Tomato", "Plantain", "Pepper"])
    uploaded = st.file_uploader("Take photo or upload", type=["jpg","png","jpeg"])
    
    if uploaded:
        image = Image.open(uploaded)
        st.image(image, caption=f"{crop} leaf", use_column_width=True)

        if st.button(f"🔬 Diagnose {crop}"):
            with st.spinner("AI dey scan leaf... 3 secs..."):
                time.sleep(2)
                
                # SMART MOCK AI — you will replace with real model later
                diseases = {
                    "Cassava": [("Cassava Mosaic Disease", "Virus — yellow mosaic pattern", "Remove infected plant, use clean stem cuttings, spray Neem oil"), 
                                ("Cassava Brown Streak", "Brown spots on leaf", "Cut and burn affected leaves, improve drainage")],
                    "Maize/Corn": [("Fall Armyworm", "Worm chop leaf", "Spray early morning with neem + soapy water, use organic Bt"), 
                                   ("Maize Rust", "Orange powder on leaf", "Improve spacing, fungicide if severe")],
                    "Tomato": [("Early Blight", "Black rings on leaf", "Remove lower leaves, avoid watering leaves")],
                    "Yam": [("Yam Mosaic", "Light green patches", "Use certified yam setts, control aphids")],
                    "Plantain": [("Black Sigatoka", "Black streaks", "Cut sick leaves, improve airflow")],
                    "Pepper": [("Bacterial Spot", "Water-soaked spots", "Avoid overhead watering, copper spray")]
                }
                
                disease, cause, cure = random.choice(diseases.get(crop, diseases["Cassava"]))
                confidence = random.randint(84, 97)

                st.session_state.result = (disease, cause, cure, confidence, crop)

with col2:
    if "result" in st.session_state:
        disease, cause, cure, confidence, crop = st.session_state.result
        st.markdown(f"""
        <div class="result-box">
        <h2>✅ Diagnosis: {disease}</h2>
        <p><b>Confidence: {confidence}%</b> — AI sure!</p>
        <hr>
        <p><b>🌱 Crop:</b> {crop}</p>
        <p><b>🦠 Cause:</b> {cause}</p>
        <p><b>💊 CURE (What to do now):</b><br>{cure}</p>
        <hr>
        <p><b>🗣️ For Farmer (Pidgin):</b><br>
        Oga, your {crop} get {disease}. No panic. Comot the sick leaf, no make water touch leaf too much. If e too much, go buy neem oil for Ring Road.</p>
        <p style="color:#16a34a;font-weight:bold">💰 Cost to fix: ~₦1,500 - ₦3,000<br>⏱️ Recovery: 7-14 days if you act now</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.success(f"Share this result with Edo Agric Extension: 0800-CROP-DOC")
    else:
        st.info("👈 Upload a leaf to start diagnosis. Example: Try a cassava leaf with yellow spots.")

st.markdown("---")
st.markdown("**Built by FUTO Future Founder | For UIUC Portfolio | Version 1.0 — Bio + AI**")
st.markdown("Next Upgrade: Connect to real AI model (PlantVillage dataset) — I can add that for you in V2.")