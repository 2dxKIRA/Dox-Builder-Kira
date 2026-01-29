# ╔════════════════════════════════════════════════════════════════════════════════════════╗
# ║ MIT License                                                                            ║
# ║                                                                                        ║
# ║ Copyright (c) 2026 2DX NEWsociety                                                      ║
# ║                                                                                        ║
# ║ Permission is hereby granted, free of charge, to any person obtaining a copy           ║
# ║ of this software and associated documentation files (the "Software"), to deal          ║
# ║ in the Software without restriction, including without limitation the rights           ║
# ║ to use, copy, modify, merge, publish, distribute, sublicense, and/or sell              ║
# ║ copies of the Software, and to permit persons to whom the Software is                  ║
# ║ furnished to do so, subject to the following conditions:                               ║
# ║                                                                                        ║
# ║ The above copyright notice and this permission notice shall be included in all         ║
# ║ copies or substantial portions of the Software.                                        ║
# ║                                                                                        ║
# ║ THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR             ║
# ║ IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,               ║
# ║ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE            ║
# ║ AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                 ║
# ║ LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,          ║
# ║ OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE          ║
# ║ SOFTWARE.                                                                              ║
# ╚════════════════════════════════════════════════════════════════════════════════════════╝


# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx

import customtkinter as ctk# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
import tkinter.messagebox as messagebox# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
from tkinter import filedialog
import json

HACKER_ASCII_HEADER = r"""
    ▄█   ▄█▄  ▄█     ▄████████    ▄████████      ████████▄   ▄██████▄  ▀████    ▐████▀ 
    ███ ▄███▀ ███    ███    ███   ███    ███      ███   ▀███ ███    ███   ███▌   ████▀  
    ███▐██▀   ███▌   ███    ███   ███    ███      ███    ███ ███    ███    ███  ▐███    
  ▄█████▀     ███▌  ▄███▄▄▄▄██▀   ███    ███      ███    ███ ███    ███    ▀███▄███▀    
  ▀▀█████▄    ███▌ ▀▀███▀▀▀▀▀   ▀███████████      ███    ███ ███    ███    ████▀██▄     
    ███▐██▄   ███  ▀███████████   ███    ███      ███    ███ ███    ███   ▐███  ▀███    
    ███ ▀███▄ ███    ███    ███   ███    ███      ███   ▄███ ███    ███  ▄███     ███▄  
    ███   ▀█▀ █▀     ███    ███   ███    █▀       ████████▀   ▀██████▀  ████       ███▄ 
    ▀                ███    ███                                                         " 
"""

HACKER_ASCII_PREVIEW = r"""
dP     dP oo                      888888ba                    
88   .d8'                         88    `8b                   
88aaa8P'  dP 88d888b. .d8888b.    88     88 .d8888b. dP.  .dP 
88   `8b. 88 88'  `88 88'  `88    88     88 88'  `88  `8bd8'  
88     88 88 88       88.  .88    88    .8P 88.  .88  .d88b.  
dP     dP dP dP       `88888P8    8888888P  `88888P' dP'  `dP 
                                                                                                                    
"""

HACKER_ASCII = r"""
     ▄█   ▄█▄  ▄█     ▄████████    ▄████████      ████████▄   ▄██████▄  ▀████    ▐████▀ 
    ███ ▄███▀ ███    ███    ███   ███    ███      ███   ▀███ ███    ███   ███▌   ████▀  
    ███▐██▀   ███▌   ███    ███   ███    ███      ███    ███ ███    ███    ███  ▐███    
  ▄█████▀     ███▌  ▄███▄▄▄▄██▀   ███    ███      ███    ███ ███    ███    ▀███▄███▀    
 ▀▀█████▄     ███▌ ▀▀███▀▀▀▀▀   ▀███████████      ███    ███ ███    ███    ████▀██▄     
    ███▐██▄   ███  ▀███████████   ███    ███      ███    ███ ███    ███   ▐███  ▀███    
    ███ ▀███▄ ███    ███    ███   ███    ███      ███   ▄███ ███    ███  ▄███     ███▄  
    ███   ▀█▀ █▀     ███    ███   ███    █▀       ████████▀   ▀██████▀  ████       ███▄ 
    ▀                ███    ███                                                         " 
"""

