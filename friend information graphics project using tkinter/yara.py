from tkinter import*
from tkinter import ttk
import time as ti
import datetime as dtim
from tkinter import messagebox
def submit():
    with open("FriendData.text","a") as f:
        f.write(f" Curret Time is : {dtim.datetime.now()}\n")
        print("\n")
        f.write(f"*********************Data of Jigri Friends*****************************\n")
        f.write("\n")
        f.write(f"This Friend of {root.categorise.get()}\n")
        f.write(f"This Friend Name is  {root.FriendName.get()}\n")
        f.write(f"This Friend is belong to {root.city.get()}\n")
        f.write(f"It Birth Date is {root.Birthdate.get()}\n")
        f.write(f"Interest of Area is {root.Interest.get()}\n")
        f.write(f"This Friend is  {root.Levelofstudy.get()}\n")
        f.write(f"My Friend Dreams is {root.FriendDreams.get()}\n")
        f.write(f"More Information is  {root.FutherInformation.get()}\n")
        f.write(f"Friend Mobile Number is {root.mobileNumber.get()}\n")
        f.write(f"Friend Current Location is {root.CurrentLocation.get()}\n")
        f.write(f"My Friend Whatsapp Number is  {root.Whatsapp.get()}\n")
        f.write(f"MY Friend Email ID is {root.EmailID.get()}\n")
        f.write(f"My Friend is Instagram ID is  {root.InstagramId.get()}\n")
        f.write(f"Friend Address is {root.Address.get()}\n")
        f.write("\n")
        f.write("+++++++++++++++++++++++++++++++ End Data ++++++++++++++++++++++++++++++++++++ \n")
        print("\n")
    messagebox.showinfo("Success","Record has been inserted")
    print("*********************Data of Jigri Friends*****************************")
    print(f"This Friend of {root.categorise.get()}")
    print(f"This Friend Name is  {root.FriendName.get()}")
    print(f"This Friend is belong to {root.city.get()}")
    print(f"It Birth Date is {root.Birthdate.get()}")
    print(f"Interest of Area is {root.Interest.get()}")
    print(f"This Friend is  {root.Levelofstudy.get()}")
    print(f"My Friend Dreams is {root.FriendDreams.get()}")
    print(f"More Information is  {root.FutherInformation.get()}")
    print(f"Friend Mobile Number is {root.mobileNumber.get()}")
    print(f"Friend Current Location is {root.CurrentLocation.get()}")
    print(f"My Friend Whatsapp Number is  {root.Whatsapp.get()}")
    print(f"MY Friend Email ID is {root.EmailID.get()}")
    print(f"My Friend is Instagram ID is  {root.InstagramId.get()}")
    print(f"Friend Address is {root.Address.get()}")
    print("+++++++++++++++++++++++++++++++ End Data ++++++++++++++++++++++++++++++++++++")

root = Tk()
root.title("Prem ke yaar...")
root.geometry("1350x800")
root.iconbitmap("friend.ico")
root.maxsize(width=1350,height=800)
root.minsize(width=1350,height=800)

root.categorise = StringVar()
root.FriendName = StringVar()
root.city= StringVar()
root.Birthdate = StringVar()
root.Interest = StringVar()
root.Levelofstudy = StringVar()
root.FriendDreams = StringVar()
root.FutherInformation = StringVar()
root.mobileNumber = StringVar()
root.CurrentLocation = StringVar()
root.Whatsapp = StringVar()
root.EmailID = StringVar()
root.InstagramId = StringVar()
root.Address= StringVar()

lbltitle = Label(root,bd=20,relief=RIDGE,text="Friends of Prem",fg="red",bg="white",font="Arial 35 bold")
lbltitle.pack(side=TOP,fill=X)

dataframe = Frame(root, bd=20,relief=RIDGE)
dataframe.place(x=0,y=100,width=1350,height=400)

dataframeleft =  LabelFrame(dataframe,bd=10,padx=10,relief=RIDGE,font="Arial 12 bold", text="Friend Informations")
dataframeleft.place(x=0,y=5,width=1310,height=350)

# dataframe =  LabelFrame(dataframe,bd=10,padx=10,relief=RIDGE,font="Arial 12 bold")
# dataframe.place(x=10,y=270,width=1290,height=70)


lblNameTablet = Label(dataframeleft,text="Categorise",font="Arial 12 bold",padx=60,pady=6)
lblNameTablet.grid(row=0,column=0)

comNametablet = ttk.Combobox(dataframeleft,textvariable=root.categorise,state="readonly",font="Arial 12 bold",width=33)

