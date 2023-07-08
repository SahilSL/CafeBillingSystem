import sys
import os
from tkinter import *
import math,random
from tkinter import messagebox
from tkinter import ttk
import datetime
import time

root=Tk() 

class cafe_billing_application:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("CBS: CAFE BILLING APPLICATION - By SahilSL")
        self.root.iconbitmap('icon.ico')
        self.root.configure(bg="cyan2")
        
        title=Label(self.root,text="CAFE BILLING APPLICATION",bd=10,relief=GROOVE,bg='cyan2',fg="black",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        # var ---->
        # ATF ---->
        self.frenchfries=IntVar()
        self.sandwich=IntVar()
        self.burger=IntVar()
        self.pizza=IntVar()
        self.dessert=IntVar()
        self.pasta=IntVar()

        # Starter ---->
        self.chickentikka=IntVar()
        self.chickenangara=IntVar()
        self.paneertikka=IntVar()
        self.noodles=IntVar()
        self.manchurian=IntVar()
        self.alootikki=IntVar()

        # Drinks ---->
        self.cocktail=IntVar()
        self.mojito=IntVar()
        self.pepsi=IntVar()
        self.sprite=IntVar()
        self.soda=IntVar()
        self.fruti=IntVar()

        # Total Price ---->
        self.atf_price=StringVar()
        self.starter_price=StringVar()
        self.drinks_price=StringVar()

        # Tax price ---->
        self.atf_tax=StringVar()
        self.starter_tax=StringVar()
        self.drinks_tax=StringVar()

        # Name of customer ---->
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill=StringVar()
        a=random.randint(1000,9999)
        self.bill.set(str(a))
        self.search_bill=StringVar()
        

        # Customer Detail ---->
        F1=LabelFrame(self.root,text=" Customer Details ",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),bg='cyan2',fg="black")#
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Name Of Customer",bg='cyan2',fg="black",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=20,textvariable=self.c_name,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)

        cphn_lbl=Label(F1,text="Phone Number",bg='cyan2',fg="black",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=20,textvariable=self.c_phon,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg='cyan2',fg="black",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=20,textvariable=self.search_bill,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=5,pady=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,bg='cyan2',fg="white",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=40)
        

        # ATF Frame ---->
        F2=LabelFrame(self.root,text=" ATF ",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="black",bg='cyan2')
        F2.place(x=5,y=180,width=325,height=380)

        frenchfries_lbl1=Label(F2,text="French Fries",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        frenchfries_txt=Entry(F2,width=10,textvariable=self.frenchfries,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
     
        sandwich_lbl1=Label(F2,text="Sandwich",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        sandwich_txt=Entry(F2,width=10,textvariable=self.sandwich,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        burger_lbl1=Label(F2,text="Burger",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        burger_txt=Entry(F2,width=10,textvariable=self.burger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        pizza_lbl1=Label(F2,text="Pizza",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        pizza_txt=Entry(F2,width=10,textvariable=self.pizza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
       
        dessert_lbl1=Label(F2,text="Dessert",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        dessert_txt=Entry(F2,width=10,textvariable=self.dessert,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        pasta_lbl1=Label(F2,text="Pasta",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        pasta_txt=Entry(F2,width=10,textvariable=self.pasta,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        # Starter Frame ---->
        F3=LabelFrame(self.root,text="Starter",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="black",bg='cyan2')
        F3.place(x=340,y=180,width=325,height=380)

        chickentikka_lbl1=Label(F3,text="Chicken Tikka",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        chickentikka_txt=Entry(F3,width=10,textvariable=self.chickentikka,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
     
        chickenangara_lbl1=Label(F3,text="Chicken Angara",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        chickenangara_txt=Entry(F3,width=10,textvariable=self.chickenangara,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        paneertikka_lbl1=Label(F3,text="Paneer Tikka",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        paneertikka_txt=Entry(F3,width=10,textvariable=self.paneertikka,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        noodles_lbl1=Label(F3,text="Noodles",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        noodles_txt=Entry(F3,width=10,textvariable=self.noodles,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
       
        manchurian_lbl1=Label(F3,text="Manchurian",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        manchurian_txt=Entry(F3,width=10,textvariable=self.manchurian,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        alootikki_lbl1=Label(F3,text="Aloo Tikki",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        alootikki_txt=Entry(F3,width=10,textvariable=self.alootikki,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        # Drinks ---->
        F4=LabelFrame(self.root,text="Drinks",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="black",bg='cyan2')
        F4.place(x=670,y=180,width=325,height=380)

        cocktail_lbl1=Label(F4,text="Cocktail",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        cocktail_txt=Entry(F4,width=10,textvariable=self.cocktail,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
     
        mojito_lbl1=Label(F4,text="Mojito",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        mojito_txt=Entry(F4,width=10,textvariable=self.mojito,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        pepsi_lbl1=Label(F4,text="Pepsi",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        pepsi_txt=Entry(F4,width=10,textvariable=self.pepsi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        sprite_lbl1=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        sprite_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
       
        soda_lbl1=Label(F4,text="Soda",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        soda_txt=Entry(F4,width=10,textvariable=self.soda,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        fruti_lbl1=Label(F4,text="Fruti",font=("times new roman",16,"bold"),bg='cyan2',fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        fruti_txt=Entry(F4,width=10,textvariable=self.fruti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        
        # Bill ----->
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1008,y=180,width=520,height=380)
        bill=Label(F5,text="BILL",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        # Buttons ---->
        F6=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="black",bg='cyan2')
        F6.place(x=0,y=560,relwidth=1,height=140)

        a1_lbl1=Label(F6,text="Total ATF Price",bg='cyan2',fg="black",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        a1_txt=Entry(F6,width=18,textvariable=self.atf_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        a2_lbl1=Label(F6,text="Total Starter Price",bg='cyan2',fg="black",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        a2_txt=Entry(F6,width=18,textvariable=self.starter_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        a3_lbl1=Label(F6,text="Total Drinks Price",bg='cyan2',fg="black",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        a3_txt=Entry(F6,width=18,textvariable=self.drinks_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        
        b1_lbl1=Label(F6,text="ATF Tax",bg='cyan2',fg="black",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        b1_txt=Entry(F6,width=18,textvariable=self.atf_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        b2_lbl1=Label(F6,text="Starter Tax",bg='cyan2',fg="black",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        b2_txt=Entry(F6,width=18,textvariable=self.starter_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        b3_lbl1=Label(F6,text="Drinks Tax",bg='cyan2',fg="black",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        b3_txt=Entry(F6,width=18,textvariable=self.drinks_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_A=Frame(F6,bd=7,relief=GROOVE)
        btn_A.place(x=750,width=650,height=105)

        ResLabel=Label(btn_A,text="How To use?\n 1. Enter the Customer Details.\n 2. Selects quantity of items from menu.\n 3. Click on Total buttton and then generate bill button.",bg="#03C04A",fg="White",bd=5,pady=5,width=76, font="arial 10 bold").grid(row=0,column=0,padx=5,pady=5,sticky="w")
        #Generate_bill=Button(btn_A,command=self.bill_area,#text="Generate Bill",bg="#03C04A",fg="White",bd=5,#pady=15,width=11,font="arial 13 bold").grid(row=0,#column=1,padx=5,pady=5)
        #clear=Button(btn_A,text="Clear",command=self.#clear_data,bg="#03C04A",fg="White",bd=5,pady=15,#width=11,font="arial 13 bold").grid(row=0,column=2,#padx=5,pady=5)
        #Exit=Button(btn_A,text="Exit",command=self.Exit_app,#bg="#03C04A",fg="White",bd=5,pady=15,width=11,#font="arial 13 bold").grid(row=0,column=3,padx=5,#pady=5)
        #self.welcome_bill()

        F6=Frame(self.root,bd=10,relief=GROOVE)
        F6.place(x=0,y=690,relwidth=1,height=110)
        
        total=Button(F6,command=self.total,text="Total",bg="red1",fg="White",bd=5,pady=15,width=20,font="arial 13 bold").grid(row=0,column=0,padx=75,pady=5)
        Generate_bill=Button(F6,command=self.bill_area,text="Generate Bill",bg="red1",fg="White",bd=5,pady=15,width=20,font="arial 13 bold").grid(row=0,column=1,padx=75,pady=5)
        clear=Button(F6,text="Clear",command=self.clear_data,bg="red1",fg="White",bd=5,pady=15,width=20,font="arial 13 bold").grid(row=0,column=2,padx=75,pady=5)
        Exit=Button(F6,text="Exit",command=self.Exit_app,bg="red1",fg="White",bd=5,pady=15,width=20,font="arial 13 bold").grid(row=0,column=3,padx=75,pady=5)
        self.welcome_bill()

         # scroll text bill ----->
        
        '''def display():
            global text2, n, msg2
            for t in range(len(msg2)):
                for k in range(t):
                    text2 += ' '
                for g in range(len(msg2) - t):
                    text2 += msg2[g]
                #text2 = text2.strip()
                F6.update()
                F6.after(200)
                text2 = text2.strip()
                scroll_text.set('')
                scroll_text.set(text2)
                text2 = ''
            scroll_text.set('')
            txtscroll.after(200,display)
        
        txtscroll=Entry(F6,textvariable=scroll_text, font=('arial',50,'bold'), fg='black', bd=10, bg='cyan2', width=150)
        txtscroll.grid(row=0, column=0, columnspan=4)
        display()'''

    def total(self):
        self.chickentikka_price=10
        self.chickenangara_price=50
        self.paneertikka_price=90
        self.noodles_price=90
        self.manchurian_price=10
        self.alootikki_price=10
        self.c_l_p=(self.chickentikka.get()*self.chickentikka_price)
        self.c_d_p=(self.chickenangara.get()*self.chickenangara_price)
        self.c_p_p=(self.paneertikka.get()*self.paneertikka_price)
        self.c_pe_p=(self.noodles.get()*self.noodles_price)
        self.c_ku_p=(self.manchurian.get()*self.manchurian_price)
        self.c_w_p=(self.alootikki.get()*self.alootikki_price)
        self.total_starter_price=float(
                                self.c_l_p+
                                self.c_d_p+
                                self.c_p_p+
                                self.c_pe_p+
                                self.c_ku_p+
                                self.c_w_p
                                )
        self.starter_price.set("Rs. "+str(self.total_starter_price))
        self.cs_tax=round((self.total_starter_price*0.1),2)
        self.starter_tax.set("Rs. "+str(self.cs_tax))

        self.frenchfries_price=60
        self.sandwich_price=50
        self.burger_price=50
        self.pizza_price=80
        self.dessert_price=80
        self.pasta_price=50
        self.j_s_p= (self.frenchfries.get()*self.frenchfries_price)
        self.j_t_p=(self.sandwich.get()*self.sandwich_price)
        self.j_c_p=(self.burger.get()*self.burger_price)
        self.j_sv_p=(self.pizza.get()*self.pizza_price)
        self.j_d_p=(self.dessert.get()*self.dessert_price)
        self.j_m_p=(self.pasta.get()*self.pasta_price)
        self.total_atf_price=float(
                                self.j_s_p+
                                self.j_t_p+
                                self.j_c_p+
                                self.j_sv_p+
                                self.j_d_p+
                                self.j_m_p
                                )
        self.atf_price.set("Rs. "+str(self.total_atf_price))
        self.je_tax=round((self.total_atf_price*0.05),2)
        self.atf_tax.set("Rs. "+str(self.je_tax))

        self.cocktail_price=80
        self.mojito_price=50
        self.pepsi_price=40
        self.sprite_price=50
        self.soda_price=30
        self.fruti_price=20
        self.c_s_p=(self.cocktail.get()*self.cocktail_price)
        self.c_t_p=(self.mojito.get()*self.mojito_price)
        self.c_k_p=(self.pepsi.get()*self.pepsi_price)
        self.c_sr_p=(self.sprite.get()*self.sprite_price)
        self.c_st_p=(self.soda.get()*self.soda_price)
        self.c_f_p=(self.fruti.get()*self.fruti_price)
        self.total_drinks_price=float(
                                self.c_s_p+
                                self.c_t_p+
                                self.c_k_p+
                                self.c_sr_p+
                                self.c_st_p+
                                self.c_f_p
                                )
        self.drinks_price.set("Rs. "+str(self.total_drinks_price))
        self.ch_tax=round((self.total_drinks_price*0.15),2)
        self.drinks_tax.set("Rs. "+str(self.ch_tax))
    
        self.Total_bill=float(self.total_starter_price+
                            self.total_drinks_price+
                            self.total_atf_price+
                            self.cs_tax+
                            self.je_tax+
                            self.ch_tax
                            )   

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END," \t  \t    CAFE BILLING APPLICATION\n")
        self.txtarea.insert(END,f"\n BILL NUMBER : {self.bill.get()}")
        self.txtarea.insert(END,f"\n CUSTOMER NAME : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n PHONE NUMBER : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n===========================================================")
        self.txtarea.insert(END,f"\n PRODUCTS\t\tQUANTITY\t\tPRICE\t\tTOTAL PRICE")
        self.txtarea.insert(END,f"\n===========================================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Detais are Required")
        elif self.atf_price.get()=="Rs. 0.0" and self.starter_price.get()=="Rs. 0.0" and self.drinks_price.get()=="Rs. 0.0":
             messagebox.showerror("Error","Products Not selected")
        else:
            self.welcome_bill()

            #====juice bill generate======
            if self.frenchfries.get()!=0:
                self.txtarea.insert(END,f"\n French Fries  \t\t  {self.frenchfries.get()}\t\t {self.frenchfries_price}\t\t{self.j_s_p}")
            if self.sandwich.get()!=0:
                self.txtarea.insert(END,f"\n Sandwich      \t\t  {self.sandwich.get()}\t\t {self.sandwich_price}\t\t{self.j_t_p}")
            if self.burger.get()!=0:
                self.txtarea.insert(END,f"\n Burger        \t\t  {self.burger.get()}\t\t {self.burger_price}\t\t{self.j_c_p}")
            if self.pizza.get()!=0:
                self.txtarea.insert(END,f"\n Pizza         \t\t  {self.pizza.get()}\t\t {self.pizza_price}\t\t{self.j_sv_p}")
            if self.dessert.get()!=0:
                self.txtarea.insert(END,f"\n Dessert       \t\t  {self.dessert.get()}\t\t {self.dessert_price}\t\t{self.j_d_p}")
            if self.pasta.get()!=0:
                self.txtarea.insert(END,f"\n Pasta         \t\t  {self.pasta.get()}\t\t {self.pasta_price}\t\t{self.j_m_p}")
                
            #=========chips bill generate======    
            if self.chickentikka.get()!=0:
                self.txtarea.insert(END,f"\n Chicken Tikka \t\t  {self.chickentikka.get()}\t\t {self.chickentikka_price}\t\t{self.c_l_p}")
            if self.chickenangara.get()!=0:
                self.txtarea.insert(END,f"\n Chicken Angara\t\t  {self.chickenangara.get()}\t\t {self.chickenangara_price}\t\t{self.c_d_p}")
            if self.paneertikka.get()!=0:
                self.txtarea.insert(END,f"\n Paneer Tikka  \t\t  {self.paneertikka.get()}\t\t {self.paneertikka_price}\t\t{self.c_p_p}")
            if self.noodles.get()!=0:
                self.txtarea.insert(END,f"\n Noodles       \t\t  {self.noodles.get()}\t\t {self.noodles_price}\t\t{self.c_pe_p}")
            if self.manchurian.get()!=0:
                self.txtarea.insert(END,f"\n Manchurian    \t\t  {self.manchurian.get()}\t\t {self.manchurian_price}\t\t{self.c_ku_p}")
            if self.alootikki.get()!=0:
                self.txtarea.insert(END,f"\n Aloo Tikki    \t\t  {self.alootikki.get()}\t\t {self.alootikki_price}\t\t{self.c_w_p}")

            #=========chocolate bill generate=====
            if self.cocktail.get()!=0:
                self.txtarea.insert(END,f"\n Cocktail      \t\t  {self.cocktail.get()}\t\t {self.cocktail_price}\t\t{self.c_s_p}")
            if self.mojito.get()!=0:
                self.txtarea.insert(END,f"\n Mojito        \t\t  {self.mojito.get()}\t\t {self.mojito_price}\t\t{self.c_t_p}")
            if self.pepsi.get()!=0:
                self.txtarea.insert(END,f"\n Pepsi         \t\t  {self.pepsi.get()}\t\t {self.pepsi_price}\t\t{self.c_k_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite        \t\t  {self.sprite.get()}\t\t {self.sprite_price}\t\t{self.c_sr_p}")
            if self.soda.get()!=0:
                self.txtarea.insert(END,f"\n Soda          \t\t  {self.soda.get()}\t\t {self.soda_price}\t\t{self.c_st_p}")
            if self.fruti.get()!=0:
                self.txtarea.insert(END,f"\n Fruti         \t\t  {self.fruti.get()}\t\t {self.fruti_price}\t\t{self.c_f_p}")
            
            self.txtarea.insert(END,f"\n-----------------------------------------------------------")
            if self.atf_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n ATF Tax\t\t\t\t\t\t{self.atf_tax.get()}")
            if self.starter_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Starter Tax\t\t\t\t\t\t{self.starter_tax.get()}")
            if self.drinks_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Drinks Tax\t\t\t\t\t\t{self.drinks_tax.get()}")
            self.txtarea.insert(END,f"\n-----------------------------------------------------------")
            self.txtarea.insert(END,f"\n TOTAL BILL\t\t\t\t\t\tRs. {str(self.Total_bill)}")
            self.txtarea.insert(END,f"\n-----------------------------------------------------------")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("C:\\Users\\sahil\\OneDrive\\Desktop\\test\\bills\\"+str(self.bill.get())+".txt","w")
            f1.write(self.bill_data)
           
            f1.close()
            messagebox.showinfo("Saved",f"Bill No :{self.bill.get()} Saved Successfully")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("C:\\Users\\sahil\\OneDrive\\Desktop\\test\\bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"C:\\Users\\sahil\\OneDrive\\Desktop\\test\\bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill Number")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you want to clear?")
        if op>0:
            self.frenchfries.set(0)
            self.sandwich.set(0)
            self.burger.set(0)
            self.pizza.set(0)
            self.dessert.set(0)
            self.pasta.set(0)

            #=====Starter=====
            self.chickentikka.set(0)
            self.chickenangara.set(0)
            self.paneertikka.set(0)
            self.noodles.set(0)
            self.manchurian.set(0)
            self.alootikki.set(0)

            #=====Drinks====
            self.cocktail.set(0)
            self.mojito.set(0)
            self.pepsi.set(0)
            self.sprite.set(0)
            self.soda.set(0)
            self.fruti.set(0)

            #=====Total Price=====
            self.atf_price.set("")
            self.starter_price.set("")
            self.drinks_price.set("")

            #=======Tax price======
            self.atf_tax.set("")
            self.starter_tax.set("")
            self.drinks_tax.set("")

            #====name of customer=====
            self.c_name.set("")
            self.c_phon.set("")
            self.bill.set("")
            a=random.randint(1000,9999)
            self.bill.set(str(a))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()
  
obj=cafe_billing_application(root)

#root.configure(bg="cyan2")
root.mainloop()
