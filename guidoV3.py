import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pyperclip

class app():

    def __init__(self): #Initialzes the main menu.
        self.app = tk.Tk()
        self.app.resizable(width=False, height=False)
        #self.app.geometry('250x250')
        self.app.title('Guido')
        self.description = tk.Label(text='GUIDO. - WIP')
        self.description.grid(row=0)
        self.new_note_button = tk.Button(text='Create new note!', command=self.stickyNotes)
        self.new_note_button.grid(row=1)
        self.open_note_button = tk.Button(text='Open previous note', command=self.openNote)
        self.open_note_button.grid(row=2)
        self.exit_program_button = tk.Button(text='Quit...', command=self.normalQuit)
        self.exit_program_button.grid(row=3)
        self.app.mainloop()

    def normalQuit(self):
        self.app.destroy()

    def quitApp(self): #Quits application
        if messagebox.askyesno('Save?', 'Do you want to save your work?') == True:
            self.saveNote()
            self.app.destroy()
        else:
            self.Notes.destroy()


    def openNote(self): #This function opens the note from the main menu 
        self.stickyNotes()
        self.openFile() 

    def saveNote(self): #Saves the note into a normal text file
        note_contents = self.textWidget.get('1.0', 'end-1c')
        save_file = filedialog.asksaveasfile(mode='w')
        save_file.write(note_contents)
        save_file.close()

    def openFile(self): #Open's a file that the user has pressed
        self.app.filename = filedialog.askopenfilename(filetypes=[('All files', '*.*')])
        file1 = open(self.app.filename)
        self.stickyNotes()
        content = file1.read()
        self.textWidget.insert('1.0', content)

    def searchForWord(self):
        startpos = 1.0
        endpos = 'end-1c'
        word = self.searchEntry.get()
        count = tk.StringVar()
        self.search_word = self.textWidget.search(word, startpos, endpos)

    def searchEntry(self): #This function has the GUI interface for when you want to search a word
        self.searchbox = tk.Toplevel()
        self.searchbox.title('Guido Search')
        self.label1 = tk.Label(self.searchbox, text='Enter search below')
        self.label1.grid(row=0)
        self.search_entry = tk.Entry(self.searchbox)
        self.search_entry.grid(row=1)
        self.search_button = tk.Button(self.searchbox, text='Enter', command=self.searchForWord)
        self.search_button.grid(row=2)

    def aboutInformation(self):
        messagebox.showinfo('Author', 'This program was developed by LT. Email the owner about any bugs or feedback at cosmicjoke5@hotmail.com')



    
    def paste(self): #Pastes whatever is in the user's clipboard.
        self.result = pyperclip.paste()
        self.text_widget.insert('end-1c', self.result)



    def clearWin(self): #This function clears the text widget
        self.text_widget.delete('1.0', 'end-1c')



    def defaultFont(self): #Sets the font back to the default
        self.text_widget.config(font='default')



    def boldFont(self): #Set's the font to bold
        self.text_widget.config(font='bold')



    def courierFont(self): #Set's the font to the courier font.
        self.text_widget.config(font='courier')



    def select_all_text(self): #selects all text in the text widget
        text_to_select = self.text_widget.get('1.0', 'end-1c')
        pyperclip.copy(text_to_select)



    def getWordCount(self):
        words = self.text_widget.get('1.0', 'end-1c')
        split = words.split(' ')
        count = 0
        for letters in words:
            if letters.isalpha():
                count += 1
            else:
                pass
        #count -= 1
        wordCounter = 0
        for item in split:
            if item == '':
                pass
            else:
                wordCounter += 1
        messagebox.showinfo('Word count', '{} words and {} letters'.format(wordCounter, count))
        
    def stickyNotes(self):  #This function is responsible for setting up the text editor
        self.app.withdraw()
        self.Notes = tk.Toplevel(self.app)
        self.Notes.resizable(width=False, height=False)
        #self.Notes.geometry('500x500')
        self.text_widget = tk.Text(self.Notes)  # Sets up scrollbar widget and text widget.
        self.text_widget.grid(row=1)
        self.scrollbar = tk.Scrollbar(self.Notes)
        self.scrollbar.grid(row=0, sticky=tk.E)
        self.scrollbar.config(command=self.text_widget.yview)
        self.text_widget.config(yscrollcommand=self.scrollbar.set)
        self.main_menu = tk.Menu(self.Notes)  # Sets up menu widget's
        self.Notes.config(menu=self.main_menu)
        self.submenu1 = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(label='File...', menu=self.submenu1)
        self.submenu1.add_command(label='New...', command=self.stickyNotes)
        self.submenu1.add_command(label='Save As...', command=self.saveNote)
        self.submenu1.add_command(label='Open...', command=self.openFile)
        self.submenu1.add_separator()
        self.submenu1.add_command(label='Exit...', command=self.quitApp)
        self.submenu2 = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(label='Edit...', menu=self.submenu2)
        self.submenu2.add_command(label='Search...', command=self.searchEntry)
        self.submenu2.add_command(label='Paste...', command=self.paste)
        self.submenu2.add_command(label='Clear Window', command=self.clearWin)
        self.submenu2.add_command(label='Copy All Text', command=self.select_all_text)
        self.fontMenu = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(menu=self.fontMenu, label='Font...')
        self.fontMenu.add_command(label='bold', command=self.boldFont)
        self.fontMenu.add_command(label='Courier', command=self.courierFont)
        self.fontMenu.add_command(label='Default font', command=self.defaultFont)
        self.submenu3 = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(menu=self.submenu3, label='About...')
        self.submenu3.add_command(label='About GUIDO', command=self.aboutInformation)
        self.submenu4 = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(menu=self.submenu4, label='Word count')
        self.submenu4.add_command(label='Get word count', command=self.getWordCount)

app1 = app()
