
from tkinter import *
import tkinter.messagebox
import LibDatabase_BackEnd


class Library:


    def __init__(self, root):
        self.root = root
        self.root.title("Library Database management Systems")
        self.root.geometry("")
        self.root.config(bg="cadet blue")

        MType = StringVar()
        Rno = StringVar()
        Tit = StringVar()
        Fna = StringVar()
        Sna = StringVar()
        Add1 = StringVar()
        Add2 = StringVar()
        PostCode = StringVar()
        MobNo = StringVar()
        BkID = StringVar()
        BkTit = StringVar()
        Aur = StringVar()
        DtB = StringVar()
        DtD = StringVar()
        DyOL = StringVar()
        LtR = StringVar()
        DtOD = StringVar()
        SellPr = StringVar()

# ===========================================Functions===================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Library Database management Systems", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
            return

        def ClearData():
            self.txtMType.delete(0, END)
            self.txtTit.delete(0, END)
            self.txtRno.delete(0, END)
            self.txtFna.delete(0, END)
            self.txtSna.delete(0, END)
            self.txtAdd1.delete(0, END)
            self.txtAdd2.delete(0, END)
            self.txtPostcode.delete(0, END)
            self.txtMobNo.delete(0, END)
            self.txtBkID.delete(0, END)
            self.txtBkTit.delete(0, END)
            self.txtAr.delete(0, END)
            self.txtDtB.delete(0, END)
            self.txtDtD.delete(0, END)
            self.txtDoL.delete(0, END)
            self.txtLtR.delete(0, END)
            self.txtDtOD.delete(0, END)
            self.txtSellPr.delete(0, END)


        def AddBkRec():
            if len(MType.get()) != 0:
                LibDatabase_BackEnd.AddData(MType.get(), Rno.get(), Tit.get(), Fna.get(), Sna.get(), Add1.get(),
                                            Add2.get(), PostCode.get(), MobNo.get(), BkID.get(), BkTit.get(),
                                            Aur.get(), DtB.get(), DtD.get(), DyOL.get(), LtR.get(), DtOD.get(),
                                            SellPr.get())
                booklist.delete(0, END)
                booklist.insert(MType.get(), Rno.get(), Tit.get(), Fna.get(), Sna.get(), Add1.get(), Add2.get(),
                                PostCode.get(), MobNo.get(), BkID.get(), BkTit.get(), Aur.get(), DtB.get(), DtD.get(),
                                DyOL.get(), LtR.get(), DtOD.get(), SellPr.get())


        def DisplayData():
            booklist.delete(0, END)
            for row in LibDatabase_BackEnd.viewData():
                booklist.insert(END, row, str(""))

        def SelectedBk(event):
            global sb
            searchBk = booklist.curselection()[0]
            sb = booklist.get(searchBk)

            self.txtMType.delete(0, END)
            self.txtMType.insert(END, sb[1])
            self.txtRno.delete(0, END)
            self.txtRno.insert(END, sb[2])
            self.txtTit.delete(0, END)
            self.txtTit.insert(END, sb[3])
            self.txtFna.delete(0, END)
            self.txtFna.insert(END, sb[4])
            self.txtSna.delete(0, END)
            self.txtSna.insert(END, sb[5])
            self.txtAdd1.delete(0, END)
            self.txtAdd1.insert(END, sb[6])
            self.txtAdd2.delete(0, END)
            self.txtAdd2.insert(END, sb[7])
            self.txtPostcode.delete(0, END)
            self.txtPostcode.insert(END, sb[8])
            self.txtMobNo.delete(0, END)
            self.txtMobNo.insert(END, sb[9])
            self.txtBkID.delete(0, END)
            self.txtBkID.insert(END, sb[10])
            self.txtBkTit.delete(0, END)
            self.txtBkTit.insert(END, sb[11])
            self.txtAr.delete(0, END)
            self.txtAr.insert(END, sb[12])
            self.txtDtB.delete(0, END)
            self.txtDtB.insert(END, sb[13])
            self.txtDtD.delete(0, END)
            self.txtDtD.insert(END, sb[14])
            self.txtDoL.delete(0, END)
            self.txtDoL.insert(END, sb[15])
            self.txtLtR.delete(0, END)
            self.txtLtR.insert(END, sb[16])
            self.txtDtOD.delete(0, END)
            self.txtDtOD.insert(END, sb[17])
            self.txtSellPr.delete(0, END)
            self.txtSellPr.insert(END, sb[18])


        def DeleteData():
            if len(MType.get()) != 0:
                LibDatabase_BackEnd.DeleteRec(sb[0])
                ClearData()
                DisplayData()

        def SearchDatabase():
            booklist.delete(0, END)
            for row in LibDatabase_BackEnd.SearchData(MType.get(), Rno.get(), Tit.get(), Fna.get(), Sna.get(), Add1.get(),
                                                      Add2.get(), PostCode.get(), MobNo.get(), BkID.get(), BkTit.get(),
                                                      Aur.get(), DtB.get(), DtD.get(),
                                                      DyOL.get(), LtR.get(), DtOD.get(), SellPr.get()):
                booklist.insert(END, row,)

        def UpdateDatabase():
            if len(MType.get()) != 0:
                LibDatabase_BackEnd.DeleteRec(sb[0])
            if len(MType.get()) != 0:
                LibDatabase_BackEnd.UpdateData(MType.get(), Rno.get(), Tit.get(), Fna.get(), Sna.get(), Add1.get(),
                                               Add2.get(), PostCode.get(), MobNo.get(), BkID.get(), BkTit.get(),
                                               Aur.get(), DtB.get(), DtD.get(), DyOL.get(), LtR.get(), DtOD.get(),
                                               SellPr.get())
                booklist.delete(0, END)
                booklist.insert(END, (MType.get(), Rno.get(), Tit.get(), Fna.get(), Sna.get(), Add1.get(), Add2.get(),
                                PostCode.get(), MobNo.get(), BkID.get(), BkTit.get(), Aur.get(), DtB.get(), DtD.get(),
                                DyOL.get(), LtR.get(), DtOD.get(), SellPr.get()))


