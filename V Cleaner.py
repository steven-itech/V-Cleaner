import ctypes
import pyttsx3
import hashlib
import os
import requests
import subprocess
import wget
import tkinter as tk
import smtplib
import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox, Menu
from PIL import Image, ImageTk

ctypes.windll.kernel32.SetConsoleTitleW("V Cleaner :")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def tts(message):
    
    engine.say(message)
    engine.runAndWait()

if not ctypes.windll.shell32.IsUserAnAdmin():
    
    tts("Veuillez exécuter ce programme, via l'invite de commande en mode administrateur afin de pouvoir l'utiliser de manière optimale !")
    messagebox.showinfo(title="V Cleaner :", message="Veuillez exécuter ce programme, via l'invite de commande en mode adminstrateur afin de pouvoir l'utiliser de manière optimale !")
    
    quit()

def closing():

    pass

hash = "fbd90d911b1cb9be16d4cb6be6fc5aeabd7edb7193a09cf61c3a9abaef885000"

if ctypes.windll.shell32.IsUserAnAdmin():
    
    window_acces = tk.Tk()
    window_acces.title("Accès au programme.")
    window_acces.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico"))
    window_acces.geometry("600x400")
    window_acces.resizable(False, False)
    window_acces.protocol("WM_DELETE_WINDOW", closing)

    tk.Label(window_acces, text="Veuillez transmettre le code d'accès du programme afin de pouvoir l'utiliser : ", font=("Arial", 12)).pack(pady=10)
        
    code = tk.Entry(window_acces, font=("Arial", 12), width=40)
    code.pack(pady=5)

    def acces():
        
        code_input = code.get()

        sha256 = hashlib.sha256()
        sha256.update(code_input.encode("utf-8"))
                    
        input_hash = sha256.hexdigest()

        if input_hash == hash:
                    
            tts("Le code d'accès du programme est correct, vous pouvez dès à présent l'utiliser !")
            messagebox.showinfo(title="V Cleaner :", message="Le code d'accès du programme est correct, vous pouvez dès à présent l'utiliser !")

            window_acces.destroy()
                    
        else:
            
            tts("Ce code d'accès est invalide, veuillez réessayer !")
            messagebox.showerror(title="V Cleaner :", message="Ce code d'accès est invalide, veuillez réesayer !")

    tk.Button(window_acces, text="Valider !", command=acces, font=("Arial", 12)).pack(pady=10)

    window_acces.mainloop()

def clean():
    
    os.system("cls")

def avast_download():
    
    request = requests.get("https://www.google.com")
    statut = request.status_code

    if statut == 200:

        pass
    
    else:

        tts("Vous n'êtes pas connecté à Internet, veuillez vous connecter à un réseau Wi-Fi afin de pouvoir télécharger l'antivirus Avast !")
        messagebox.showwarning(title="Vous n'êtes pas connecté à Internet, veuillez vous connecter à un réseau Wi-Fi afin de pouvoir télécharger l'antivirus Avast !")
    
    tts("L'antivirus Avast est en cours de téléchargement !")
    messagebox.showinfo(title="Téléchargement et installation de l'antivirus Avast.", message="L'antivirus Avast est en cours de téléchargement !")
    
    url = "https://bits.avcdn.net/productfamily_ANTIVIRUS/insttype_APR/platform_WIN/installertype_ONLINE/"
    destination = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Avast.exe")
    
    avast_file = wget.download(url, destination)
    
    download = subprocess.Popen([avast_file], stdout=subprocess.PIPE)
    download.communicate()
    
    if download.returncode == 0:
        
        tts("L'antivirus Avast vient d'être installé sur votre ordinateur !")
        messagebox.showinfo(title="Téléchargement et installation de l'antivirus Avast.", message="L'antivirus Avast vient d'être installé sur votre ordinateur !")
    
    else:
        
        tts("L'antivirus Avast n'a pas pu être installé sur votre ordinateur !")
        messagebox.showerror(title="Téléchargement et installation de l'antivirus Avast.", message="L'antivirus Avast n'a pas pu être installé sur votre ordinateur !")

