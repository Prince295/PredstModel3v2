import tkinter as interface
from widgets import *
from main import *
from tkinter.messagebox import *
import pickle

class MainWidget():
    def __init__(self, parent = None):
        button = []
        self.mainform = interface.Frame(parent)
        self.mainform.pack(fill = 'both', expand = True)

        form1 = Navs( self.mainform )
        form1.pack(fill = 'y')
        self.form2 = MainFrame( self.mainform )
        self.form2.pack()
        for i in range( 8 ):
            button.append( ThemedButton(form1) )
        button[0].config(text = "Открыть", command = self.open_collection )
        button[1].config(text = "Сохранить", command = self.save_collection)
        button[2].config(text = "Добавить/изменить фрейм", command = self.add_frame)
        button[3].config(text = "Добавить/изменить слот", command = self.add_slot)
        button[4].config(text = "Поиск по названию", command = self.find_keys)
        button[5].config(text = "Удалить", command = self.delete)
        button[6].config(text = "Просмотр коллекции", command = self.watch)
        button[7].config(text = "Поиск по значению", command = self.find_values)

        for i in range(len(button)):
            button[i].pack(in_ = form1, side = 'top', padx = 30, pady = 5)

        self.collection = {}

    def open_collection(self):
        f1 = open( 'temp', 'rb' )
        self.collection = pickle.load( f1 )
        f1.close()
        showinfo( "Открыто", "Успешно!" )

        print( self.collection )

    def save_collection(self):
        f1 = open( 'temp', 'wb' )
        pickle.dump( self.collection, f1 )
        f1.close()
        showinfo( "Сохраненено", "Успешно!" )

    def add_frame(self):
        self.clear_form()
        form1 = Navs( self.form2, padx=0 )
        form1.pack( expand=True, fill="both" )
        form2 = Navs( self.form2, padx=0 )
        form2.pack( expand=True, fill="both" )
        label = []
        entry = []

        container1 = Container( form1 )
        container2 = Container( form2 )
        button1 = CommandButton( container1 )
        button1.config( text='Добавить', command = lambda  : self.add_frame_to_dict(entry))
        button2 = CommandButton( container2 )
        button2.config( text='Отмена', command=lambda: self.clear_form() )

        for i in range( 2 ):
            label.append( OutLabel( form1 ) )
            entry.append( ThemedMessage( form2 ) )

        label[0].config( text="Имя фрейма" )
        label[1].config(text = "Слот-ссылка")




        for i in range( len( label ) ):
            label[i].pack( in_=form1, side='top', padx=10, pady=5 )
            entry[i].pack( in_=form2, side='top', padx=10, pady=5 )
        container1.pack( side='bottom', fill='x', expand=True )
        button1.pack( side='right', padx=0.5 )
        container2.pack( side='bottom', fill='x', expand=True )
        button2.pack( side='left' )

    def add_frame_to_dict(self,entry):
        frame = entry[0].get()
        slot = entry[1].get()

        if frame not in self.collection.keys() :
            self.collection[frame] = {}
            showinfo("Добавление", "Успешно!")
        else:
            if slot != "" :
                self.collection[frame][slot] = {}
            else :
                if askyesno('Изменение','Фрейм с таким названием существует, хотите очистить его? '):
                    self.collection[frame] = {}
                else:
                    pass
        print(self.collection)


    def add_slot(self):

        self.clear_form()
        form1 = Navs( self.form2, padx=0 )
        form1.pack( expand=True, fill="both" )
        form2 = Navs( self.form2, padx=0 )
        form2.pack( expand=True, fill="both" )
        label = []
        entry = []

        container1 = Container( form1 )
        container2 = Container( form2 )
        button1 = CommandButton( container1 )
        button1.config( text='Добавить', command = lambda : self.add_slot_to_dict(entry))
        button2 = CommandButton( container2 )
        button2.config( text='Отмена', command=lambda: self.clear_form() )

        for i in range( 3 ):
            label.append( OutLabel( form1 ) )
            entry.append( ThemedMessage( form2 ) )

        label[0].config(text = "Фрейм")
        label[1].config( text="Слот" )
        label[2].config( text="Значение" )

        for i in range( len( label ) ):
            label[i].pack( in_=form1, side='top', padx=10, pady=5 )
            entry[i].pack( in_=form2, side='top', padx=10, pady=5 )
        container1.pack( side='bottom', fill='x', expand=True )
        button1.pack( side='right', padx=0.5 )
        container2.pack( side='bottom', fill='x', expand=True )
        button2.pack( side='left' )

    def add_slot_to_dict(self,entry):
        frame = entry[0].get()
        slot = entry[1].get()
        value = entry[2].get()
        finder = self.collection
        for k, v in self.collection.items():
            for key, val in v.items():
                if type(val) == dict:
                    if frame in v.keys():
                        finder = v
        if slot not in finder[frame].keys():
            finder[frame].update({slot : value})
            showinfo( "Добавление", "Успешно!" )
        else:
            if askyesno( 'Изменение', 'Слот с таким названием существует, хотите изменить его? ' ):
                finder[frame][slot] = value
            else:
                pass

    def find_keys(self):
        self.clear_form()
        form1 = Navs( self.form2, padx=0 )
        form1.pack( expand=True, fill="both" )
        form2 = Navs( self.form2, padx=0 )
        form2.pack( expand=True, fill="both" )
        label = []
        entry = []

        container1 = Container( form1 )
        container2 = Container( form2 )
        button1 = CommandButton( container1 )
        button1.config( text='Искать', command = lambda : self.find_keys_in_dict(entry) )

        for i in range( 1 ):
            label.append( OutLabel( form1 ) )
            entry.append( ThemedMessage( form2 ) )

        label[0].config( text="Поиск" )

        for i in range( len( label ) ):
            label[i].pack( in_=form1, side='top', padx=10, pady=5 )
            entry[i].pack( in_=form2, side='top', padx=10, pady=5 )
        container1.pack( side='bottom', fill='x', expand=True )
        button1.pack( side='right', padx=0.5 )
        container2.pack( side='bottom', fill='x', expand=True )

    def find_keys_in_dict(self,entry):
        keyword = entry[0].get()
        if ',' in keyword:
            key = keyword.split(",")

        else:
            key =[keyword]

        string = ""
        values = []
        for i in range(len(key)):
            if key[i] in self.collection.keys():
                string += 'Поиск', "Найден фрейм '{}' со слотами '{}' ".format(key[i],list(self.collection[key[i]].keys()))
            else:
                for k,v in self.collection.items():
                    if key[i] in v.keys():
                        if  type(v[key[i]]) == dict:
                            string += "Найден фрейм '{}' по слот-фрейму '{}'  \n".format( k, key[i] )
                            for index in key:
                                if index not in self.collection[k].keys():
                                    string = ""

                        else:
                            values.append(v[key[i]])
                            if len(key)==1:
                                string += "Найден фрейм '{}' по слоту '{}' со значением '{}' \n".format( k, key[i],
                                                                                                     v[key[i]] )
                            else:
                                string = "Найден фрейм '{}' по слотам '{}' со значениями '{}' \n".format( k, key,
                                                                                                         values )
                            for index in key:
                                if index not in self.collection[k].keys():
                                    string = ""

                    else:
                        for keyy, vall in v.items():
                            if type(vall) == dict:
                                if key[i] in vall.keys():
                                    if len(key) ==1:
                                        string += "Найден фрейм '{}' по слоту '{}' в слот-фрейме '{}'  \n".format( k, key[i], keyy )
                                    else:
                                        string = "Найден фрейм '{}' по слотам '{}' в слот-фрейме '{}'  \n".format( k,
                                                                                                                   key,
                                                                                                                   keyy )
                                    for index in key:
                                        if index not in self.collection[k][keyy].keys():
                                            string = ""


        if string == "":
            showinfo("Поиск", "Ничего не найдено!")
        else:
            showinfo("Поиск", string)

    def find_values(self):
        self.clear_form()
        form1 = Navs( self.form2, padx=0 )
        form1.pack( expand=True, fill="both" )
        form2 = Navs( self.form2, padx=0 )
        form2.pack( expand=True, fill="both" )
        label = []
        entry = []

        container1 = Container( form1 )
        container2 = Container( form2 )
        button1 = CommandButton( container1 )
        button1.config( text='Искать', command=lambda: self.find_values_in_dict( entry ) )

        for i in range( 1 ):
            label.append( OutLabel( form1 ) )
            entry.append( ThemedMessage( form2 ) )

        label[0].config( text="Поиск" )

        for i in range( len( label ) ):
            label[i].pack( in_=form1, side='top', padx=10, pady=5 )
            entry[i].pack( in_=form2, side='top', padx=10, pady=5 )
        container1.pack( side='bottom', fill='x', expand=True )
        button1.pack( side='right', padx=0.5 )
        container2.pack( side='bottom', fill='x', expand=True )

    def find_values_in_dict(self, entry):
        keyword = entry[0].get()
        if ',' in keyword:
            key = keyword.split( "," )
            print( key )
        else:
            key = [keyword]

        string = ""
        slots=[]
        for i in range( len( key ) ):
            for k, v in self.collection.items():

                for keyy,val in v.items():
                    if type(val) != dict:
                        if key[i] == val:
                            slots.append(keyy)
                            if len( key ) == 1:
                                string += "Найден фрейм '{}' со слотом '{}' по значению '{}' \n".format(k, keyy, key[i] )
                            else:
                                string += "Найден фрейм '{}' со слотами '{}' по значениям '{}' \n".format( k, slots,key )
                            for index in key:
                                if index not in self.collection[k].values():
                                    string = ""

                    else:
                        for kkey,vall in val.items():
                            if key[i] == vall:
                                slots.append( keyy )
                                if len(key) == 1:
                                    string += "Найден фрейм '{}'  - во фрейме-ссылке '{}' со слотом '{}' по значению '{}' \n".format( k,
                                                                                                         keyy, key[i] )
                                else:
                                    string = "Найден фрейм '{}'  - во фрейме-ссылке '{}'  по значениям '{}' слотов '{}' \n".format(
                                                                                                                k,
                                                                                                                keyy,  key, slots )
                                for index in key:
                                    if index not in self.collection[k][keyy].values():
                                        string = ""

        if string == "":
            showinfo( "Поиск", "Ничего не найдено!" )
        else:
            showinfo( "Поиск", string )

    def delete(self):
        self.clear_form()
        form1 = Navs( self.form2, padx=0 )
        form1.pack( expand=True, fill="both" )
        form2 = Navs( self.form2, padx=0 )
        form2.pack( expand=True, fill="both" )
        label = []
        entry = []

        container1 = Container( form1 )
        container2 = Container( form2 )
        button1 = CommandButton( container1 )
        button1.config( text='Удалить' , command = lambda : self.delete_keys_in_dict(entry))

        for i in range( 1 ):
            label.append( OutLabel( form1 ) )
            entry.append( ThemedMessage( form2 ) )

        label[0].config( text="Объект" )

        for i in range( len( label ) ):
            label[i].pack( in_=form1, side='top', padx=10, pady=5 )
            entry[i].pack( in_=form2, side='top', padx=10, pady=5 )
        container1.pack( side='bottom', fill='x', expand=True )
        button1.pack( side='right', padx=0.5 )
        container2.pack( side='bottom', fill='x', expand=True )

    def delete_keys_in_dict(self,entry):
        keyword = entry[0].get()
        if keyword in self.collection.keys():
            if askyesno('Удаление', "Найден фрейм '{}' со слотами '{}', удалить? ".format(keyword,list(self.collection[keyword].keys()))):
                self.collection.pop(keyword)

        else:
            for k,v in self.collection.items():
                if keyword in v.keys():
                    if askyesno( 'Удаление', "Во фрейме '{}'  Найден слот '{}' со значением '{}' , удалить?".format(k, keyword, v[keyword] ) ):
                        v.pop(keyword)


                elif keyword in v.values():
                    for key,val in v.items():
                        if keyword == val:
                             if askyesno( 'Удаление', " Во фрейме '{}' Найден слот '{}' со значением '{}' , удаление?".format(k, key, keyword ) ):
                                 v.pop(key)
                else:
                    showinfo('Удаление', "Ничего не найдено!")

    def watch(self):
        self.clear_form()
        self.form3 = Navs1( self.form2, padx=0 )
        self.form3.pack( side = 'top', expand=True, fill="both" )
        self.form4 = Navs( self.form2, padx=0 )
        self.form4.pack(side = 'top',  expand=True, fill="both" )

        self.form5 = Navs1( self.form3, padx=40, pady = 40 )
        self.form5.pack( side='top', expand=True, fill="both" )




        sbar = interface.Scrollbar( self.form5 )
        list = interface.Listbox( self.form5, relief='solid', bd=1, font='verdana 12' )


        sbar.config( command=list.yview )
        list.config( yscrollcommand=sbar.set )
        sbar.pack( side='right', fill='y' )
        list.pack( side='left', expand=True, fill='both' )
        self.text_message = ThemedOut( self.form4 )

        pos = 0
        for label in self.collection.keys():
            list.insert( pos, label )
            pos += 1
        list.config( selectmode='single' )
        list.bind( '<Double-1>', self.handleList )
        self.listbox = list

    def handleList(self, event):
        self.index = self.listbox.curselection()
        self.label = self.listbox.get( self.index )
        self.listbox.activate( self.index )
        self.runCommand( self.index )

    def runCommand(self, selection):
        self.text_message.destroy()
        self.text_message = ThemedOut( self.form4 )
        self.text_message.config( text=self.collection[self.label] )


    def clear_form(self):
        self.form2.destroy()
        self.form2 = MainFrame( self.mainform )
        self.form2.pack()


if __name__ == "__main__":
    root = interface.Tk()
    root.geometry( "800x600+100+100" )
    MainWidget( root )
    root.mainloop()