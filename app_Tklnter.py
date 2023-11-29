import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo
show = tkinter.Tk()

show.title("Project : Biodata")
show.configure(bg="pink")
show.geometry("300x500")
show.resizable(True,True)   #resize( kanan/kiri, bawah/atas)
   
frame = ttk.Frame(show)
#pengaturan tampilan : pack, pad, place
frame.pack(padx=15, pady=15, fill="x", expand=True)

labe_nama = ttk.Label(frame, text="<3  Name  <3 ")
labe_nama.pack( padx=10, pady=10, expand=True )    #klo mau di ujung kiri (fill="x") 

varNama = tkinter.StringVar()

entry_nama = ttk.Entry(frame, textvariable = varNama)
entry_nama.pack( padx=10, pady=10, fill="x", expand=True)

label_kelas = ttk.Label(frame, text="<3  Class  <3")
label_kelas.pack( padx=10, pady=10,  expand=True)

varkelas = tkinter.StringVar()

entry_kelas = ttk.Entry(frame, textvariable = varkelas)
entry_kelas.pack( padx=10, pady=10, fill="x", expand=True) 


label_email = ttk.Label(frame, text="<3  Email  <3")
label_email.pack( padx=10, pady=10,  expand=True)

varemail = tkinter.StringVar()

entry_email = ttk.Entry(frame, textvariable = varemail)
entry_email.pack( padx=10, pady=10, fill="x", expand=True) 



label_no = ttk.Label(frame, text="<3  Handphone number <3")
label_no.pack( padx=10, pady=10,  expand=True)

varno = tkinter.StringVar()

entry_no = ttk.Entry(frame, textvariable = varno)
entry_no.pack( padx=10, pady=10, fill="x", expand=True) 




label_alamat = ttk.Label(frame, text="<3  Adress  <3")
label_alamat.pack( padx=10, pady=10,  expand=True)

varalamat = tkinter.StringVar()

entry_alamat = ttk.Entry(frame, textvariable = varalamat)
entry_alamat.pack( padx=10, pady=10, fill="x", expand=True) 



def Aksikirim():
    output = f"Heyyy i'm {varNama.get()} from class {varkelas.get()}. You can contact me through email on {varemail.get()} or no. {varno.get()}. You can find me in {varalamat.get()}"
    showinfo(message=output)

submit = ttk.Button( frame, text="Submit  :D", command=Aksikirim)
submit.pack( padx=10, pady=10, fill="x", expand=True) 






show.mainloop()