def avast():
    
    avast_path = r"C:\Program Files\AVAST Software\Avast"
    ash_cmd = os.path.join(avast_path, "ashCmd.exe")
    
    if os.path.exists(avast_path) and os.path.exists(ash_cmd):
        
        tts("Vous possédez l'antivirus Avast, ainsi que son scanner en ligne de commande sur votre ordinateur !")
        messagebox.showinfo(title="V Cleaner :", message="Vous possédez Avast, ainsi que son scanner en ligne de commande sur votre ordinateur !")
    
    else:
       
        tts("Vous ne possédez pas l'antivirus Avast, ainsi que son scanner en ligne de commande sur votre ordinateur !")
        messagebox.showwarning(title="V Cleaner :", message="Vous ne possédez pas l'antivirus Avast sur votre ordinateur, ainsi que son scanner en ligne de commande !")
        
        tts("Souhaitez-vous télécharger et installer l'antivirus Avast, ainsi que son scanner en ligne de commande ?")

        def yes():
            
            avast_download()
            avast_window.destroy()

        avast_window = tk.Tk()
        avast_window.title("Téléchargement et installation de l'antivirus Avast.")
        avast_window.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico"))
        avast_window.geometry("580x150")
        avast_window.resizable(False, False)

        label = tk.Label(avast_window, text="Souhaitez-vous télécharger et installer l'antivirus Avast, ainsi que son scanner en ligne de commande ?")
        label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        yes_button = tk.Button(avast_window, text="Oui !", command=yes)
        yes_button.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="e")

        no_button = tk.Button(avast_window, text="Non !", command=avast_window.destroy())
        no_button.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

        avast_window.mainloop()

def avast_system():
    
    tts("Cette opération peut prendre plusieurs minutes, souhaitez-vous continuer ?")

    def yes():
        
        avast_analysis_system()
        window_avast_system.destroy()

    window_avast_system = tk.Tk()
    window_avast_system.title("Analyse antivirus de votre ordinateur.")
    window_avast_system.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico"))
    window_avast_system.geometry("450x150")
    window_avast_system.resizable(False, False)
    
    label = tk.Label(window_avast_system, text="Souhaitez-vous effectuer une analyse antivirus avec Avast pour votre ordinateur ?", padx=10, pady=10)
    label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
    
    yes_button = tk.Button(window_avast_system, text="Oui !", command=yes)
    yes_button.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="e")
    
    no_button = tk.Button(window_avast_system, text="Non !", command=window_avast_system.destroy())
    no_button.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
    
    window_avast_system.mainloop()

def avast_analysis_system():
    
    avast_path = r"C:\Program Files\AVAST Software\Avast\ashCmd.exe"
    subprocess.run([avast_path, "C:"], creationflags=subprocess.CREATE_NEW_CONSOLE)

def windows_system():
    
    tts("Cette opération peut prendre plusieurs minutes, souhaitez-vous continuer ?")

    def yes():
        
        windows_defender_analysis()
        window_windows_system_analysis.destroy()

    window_windows_system_analysis = tk.Tk()
    window_windows_system_analysis.title("Analyse antivirus de votre ordinateur.")
    window_windows_system_analysis.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico"))
    window_windows_system_analysis.geometry("560x150")
    window_windows_system_analysis.resizable(False, False)
    
    label = tk.Label(window_windows_system_analysis, text="Souhaitez-vous effectuer une analyse antivirus avec Windows Defender pour votre ordinateur ?", padx=10, pady=10)
    label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
    
    yes_button = tk.Button(window_windows_system_analysis, text="Oui !", command=yes)
    yes_button.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="e")
    
    no_button = tk.Button(window_windows_system_analysis, text="Non !", command=window_windows_system_analysis.destroy())
    no_button.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
    
    window_windows_system_analysis.mainloop()

