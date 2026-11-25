import html
from datetime import datetime
from urllib.parse import quote
import streamlit as st

st.set_page_config(
    page_title="Asisten PSM UPTD PPKS",
    page_icon="💬",
    layout="centered",
)

# Ganti dengan nomor WhatsApp resmi UPTD PPKS (format: 628xxxxxxxxxx)
WA_NUMBER = "6288218511768"
WA_DEFAULT_TEXT = "Halo Admin UPTD PPKS, saya ingin berkonsultasi terkait layanan PSM."
WA_CHAT_URL = f"https://wa.me/{WA_NUMBER}?text={quote(WA_DEFAULT_TEXT)}"

LAYANAN_MENU = [
    {
        "id": 1,
        "short_title": "Menyampaikan Keluhan",
        "subtitle": "Pengaduan dan kendala pascapelatihan UPTD PPKS",
        "title": "1. Pengaduan dan Kendala Pascapelatihan UPTD PPKS",
        "desc": "Silakan isi formulir pengaduan atau kendala pascapelatihan melalui tautan resmi berikut:",
        "url": "https://forms.gle/MrDyxwdNafgqm48T8",
    },
    {
        "id": 2,
        "short_title": "Evaluasi Kinerja",
        "subtitle": "Evaluasi kinerja dan penerapan hasil pelatihan PSM",
        "title": "2. Evaluasi Kinerja dan Penerapan Hasil Pelatihan PSM – UPTD PPKS",
        "desc": "Silakan lengkapi formulir evaluasi kinerja dan penerapan hasil pelatihan PSM pada tautan berikut:",
        "url": "https://forms.gle/v4ZrYztwubocBZKA9",
    },
    {
        "id": 3,
        "short_title": "Konsultasi dan Informasi",
        "subtitle": "Layanan konsultasi dan informasi pelatihan UPTD PPKS",
        "title": "3. Layanan Konsultasi dan Informasi Pelatihan UPTD PPKS",
        "desc": "Ajukan pertanyaan konsultasi atau permintaan informasi pelatihan melalui tautan berikut:",
        "url": "https://forms.gle/89uYeZipe2RCAs6ZA",
    },
    {
        "id": 4,
        "short_title": "Laporan Perkembangan",
        "subtitle": "Laporan kegiatan dan perkembangan lapangan PSM",
        "title": "4. Laporan Kegiatan dan Perkembangan Lapangan PSM – UPTD PPKS",
        "desc": "Kirimkan laporan kegiatan dan perkembangan lapangan PSM melalui formulir berikut:",
        "url": "https://forms.gle/Garg9q4zd5EzCWGy8",
    },
    {
        "id": 5,
        "short_title": "Hubungi Admin UPTD",
        "subtitle": "Permohonan tindak lanjut petugas admin UPTD PPKS",
        "title": "5. Permohonan Tindak Lanjut Petugas Admin – UPTD PPKS",
        "desc": "Ajukan permohonan tindak lanjut ke petugas admin UPTD PPKS melalui tautan berikut:",
        "url": "https://forms.gle/x3Cm6mYqAzLYHub46",
    },
]

