from tkinter import *
from tkcalendar import *
from datetime import datetime
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog
from tkinter import filedialog
import math

# Declared custom colours for the selected shapes on the first window for ease of use
# and to avoid having to remember the hex values

Purple = "#660899"
LightPurple = "#7E0ABD"
DarkPurple = "#54006E"

# Dictionary of colours for the radio buttons
COLORS = {
    "purple": "#A020F0",
    "DarkSlateGray4": "#528B8B",
    "deep sky blue": "#00BFFF",
    "light sea green": "#20B2AA",
    "VioletRed2": "#EE3A8C",
    "gold": "#FFD700",
}

# Selected colours for the radio buttons
SELECTED_COLORS = {
    "#A020F0", 
    "#528B8B",
    "#00BFFF",
    "#20B2AA",
    "#EE3A8C",
    "#FFD700",
}

# Main window for the customer screen

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Customer Screen")
        self.geometry("500x720")
        self.configure(bg="white")

        SelectionWindow(self) # Initialize SelectionWindow inside the main window

# Selection for the shapes
# As well as to make it easier to add new shapes in the future
# The user can select a shape and it will take them to a menu panel where they can select a pattern, colour, accessories and dimensions
# The user can then book a slot to collect their order
# The user can also go back to the shape selection screen

class SelectionWindow(Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.pack(fill="both", expand=True)

        # frames for the top, center and bottom of the repository
        top_frame = Frame(self, bg="white")
        top_frame.place(relx=0.5, rely=0.1, anchor=N)
        center_frame = Frame(self, bg="white")
        center_frame.place(relx=0.5, rely=0.75, anchor=CENTER)
        bottom_frame = Frame(self, bg="white")
        bottom_frame.place(relx=0.5, rely=0.9, anchor=S)

        # Widgets placed in the top, center and bottom frames of the repository
        select_shape_label = ttk.Label(top_frame, text="Select Shape", font=("Amasis MT Pro Black", 20, "bold"), background="white")
        select_shape_label.grid(row=0, column=1, padx=10, pady=0)

        info_label = ttk.Label(center_frame, text="        A button you select,\nwill take you to a menu panel", font=("calibri", 12), background="white")
        info_label.grid(row=1, column=2, padx=10, pady=10)

        # Shapes displayed in the top frame
        # Each shape is displayed in a canvas widget
        cube_canvas = Canvas(top_frame, width=100, height=100, bg="white")
        cube_canvas.grid(row=3, column=0, padx=10, pady=10)
        cube_canvas.create_rectangle(0, 30, 75, 100, fill=Purple)
        cube_canvas.create_polygon(0, 30, 30, 0, 100, 0, 75, 30, fill=LightPurple)
        cube_canvas.create_polygon(100, 0, 100, 70, 75, 100, 75, 30, fill=DarkPurple)

        cuboid_canvas = Canvas(top_frame, width=100, height=100, bg="white")
        cuboid_canvas.grid(row=3, column=1, padx=30, pady=30)
        cuboid_canvas.create_rectangle(0, 60, 90, 90, fill=Purple)
        cuboid_canvas.create_polygon(0, 60, 10, 50, 100, 50, 90, 60, fill=LightPurple)
        cuboid_canvas.create_polygon(100, 50, 100, 75, 90, 90, 90, 60, fill=DarkPurple)

        cyclinder_canvas = Canvas(top_frame, width=100, height=100, bg="white")
        cyclinder_canvas.grid(row=3, column=2, padx=10, pady=10)
        cyclinder_canvas.create_oval(30, 100, 80, 80, fill=Purple)
        cyclinder_canvas.create_polygon(30, 90, 30, 30, 80, 30, 80, 90, fill=Purple)
        cyclinder_canvas.create_oval(30, 40, 80, 10, fill=LightPurple)

        # Buttons
        cube_button = Button(top_frame, text="Cube", command=self.cube_panel, font=("calibri", 12))
        cube_button.grid(row=4, column=0, padx=10, pady=10)
        cuboid_button = Button(top_frame, text="Cuboid", command=self.cuboid_panel, font=("calibri", 12))
        cuboid_button.grid(row=4, column=1, padx=10, pady=10)
        cylinder_button = Button(top_frame, text="Cylinder", command=self.cylinder_panel, font=("calibri", 12))
        cylinder_button.grid(row=4, column=2, padx=10, pady=10)

        exit_button = Button(bottom_frame, text="Exit", command=self.exit_app, font=("calibri", 15), width=30)
        exit_button.grid(row=0, column=0, padx=10, pady=0)

    # Function to switch to the Menu Panel for the shape selected
    # This allows to user to pick any shape and still be sent to the menu panel 
    
    # When selected it sets the dimension frame to the selected shape (Cube)
    def cube_panel(self):
        self.pack_forget()
        self.shape_selected = "Cube"
        print(self.shape_selected)
        menu_panel = MenuPanel(self.master)
        menu_panel.shape_var.set(self.shape_selected)
        menu_panel.switch_frame(self.shape_selected)

    # When selected it sets the dimension frame to the selected shape (Cuboid)
    def cuboid_panel(self):
        self.pack_forget()
        self.shape_selected = "Cuboid"
        print(self.shape_selected)
        menu_panel = MenuPanel(self.master)
        menu_panel.shape_var.set(self.shape_selected)
        menu_panel.switch_frame(self.shape_selected)

    # When selected it sets the dimension frame to the selected shape (Cylinder)
    def cylinder_panel(self):
        self.pack_forget()
        self.shape_selected = "Cylinder"
        print(self.shape_selected)
        menu_panel = MenuPanel(self.master)
        menu_panel.shape_var.set(self.shape_selected)
        menu_panel.switch_frame(self.shape_selected)

    def exit_app(self):
        result = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if result:
            self.quit()

# Menu Panel for the customer screen 
# -> The user can select a pattern, colour, accessories and dimensions
# -> The user can then book a slot to collect their order
# -> The user can also go back to the shape selection screen
# -> The user can also save the order details to a text file
# -> The user can also edit the order details
# -> The user can also close the booking window
# -> The user can also exit the application

class MenuPanel(Frame): # Menu Panel for the customer screen
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.pack(fill="both", expand=True)

        # Frames which use, pack, place, grid
        # Frames are: main_frame, patterns_frame, dimensions_frame, colour_frame, accessories_frame

        main_frame = Frame(self, bg="white")
        main_frame.pack(fill="both", expand=True)
        patterns_frame = LabelFrame(main_frame, bg="white", text="Select Pattern", font=("Helvetica", 8, "bold"))
        patterns_frame.place(relx=0.5, rely=0, anchor=N)
        dimensions_frame = LabelFrame(main_frame, bg="white", text="Enter Dimensions & Change Shape", font=("Helvetica", 8, "bold"))
        dimensions_frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        colour_frame = LabelFrame(main_frame, bg="white", text="Select Colour", font=("Helvetica", 8, "bold"))
        colour_frame.place(relx=0.5, rely=0.9, anchor=S)
        accessories_frame = LabelFrame(main_frame, bg="white", text="Select Accessories", font=("Helvetica", 8, "bold")) 
        accessories_frame.place(relx=0.5, rely=0.5, anchor=N)

        # Variables for the widgets in the frames
        self.combo_var = StringVar()
        self.colour_var = StringVar()
        self.bow_var = StringVar(value="Add Bow")
        self.no_tag_var = StringVar(value="Yes")
        self.gift_tag_var = StringVar()
        self.length_var = DoubleVar()
        self.cube_length_var = DoubleVar()
        self.width_var = DoubleVar()
        self.cylinder_height_var = DoubleVar()
        self.height_var = DoubleVar()
        self.radius_var = DoubleVar()
        self.shape_var = StringVar()

        # Pattern Frames, widgets & dimension frames, widgets
        pattern_two_label = Label(patterns_frame, text="Pattern 2\n(Cheaper Paper: 0.4p Per cm2)", bg="white")
        pattern_two_label.grid(row=1, column=1, padx=10, pady=10)
        pattern_seven_label = Label(patterns_frame, text="Pattern 7\n(Expensive Paper: 0.75p Per cm2)", bg="white")
        pattern_seven_label.grid(row=1, column=2, padx=10, pady=10)

        combo_pattern = ttk.Combobox(patterns_frame, values=["2", "7"], textvariable=self.combo_var)
        combo_pattern.grid(row=3, column=1, padx=10, pady=10)

        self.pattern_2 = Canvas(patterns_frame, width=100, height=100, bg="white")
        self.pattern_2.grid(row=2, column=1, padx=10, pady=10)
        self.pattern_7 = Canvas(patterns_frame, width=120, height=100, bg="white")
        self.pattern_7.grid(row=2, column=2, padx=10, pady=10)

        # Pattern 2, Design using a loop to create a grid of ovals
        oval_size_2 = 20
        num_rows_2 = 5
        num_columns_2 = 5

        for row in range(num_rows_2):
            for col in range(num_columns_2):
                x1 = col * oval_size_2
                y1 = row * oval_size_2
                x2 = x1 + oval_size_2
                y2 = y1 + oval_size_2

                if (row + col) % 2 == 0:
                    fill_color = "magenta" 
                else:
                    fill_color = "white" 

                self.pattern_2.create_oval(x1, y1, x2, y2, fill=fill_color, outline="black")
        pattern = 2 

        # Pattern 7, Design using a loop to create a grid of polygons
        for i in range(7): # Rows
            for j in range(5): # Columns
                x = 12 + j * 25
                y = i * 50
                self.pattern_7.create_polygon(x, y, x - 12, y + 35, x + 13, y + 35, fill="magenta")
                self.pattern_7.create_polygon(x, y + 50, x - 12, y + 15, x + 13, y + 15, fill="magenta")
        
        # Selection of Colour
        # Widgets for the Colour Frame
        # Create a radio button for each colour in the COLORS dictionary
        # When a radio button is selected, the update_color method is called
        # This method updates the colour of the pattern based on the selected colour

        self.colour_var = StringVar()
        row_num = 2
        column_num = 0

        for color_name in COLORS:
            radio_button = ttk.Radiobutton(colour_frame, text=color_name, value=color_name, variable=self.colour_var, command=self.update_color)
            radio_button.grid(row=row_num, column=column_num, padx=10, pady=5)
    
            column_num += 1
    
            if column_num == 3:
                column_num = 0
                row_num += 1

        # Accessories Frame
        # Radio buttons for the bow and gift tag options
        # Define labels and widgets for accessories

        self.bow_label = Label(accessories_frame, text="(Bow costs £1.50)", bg="white")
        self.bow_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.add_bow_radio = ttk.Radiobutton(accessories_frame, text="Add Bow", value="Add Bow", variable=self.bow_var)
        self.add_bow_radio.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.no_bow_radio = ttk.Radiobutton(accessories_frame, text="No Bow", value="No Bow", variable=self.bow_var)
        self.no_bow_radio.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Gift tag label and radio buttons
        gift_tag_text_label = Label(accessories_frame, text="Would you like a Gift Tag?", bg="white")
        gift_tag_text_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.yes_gift_tag_radio = ttk.Radiobutton(accessories_frame, text="Yes", value="Yes", command=self.toggle_radio_button, variable=self.no_tag_var)
        self.yes_gift_tag_radio.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self.no_gift_tag_radio = ttk.Radiobutton(accessories_frame, text="No", value="No", command=self.toggle_radio_button, variable=self.no_tag_var)
        self.no_gift_tag_radio.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Gift tag entry and label
        gift_tag_label = Label(accessories_frame, text="Enter Gift Tag:\n (e.g., each letter costs 2p)", bg="white")
        gift_tag_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        self.gift_tag_entry = Entry(accessories_frame, textvariable=self.gift_tag_var)
        self.gift_tag_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        # Buttons for booking and going back
        Bookings_button = Button(main_frame, text="Book a slot", command=self.open_booking_window, padx=10, pady=10)
        Bookings_button.place(relx=0.8, rely=1, anchor=S)
        back_button = Button(main_frame, text="Go Back", command=self.back, padx=10, pady=10)
        back_button.place(relx=0.2, rely=1, anchor=S)

        shape_optionmenu_label = Label(dimensions_frame, text="Select Shape", bg="white")
        shape_optionmenu_label.grid(row=0, column=0)

        shape_optionmenu = OptionMenu(dimensions_frame, self.shape_var, 'Cube', 'Cuboid', 'Cylinder', command=self.switch_frame)
        shape_optionmenu.grid(row=0, column=1)

        # Create separate frames for each shape
        self.cube_frame = Frame(dimensions_frame)
        self.cuboid_frame = Frame(dimensions_frame)
        self.cylinder_frame = Frame(dimensions_frame)

        # Cube widgets within the cube_frame
        length_entry_label = Label(self.cube_frame, text="Length", bg="white")
        length_entry_label.grid(row=0, column=0)
        length_entry = Entry(self.cube_frame, textvariable=self.cube_length_var)
        length_entry.grid(row=0, column=1)


        # Cuboid widgets within the cuboid_frame
        length_entry_label = Label(self.cuboid_frame, text="Length", bg="white")
        length_entry_label.grid(row=0, column=0)
        length_entry = Entry(self.cuboid_frame, textvariable=self.length_var)
        length_entry.grid(row=0, column=1)

        width_entry_label = Label(self.cuboid_frame, text="Width", bg="white")
        width_entry_label.grid(row=1, column=0)
        width_entry = Entry(self.cuboid_frame, textvariable=self.width_var)
        width_entry.grid(row=1, column=1)

        height_entry_label = Label(self.cuboid_frame, text="Height", bg="white")
        height_entry_label.grid(row=2, column=0)
        height_entry = Entry(self.cuboid_frame, textvariable=self.height_var)
        height_entry.grid(row=2, column=1)


        # Cylinder widgets within the cylinder_frame
        height_entry_label = Label(self.cylinder_frame, text="Height", bg="white")
        height_entry_label.grid(row=0, column=0)
        height_entry = Entry(self.cylinder_frame, textvariable=self.height_var)
        height_entry.grid(row=0, column=1)

        radius_entry_label = Label(self.cylinder_frame, text="Radius", bg="white")
        radius_entry_label.grid(row=1, column=0)
        radius_entry = Entry(self.cylinder_frame, textvariable=self.radius_var)
        radius_entry.grid(row=1, column=1)

    def switch_frame(self, shape):
        # Hide all frames
        self.cube_frame.grid_remove()
        self.cuboid_frame.grid_remove()
        self.cylinder_frame.grid_remove()

        # Show the selected frame
        if shape == 'Cube':
            self.cube_frame.grid(row=1, column=0, padx=10, pady=10)
        elif shape == 'Cuboid':
            self.cuboid_frame.grid(row=1, column=0, padx=10, pady=10)
        elif shape == 'Cylinder':
            self.cylinder_frame.grid(row=1, column=0, padx=10, pady=10)
    
    def order_results(self):
        main_frame = Frame(self, bg="white")
        main_frame.pack(fill="both", expand=True)

    # Function to update the colour of the pattern based on the selected colour
    def update_color(self):
        color = self.colour_var.get()
        if color in COLORS:
            fill_color = COLORS[color]
            for item in self.pattern_2.find_all():
                self.pattern_2.itemconfig(item, fill=fill_color)

            for item in self.pattern_7.find_all():
                self.pattern_7.itemconfig(item, fill=fill_color)

            for index, item in enumerate(self.pattern_2.find_all()):
                if index % 2 == 0:  # Even index, keep it white
                    fill_color = "white"
                else:  # Odd index, use selected color
                    fill_color = COLORS[color]
                self.pattern_2.itemconfig(item, fill=fill_color)


    # -- Function that retrieves data from all inputs
    # -- calculates the cost of the order
    #  -- displays the order details in a messagebox
    # -- saves the order details to a text file

    def complete_order(self):
    
        # Error checks for all user input fields in the booking window
        if self.booking_calendar.get_date() == "":
            messagebox.showerror("Error", "You must enter a booking date")
            return
        if self.collection_calendar.get_date() == "":
            messagebox.showerror("Error", "You must enter a collection date")
            return
        if self.collection_calendar.get_date() == self.booking_calendar.get_date():
            messagebox.showerror("Error", "Booking and collection dates cannot be the same")
            return
        if self.booking_calendar.get_date() == self.collection_calendar.get_date():
            messagebox.showerror("Error", "Booking and collection dates cannot be the same")
            return
        if self.booking_calendar.get_date() > self.collection_calendar.get_date():
            messagebox.showerror("Error", "Collection date must be after booking date")
            return
        if self.booking_calendar.get_date() < datetime.today().strftime('%Y-%m-%d'):
            messagebox.showwarning("Warning", "Booking date must be in the future")
        if self.booking_time_var.get() == "":
            messagebox.showerror("Error", "You must enter a booking time")
            return
        if self.collection_time_var.get() == "":
            messagebox.showerror("Error", "You must enter a collection time")
            return
        if self.booking_time_var.get() == self.collection_time_var.get():
            messagebox.showerror("Error", "Booking and collection times cannot be the same")
            return
        if self.booking_time_var.get() == "9:00 PM":
            messagebox.showwarning("Warning", "Booking time must be before 9:00 PM")
            return
        if self.booking_time_var.get() == "10:00 PM":
            messagebox.showwarning("Error", "Booking time must be before 10:00 PM")
            return
        if self.collection_time_var.get() == "8:00 PM":
            messagebox.showerror("Error", "Collection time must be before 8:00 PM")
            return
        
        
        self.booking_window.withdraw()

        # Get the values of the variables
        self.cube_length_var.get()
        pattern = self.combo_var.get()
        self.colour_var.get()
        bow = self.bow_var.get()
        self.no_tag_var.get()
        self.gift_tag_var.get()
        self.booking_time_var.get()
        self.collection_time_var.get()
        self.booking_calendar.get_date()
        self.collection_calendar.get_date()

        # Calculate the cost of the gift tag
        cost_per_letter = 0.02
        num_letters = len(self.gift_tag_var.get())
        letter_count_cost = num_letters * cost_per_letter

        area = (self.length_var.get() * self.width_var.get() * self.height_var.get())

        # Calculate the cost of the pattern
        if pattern == "2":
            price_per_cm2 = 0.4
        elif pattern == "7":
            price_per_cm2 = 0.75
        else:
            price_per_cm2 = 0

        total_cost = price_per_cm2 * area

        # Calculate the cost of the bow
        if bow == "Add Bow":
            bow_cost = 1.5
        else:
            bow_cost = 0

        # Calculate the total cost

        # Calculate the cost of the cube
        shape = self.shape_var.get()
        if shape == 'Cube':
            area = round(self.calcCubeArea(float(self.cube_length_var.get())),2)
            total_cost = price_per_cm2 * area
            print(area)
        
        # Calculate the cost of the cuboid
        elif shape == 'Cuboid':
            area = round(self.calcArea(float(self.length_var.get()), float(self.width_var.get()), float(self.height_var.get())),2)
            total_cost = price_per_cm2 * area
            print(area)

        # Calculate the cost of the cylinder
        elif shape == 'Cylinder':
            area = round(self.calc_cylinder_surface_area(float(self.radius_var.get()), float(self.cylinder_height_var.get())),2)
            total_cost = price_per_cm2 * area
            print (total_cost)
            print(area)
        
        final_cost = total_cost
    
        final_cost_rounded = round(final_cost)
        final_cost_formatted = (final_cost_rounded / 100)
        print(final_cost_formatted)
        
        final_cost_formatted = (bow_cost + letter_count_cost + final_cost_formatted)

        print("Pattern: \n", self.combo_var.get(),"Colour: \n", self.colour_var.get(),"bow: \n", self.bow_var.get(),"gift tag: \n", self.no_tag_var.get(),"letter cost: \n", letter_count_cost)
        print(area)
        
        messagebox.showinfo("Order Complete", f"Shape: {shape}\nPattern: {self.combo_var.get()}\nColour: {self.colour_var.get()}\nBow: {self.bow_var.get()}\nNo Gift Tag: {self.no_tag_var.get()}\nGift Tag Text: {self.gift_tag_var.get()}\nArea: {area}cm2\nLetter Count Cost: £{letter_count_cost}\nFinal Cost: £{final_cost_formatted}\nBooking Date: {self.booking_calendar.get_date()}\nBooking Time: {self.booking_time_var.get()}\nCollection Date: {self.collection_calendar.get_date()}\nCollection Time: {self.collection_time_var.get()}")
        
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            text_to_append = simpledialog.askstring("Nearly there!\n", "Enter your name to save your order as a txt.file:")
            if text_to_append is None:
                messagebox.showwarning("Operation Cancelled", "No named entered, file not saved.")
            else:
                # Check if the name is empty
                if not text_to_append:
                    raise ValueError("Name cannot be empty")
                with open(file_path, "a") as file:
                    file.write(f"\nCustomer Name: {text_to_append}\nShape: {shape}\nPattern: {self.combo_var.get()}\nColour: {self.colour_var.get()}\nBow: {self.bow_var.get()}\nNo Gift Tag: {self.no_tag_var.get()}\nGift Tag Text: {self.gift_tag_var.get()}\nArea: {area}cm2\nLetter Count Cost: £{letter_count_cost}\nFinal Cost: £{final_cost_formatted}\nBooking Date: {self.booking_calendar.get_date()}\nBooking Time: {self.booking_time_var.get()}\nCollection Date: {self.collection_calendar.get_date()}\nCollection Time: {self.collection_time_var.get()}\n")
                    messagebox.showinfo("File Saved", f"File saved to {file_path}")

    # Function to edit the order details
    def edit_file(self):

        # Error checks for all user input fields in the booking window
        if self.booking_calendar.get_date() == "":
            messagebox.showerror("Error", "You must enter a booking date")
            return
        if self.collection_calendar.get_date() == "":
            messagebox.showerror("Error", "You must enter a collection date")
            return
        if self.collection_calendar.get_date() == self.booking_calendar.get_date():
            messagebox.showerror("Error", "Booking and collection dates cannot be the same")
            return
        if self.booking_calendar.get_date() == self.collection_calendar.get_date():
            messagebox.showerror("Error", "Booking and collection dates cannot be the same")
            return
        if self.booking_calendar.get_date() > self.collection_calendar.get_date():
            messagebox.showerror("Error", "Collection date must be after booking date")
            return
        if self.booking_calendar.get_date() < datetime.today().strftime('%Y-%m-%d'):
            messagebox.showwarning("Warning", "Booking date must be in the future")
        if self.booking_time_var.get() == "":
            messagebox.showerror("Error", "You must enter a booking time")
            return
        if self.collection_time_var.get() == "":
            messagebox.showerror("Error", "You must enter a collection time")
            return
        if self.booking_time_var.get() == self.collection_time_var.get():
            messagebox.showerror("Error", "Booking and collection times cannot be the same")
            return


        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                contents = file.read()
                messagebox.showinfo("File Contents", contents)
        


    # Calculate the area of the cube
    def calcCubeArea(self, length): 
        area = length * 6
        return area

    # Calculate the area of the cuboid
    def calcArea(self, length, width, height): 
        area = length * width * height
        return area

    # Calculate the area of the cylinder
    def calc_cylinder_surface_area(self, radius, height):
        radius = float(radius)
        height = float(height)
        area = 2 * math.pi * radius * (radius + height)
        return area

    # Toggle the gift tag entry based on the radio button selection
    def toggle_radio_button(self):
        if self.no_tag_var.get() == "No":
            error = messagebox.askyesno("Error", "Are you sure you want to remove the gift tag?")
            if error:
                self.gift_tag_var.set("")
                self.gift_tag_entry.configure(state="disabled")
            else:
                self.gift_tag_entry.configure(state="normal")
        else:
            self.gift_tag_entry.configure(state="normal")
    
    # Function to open the booking window
    def open_booking_window(self):
        # Error Checks for all user input fields
        pattern = self.combo_var.get()
        if pattern == "":
            messagebox.showerror("Value Error", "Please select a pattern")
            return
        shape = self.shape_var.get()
        if shape in ['Cube']:
            if self.cube_length_var.get() == 0:
                messagebox.showerror("Error", "Please enter length")
                return
        if shape in ['Cuboid']:
            if self.length_var.get() == 0:
                messagebox.showerror("Error", "Please enter length")
                return
            if self.width_var.get() == 0:
                messagebox.showerror("Error", "Please enter width")
                return
            if self.height_var.get() == 0:
                messagebox.showerror("Error", "Please enter height")
                return
        elif shape == 'Cylinder':
            if self.radius_var.get() == 0:
                messagebox.showerror("Error", "Please enter radius")
                return
            if self.height_var.get() == 0:
                messagebox.showerror("Error", "Please enter height")
                return
        if self.colour_var.get() == "":
            messagebox.showerror("Value Error", "Please select a colour")
            return
        if self.bow_var.get() == "":
            messagebox.showerror("Value Error", "Please select a bow option")
            return
        if self.no_tag_var.get() == "":
            messagebox.showerror("Value Error", "Please select a gift tag option")
            return
        if self.no_tag_var.get() == "Yes":
            if self.gift_tag_var.get() == "":
                messagebox.showerror("Value Error", "Please enter gift tag text")
                return
        
        
        # Open the booking window
        self.booking_window = Toplevel(self.master)
        self.booking_window.title("Booking Window")
        main_frame = Frame(self.booking_window, bg="white")
        main_frame.pack(fill="both", expand=True)

        # Calendar widgets for booking and collection dates
        self.current_date = datetime.today()
        self.booking_calendar  = Calendar(main_frame, selectmode='day', year=self.current_date.year, month=self.current_date.month, day=self.current_date.day)
        self.booking_calendar.grid(row=1, column=0, padx=10, pady=10)
        self.collection_calendar  = Calendar(main_frame, selectmode='day', year=2024, month=5, day=22)
        self.collection_calendar.grid(row=3, column=0, padx=10, pady=10)
        self.booking_calendar.get_date()
        self.collection_calendar.get_date()

        booking_date_label = Label(main_frame, text="Enter Booking Date", font=("Helvetica", 12, "bold"))
        booking_date_label.grid(row=0, column=0, padx=10, pady=10)
        
        # Entry widgets for booking and collection times
        self.booking_time_var = StringVar()

        # Booking Time List
        time_booking = [
            "9:00 AM", "10:00 AM", "11:00 AM", 
            "12:00 PM", "1:00 PM", "2:00 PM", 
            "3:00 PM", "4:00 PM", "5:00 PM", 
            "6:00 PM", "7:00 PM", "8:00 PM", 
            "9:00 PM", "10:00 PM"
            ]
        booking_time_label = Label(main_frame, text="Select Booking Time", font=("Helvetica", 12, "bold"))
        booking_time_label.grid(row=0, column=1, padx=10, pady=10)
        self.booking_time_entry = ttk.Combobox(main_frame, values=time_booking, textvariable=self.booking_time_var)
        self.booking_time_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Collection Date Label
        collection_date_label = Label(main_frame, text="Enter Collection Date", font=("Helvetica", 12, "bold"))
        collection_date_label.grid(row=2, column=0, padx=10, pady=10)

        # Collection Time Entry
        self.collection_time_var = StringVar()

        # Collection Time List
        time_collection = [
            "9:00 AM", "10:00 AM", "11:00 AM",
            "12:00 PM", "1:00 PM", "2:00 PM",
            "3:00 PM", "4:00 PM", "5:00 PM",
            "6:00 PM", "7:00 PM", "8:00 PM",
        ]

        # Collection Time Label
        # Collection Time Entry
        collection_date_label = Label(main_frame, text="Select Collection Time", font=("Helvetica", 12, "bold"))
        collection_date_label.grid(row=2, column=1, padx=10, pady=10)
        self.collection_time_entry = ttk.Combobox(main_frame, values=time_collection, textvariable=self.collection_time_var)
        self.collection_time_entry.grid(row=3, column=1, padx=10, pady=10)

        close_button = Button(main_frame, text="Close", command=self.close_booking_window)
        close_button.grid(row=4, column=0, padx=10, pady=10)

        edit_order = Button(main_frame, text="Edit Order", command=self.edit_file)
        edit_order.grid(row=4, column=2, padx=10, pady=10)

        complete_button = Button(main_frame, text="Complete", command=self.complete_order)
        complete_button.grid(row=4, column=1, padx=10, pady=10)

        # Function to close the booking window
    def close_booking_window(self):
        response = messagebox.askyesno("Close Window", "Are you sure you want to close the booking window?")
        if response: YES
        self.booking_window.withdraw()

        # Function to close the booking window without losing data
    def exit_and_save(self): 
        booking_date = self.booking_calendar.get_date()
        booking_time = self.booking_time_var.get()
        collection_date = self.collection_calendar.get_date()
        collection_time = self.collection_time_var.get()

        print(booking_date, booking_time, collection_date, collection_time)
        messagebox.showinfo("Booking Details", f"Booking Date: {booking_date}\nBooking Time: {booking_time}\nCollection Date: {collection_date}\nCollection Time: {collection_time}")

        # Function to close the booking window
    def back(self):
        response = messagebox.askyesno("Go Back", "Are you sure you want to go back?\n All data will be lost.")
        if response:
            self.pack_forget()
            panel_one = SelectionWindow(self.master)

def main():
    app.mainloop()
if __name__ == "__main__":
    app = App()
    main()