def windows_defender_analysis():

    analysis_command = subprocess.Popen(["powershell.exe", "Start-MpScan -ScanType FullScan"], creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE)  
    analysis_command.communicate()

    if analysis_command.returncode == 0:

        tts("L'analyse antivirus de votre ordinateur via l'antivirus Windows Defender vient d'être effectué !")
        messagebox.showinfo(title="Analyse antivirus de votre ordinateur.", message="L'analyse antivirus de votre ordinateur via l'antivirus Windows Defender vient d'être effectué !")

    elif analysis_command.returncode == 1:

        tts("L'analyse antivirus de votre ordinateur via l'antivirus Windows Defender, n'a pas pu être effectué !")
        messagebox.showerror(title="Analyse antivirus de votre ordinateur.", message="L'analyse antivirus de votre ordinateur via l'antivirus Windows Defender, n'a pas pu être effectué !")    
    
def apps_updates():
    
    winget = subprocess.run(["winget"], stdout=subprocess.PIPE)
    
    if b"winget" in winget.stdout:
        
        install_updates = subprocess.Popen(["winget", "upgrade", "--all"], shell=True, stdout=subprocess.PIPE)
        install_updates.communicate()

        if install_updates.returncode == 0:
            
            tts("L'ensemble des mises à jour applicatives et logicielles a été téléchargé !")
            messagebox.showinfo(title="V Cleaner :", message="L'ensemble des mises à jour applicatives et logicielles a été téléchargé !")
       
        else:
            
            tts("L'ensemble des mises à jour applicatives et logicielles n'ont pas pu être téléchargé !")
            messagebox.showerror(title="V Cleaner :", message="L'ensemble des mises à jour applicatives et logicielles n'ont pas pu être téléchargé !")
    
    else:
        
        tts("Vous ne possédez pas le gestionnaire de packages Windows sur votre ordinateur, afin de procéder à la recherche et à l'installation des mises à jour disponibles pour vos applications et logiciels !")
        messagebox.showwarning(title="V Cleaner :", message="Vous ne possédez pas le gestionnaire de packages Windows sur votre ordinateur, afin de procéder à la recherche et à l'installation des mises à jour disponibles pour vos applications et logiciels !")
        
        tts("Souhaitez-vous télécharger et installer le gestionnaire de packages Windows ?")

        def yes():
            
            wget.download("https://aka.ms/getwingetpreview", path)
            window_apps_updates.destroy()

        window_apps_updates = tk.Tk()
        window_apps_updates.title("Téléchargement et installation du gestionnaire de packages Windows.")
        window_apps_updates.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico"))
        window_apps_updates.geometry("600x150")
        window_apps_updates.resizable(False, False)
        
        label = tk.Label(window_apps_updates, text="Souhaitez-vous télécharger et installer le gestionnaire de packages Windows ?", padx=10, pady=10)
        label.pack()
        
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "winget.msixbundle")
        
        yes_button = tk.Button(window_apps_updates, text="Oui !", command=yes)
        yes_button.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="e")
        
        no_button = tk.Button(window_apps_updates, text="Non !", command=window_apps_updates.destroy())
        no_button.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
        
        window_apps_updates.mainloop()

def developer_message():
    
    window_developper_message = tk.Tk()
    window_developper_message.title("Envoyer un courriel au développeur du programme.")
    window_developper_message.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico"))
    window_developper_message.geometry("600x500")
    window_developper_message.resizable(False, False)

    tk.Label(window_developper_message, text="Quelle est votre adresse électronique ? :", font=("Arial", 12)).pack(pady=10)
    
    email_entry = tk.Entry(window_developper_message, font=("Arial", 12), width=40)
    email_entry.pack(pady=5)

    tk.Label(window_developper_message, text="Quel est votre mot de passe d'application ? :", font=("Arial", 12)).pack(pady=10)
    
    password_entry = tk.Entry(window_developper_message, font=("Arial", 12), show="*", width=40)
    password_entry.pack(pady=5)

    tk.Label(window_developper_message, text="Quel est votre message à destination du développeur du programme ? :", font=("Arial", 12)).pack(pady=10)
    
    message_text = tk.Text(window_developper_message, font=("Arial", 12), width=50, height=10)
    message_text.pack(pady=5)

    send_button = tk.Button(window_developper_message, text="Envoyer votre message !", font=("Arial", 12), command=lambda: send_message(email_entry, password_entry, message_text))
    send_button.pack(pady=20)

    window_developper_message.mainloop()

