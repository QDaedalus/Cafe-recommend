from Tkinter import*
from tkFileDialog import askopenfilename
from xlrd import *
import ttk
import tkFont
import anydbm
import pickle
from recommendations import*
class Import():     ######################## Taking cafe infos from excel file
    def initial(self):

        self.cafes = []
    def importing(self):    #Importing Cafes
        Import.initial(self)
        filename = askopenfilename()
        workbook = open_workbook(filename)
        worksheet = workbook.sheet_by_index(0)
        for i in range(1,worksheet.nrows):
            self.cafes.append(worksheet.cell_value(i,0))
        # print self.list
        self.combobox['values'] = self.cafes
    def addingcafe(self):   #Getting cafe ratings from user
        self.userdict[self.combobox.get()]=self.scale.get()
        print self.userdict
        self.dict['User']=self.userdict
        self.tree.insert('', 'end',text=self.combobox.get(), values=(self.scale.get()))
    def deleting_cafe_ratings(self):
        self.selected_item = self.tree.selection()[0]  ## get selected item
        self.x=(self.tree.item(self.selected_item)['text'])##self.x=item that deleted from treview
        self.tree.delete(self.selected_item)
        del self.userdict[self.x]
        # print self.userdict
class Upload():                         ######Taking informations from database and converting it to dictionary
    def upload_ratings(self):
        db = anydbm.open('ratings.db', 'c')
        self.dict = {}

        for key, values in db.iteritems():
            s = pickle.loads(values)
            self.dict[key] = s
        self.bosliste = [] ##### BURADA LISTELER OLUSTURUP KULLANACAKSIN
        # print