class IdentityApp(ctk.CTk):
    def __init__(self):# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
        super().__init__()
        self.title("🟥 By 2dx 🦾")
        self.geometry("1100x800")
        ctk.set_appearance_mode("dark")# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
        ctk.set_default_color_theme("dark-blue")
        self.configure(fg_color="#0a0a0a")
        self.entries = {}
        self.create_widgets()    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx

    def create_widgets(self):
        # ASCII Art
        ascii_label = ctk.CTkLabel(self, text=HACKER_ASCII_HEADER, font=("Consolas", 13, "bold"), text_color="#ff2222", anchor="w", justify="left")
        ascii_label.pack(pady=(8, 0), anchor="w")
        subtitle = ctk.CTkLabel(self, text="🟥🦾 By 2dx 🦾🟥", font=("Consolas", 16, "bold"), text_color="#ff2222")
        subtitle.pack(pady=(0, 10))

        main_frame = ctk.CTkFrame(self)# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        # --- Ajout du scrollable frame à gauche ---
        left_container = ctk.CTkFrame(main_frame)
        left_container.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=5)
        left_canvas = ctk.CTkCanvas(left_container, bg="#0a0a0a", highlightthickness=0)    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
        left_canvas.pack(side="left", fill="both", expand=True)
        left_scrollbar = ctk.CTkScrollbar(left_container, orientation="vertical", command=left_canvas.yview)
        left_scrollbar.pack(side="right", fill="y")
        left_canvas.configure(yscrollcommand=left_scrollbar.set)
        left = ctk.CTkFrame(left_canvas)# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
        left_id = left_canvas.create_window((0, 0), window=left, anchor="nw")

        def _on_frame_configure(event):
            left_canvas.configure(scrollregion=left_canvas.bbox("all"))
        left.bind("<Configure>", _on_frame_configure)
        def _on_mousewheel(event):
            left_canvas.yview_scroll(int(-1*(event.delta/120)), "units")    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
        left_canvas.bind_all("<MouseWheel>", _on_mousewheel)

        right = ctk.CTkFrame(main_frame)
        right.pack(side="right", fill="both", expand=True, padx=(10, 0), pady=5)

        # Champs organisés par cohérence# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
        sections = [
            ("Identifiants", [
                ("🦾 Nom d'utilisateur", "username"),
                ("🟥 Nom d'affichage", "display_name"),
                ("📧 Email", "email"),
                ("🔑 Mot de passe", "password"),
                ("🔒 Mot de passe hashé", "hashed_password"),
                ("💬 Discord ID", "discord_id"),
            ]),
            ("Identité", [# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
                ("🧑‍💻 Nom de famille", "last_name"),
                ("🧑‍� Prénom", "first_name"),
                ("� Nom de naissance", "birth_name"),
                ("⚧️ Genre", "gender"),
                ("🎂 Date de naissance", "birth_date"),
                ("📅 Année de naissance", "birth_year"),
                ("🌍 Ville de naissance", "birth_city"),
                ("🆔 NIR", "ssn"),    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
                ("📝 Biographie", "bio"),
            ]),
            ("Famille", [
                ("👩 Soeur", "soeur"),
                ("👦 Frère", "frere"),
                ("👨 Père", "pere"),# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
                ("👩 Mère", "mere"),
                ("👧 Fille", "fille"),
                ("👦 Fils", "fils"),
                ("👪 Autre membre de la famille", "autre_famille"),
            ]),
            ("Coordonnées", [
                ("🏠 Adresse", "address"),
                ("🏷️ Code postal", "postal_code"),
                ("🏙️ Ville", "city"),
                ("� Numéro de téléphone", "phone"),
                ("🌐 Adresse IP", "ip_address"),
            ]),
            ("Finances & Véhicule", [# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
                ("🏦 IBAN", "iban"),
                ("🏦 BIC", "bic"),
                ("🚗 VIN / Plaque", "vin_plate"),    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
            ]),
            ("Réseaux & Système", [
                ("⛏️ UUID Minecraft", "uuid"),
            ]),
            ("Autre", [
                ("📝 Autre information supplémentaire", "autre_info"),
            ]),# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
        ]
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
        for section, fields in sections:
            sec_label = ctk.CTkLabel(left, text=f"🟥 [ {section} ] 🦾", font=("Consolas", 14, "bold"), text_color="#ff2222")
            sec_label.pack(anchor="w", pady=(10, 0))
            for label, key in fields:    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
                row = ctk.CTkFrame(left, fg_color="#111")
                row.pack(fill="x", pady=1)
                ctk.CTkLabel(row, text=label+":", width=180, anchor="w", font=("Consolas", 12), text_color="#ff2222").pack(side="left")
                entry = ctk.CTkEntry(row, width=260, font=("Consolas", 12), fg_color="#0a0a0a", text_color="#fff")
                entry.pack(side="left", fill="x", expand=True)    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
                self.entries[key] = entry

        # Actions
        actions = ctk.CTkFrame(left, fg_color="#111")
        actions.pack(pady=12)
        ctk.CTkButton(actions, text="💾 Enregistrer", command=self.save_identity, fg_color="#ff2222", text_color="#fff").pack(side="left", padx=4)
        ctk.CTkButton(actions, text="📂 Charger", command=self.load_identity, fg_color="#222", text_color="#ff2222").pack(side="left", padx=4)
        ctk.CTkButton(actions, text="🗑️ Réinitialiser", command=self.reset_form, fg_color="#0a0a0a", text_color="#fff", hover_color="#ff2222").pack(side="left", padx=4)

        # Aperçu
        # Plus d'ASCII art dans l'UI à droite, juste le champ texte
        self.preview_text = ctk.CTkTextbox(right, height=40, width=500, font=("Consolas", 12), fg_color="#0a0a0a", text_color="#ff2222")# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
        self.preview_text.pack(fill="both", expand=True)
        self.preview_text.configure(state="disabled")    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
        for entry in self.entries.values():
            entry.bind("<KeyRelease>", lambda e: self.update_preview())

    def update_preview(self):
        d = {k: e.get() for k, e in self.entries.items()}
        preview = (
f"{HACKER_ASCII_PREVIEW}\n"
f"🟥🦾===================[ IDENTIFIANTS ]===================🦾🟥\n"
f"🦾 Nom d'utilisateur : {d.get('username','')}\n"
f"🟥 Nom d'affichage   : {d.get('display_name','')}\n"
f"📧 Email             : {d.get('email','')}\n"
f"🔑 Mot de passe      : {d.get('password','')}\n"
f"🔒 Hashé             : {d.get('hashed_password','')}\n"
f"💬 Discord ID        : {d.get('discord_id','')}\n\n"    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
f"🟥🦾====================[ IDENTITÉ ]======================🦾🟥\n"
f"🧑‍💻 Nom de famille    : {d.get('last_name','')}\n"
f"🧑‍💻 Prénom            : {d.get('first_name','')}\n"
f"🧬 Nom de naissance  : {d.get('birth_name','')}\n"# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
f"⚧️ Genre             : {d.get('gender','')}\n"
f"🎂 Date de naissance : {d.get('birth_date','')}\n"
f"📅 Année naissance   : {d.get('birth_year','')}\n"
f"🌍 Ville naissance   : {d.get('birth_city','')}\n"
f"🆔 NIR               : {d.get('ssn','')}\n"
f"📝 Biographie        : {d.get('bio','')}\n\n"
f"🟥🦾====================[ FAMILLE ]=======================🦾🟥\n"
f"👩 Soeur             : {d.get('soeur','')}\n"
f"👦 Frère             : {d.get('frere','')}\n"
f"👨 Père              : {d.get('pere','')}\n"# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
f"👩 Mère              : {d.get('mere','')}\n"
f"👧 Fille             : {d.get('fille','')}\n"
f"👦 Fils              : {d.get('fils','')}\n"
f"👪 Autre membre      : {d.get('autre_famille','')}\n\n"
f"🟥🦾===================[ COORDONNÉES ]====================🦾🟥\n"
f"🏠 Adresse           : {d.get('address','')}\n"
f"🏷️ Code postal       : {d.get('postal_code','')}\n"
f"🏙️ Ville             : {d.get('city','')}\n"
f"📱 Téléphone         : {d.get('phone','')}\n"    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
f"🌐 Adresse IP        : {d.get('ip_address','')}\n\n"
f"🟥🦾==============[ FINANCES & VÉHICULE ]=================🦾🟥\n"# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
f"🏦 IBAN              : {d.get('iban','')}\n"
f"🏦 BIC               : {d.get('bic','')}\n"
f"🚗 VIN / Plaque      : {d.get('vin_plate','')}\n\n"
f"🟥🦾================[ RÉSEAUX & SYSTÈME ]=================🦾🟥\n"
f"⛏️ UUID Minecraft    : {d.get('uuid','')}\n\n"
f"🟥🦾=================[ AUTRE INFO ]=======================🦾🟥\n"
f"📝 Autre information : {d.get('autre_info','')}\n"
f"🟥🦾======================================================🦾🟥\n\n tool made by 2dx\n tool made by 2dx\n tool made by 2dx"
        )
        self.preview_text.configure(state="normal")
        self.preview_text.delete("1.0", "end")
        self.preview_text.insert("end", preview)
        self.preview_text.configure(state="disabled")# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx

    def save_identity(self):
        # Sauvegarder l'aperçu (preview) dans un fichier texte
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file:    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
            self.update_preview()  # S'assurer que l'aperçu est à jour
            preview_content = self.preview_text.get("1.0", "end").strip()
            with open(file, "w", encoding="utf-8") as f:
                f.write(preview_content)
            messagebox.showinfo("Succès", "Identité enregistrée dans un fichier texte !")# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx

    def load_identity(self):
        try:
            file = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
            if not file:
                return
            with open(file, "r", encoding="utf-8") as f:
                d = json.load(f)
            for k, e in self.entries.items():
                e.delete(0, "end")
                e.insert(0, d.get(k, ""))
            self.update_preview()    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
        except Exception as ex:
            pass# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx

    def reset_form(self):
        for e in self.entries.values():
            e.delete(0, "end")
        self.update_preview()

if __name__ == "__main__":
    app = IdentityApp()
    app.mainloop()# JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
    # JAI PASSER DU TEMPS A FAIR DONC MODIFI RIEN ET VOLE PAS JTE VOIS by 2dx
