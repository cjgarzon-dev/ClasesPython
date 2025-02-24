from tkinter import ttk, messagebox
import tkinter as tk
import datetime

class Vehicle:
    def __init__(self, licensePlate, hourIn):
        self.licensePlate = licensePlate
        self.hourIn = hourIn 
    
    def calculateTime(self):
        hourOut = datetime.datetime.now()
        totalTime = hourOut - self.hourIn
        return totalTime.total_seconds() / 60

class ParkingApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Control de Parqueadero')
        self.root.geometry('500x400')
        
        self.vehicles = {}
        
        #ENTRADA DE PLACA
        tk.Label(root, text='Placa del Vehículo: ').pack(pady=5)    #TEXTO
        self.entry_LicensePlate = tk.Entry(root)                     #CAJA DE TEXTO (Entry)
        self.entry_LicensePlate.pack(pady=5)
        
        #BOTONES DE APLICACION
        tk.Button(root, text='Registro de entrada', command=self.registerIn).pack(pady=5)
        tk.Button(root, text='Registro de salida', command=self.registerOut).pack(pady=5)
        
        #TABLA DE VEHICULOS
        self.tree = ttk.Treeview(root, columns=('Placa', 'Hora de Entrada'), show='headings')
        self.tree.heading('Placa', text='Placa')
        self.tree.heading('Hora de Entrada', text='Hora de Entrada')
        #self.tree.heading('Hora de Salida', text='Hora de Salida')
        self.tree.pack(pady=10, fill='both', expand=True)           #fill='both' -> SIRVE PARA USAR TODO EL ESPACIO QUE REQUIERA
    
    def registerIn(self):
        licensePlate = self.entry_LicensePlate.get().upper()
        print(licensePlate)
        
        if licensePlate not in self.vehicles:
            hourNow = datetime.datetime.now().strftime('%H:%M:%S')
            #print(hourNow)
            self.vehicles[licensePlate] = Vehicle(licensePlate, datetime.datetime.now())    # GUARDA LA PLACA COMO DATO MADRE
            self.tree.insert('', 'end', iid=licensePlate, values=(licensePlate, hourNow))
        else:
            messagebox.showerror('Error', 'Placa ya registrada o inválida')

    
    def registerOut(self):
        licensePlate = self.entry_LicensePlate.get().upper()
        
        if licensePlate in self.vehicles:
            vehicle = self.vehicles.pop(licensePlate)
            timeParking = vehicle.calculateTime()
            #print(timeParking)
            self.tree.delete(licensePlate)
            messagebox.showinfo('Info', f'Vehículo de placa: {licensePlate} salió. \nTiempo de parqueo: {timeParking:.2f} minutos')
        else:
            messagebox.showinfo('Salida', 'Placa no encontrada')

root = tk.Tk()
app = ParkingApp(root)
root.mainloop()