st.markdown(
    """
<style>
.stApp {
    background-color: #eef3f2;
    color: #1f2937;
}
.block-container {
    width: 100% !important;
    max-width: 480px !important;
    background-color: #f8fafa;
    border: 1px solid #dce5e4;
    border-radius: 18px;
    padding: 1rem 1.1rem 6.5rem 1.1rem !important;
    margin-top: 1rem !important;
    margin-bottom: 1.5rem !important;
    box-shadow: 0 8px 28px rgba(15, 23, 42, 0.06);
    transition: all 0.2s ease;
}
header[data-testid="stHeader"] {
    background: transparent;
}
[data-testid="stBottom"], [data-testid="stBottom"] > div {
    background-color: #eef3f2 !important;
}
[data-testid="stChatInput"] {
    width: 100% !important;
    max-width: 480px !important;
    margin: 0 auto !important;
    background-color: #ffffff !important;
    border: 1px solid #cbd8d6 !important;
    border-radius: 14px !important;
}
[data-testid="stChatInput"] textarea {
    color: #1f2937 !important;
}

/* Responsif HP (<= 600px) */
@media (max-width: 600px) {
    .block-container {
        max-width: 100% !important;
        border-radius: 0 !important;
        border-left: none !important;
        border-right: none !important;
        margin-top: 0 !important;
        margin-bottom: 0 !important;
        padding: 0.85rem 0.85rem 6.5rem 0.85rem !important;
        box-shadow: none !important;
    }
    [data-testid="stChatInput"] {
        max-width: 100% !important;
        border-radius: 12px !important;
    }
    .psm-header {
        padding: 13px 14px !important;
        border-radius: 12px !important;
    }
    .psm-title {
        font-size: 14.5px !important;
    }
    .psm-subtitle {
        font-size: 11px !important;
    }
    .wa-fab {
        width: 50px !important;
        height: 50px !important;
        right: 16px !important;
        bottom: 84px !important;
    }
}

/* Responsif Tablet (601px - 1024px) */
@media (min-width: 601px) and (max-width: 1024px) {
    .block-container {
        max-width: 540px !important;
        border-radius: 20px !important;
        padding: 1.25rem 1.35rem 6.5rem 1.35rem !important;
        margin-top: 1.5rem !important;
        box-shadow: 0 12px 32px rgba(15, 23, 42, 0.08) !important;
    }
    [data-testid="stChatInput"] {
        max-width: 540px !important;
    }
}

/* Responsif Laptop / Desktop (>= 1025px) */
@media (min-width: 1025px) {
    .block-container {
        max-width: 470px !important;
        border-radius: 22px !important;
        padding: 1.2rem 1.25rem 6.5rem 1.25rem !important;
        margin-top: 1.4rem !important;
        box-shadow: 0 16px 40px rgba(15, 23, 42, 0.09) !important;
    }
    [data-testid="stChatInput"] {
        max-width: 470px !important;
    }
}

.psm-header {
    background: linear-gradient(135deg, #118a7e 0%, #0e766c 100%);
    padding: 15px 16px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    margin-bottom: 16px;
    box-shadow: 0 4px 12px rgba(17, 138, 126, 0.22);
}
.psm-header-left {
    display: flex;
    align-items: center;
    gap: 11px;
}
.psm-icon {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    border: 2px solid rgba(255, 255, 255, 0.85);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    font-size: 16px;
    flex-shrink: 0;
}
.psm-title {
    font-size: 15.5px;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.25;
}
.psm-subtitle {
    font-size: 11.5px;
    color: rgba(255, 255, 255, 0.88);
    margin-top: 2px;
}
.psm-online {
    background-color: rgba(255, 255, 255, 0.16);
    color: #a7f3d0;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.22);
    flex-shrink: 0;
}
.bubble-bot {
    background-color: #edf2f2;
    color: #1f2937;
    padding: 13px 15px;
    border-radius: 14px;
    border-top-left-radius: 4px;
    margin-bottom: 12px;
    font-size: 14px;
    line-height: 1.55;
    border: 1px solid #e0e8e7;
}
.bubble-user {
    background-color: #118a7e;
    color: #ffffff;
    padding: 10px 14px;
    border-radius: 14px;
    border-top-right-radius: 4px;
    margin-bottom: 10px;
    margin-left: auto;
    max-width: 85%;
    font-size: 14px;
    line-height: 1.45;
    box-shadow: 0 2px 6px rgba(17, 138, 126, 0.18);
}
.bubble-title {
    font-weight: 700;
    font-size: 14.5px;
    color: #0f172a;
    margin-bottom: 4px;
    display: block;
}
.bubble-time {
    font-size: 10.5px;
    color: #64748b;
    text-align: right;
    margin-top: 6px;
}
.bubble-user .bubble-time {
    color: rgba(255, 255, 255, 0.82);
}
.form-url-box {
    background-color: #ffffff;
    padding: 9px 11px;
    border-radius: 8px;
    margin-top: 8px;
    font-family: monospace;
    font-size: 12px;
    color: #0e766c;
    word-break: break-all;
    border: 1px solid #cbe0dd;
}

/* Tombol WhatsApp melayang (hanya logo) */
.wa-fab {
    position: fixed;
    right: 24px;
    bottom: 92px;
    width: 54px;
    height: 54px;
    border-radius: 50%;
    background-color: #25d366;
    display: flex;
    align-items: center;
    justify-content: center;
    text-decoration: none !important;
    box-shadow: 0 8px 20px rgba(37, 211, 102, 0.36);
    border: 2px solid #ffffff;
    z-index: 999;
    transition: transform 0.18s ease, box-shadow 0.18s ease, background-color 0.18s ease;
}
.wa-fab:hover {
    transform: translateY(-3px) scale(1.04);
    background-color: #20bd5a;
    box-shadow: 0 12px 24px rgba(37, 211, 102, 0.45);
}

div.stButton > button,
button[data-testid="stBaseButton-secondary"] {
    width: 100% !important;
    display: flex !important;
    justify-content: flex-start !important;
    align-items: center !important;
    text-align: left !important;
    background-color: #ffffff !important;
    color: #1e293b !important;
    border: 1px solid #dce5e4 !important;
    border-radius: 12px !important;
    padding: 13px 42px 13px 16px !important;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04) !important;
    position: relative !important;
    transition: all 0.15s ease !important;
}
div.stButton > button::after {
    content: "";
    position: absolute;
    right: 15px;
    top: 50%;
    transform: translateY(-50%);
    width: 18px;
    height: 18px;
    opacity: 0.65;
    background-repeat: no-repeat;
    background-size: contain;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='%23475569' stroke-width='1.8'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' d='M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z'/%3E%3C/svg%3E");
}
div.stButton > button > div,
div.stButton > button [data-testid="stMarkdownContainer"] {
    width: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: flex-start !important;
    text-align: left !important;
}
div.stButton > button p:first-child {
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    margin: 0 0 5px 0 !important;
    font-size: 14.5px !important;
    font-weight: 700 !important;
    color: #1e293b !important;
    text-align: left !important;
    line-height: 1.3 !important;
}
div.stButton > button p:first-child strong:first-child {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 24px !important;
    height: 24px !important;
    min-width: 24px !important;
    border-radius: 50% !important;
    background-color: #e6eceb !important;
    color: #334155 !important;
    font-size: 12px !important;
    font-weight: 700 !important;
}
div.stButton > button p:nth-child(2) {
    width: 100% !important;
    margin: 0 !important;
    font-size: 12.5px !important;
    font-weight: 400 !important;
    color: #64748b !important;
    line-height: 1.4 !important;
    text-align: left !important;
}
div.stButton > button p:only-child {
    margin: 0 !important;
    color: #0e766c !important;
    font-weight: 600 !important;
    font-size: 13.5px !important;
}
div.stButton > button:hover {
    background-color: #f0faf8 !important;
    border-color: #118a7e !important;
    transform: translateY(-1px);
}
div[data-testid="stLinkButton"] > a {
    background-color: #118a7e !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
    border: none !important;
    box-shadow: 0 2px 8px rgba(17, 138, 126, 0.25) !important;
}
div[data-testid="stLinkButton"] > a:hover {
    background-color: #0e766c !important;
}
</style>
""",
    unsafe_allow_html=True,
)


