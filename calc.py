from tkinter import *
import math
import time

root = Tk()
root.title('Circle Calculations')

pi = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494639522473719070217986094370277053921717629317675238467481846766940513200056812714526356082778577134275778960917363717872146844090122495343014654958537105079227968925892354201995611212902196086403441815981362977477130996051870721134999999837297804995105973173281609631859502445945534690830264252230825334468503526193118817101000313783875288658753320838142061717766914730359825349042


def home():
    # creating widgets and place them in root
    Label(root, text='Shapes:').grid(row=0, column=0)
    Button(root, text='circle', command=circle, padx=5).grid(row=1, column=0)
    Button(root, text='square', command=square).grid(row=1, column=2)
    Button(root, text='rectangle', command=rectangle).grid(row=1, column=3)
    Button(root, text='circular arcs', command=circular_arcs).grid(row=1, column=1)
    Label(root, text='Body:').grid(row=2, column=0)
    Button(root, text='Cube', command=cube, padx=5).grid(row=3, column=0)
    Button(root, text='Cuboid', command=cuboid, padx=13).grid(row=3, column=1)


def circle():
    window_clear()
    print('Debug: Circle function called')


    def calculate_circle():
        d = entry_d.get()
        r = entry_r.get()
        u = entry_u.get()
        A = entry_A.get()
        clear_circle()
        try:
            if r != '':
                entry_u.insert(0, str(float(r) * 2 * pi))
                entry_d.insert(0, str(float(r) * 2))
                entry_r.insert(0, str(float(r)))
                entry_A.insert(0, str(pi * float(r) ** 2))
            elif d != '':
                entry_u.insert(0, str(float(d) * pi))
                entry_d.insert(0, str(float(d)))
                entry_r.insert(0, str(float(d) / 2))
                entry_A.insert(0, str(float(d) / 2 * float(d) / 2 * pi))
            elif u != '':
                entry_u.insert(0, str(float(u)))
                entry_d.insert(0, str(float(u) / pi))
                entry_r.insert(0, str(float(u) / pi / 2))
                entry_A.insert(0, str(float(u) / pi / 2 * float(u) / pi / 2 * pi))
            elif A != '':
                entry_u.insert(0, str(2 * math.sqrt(float(A) / pi) * pi))
                entry_d.insert(0, str(math.sqrt(float(A)) / pi * 2))
                entry_r.insert(0, str(math.sqrt(float(A)) / pi))
                entry_A.insert(0, str(float(A)))
            else:
                warning = Button(root, text='please enter something', fg='red', command=lambda: warning.grid_forget())
                warning.grid(row=10, column=0, columnspan=3)
        except ValueError:
            warning = Button(root, text='please enter a number', fg='red', command=lambda: warning.grid_forget())
            warning.grid(row=10, column=0, columnspan=3)

    def clear_circle():
        entry_A.delete(0, END)
        entry_u.delete(0, END)
        entry_d.delete(0, END)
        entry_r.delete(0, END)

    def back():
        window_clear()
        home()

    # creating all widgets
    Label_d = Label(root, text='diameter (d)')
    entry_d = Entry(root)
    Label_r = Label(root, text='radius (r)')
    entry_r = Entry(root)
    Label_u = Label(root, text='circumference (u)')
    entry_u = Entry(root)
    Label_A = Label(root, text='area (A)')
    entry_A = Entry(root)
    calculate = Button(root, text='calculate', command=calculate_circle)
    clear = Button(root, text='clear', command=clear_circle)
    back = Button(root, text='<', command=back)

    # place widgets in root
    Label_d.grid(row=1, column=0, columnspan=3)
    entry_d.grid(row=2, column=0, columnspan=3)
    Label_r.grid(row=3, column=0, columnspan=3)
    entry_r.grid(row=4, column=0, columnspan=3)
    Label_u.grid(row=5, column=0, columnspan=3)
    entry_u.grid(row=6, column=0, columnspan=3)
    Label_A.grid(row=7, column=0, columnspan=3)
    entry_A.grid(row=8, column=0, columnspan=3)
    calculate.grid(row=9, column=1)
    clear.grid(row=9, column=2)
    back.grid(row=9, column=0)