comNametablet["values"]=("School","College","Village","Gali","Family")
comNametablet.grid(row=0,column=1)


leblref = Label(dataframeleft,font="Arial 12 bold",text="Friend Name",padx=70)
leblref.grid(row=1,column=0,sticky=W)
txtref =Entry(dataframeleft,font="Arial 13 bold",textvariable=root.FriendName,width=35)
txtref.grid(row=1,column=1)


leblDose = Label(dataframeleft,font="Arial 12 bold",text="City/Village",padx=70,pady=4)
leblDose.grid(row=2,column=0,sticky=W)
txtdose =Entry(dataframeleft,font="Arial 13 bold",textvariable=root.city,width=35)
txtdose.grid(row=2,column=1)


leblNoOfTablets = Label(dataframeleft,font="Arial 12 bold",text="Birth Date",padx=70,pady=6)
leblNoOfTablets.grid(row=3,column=0,sticky=W)
txtnoftablet =Entry(dataframeleft,font="Arial 13 bold",textvariable=root.Birthdate,width=35)
txtnoftablet.grid(row=3,column=1)

leblLot= Label(dataframeleft,font="Arial 12 bold",text="Interest",padx=70,pady=6)
leblLot.grid(row=4,column=0,sticky=W)
txtlLot=Entry(dataframeleft,font="Arial 13 bold",textvariable=root.Interest,width=35)
txtlLot.grid(row=4,column=1)

leblIssueDate = Label(dataframeleft,font="Arial 12 bold",text="Level Of Study",padx=70,pady=6)
leblIssueDate.grid(row=5,column=0,sticky=W)
txtref =Entry(dataframeleft,font="Arial 13 bold",textvariable=root.Levelofstudy,width=35)
txtref.grid(row=5,column=1)

leblExpDate = Label(dataframeleft,font="Arial 12 bold",text="Friend Dreams",padx=70,pady=6)
leblExpDate.grid(row=6,column=0,sticky=W)
txtref =Entry(dataframeleft,font="Arial 13 bold",textvariable=root.FriendDreams,width=35)
txtref.grid(row=6,column=1)

# this is second side column 
leblFutherInfo = Label(dataframeleft,font="Arial 12 bold",text="More Information",padx=80,pady=6)
leblFutherInfo.grid(row=0,column=2,sticky=W)
txtref =Entry(dataframeleft,font="Arial 13 bold",textvariable=root.FutherInformation,width=35)
txtref.grid(row=0,column=3)

leblBlood = Label(dataframeleft,font="Arial 12 bold",text="Mobile Number",padx=80)
leblBlood.grid(row=1,column=2,sticky=W)
txtref =Entry(dataframeleft,font="Arial 13 bold",textvariable=root.mobileNumber,width=35)
txtref.grid(row=1,column=3)


leblStorage = Label(dataframeleft,font="Arial 12 bold",text="Current Location",padx=80,pady=4)
leblStorage.grid(row=2,column=2,sticky=W)
txtref =Entry(dataframeleft,font="Arial 13 bold",textvariable=root.CurrentLocation,width=35)
txtref.grid(row=2,column=3)


leblMedication = Label(dataframeleft,font="Arial 12 bold",text="Whatsapp No.",padx=80,pady=6)
leblMedication.grid(row=3,column=2,sticky=W)
txtref =Entry(dataframeleft,font="Arial 13 bold",textvariable=root.Whatsapp,width=35)
txtref.grid(row=3,column=3)

leblPatient = Label(dataframeleft,font="Arial 12 bold",text="Email Id",padx=80,pady=6)
leblPatient.grid(row=4,column=2,sticky=W)
txtref =Entry(dataframeleft,font="Arial 13 bold",textvariable=root.EmailID,width=35)
txtref.grid(row=4,column=3)

leblNShNumber = Label(dataframeleft,font="Arial 12 bold",text="Instagram Id",padx=80,pady=6)
leblNShNumber.grid(row=5,column=2,sticky=W)
txtref =Entry(dataframeleft,font="Arial 13 bold",textvariable=root.InstagramId,width=35)
txtref.grid(row=5,column=3)

leblPatientName = Label(dataframeleft,font="Arial 12 bold",text="Address",padx=80,pady=6)
leblPatientName.grid(row=6,column=2,sticky=W)
txtref =Entry(dataframeleft,font="Arial 13 bold",textvariable=root.Address,width=35)
txtref.grid(row=6,column=3)


btn=Button(root,text="Submit Data",bg="green",fg="white",font="Arial 15 bold",padx=5,pady=8,command=submit)
btn.place(x=600,y=400)
root.mainloop()