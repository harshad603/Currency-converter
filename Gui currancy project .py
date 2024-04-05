# creating Windows

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
t=Tk()
t.geometry('410x440')
t.config(bg='#7979CD')     
t.title('Currency Convertor')
t.resizable(height=FALSE,width=FALSE)


Label(t,text='Currancy Convertor',bg='#7979CD',font=('Britannic bold',26)).place(x=50,y=20)
Label(t,text='Enter Value',bg='#7979CD',font=('Iskoola Pota bold',18)).place(x=130,y=200)
Label(t,text='⇄',fg='black',bg='#7979CD',font=('Arial Rounded MT Bold',30)).place(x=180,y=135)
Label(t,text='From',bg='#7979CD',font=('Iskoola Pota bold',18 )).place(x=40,y=110)
Label(t,text='To',bg='#7979CD',font=('Iskoola Pota bold',18)).place(x=290,y=110)
result=Label(t,text='',width=30,height=5,relief="solid",anchor=CENTER,justify=CENTER).place(x=80,y=285)

def solve():
    a=fromvalue.get()
    b=tovalue.get()
    c=int(entryvalue.get())
    if(a=='₹ - INR (Rupee)' and b=='$ - USD (Dollar)'):
        valuemoney=c/82.5577
        Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='$ - USD (Dollar)' and b=='₹ - INR (Rupee)'):
         valuemoney=c*82.5577
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)

    elif(a=='₹ - INR (Rupee)' and b=='E£ - EGP (EgyptPound)'):
        valuemoney=c/2.66
        Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='E£ - EGP (EgyptPound)' and b=='₹ - INR (Rupee)'):
         valuemoney=c*2.66
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)

    elif(a=='₹ - INR (Rupee)' and b=='€ - EUR (Euro)'):
        valuemoney=c/88.86
        Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='€ - EUR (Euro)' and b=='₹ - INR (Rupee)'):
         valuemoney=c*88.86
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='$ - USD (Dollar)' and b=='€ - EUR (Euro)'):
         valuemoney=c*0.92
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='$ - USD (Dollar)' and b=='E£ - EGP (EgyptPound)'):
         valuemoney=c*30.90
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='E£ - EGP (EgyptPound)' and b=='€ - EUR (Euro)'):
         valuemoney=c*0.030
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='E£ - EGP (EgyptPound)' and b=='$ - USD (Dollar)'):
         valuemoney=c*0.032
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='€ - EUR (Euro)' and b=='E£ - EGP (EgyptPound)'):
         valuemoney=c*33.28
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='€ - EUR (Euro)' and b=='$ - USD (Dollar)'):
         valuemoney=c*1.08
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='₹ - INR (Rupee)' and b=='ع.د - IQD (Iraqi dinar)'):
        valuemoney=c/0.063
        Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='ع.د - IQD (Iraqi dinar)' and b=='₹ - INR (Rupee)'):
         valuemoney=c*0.063
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='ع.د - IQD (Iraqi dinar)' and b=='$ - USD (Dollar)'):
         valuemoney=c*0.00076
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='ع.د - IQD (Iraqi dinar)' and b=='€ - EUR (Euro)'):
         valuemoney=c*0.00076
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='ع.د - IQD (Iraqi dinar)' and b=='E£ - EGP (EgyptPound)'):
         valuemoney=c*0.024
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)

    elif(a=='₹ - INR (Rupee)' and b=='ر.ع.- OMR (Omani rial)'):
        valuemoney=c/214.06
        Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='ر.ع.- OMR (Omani rial)' and b=='₹ - INR (Rupee)'):
         valuemoney=c*214.06
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='ر.ع.- OMR (Omani rial)' and b=='$ - USD (Dollar)'):
         valuemoney=c*2.60
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='ر.ع.- OMR (Omani rial)' and b=='€ - EUR (Euro)'):
         valuemoney=c*2.42
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    elif(a=='ر.ع.- OMR (Omani rial)' and b=='E£ - EGP (EgyptPound)'):
         valuemoney=c*80.24
         Label(t,text=valuemoney,width=20,height=3,bg='white',font=('Arial Black',10)).place(x=100,y=290)
    
    else:
        messagebox.showerror('Erorr','Something went wrong')

    

    
n=IntVar()
fromvalue= ttk.Combobox(t, width = 24, textvariable = n)
fromvalue['values']=('₹ - INR (Rupee)','$ - USD (Dollar)','E£ - EGP (EgyptPound)','€ - EUR (Euro)','ع.د - IQD (Iraqi dinar)','ر.ع.- OMR (Omani rial)')
fromvalue.place(x=5,y=150)
fromvalue.current(0)
g=IntVar()
tovalue= ttk.Combobox(t, width = 24, textvariable = g)
tovalue['values']=('€ - EUR (Euro)','₹ - INR (Rupee)','E£ - EGP (EgyptPound)','$ - USD (Dollar)','ع.د - IQD (Iraqi dinar)','ر.ع.- OMR (Omani rial)')
tovalue.place(x=230,y=150)
tovalue.current(0)
entryvalue=Entry(t,width=25,justify=CENTER,font=('Arial Black',9))
entryvalue.place(x=85,y=250)
button=Button(t,text='convert',width=10,borderwidth=10,bg='green',font=('Iskoola Pota bold',15),command=solve).place(x=115,y=380)

t.mainloop()






