def square():
    def calculate_square():
        # reading the entry widgets
        a = a_entry.get()
        surface = surface_square_e.get()

        clear_square()

        try:
            if a != '':
                surface_square_e.insert(0, str(float(a) ** 2))
                a_entry.insert(0, a)
            elif surface != '':
                a_entry.insert(0, str(math.sqrt(float(surface))))
                surface_square_e.insert(0, surface)
            else:
                warning = Button(root, text='please enter something', fg='red', command=lambda: warning.grid_forget())
                warning.grid(row=5, column=0, columnspan=3)
        except ValueError:
            warning = Button(root, text='please enter a number', fg='red', command=lambda: warning.grid_forget())
            warning.grid(row=10, column=0, columnspan=3)

    def clear_square():
        a_entry.delete(0, END)
        surface_square_e.delete(0, END)

    def back():
        window_clear()
        home()

    window_clear()

    # creating Widgets
    side_length_a = Label(root, text='side length (a)')
    a_entry = Entry(root)
    surface_square = Label(root, text='area (A)')
    surface_square_e = Entry(root)
    calculate = Button(root, text='calculate', command=calculate_square)
    clear = Button(root, text='clear', command=clear_square)
    back = Button(root, text='<', command=back)

    # place widgets in root
    side_length_a.grid(row=0, column=0, columnspan=3)
    a_entry.grid(row=1, column=0, columnspan=3)
    surface_square.grid(row=2, column=0, columnspan=3)
    surface_square_e.grid(row=3, column=0, columnspan=3)
    calculate.grid(row=4, column=1)
    clear.grid(row=4, column=2)
    back.grid(row=4, column=0)


def rectangle():
    window_clear()

    def calculate_rectangle():
        a = side_length_a_e.get()
        b = side_length_b_e.get()
        A = surface_e.get()
        clear_rectangle()
        surface_e.config(state='normal')

        try:
            if a != '' and b != '':
                surface_e.insert(0, str(float(a) * float(b)))
                side_length_b_e.insert(0, b)
                side_length_a_e.insert(0, a)
                surface_e.config(state='readonly')
            elif a != '' and A != '':
                side_length_b_e.insert(0, str(float(A) / float(a)))
                side_length_a_e.insert(0, a)
                surface_e.insert(0, A)
            elif b != '' and A != '':
                side_length_a_e.insert(0, str(float(A) / float(b)))
                side_length_b_e.insert(0, b)
                surface_e.insert(0, A)
            else:
                warning = Button(root, text='please enter something', fg='red', command=lambda: warning.grid_forget())
                warning.grid(row=10, column=0, columnspan=3)
        except ValueError:
            warning = Button(root, text='please enter a number', fg='red', command=lambda: warning.grid_forget())
            warning.grid(row=10, column=0, columnspan=3)

    def clear_rectangle():
        surface_e.config(state='normal')
        side_length_a_e.delete(0, END)
        side_length_b_e.delete(0, END)
        surface_e.delete(0, END)

    def back():
        window_clear()
        home()

    # creating widgets
    side_length_a = Label(root, text='side length (a)')
    side_length_a_e = Entry(root)
    side_length_b = Label(root, text='side length (b)')
    side_length_b_e = Entry(root)
    surface = Label(root, text='area (A)')
    surface_e = Entry(root)
    calculate = Button(root, text='calculate', command=calculate_rectangle)
    clear = Button(root, text='clear', command=clear_rectangle)
    back = Button(root, text='<', command=back)

    # place widgets in root
    side_length_a.grid(row=0, column=0, columnspan=3)
    side_length_a_e.grid(row=1, column=0, columnspan=3)
    side_length_b.grid(row=2, column=0, columnspan=3)
    side_length_b_e.grid(row=3, column=0, columnspan=3)
    surface.grid(row=4, column=0, columnspan=3)
    surface_e.grid(row=5, column=0, columnspan=3)
    back.grid(row=6, column=0)
    calculate.grid(row=6, column=1)
    clear.grid(row=6, column=2)


def window_clear():
    for widget in root.winfo_children():
        widget.destroy()