# =======================================FRAMES===================================================
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=34, pady=2, bg="ghost white", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 50, 'bold'), text="Library Database Management Systems", pady=0,
                            padx=0, bg="cadet blue")
        self.lblTit.grid(sticky='W')

        ButtonFrame = Frame(MainFrame, width=1300, height=70, bd=2, padx=34, pady=2, bg="ghost white", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, width=135, height=600, bd=2, padx=34, pady=2, bg="ghost white", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, width=1000, height=600, bd=2, padx=34, font=('arial', 20, 'bold'),
                                   text="Library Membership Info", bg="ghost white", relief=RIDGE)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, width=350, height=400, bd=2, padx=20, pady=3, font=('arial', 20, 'bold'),
                                    text="Library Membership Info",bg="cadet blue", relief=RIDGE)
        DataFrameRIGHT.pack(side=RIGHT)

        
# =======================================Labels and Entry Ridges=================================================

        self.MTypelbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Member Type: ",
                            bg="ghost white")
        self.MTypelbl.grid(row=0, column=0, sticky=W)
        self.txtMType = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=MType, width=20)
        self.txtMType.grid(row=0, column=1, )

        self.Rnolbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Reference no: ",
                            bg="ghost white")
        self.Rnolbl.grid(row=1, column=0, sticky=W)
        self.txtRno = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=Rno, width=20)
        self.txtRno.grid(row=1, column=1, )

        self.Titlbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Title: ",
                            bg="ghost white")
        self.Titlbl.grid(row=2, column=0, sticky=W)
        self.txtTit = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=Tit, width=20)
        self.txtTit.grid(row=2, column=1, )

        self.Fnalbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="First Name: ",
                            bg="ghost white")
        self.Fnalbl.grid(row=3, column=0, sticky=W)
        self.txtFna = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=Fna, width=20)
        self.txtFna.grid(row=3, column=1, )

        self.Snalbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Surname: ",
                            bg="ghost white")
        self.Snalbl.grid(row=4, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=Sna, width=20)
        self.txtSna.grid(row=4, column=1, )

        self.Add1lbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Address 1: ",
                             bg="ghost white")
        self.Add1lbl.grid(row=5, column=0, sticky=W)
        self.txtAdd1 = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=Add1, width=20)
        self.txtAdd1.grid(row=5, column=1, )

        self.Add2lbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Address 2",
                             bg="ghost white")
        self.Add2lbl.grid(row=6, column=0, sticky=W)
        self.txtAdd2 = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=Add2, width=20)
        self.txtAdd2.grid(row=6, column=1, )

        self.Postcodelbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Post Code",
                             bg="ghost white")
        self.Postcodelbl.grid(row=7, column=0, sticky=W)
        self.txtPostcode = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=PostCode, width=20)
        self.txtPostcode.grid(row=7, column=1, )

        self.MobNolbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Mobile No:",
                             bg="ghost white")
        self.MobNolbl.grid(row=8, column=0, sticky=W)
        self.txtMobNo = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=MobNo, width=20)
        self.txtMobNo.grid(row=8, column=1, )

        self.BkIDlbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Book ID: ",
                             bg="ghost white")
        self.BkIDlbl.grid(row=0, column=2, sticky=W)
        self.txtBkID = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=BkID, width=20)
        self.txtBkID.grid(row=0, column=3, )

        self.BkTitlbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Book Title: ",
                              bg="ghost white")
        self.BkTitlbl.grid(row=1, column=2, sticky=W)
        self.txtBkTit = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=BkTit, width=20)
        self.txtBkTit.grid(row=1, column=3, )

        self.Arlbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Author: ",
                           bg="ghost white")
        self.Arlbl.grid(row=2, column=2, sticky=W)
        self.txtAr = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=Aur, width=20)
        self.txtAr.grid(row=2, column=3, )

        self.DtBlbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Date Borrowed: ",
                            bg="ghost white")
        self.DtBlbl.grid(row=3, column=2, sticky=W)
        self.txtDtB = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=DtB, width=20)
        self.txtDtB.grid(row=3, column=3, )

        self.DtDlbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Date Due: ",
                            bg="ghost white")
        self.DtDlbl.grid(row=4, column=2, sticky=W)
        self.txtDtD = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=DtD, width=20)
        self.txtDtD.grid(row=4, column=3, )

        self.DoLlbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Days on Loan: ",
                            bg="ghost white")
        self.DoLlbl.grid(row=5, column=2, sticky=W)
        self.txtDoL = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=DyOL, width=20)
        self.txtDoL.grid(row=5, column=3, )

        self.LtRlbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Late Return Fine: ",
                            bg="ghost white")
        self.LtRlbl.grid(row=6, column=2, sticky=W)
        self.txtLtR = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=LtR, width=20)
        self.txtLtR.grid(row=6, column=3, )

        self.DtODlbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Date Over Due: ",
                             bg="ghost white")
        self.DtODlbl.grid(row=7, column=2, sticky=W)
        self.txtDtOD = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=DtOD, width=20)
        self.txtDtOD.grid(row=7, column=3, )

        self.SellPrlbl = Label(DataFrameLEFT, bd=2, padx=20, pady=3, font=('arial', 15, 'bold'), text="Sell Price: ",
                               bg="ghost white")
        self.SellPrlbl.grid(row=8, column=2, sticky=W)
        self.txtSellPr = Entry(DataFrameLEFT, font=('arial', 15, 'bold'), textvariable=SellPr, width=20)
        self.txtSellPr.grid(row=8, column=3, )

