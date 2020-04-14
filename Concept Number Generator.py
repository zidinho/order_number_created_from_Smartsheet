import smartsheet.sheets
import tkinter as tk

#Smartsheet client acess token
smartsheet_client = smartsheet.Smartsheet('acess_token')


#function to print the current row and delete it in case of repeat
def concept_num():

    #Order Dashboard sheet ID
    my_sheet=smartsheet_client.Sheets.get_sheet(sheet-id)

    # initialize row_id
    row_id = None

    for row in my_sheet.rows:
        # get the ID of the current (first) row
        row_id = row.id

        # get the Cell object for the first cell of the current (first) row
        cell = row.cells[0]

        # set labels
        label1['text'] = int(cell.value)
        label2['text'] = "Your concept number is created" 

        # exit the 'for' loop (so that only the first row is processed)
        break

    # delete the row that was just processed
    if row_id != None:
        smartsheet_client.Sheets.delete_rows(shee_id, row_id)



#create GUI
Height=200
Width=400

root=tk.Tk()

#GUI naming
root.title("Concept Number Creater")

canvas=tk.Canvas(root, height=Height, width=Width)
canvas.pack()

frame=tk.Frame(root, bg="grey")
frame.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.4)

button=tk.Button(root, text="Create",command=concept_num)
button.pack(side='bottom')

#Label 1 is for the number
label1=tk.Label(frame,font=15)
label1.place(relx=0.1, rely=0.1,relwidth=0.8, relheight=0.8)

#Label 2 is for the successful text
label2=tk.Label(root)
label2.place(relwidth=1,relheight=0.2)

root.mainloop()  