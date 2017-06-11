import Tkinter as tk

DICT_TABELAS = {
    "Paciente" : ["Nome", "Telefone", "CPF", "Data Nasc", "Sexo"],

    "Vacina" : ["Nome", "Quantidade", "Lote", "Vencimento"],

    "Remedio" : ["Nome", "Quantidade", "Lote", "Vencimento"],
}

class Lista(tk.Listbox):
    def __init__(self, parent, elementos, *args, **kwargs):
        tk.Listbox.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        for i, elem in enumerate(elementos):
            self.insert(i, elem)
        self.pack(fill="both", expand=True)

class Form(tk.Frame):
    def __init__(self, parent, dict_form, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.dict_form = dict_form
        self.entries = []
        for i, k in enumerate(dict_form):
            label = tk.Label(self, text=k)
            label.grid(row=i, column=0)
            entry = tk.Entry(self)
            entry.grid(row=i, column=1)
            self.entries.append(entry)
        self.pack(fill="both", expand=True)

    def setText(self, lista):
        for i, entry in enumerate(self.entries):
            entry.delete(0, tk.END)
            entry.insert(0, lista[i])

    def getInput(self):
        output = []
        for entry in self.entries:
            output.append(entry.get())
        return output

    def clear(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

class Buttons(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.criar = tk.Button(self, text="Registrar")
        self.ver = tk.Button(self, text="Ver")
        self.voltar = tk.Button(self, text="Back")
        self.delete = tk.Button(self, text="Deletar")
        self.atualizar = tk.Button(self, text="Atualizar")
        self.pack(fill="both", expand=True)

    # Create Register
    def configCR(self):
        self.voltar.grid_forget()
        self.atualizar.grid_forget()
        self.delete.grid_forget()
        self.criar.grid(row=0, column=0)
        self.ver.grid(row= 0,column=1)

    # Update Delete (and back)
    def configUD(self):
        self.ver.grid_forget()
        self.criar.grid_forget()
        self.atualizar.grid(row=0, column=0)
        self.delete.grid(row=0, column=1)
        self.voltar.grid(row=0, column=2)

    def configBack(self):
        self.ver.grid_forget()
        self.criar.grid_forget()
        self.atualizar.grid_forget()
        self.delete.grid_forget()
        self.voltar.grid(row=0, column=1)



    def onCriar(self, command):
        self.criar.bind("<Button-1>", command)

    def onVer(self, command):
        self.ver.bind("<Button-1>", command)

    def onVoltar(self, command):
        self.voltar.bind("<Button-1>", command)

    def onDelete(self, command):
        self.delete.bind("<Button-1>", command)

    def onAtualizar(self, command):
        self.atualizar.bind("<Button-1>", command)



class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.selected_categoria = "Vacina" # O que tiver escolhido na lista da esquerda
        self.selected_element = 0

        # Frame onde fica a lista
        self.frame_lista = tk.Frame(self)
        self.lista = Lista(self.frame_lista, DICT_TABELAS)
        self.frame_lista.grid(row=0, column=0, rowspan=2)

        # Frame onde ficam os forms
        self.frame_form = tk.Frame(self)
        self.form = Form(self.frame_form, DICT_TABELAS['Vacina'])
        self.frame_form.grid(column=2, row=0)

        # Frame onde ficam os butoes
        self.frame_buttons = tk.Frame(self)
        self.buttons = Buttons(self.frame_buttons)
        self.frame_buttons.grid(column=2, row=1)
        self.buttons.configCR()

        # Frame onde ficam as informacoes das tabelas
        self.frame_info = tk.Frame(self)
        self.lista_info = Lista(self.frame_info, ["FAKE DATA"])


        # binds
        self.lista.bind('<<ListboxSelect>>', self.change_categoria)
        self.lista_info.bind('<<ListboxSelect>>', self.show_info)
        self.buttons.onCriar(self.registrar)
        self.buttons.onVer(self.ver)
        self.buttons.onVoltar(self.voltar)

    def change_categoria(self, event):
        selection = event.widget.curselection()
        value = event.widget.get(selection[0])
        self.selected_categoria = value
        self.form.pack_forget()
        self.form = Form(self.frame_form, DICT_TABELAS[value])
        self.buttons.configCR()

    def show_info(self, event):
        selection = event.widget.curselection()
        value = event.widget.get(selection[0])
        self.selected_element = selection[0]
        self.form.pack_forget()
        self.form = Form(self.frame_form, DICT_TABELAS[self.selected_categoria])
        self.form.setText(['FAKE','FAKE','FAKE','FAKE','FAKE','FAKE',])
        self.buttons.configUD()

    def registrar(self, event):
        a = self.form.getInput()
        print a
        self.form.clear()

    def ver(self, event):
        self.frame_info.grid(row=0, column=1,rowspan=2)
        self.buttons.configBack()

    def voltar(self, event):
        self.frame_info.grid_forget()
        self.form.pack_forget()
        self.form = Form(self.frame_form, DICT_TABELAS['Vacina'])
        self.buttons.configCR()



if __name__ == "__main__":
    root = tk.Tk()
    Main(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