class myGUI(Frame,Import,Upload): #############GUI CLASS
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.userdict = {}
        self.similarity = None
        self.var_pear = BooleanVar()
        self.var_euc = BooleanVar()
        self.var_jac = BooleanVar()
        for r in range(7):
            parent.rowconfigure(r, weight=1)
        for c in range(15):
            parent.columnconfigure(c, weight=1)
        self.first_page()
    # def old_page(self):
    #     self.label_settings.grid_remove()
    #     self.NOR.grid_remove()
    #     self.NORentry.grid_remove()
    #     self.butRSU.grid_remove()
    #     self.butRC.grid_remove()
    #     self.labelSM.grid_remove()
    #     self.check1.grid_remove()
    #     self.check2.grid_remove()
    #     self.check3.grid_remove()
    #     self.label1.grid_remove()
    #     self.label2.grid_remove()
    #     self.label3.grid_remove()
    #     self.labelSU.grid_remove()
    #     self.treeSU.grid_remove()
    #     self.treerate.grid_remove()
    #     self.labelrate.grid_remove()
    #     self.butGUR.grid_remove()
    #
    #     self.tree.grid(row=4, column=2)
    #     self.REMOVE.grid(row=4, column=7)
    #     self.label_Choose.grid(row=1, column=5)
    #     self.combobox.grid(row=2, column=5)
    #     self.label_CR.grid(row=3, column=5)
    #     self.scale.grid(row=4, column=5)
    #     self.ADD.grid(row=6, column=5)
    def second_page(self):
        if self.userdict=={}:
            print 'Please choose some cafes to evaluation !'


        self.mystring =StringVar()

        try:
            self.labelSC.grid_remove()
            self.treeSC.grid_remove()


            self.labelSU.grid_remove()


            self.treeSU.grid_remove()

            self.butGUR.grid_remove()



            self.treerate.grid_remove()




        except AttributeError as error:
            pass


        self.tree.grid_remove()
        self.REMOVE.grid_remove()
        self.label_Choose.grid_remove()
        self.combobox.grid_remove()
        self.label_CR.grid_remove()
        self.scale.grid_remove()
        self.ADD.grid_remove()
        self.label_settings=Label(self.frame_4,text='Settings',fg='black',font='Helvetica 18 bold',bg='palegreen',underline=TRUE)
        self.label_settings.grid(row=0,column=0)
        f = tkFont.Font(self.label_settings, self.label_settings.cget("font"))
        f.configure(underline=True)
        self.label_settings.configure(font=f)
        self.NOR=Label(self.frame_4,text='Number of Recommendation',fg='black',bg='palegreen',width=25)
        self.NOR.grid(row=1,column=0)
        self.NORentry=Entry(self.frame_4,width=7,textvariable=self.mystring)
        self.NORentry.grid(row=2,column=0)
        self.butRSU=Button(self.frame_4,bg='red',text='Recommend\n Similar Users',height = 3, width = 10,fg='white',command=self.recom_user)
        self.butRSU.grid(row=3,column=5)
        self.butRC=Button(self.frame_4,bg='red',text='Recommend\n Cafe',height = 3, width = 10,fg='white',command=self.second_newpage)
        self.butRC.grid(row=4,column=5)
        self.labelSM=Label(self.frame_4,text='Similarity Metrics',fg='black',font='Helvetica 18 bold',bg='palegreen')
        self.labelSM.grid(row=4,column=0)
        self.check1=Checkbutton(self.frame_4,bg='palegreen',variable=self.var_euc,command=self.make_euc)
        self.check1.grid(row=5,column=0)
        self.check2=Checkbutton(self.frame_4,bg='palegreen',variable=self.var_pear,command=self.make_pear)
        self.check2.grid(row=6,column=0)
        self.check3=Checkbutton(self.frame_4,bg='palegreen',variable=self.var_jac,command=self.make_jac)
        self.check3.grid(row=7,column=0)
        self.label1=Label(self.frame_4,text='Euclidean',fg='black',bg='palegreen')
        self.label1.grid(row=5,column=1)
        self.label2=Label(self.frame_4,text='Pearson Metrics',fg='black',bg='palegreen')
        self.label2.grid(row=6,column=1)
        self.label3=Label(self.frame_4,text='Jaccard',fg='black',bg='palegreen')
        self.label3.grid(row=7,column=1)

        self.labelSU=Label(self.frame_5,text='Similar User',fg='black',font='Helvetica 18 bold',bg='palegreen')
        self.labelSU.grid(column=4)
        self.treeSU = ttk.Treeview(self.frame_5, height=5, column=2)
        # self.tree.heading('#1', text='Cafe')
        self.treeSU.heading('#0', text='User')
        self.treeSU.heading('#1', text='Similarity')
        self.treeSU.grid(row=1, column=4)
        self.butGUR=Button(self.frame_5,text="Get User's Rating")
        self.butGUR.grid(column=4)
        # self.labelrate=Label(self.frame_5,text='awndawd',fg='black',bg='palegreen')
        # self.labelrate.grid(column=4)
        self.treerate = ttk.Treeview(self.frame_5, height=5, column=2)
        # self.tree.heading('#1', text='Cafe')
        self.treerate.heading('#0', text='Cafe')
        self.treerate.heading('#1', text='Ratings')
        self.treerate.grid(row=4, column=4)
    def second_newpage(self):

        self.labelSU.grid_remove()
        self.treeSC.grid_remove()
        self.butGUR.grid_remove()
        self.treerate.grid_remove()

        # self.labelrate.grid_remove()

        self.labelSC = Label(self.frame_5, text='Similar Cafes', fg='black', bg='palegreen', font='Helvetica 18 bold')
        self.labelSC.grid(row=0, column=0)
        self.treeSC = ttk.Treeview(self.frame_5, height=15, column=2)
        self.treeSC.heading('#0', text='Cafe')
        self.treeSC.heading('#1', text='Similarity')
        self.treeSC.grid()
        self.cafes = calculateSimilarItems(self.dict)
        self.topcafe = []
        self.topcafescore = []
        self.y = getRecommendedItems(self.dict, self.cafes, 'User')
        print self.y
        for i in range(len(self.y)):
            self.topcafe.append(self.y[i][1])
        print self.topcafe
        for b in range(len(self.y)):
            self.topcafescore.append(float(self.y[b][0]))
        print self.topcafescore

        for j in range(len(self.topcafescore)):
            # print self.topcafescore[j]
            self.treeSC.insert('', 'end', text=self.topcafe[j], values=self.topcafescore[j])
    def third_newpage(self):
        self.labelSU.grid(column=4)
        self.treeSU.grid(row=1, column=4)
        self.butGUR.grid(column=4)
        # self.labelrate.grid(column=4)
        self.treerate.grid(row=4, column=4)
    def recom_user(self):
        #####SIMILAR USER BULMAK
        try:
            self.labelSC.grid_remove()
            self.treeSC.grid_remove()
        except AttributeError as error:
            pass


        try:
            self.labelSC.grid_remove()
            self.treeSC.grid_remove()
        except AttributeError as error:
            pass
        self.labelSU.grid(column=4)
        self.treeSU = ttk.Treeview(self.frame_5, height=5, column=2)
        self.treeSU.heading('#0', text='User')
        self.treeSU.heading('#1', text='Similarity')
        self.treeSU.grid(row=1, column=4)
        self.butGUR.grid(column=4)
        self.treerate.grid(row=4, column=4)

        self.toplist = []
        self.topliste = []
        self.t = topMatches(self.dict, 'User', n=int(self.mystring.get()))
        # print topMatches(self.dict, 'User', n=int(self.mystring.get()))

        for i in range(len(self.t)):
            self.toplist.append(self.t[i][1])
        # print self.toplist
        for b in range(len(self.t)):
            self.topliste.append(float(self.t[b][0]))

        # print self.topliste
        for j in range(len(self.toplist)):
            # print self.toplist[j]
            self.treeSU.insert('', 'end', text=self.toplist[j], values=self.topliste[j])

    def first_page(self):
        #Frame1
        self.frame_1=Frame(bg='palegreen',highlightbackground="black",highlightthickness=2)
        for r in range(12):
            self.frame_1.rowconfigure(r, weight=1)
        for c in range(10):
            self.frame_1.columnconfigure(c, weight=1)
        self.label=Label(self.frame_1,text='CAFE RECOMMENDER',fg='red',font='Helvetica 18 bold',bg='palegreen')
        self.label.grid(row=4,column=4,sticky=W+E+N+S)
        self.frame_1.grid(row=0,column=0,rowspan=1,sticky=W+E+N+S,columnspan=15)

        #Frame2
        self.frame_2=Frame(bg='palegreen',borderwidth=5,highlightbackground="black",highlightthickness=2)
        for r in range(12):
            self.frame_2.rowconfigure(r, weight=1)
        for c in range(10):
            self.frame_2.columnconfigure(c, weight=1)
        self.UCD=Button(self.frame_2,bg='red',text='Upload Cafe Data',height = 3, width = 20,fg='white',command=self.importing)
        self.UCD.grid(row=4,column=2)
        self.UR = Button(self.frame_2, bg='red', text='Upload Ratings',height = 3, width = 20,fg='white',command=self.upload_ratings)
        self.UR.grid(row=4,column=7)
        self.frame_2.grid(row=1,column=0,rowspan=1,sticky=W+E+N+S,columnspan=15)

        #Frame3
        self.frame_3=Frame(bg='palegreen',highlightbackground="black",highlightthickness=2)
        for r in range(15):
            self.frame_3.rowconfigure(r, weight=1)
        for c in range(10):
            self.frame_3.columnconfigure(c, weight=1)
        self.button_rating=Button(self.frame_3, bg='red', text='R\nA\nT\nI\nN\nG',height = 9, width = 5,fg='white',command=self.first_page)
        self.button_rating.grid(row=1,column=2,sticky=W+E+N+S)
        self.button_recommend = Button(self.frame_3, bg='red', text='R\nE\nC\nO\nM\nM\nE\nN\nD', height=9, width=5, fg='white',command=self.second_page)
        self.button_recommend.grid(row=10,column=2,sticky=W+E+N+S)
        self.frame_3.grid(row=2,column=0,rowspan=5,sticky=W+E+N+S,columnspan=1)
        self.bindin1()
        self.bindin2()

        #Frame4
        self.frame_4=Frame(bg='palegreen',highlightbackground="black",highlightthickness=2)
        for r in range(12):
            self.frame_4.rowconfigure(r, weight=1)
        for c in range(10):
            self.frame_4.columnconfigure(c, weight=1)
        self.label_Choose=Label(self.frame_4,text='Choose Cafe',fg='black',font='Helvetica 18 bold',bg='palegreen')
        self.label_Choose.grid(row=1,column=5)
        self.combobox=ttk.Combobox(self.frame_4)
        self.combobox.grid(row=2,column=5)
        self.label_CR=Label(self.frame_4,text='Choose Rating',fg='black',font='Helvetica 18 bold',bg='palegreen')
        self.label_CR.grid(row=3,column=5)
        self.scale=Scale(self.frame_4,from_=0, to=10,orient=HORIZONTAL,bg='palegreen',highlightbackground="palegreen",highlightthickness=2)
        self.scale.grid(row=4,column=5)
        self.ADD=Button(self.frame_4,bg='red',text='ADD',height = 2, width = 10,fg='white',command=self.addingcafe)
        self.ADD.grid(row=6,column=5)
        self.frame_4.grid(row=2, column=1, rowspan=5, sticky=W + E + N + S, columnspan=7)


        #Frame5
        self.frame_5 = Frame(bg='palegreen', highlightbackground="black", highlightthickness=2)
        for r in range(12):
            self.frame_5.rowconfigure(r, weight=1)
        for c in range(10):
            self.frame_5.columnconfigure(c, weight=1)
        self.tree=ttk.Treeview(self.frame_5,height=15,column=2)
        # self.tree.heading('#1', text='Cafe')
        self.tree.heading('#0', text='Cafe')
        self.tree.heading('#1', text='Ratings')
        self.tree.grid(row=4,column=2)
        self.REMOVE=Button(self.frame_5,bg='red',text='REMOVE',height = 3, width = 13,fg='white',command=self.deleting_cafe_ratings)
        self.REMOVE.grid(row=4,column=7)
        self.frame_5.grid(row=2, column=8, rowspan=5, sticky=W + E + N + S, columnspan=7)
    #Bindings LEFT Buttons

    def make_pear(self): ################CHECK BUTTON FUNCTIONS
        if self.var_euc:
            self.dict['User'] = self.userdict
            self.var_euc.set(False)
            self.similarity = sim_pearson

            print'pearson'
        if self.var_jac:
            self.dict['User'] = self.userdict
            self.var_jac.set(False)



        if self.var_pear:
            self.var_pear.set(True)

    def make_euc(self): ################CHECK BUTTON FUNCTIONS
        if self.var_pear:
            self.dict['User'] = self.userdict
            self.var_pear.set(False)
            self.similarity = sim_distance

            print('Euc')
        if self.var_jac:
            self.dict['User'] = self.userdict
            self.var_jac.set(False)


        if self.var_euc:
            self.var_euc.set(True)
    def make_jac(self):  ################CHECK BUTTON FUNCTIONS
        if self.var_pear:
            self.var_pear.set(False)
            self.similarity = sim_distance
            print('jac')
        elif self.var_euc:
            self.dict['User'] = self.userdict
            self.var_euc.set(False)
            self.similarity=sim_jaccard

        if self.var_jac:
            self.var_jac.set(True)

    def on_enter1(self, t):  ##################### LEFT BUTTONs CHANGING COLORS
        self.button_rating['background'] = 'orange'
        # self.a.config(bg = "green")

    def on_leave1(self, t): ##################### LEFT BUTTONs CHANGING COLORS
        self.button_rating['background'] = 'red'
        # self.a.config(bg = "red")

    def on_enter2(self, t):  ##################### LEFT BUTTONs CHANGING COLORS
        self.button_recommend['background'] = 'orange'

    def on_leave2(self, t): ##################### LEFT BUTTONs CHANGING COLORS
        self.button_recommend['background'] = 'red'

    def bindin1(self): ##################### LEFT BUTTONs CHANGING COLORS
        self.button_rating.bind("<Enter>", self.on_enter1)
        self.button_rating.bind("<Leave>", self.on_leave1)

    def bindin2(self): ##################### LEFT BUTTONs CHANGING COLORS
        self.button_recommend.bind("<Enter>", self.on_enter2)
        self.button_recommend.bind("<Leave>", self.on_leave2)


def main():
    root = Tk()
    root.title('tk')
    root.geometry('1000x600')
    app = myGUI(root)
    # app.pack(fill=BOTH, expand=True)
    root.mainloop()

main()