def now_str() -> str:
    return datetime.now().strftime("%H:%M")


def add_menu_message():
    st.session_state.messages.append(
        {
            "role": "bot",
            "title": "Halo, Bapak/Ibu PSM! 👋",
            "text": "Selamat datang di layanan pemantauan dan evaluasi pascapelatihan UPTD PPKS.\n\nSilakan pilih layanan yang ingin Anda gunakan (atau ketik angka 1–5):",
            "time": now_str(),
            "show_menu": True,
            "show_back": False,
        }
    )


def select_service(service_id: int, user_label: str | None = None):
    layanan = next((item for item in LAYANAN_MENU if item["id"] == service_id), None)
    if not layanan:
        return

    if user_label:
        st.session_state.messages.append(
            {
                "role": "user",
                "text": user_label,
                "time": now_str(),
            }
        )

    st.session_state.messages.append(
        {
            "role": "bot",
            "title": layanan["title"],
            "text": layanan["desc"],
            "form_url": layanan["url"],
            "time": now_str(),
            "show_menu": False,
            "show_back": True,
        }
    )


if "messages" not in st.session_state:
    st.session_state.messages = []
    add_menu_message()

st.markdown(
    '<div class="psm-header">'
    '<div class="psm-header-left">'
    '<div class="psm-icon">💬</div>'
    '<div>'
    '<div class="psm-title">Asisten PSM UPTD PPKS</div>'
    '<div class="psm-subtitle">Layanan informasi dan pemantauan pascapelatihan</div>'
    '</div>'
    '</div>'
    '<div class="psm-online">Online</div>'
    '</div>',
    unsafe_allow_html=True,
)