def circular_arcs():
    window_clear()

    def back():
        window_clear()
        home()

    def clear_arc():
        radius_e.delete(0, END)
        alpha_e.delete(0, END)
        A_alpha_e.delete(0, END)
        b_alpha_e.delete(0, END)

    def calculate_arc():
        r = radius_e.get()
        alpha = alpha_e.get()
        A = A_alpha_e.get()
        b = b_alpha_e.get()
        clear_arc()

        try:
            if r != '' and alpha != '':
                portion = float(alpha) / 360
                radius_e.insert(0, r)
                alpha_e.insert(0, alpha)
                b_alpha_e.insert(0, str(2 * pi * float(r) * portion))
                A_alpha_e.insert(0, str(pi * float(r) ** 2 * portion))
            elif A != '' and r != '':
                pi_r_squared = float(r) * float(r) * pi
                A_divided_r = float(A) / float(r)
                A_alpha_e.insert(0, A)
                radius_e.insert(0, r)
                alpha_e.insert(0, str(float(A) / pi_r_squared * 360))
                b_alpha_e.insert(0, str(2 * A_divided_r))
            elif r != '' and b != '':
                pi_r_squared = float(r) * float(r) * pi
                radius_e.insert(0, r)
                b_alpha_e.insert(0, b)
                A_alpha_e.insert(0, str(float(b) * float(r) * 0.5))
                alpha_e.insert(0, str(float(b) * float(r) * 0.5 / pi_r_squared * 360))
            elif A != '' and b != '':
                r = float(A) * 2 / float(b)
                pi_r_squared = r * r * pi
                A_alpha_e.insert(0, A)
                b_alpha_e.insert(0, b)
                radius_e.insert(0, str(r))
                alpha_e.insert(0, str(float(b) * r * 0.5 / pi_r_squared * 360))
            elif alpha != '' and b != '':
                portion = float(alpha) / 360
                r = (float(b) / (2 * pi)) * (360 / float(alpha))
                pi_r_squared = (r * r) * pi
                alpha_e.insert(0, alpha)
                b_alpha_e.insert(0, b)
                radius_e.insert(0, str(r))
                A_alpha_e.insert(0, pi_r_squared * portion)
            else:
                warning = Button(root, text='please enter two numbers', fg='red', command=lambda: warning.grid_forget())
                warning.grid(row=10, column=0, columnspan=3)
        except ValueError:
            warning = Button(root, text='please enter a number', fg='red', command=lambda: warning.grid_forget())
            warning.grid(row=10, column=0, columnspan=3)

    radius = Label(root, text='radius (r)')
    radius_e = Entry(root)
    alpha = Label(root, text='Alpha (\u03B1)')
    alpha_e = Entry(root)
    A_alpha = Label(root, text='area (A\u03B1)')
    A_alpha_e = Entry(root)
    b_alpha = Label(root, text='circular arc (b\u03B1)')
    b_alpha_e = Entry(root)
    calculate = Button(root, text='calculate', command=calculate_arc)
    clear = Button(root, text='clear', command=clear_arc)
    back = Button(root, text='<', command=back)

    radius.grid(row=0, column=0, columnspan=3)
    radius_e.grid(row=1, column=0, columnspan=3)
    alpha.grid(row=2, column=0, columnspan=3)
    alpha_e.grid(row=3, column=0, columnspan=3)
    A_alpha.grid(row=4, column=0, columnspan=3)
    A_alpha_e.grid(row=5, column=0, columnspan=3)
    b_alpha.grid(row=6, column=0, columnspan=3)
    b_alpha_e.grid(row=7, column=0, columnspan=3)
    back.grid(row=8, column=0)
    calculate.grid(row=8, column=1)
    clear.grid(row=8, column=2)


def cube():
    window_clear()

    def back():
        window_clear()
        home()

    def clear_cube():
        side_l_a_E.delete(0, END)
        volume_E.delete(0, END)
        edgelength_E.delete(0, END)

    def calculate_cube():
        a = side_l_a_E.get()
        vol = volume_E.get()
        edge = edgelength_E.get()

        clear_cube()

        try:
            if a != '':
                side_l_a_E.insert(0, a)
                volume_E.insert(0, str(float(a) ** 3))
                edgelength_E.insert(0, str(float(a) * 12))
            elif vol != '':
                volume_E.insert(0, vol)
                side_l_a_E.insert(0, str(float(vol) ** (1. / 3.)))
                edgelength_E.insert(0, str((float(vol) ** (1. / 3.) * 12)))
            elif edge != '':
                edgelength_E.insert(0, edge)
                side_l_a_E.insert(0, str(float(edge) / 12))
                volume_E.insert(0, str((float(edge) / 12) ** 3))
            else:
                warning = Button(root, text='please enter a number', fg='red', command=lambda: warning.grid_forget())
                warning.grid(row=10, column=0, columnspan=3)
        except ValueError:
            warning = Button(root, text='please enter a number', fg='red', command=lambda: warning.grid_forget())
            warning.grid(row=10, column=0, columnspan=3)

    side_l_a = Label(root, text='side length (a)')
    side_l_a_E = Entry(root)
    volume = Label(root, text='volume (V)')
    volume_E = Entry(root)
    edgelength = Label(root, text='edge length')
    edgelength_E = Entry(root)
    calculate = Button(root, text='calculate', command=calculate_cube)
    clear = Button(root, text='clear', command=clear_cube)
    back = Button(root, text='<', command=back)

    side_l_a.grid(row=0, column=0, columnspan=3)
    side_l_a_E.grid(row=1, column=0, columnspan=3)
    volume.grid(row=2, column=0, columnspan=3)
    volume_E.grid(row=3, column=0, columnspan=3)
    edgelength.grid(row=4, column=0, columnspan=3)
    edgelength_E.grid(row=5, column=0, columnspan=3)
    back.grid(row=6, column=0)
    calculate.grid(row=6, column=1)
    clear.grid(row=6, column=2)


