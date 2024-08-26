import tkinter as tk
from tkinter import messagebox

class CarRentalSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Rental Management System")
        self.root.geometry("400x500")
        
        self.available_cars = 10  # Initial number of cars available
        
        # Labels and Entries for user details
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(root, text="Mobile No.:").grid(row=1, column=0, padx=10, pady=10)
        self.mobile_entry = tk.Entry(root)
        self.mobile_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=10)
        self.gender_entry = tk.Entry(root)
        self.gender_entry.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(root, text="ID Proof:").grid(row=3, column=0, padx=10, pady=10)
        self.id_proof_entry = tk.Entry(root)
        self.id_proof_entry.grid(row=3, column=1, padx=10, pady=10)
        
        tk.Label(root, text="Location:").grid(row=4, column=0, padx=10, pady=10)
        self.location_entry = tk.Entry(root)
        self.location_entry.grid(row=4, column=1, padx=10, pady=10)
        
        tk.Label(root, text="Entry Time:").grid(row=5, column=0, padx=10, pady=10)
        self.entry_time_entry = tk.Entry(root)
        self.entry_time_entry.grid(row=5, column=1, padx=10, pady=10)
        
        tk.Label(root, text="Age:").grid(row=6, column=0, padx=10, pady=10)
        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=6, column=1, padx=10, pady=10)
        
        # Rent Car button
        rent_button = tk.Button(root, text="Rent Car", command=self.rent_car)
        rent_button.grid(row=7, column=0, columnspan=2, pady=20)
        
        # Label to show available cars
        self.available_label = tk.Label(root, text=f"Cars Available: {self.available_cars}")
        self.available_label.grid(row=8, column=0, columnspan=2, pady=10)
        
    def rent_car(self):
        if self.available_cars <= 0:
            messagebox.showwarning("No Cars Available", "Sorry, all cars are rented out!")
            return
        
        # Get user inputs
        name = self.name_entry.get()
        mobile = self.mobile_entry.get()
        gender = self.gender_entry.get()
        id_proof = self.id_proof_entry.get()
        location = self.location_entry.get()
        entry_time = self.entry_time_entry.get()
        age = self.age_entry.get()
        
        # Validate inputs
        if not all([name, mobile, gender, id_proof, location, entry_time, age]):
            messagebox.showerror("Input Error", "All fields are required!")
            return
        
        # Reduce the number of available cars
        self.available_cars -= 1
        self.available_label.config(text=f"Cars Available: {self.available_cars}")
        
        # Clear the entries
        self.name_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.id_proof_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.entry_time_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        
        messagebox.showinfo("Success", f"Car rented successfully to {name}!")
        
# Create the main window
root = tk.Tk()
app = CarRentalSystem(root)
root.mainloop()
