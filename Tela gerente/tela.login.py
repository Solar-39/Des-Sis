# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⡀⠀⠀
# ⠀⠀⢠⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣾⠏⠘⠿⣦⣤
# ⠀⠀⣾⠉⠻⢶⠶⠛⢻⡇⠀⠀⠀⠘⢻⡦⠀⠀⢰⡾⠃
# ⢀⣤⠿⠀⠀⠀⠀⢠⡟⠁⠀⠀⠀⠀⠸⠷⠿⠿⣾⣷⠀
# ⢿⣥⣀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠈⠉⣿⣀⣾⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠘⠛⠁⠀⠀⠀⠀⠀⢀⣾⢻⣆⡀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠃⠀⠙⠛⣿⠇⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣶⡄⠀⠀⢸⣏⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⡷⠟⠛⠻⠿⠀⠀⠀⠀
#
# ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦ . 　⁺ 

import tkinter as tk

def login():
    print("Login realizado✩‧₊!")

app = tk.Tk()
app.title ("tela exemplo")
app.geometry("400x300")

#label email ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦ . 　⁺ 
label_email = tk.Label(app, text = "Email")
label_email.pack(pady=5)

#input email ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦ . 　⁺ 
input_email = tk.Entry(app)
input_email.pack()

#label senha ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦ . 　⁺ 
label_senha = tk.Label(app, text = "senha")
label_senha.pack(pady=5)

#input senha ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦ . 　⁺ 
input_senha = tk.Entry(app)
input_senha.pack()

#botão ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦ . 　⁺ 
btn_enviar = tk.Button(app, text = "Enviar⭑.ᐟ", command = login)
btn_enviar.pack()

email = input_email.get()
senha = input_senha.get()

if email == admin {

}

app.mainloop()