def send_message(email_entry, password_entry, message_text):
    
    email = email_entry.get()
    password = password_entry.get()
    message = message_text.get("1.0", tk.END)
    recipient = "steven_itech@proton.me"

    if not email.endswith("@gmail.com"):
        
        tts("Veuillez transmettre uniquement une adresse électronique Google !")
        messagebox.showwarning(title="Envoyer un message au développeur du programme.", message="Veuillez transmettre uniquement une adresse électronique Google !")
    
    elif not email or not password or not message.strip():
        
        tts("Veuillez remplir tous les champs, afin de pouvoir envoyer votre message au développeur du programme !")
        messagebox.showwarning(title="Envoyer un message au développeur du programme.", message="Veuillez remplir tous les champs, afin de pouvoir envoyer votre message au développeur du programme !")
    
    else:
        
        try:
            
            msg = MIMEMultipart()
            msg["Subject"] = "Courriel d'un utilisateur de V Cleaner."
            msg["From"] = email
            msg["To"] = recipient

            msg.attach(MIMEText(message, "plain"))

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, recipient, msg.as_string())
            server.quit()

            tts("Votre message a été envoyé avec succès !")
            messagebox.showinfo(title="Envoyer un message au développeur du programme.", message="Votre message a été envoyé avec succès !")
        
        except Exception as e:
            
            tts("Une erreur est survenue lors de l'envoi de votre courriel !")
            messagebox.showerror(title="Envoie du message au développeur du programme.", message=f"Une erreur est survenue lors de l'envoi de votre message au développeur du programme ! : {e}")

def open_github():

    webbrowser.open("https://github.com/steven-itech/")

if __name__ == "__main__":
   
    window = tk.Tk()
    window.title("V Cleaner :")
    window.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico"))
    window.geometry("700x500")
    window.resizable(False, False)
    
    interface = Menu(window)
    window.config(menu=interface)
    
    avast_check = Menu(interface, tearoff=0)
    avast_check.add_command(label="Vérifier si l'antivirus Avast est présent sur votre ordinateur.", command=avast)
    
    avast_analysis = Menu(interface, tearoff=0)
    avast_analysis.add_command(label="Effectuer une analyse antivirus de votre système avec Avast.", command=avast_system)
    avast_analysis.add_separator()
    avast_analysis.add_command(label="Effectuer une analyse antivirus de votre système avec Windows Defender.", command=windows_system)

    windows_anaylis = Menu(interface, tearoff=0)
    windows_anaylis.add_command(label="Effectuer une analyse antivirus de votre système avec Windows Defender.", command=windows_system)
    
    application = Menu(interface, tearoff=0)
    application.add_command(label="Recherchez et installez l'ensemble des mises à jour applicatives et logicielles disponibles.", command=apps_updates)

    developer = Menu(interface, tearoff=0)
    developer.add_command(label="Envoyer un courriel au développeur du programme, afin de lui transmettre d'éventuels problèmes.", command=developer_message)

    github = Menu(interface, tearoff=0)
    github.add_command(label="Accéder à la page Github du développeur.", command=open_github)
    
    interface.add_cascade(label="Antivirus.", menu=avast_check)
    interface.add_cascade(label="Analyse.", menu=avast_analysis)
    interface.add_cascade(label="Mises à jour.", menu=application)
    interface.add_cascade(label="Aide.", menu=developer)
    interface.add_cascade(label="Github.", menu=github)
    
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
    icon_image = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_image)
    
    background_label = tk.Label(window, image=icon_photo)
    background_label.image = icon_photo  
    background_label.place(relx=0.5, rely=0.5, anchor="center")
    
    window.mainloop()