for idx, msg in enumerate(st.session_state.messages):
    if msg["role"] == "user":
        safe_text = html.escape(msg["text"])
        st.markdown(
            f'<div class="bubble-user"><div>{safe_text}</div><div class="bubble-time">{msg["time"]} ✓✓</div></div>',
            unsafe_allow_html=True,
        )
    else:
        html_parts = ['<div class="bubble-bot">']
        if msg.get("title"):
            html_parts.append(f'<span class="bubble-title">{html.escape(msg["title"])}</span>')
        formatted_text = html.escape(msg.get("text", "")).replace("\n", "<br>")
        html_parts.append(f'<div>{formatted_text}</div>')
        if msg.get("form_url"):
            html_parts.append(f'<div class="form-url-box">{html.escape(msg["form_url"])}</div>')
        html_parts.append(f'<div class="bubble-time">{msg["time"]}</div>')
        html_parts.append('</div>')

        st.markdown("".join(html_parts), unsafe_allow_html=True)

        if msg.get("form_url"):
            st.link_button(
                "Buka Google Form ↗",
                msg["form_url"],
                use_container_width=True,
            )

        if msg.get("show_menu"):
            for item in LAYANAN_MENU:
                card_label = f"**{item['id']}** **{item['short_title']}**\n\n{item['subtitle']}"
                if st.button(
                    card_label,
                    key=f"menu_{idx}_{item['id']}",
                    use_container_width=True,
                ):
                    select_service(
                        item["id"],
                        user_label=f"{item['id']}. {item['short_title']}",
                    )
                    st.rerun()

        if msg.get("show_back"):
            if st.button(
                "↩ Kembali ke Menu Awal",
                key=f"back_{idx}",
                use_container_width=True,
            ):
                st.session_state.messages.append(
                    {
                        "role": "user",
                        "text": "↩ Kembali ke Menu Awal",
                        "time": now_str(),
                    }
                )
                add_menu_message()
                st.rerun()

safe_wa_url = html.escape(WA_CHAT_URL, quote=True)
safe_wa_title = html.escape(f"Chat WhatsApp ({WA_CHAT_URL})")
wa_svg = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" '
    'fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 '
    '8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 '
    '8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>'
    '</svg>'
)

st.markdown(
    f'<a class="wa-fab" href="{safe_wa_url}" target="_blank" rel="noopener noreferrer" '
    f'aria-label="{safe_wa_title}" title="{safe_wa_title}">{wa_svg}</a>',
    unsafe_allow_html=True,
)

user_input = st.chat_input("Ketik angka 1–5 atau 'menu'...")
if user_input:
    cleaned = user_input.strip()
    lower = cleaned.lower()

    if cleaned in {"1", "2", "3", "4", "5"}:
        select_service(int(cleaned), user_label=cleaned)
        st.rerun()
    elif any(k in lower for k in ["menu", "awal", "halo", "hai", "mulai"]):
        st.session_state.messages.append(
            {"role": "user", "text": cleaned, "time": now_str()}
        )
        add_menu_message()
        st.rerun()
    else:
        st.session_state.messages.append(
            {"role": "user", "text": cleaned, "time": now_str()}
        )
        st.session_state.messages.append(
            {
                "role": "bot",
                "text": "Maaf, silakan pilih angka 1 sampai 5 atau tekan tombol di bawah untuk membuka Menu Utama.",
                "time": now_str(),
                "show_menu": False,
                "show_back": True,
            }
        )
        st.rerun()