def cuboid():
    window_clear()

    def back():
        window_clear()
        home()

    def clear_cuboid():
        side_c_E.delete(0, END)
        side_b_E.delete(0, END)
        side_a_E.delete(0, END)
        volume_E.delete(0, END)
        edge_E.delete(0, END)

    def calculate_cuboid():
        edge_E.configure(None, state='normal')
        a = side_a_E.get()
        b = side_b_E.get()
        c = side_c_E.get()
        vol = volume_E.get()
        edgec = edge_E.get()

        try:
            if a != '' and b != '' and c != '':
                side_a_E.insert(0, a)
                side_b_E.insert(0, b)
                side_c_E.insert(0, c)
                volume_E.insert(0, str(float(a) * float(b) * float(c)))
                edge_E.insert(0, str(float(a) + float(b) + float(c)))
            elif vol != '' and b != '' and c != '':
                side_a_E.insert(0, str(float(vol) / float(b) / float(c)))
                side_b_E.insert(0, b)
                side_c_E.insert(0, c)
                edge_E.insert(0, str((float(vol) / float(b) / float(c)) + float(b) + float(c)))
                volume_E.insert(0, vol)
            elif vol != '' and a != '' and c != '':
                side_a_E.insert(0, a)
                side_b_E.insert(0, str(float(vol) / float(a) / float(c)))
                side_c_E.insert(0, c)
                volume_E.insert(0, vol)
                edge_E.insert(0, str((float(vol) / float(a) / float(c)) + float(a) + float(c)))
            elif vol != '' and a != '' and b != '':
                side_a_E.insert(0, a)
                side_b_E.insert(0, b)
                side_c_E.insert(0, str(float(vol) / float(a) / float(b)))
                volume_E.insert(0, vol)
                edge_E.insert(0, str((float(vol) / float(a) / float(b)) + float(a) + float(c)))
            else:
                warning = Button(root, text='please enter a number', fg='red', command=lambda: warning.grid_forget())
                warning.grid(row=10, column=0, columnspan=3)
        except ValueError:
            warning = Button(root, text='please enter a number', fg='red', command=lambda: warning.grid_forget())
            warning.grid(row=10, column=0, columnspan=3)
        edge_E.configure(None, state='readonly')

    side_a = Label(root, text='side length (a)')
    side_a_E = Entry(root)
    side_b = Label(root, text='side length (b)')
    side_b_E = Entry(root)
    side_c = Label(root, text='side length (c)')
    side_c_E = Entry(root)
    volume = Label(root, text='volume (V)')
    volume_E = Entry(root)
    edge = Label(root, text='edge length')
    edge_E = Entry(root, state='readonly')
    calculate = Button(root, text='calculate', command=calculate_cuboid)
    clear = Button(root, text='clear', command=clear_cuboid)
    back = Button(root, text='<', command=back)

    side_a.grid(row=0, column=0, columnspan=3)
    side_a_E.grid(row=1, column=0, columnspan=3)
    side_b.grid(row=2, column=0, columnspan=3)
    side_b_E.grid(row=3, column=0, columnspan=3)
    side_c.grid(row=4, column=0, columnspan=3)
    side_c_E.grid(row=5, column=0, columnspan=3)
    volume.grid(row=6, column=0, columnspan=3)
    volume_E.grid(row=7, column=0, columnspan=3)
    edge.grid(row=8, column=0, columnspan=3)
    edge_E.grid(row=9, column=0, columnspan=3)
    back.grid(row=10, column=0)
    calculate.grid(row=10, column=1)
    clear.grid(row=10, column=2)


home()

root.mainloop()