# =======================================Listbox and Scrollbar Ridges=================================================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(column=1, sticky='ns')

        booklist = Listbox(DataFrameRIGHT, width=40, height=20, font=('arial', 10, 'bold'), yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>', SelectedBk)
        booklist.grid(row=0, column=0)
        scrollbar.configure(command=booklist.yview)


# ========================================Button Ridges=================================================
        AddDatabtn = Button(ButtonFrame, bd=5, font=('arial', 15, 'bold'), width=15, text='Add Data', command=AddBkRec)
        AddDatabtn.grid(row=0, column=0, sticky=W)

        DisplayDatabtn = Button(ButtonFrame, bd=5, font=('arial', 15, 'bold'), width=15, text='Display Data',
                                command=DisplayData)
        DisplayDatabtn.grid(row=0, column=1, sticky=W)

        UpdateDatabtn = Button(ButtonFrame, bd=5, font=('arial', 15, 'bold'), width=15, text='Update Data',
                               command=UpdateDatabase)
        UpdateDatabtn.grid(row=0, column=2, sticky=W)

        ClearDatabtn = Button(ButtonFrame, bd=5, font=('arial', 15, 'bold'), width=15, text='Clear Data',
                              command=ClearData)
        ClearDatabtn.grid(row=0, column=3, sticky=W)

        DeleteDatabtn = Button(ButtonFrame, bd=5, font=('arial', 15, 'bold'), width=15, text='Delete Data',
                               command=DeleteData)
        DeleteDatabtn.grid(row=0, column=4, sticky=W)

        SearchDatabtn = Button(ButtonFrame, bd=5, font=('arial', 15, 'bold'), width=15, text='Search Data',
                               command=SearchDatabase)
        SearchDatabtn.grid(row=0, column=5, sticky=W)

        Exitbtn = Button(ButtonFrame, bd=5, font=('arial', 15, 'bold'), width=15, text='Exit', command=iExit)
        Exitbtn.grid(row=0, column=6, sticky=W)


if __name__ == "__main__":
    root = Tk()
    application = Library(root)
    root.mainloop()
