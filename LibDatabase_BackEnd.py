import sqlite3

#Backend


def ConnectData():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Library (id INTEGER PRIMARY KEY, MType text, Rno text,Tit text, Fna text,\
    Sna text, Add1 text, Add2 text, PostCode text, MobNo text, BkID text, BkTit text, Aur text, DtB text,\
    DtD text, DyOL text, LtR text, DtOD text, SellPr text)")
    con.commit()
    con.close()


def AddData(MType, Rno,Tit, Fna, Sna, Add1, Add2, PostCode, MobNo, BkID, BkTit, Aur, DtB, DtD, DyOL, LtR, DtOD, SellPr):
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Library VALUES (NULL, ?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (MType, Rno, Tit, Fna, Sna,
                Add1, Add2, PostCode, MobNo, BkID, BkTit, Aur, DtB, DtD, DyOL, LtR, DtOD, SellPr))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Library")
    rows = cur.fetchall()
    con.close()
    return rows


def DeleteRec(id):
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Library WHERE id=?", (id,))
    con.commit()
    con.close()


def SearchData(MType="", Rno="", Tit="", Fna="", Sna="", Add1="", Add2="", PostCode="", MobNo="", BkID="", BkTit="", \
               Aur="", DtB="", DtD="", DyOL="", LtR="", DtOD="", SellPr=""):
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("""SELECT * FROM Library WHERE id=MTy=? OR Rno=? OR Tit=? OR Fna=? OR Sna=? OR Add1=? OR Add2=? OR \
     PostCode=? OR MobNo=? OR BkID=? OR BkTit=? OR Aur=? OR DtB=? OR DtD=? OR DyOL=? OR LtR=? OR DtOD=? OR SellPr=?)""",
                (MType, Rno, Tit, Fna, Sna, Add1, Add2, PostCode, MobNo, BkID, BkTit, Aur, DtB, DtD, DyOL, LtR, DtOD,
                 SellPr))
    rows = cur.fetchall()
    con.close()
    return rows


def UpdateData(id, MTy="", Rno="", Tit="", Fna="", Sna="", Add1="", Add2="", PostCode="", MobNo="", BkID="", BkTit="", \
               Aur="", DtB="", DtD="", DyOL="", LtR="", DtOD="", SellPr=""):
    con = sqlite3.connect("Library.db")
    cur = con.cursor()
    cur.execute("""UPDATE Library SET MTy=? OR Rno=? OR Tit=? OR Fna=? OR Sna=? OR Add1=? OR Add2=? OR \
     PostCode=? OR MobNo=? OR BkID=? OR BkTit=? OR Aur=? OR DtB=? OR DtD=? OR DyOL=? OR LtR=? OR DtOD=? OR SellPr=?) \
     WHERE id =?""", (MTy, Rno, Tit, Fna, Sna, Add1, Add2, PostCode, MobNo, BkID, BkTit, Aur, DtB, DtD, DyOL, LtR,
                      DtOD, SellPr))
    con.commit()
    con.close()

ConnectData()
