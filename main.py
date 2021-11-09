from tkinter import Button, Label, Frame, Tk
from connected import connected, browse
from urllib.request import urlopen

class main(Tk):
    def __init__(self, master=None):
        Tk.__init__(self, master)
        self.frames = {}

        container = Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        for f in (main_page, canvas, google_meet, no_connection, google_meet_issue_simple, google_meet_issue_advanced,
canvas_issue_simple_no, canvas_issue_simple_yes, canvas_issue_advanced):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame(main_page)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class main_page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text ="Online School Troubleshooting", font=("Courier", 24, "bold")).grid(row = 0, column = 0,
        columnspan = 2, pady = 1)
        Label(self, text ="One can never just easily find what they need to fix problems on website help desks.",
        font=("Helvetica", 14)).grid(row = 1, column = 0, columnspan = 2, pady = 1)
        Label(self, text ="This resource is meant to take the headache out of troubleshooting.",
        font=("Helvetica", 14)).grid(row = 2, column = 0, columnspan = 2, pady = 1)
        Label(self, text ="Before consulting this guide, please check to make sure you're connected to the internet.",
        font=("Helvetica", 14)).grid(row = 3, column = 0, columnspan = 2, pady = 1)

        Button(self, text ="Troubleshoot Google Meet", command = lambda : controller.show_frame(google_meet)).grid(row = 4, column = 0,
        sticky = "e")
        Button(self, text ="Troubleshoot Canvas", command = lambda : controller.show_frame(canvas)).grid(row = 4, column = 1,
        sticky = "w")

class google_meet(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        self.problem = 0

        Label(self, text ="Google Meet Troubleshooting", font=("Courier", 24,
        "bold")).grid(row = 0, column = 0, columnspan = 2)
        Label(self, text ="What are you having trouble with?", font=("Helvetica", 14)).grid(row = 1, column = 0, columnspan = 2)

        Button(self, text ="Joining a meeting", command = lambda : [self.set_var(1), self.loop()]).grid(row = 2, column = 0, sticky = "e")
        Button(self, text ="Turning on your camera", command = lambda : [self.set_var(1), self.loop()]).grid(row = 2, column = 1,
        sticky = "w")
        Button(self, text ="Turning on your mic", command = lambda : [self.set_var(1), self.loop()]).grid(row = 3, column = 0,
        sticky = "e")
        Button(self, text ="Other", command = lambda : [self.set_var(2), self.loop()]).grid(row = 3, column = 1, sticky = "w")

        Button(self, text ="Home", command = lambda : self.controller.show_frame(main_page)).grid(row = 6, column = 0, sticky = "e")
        Button(self, text ="Exit", command = lambda : exit()).grid(row = 6, column = 1, sticky = "w")

    def loop(self):
        if self.problem != 0:
            is_connected = connected()

            if is_connected == False:
                self.controller.show_frame(no_connection)
            else:
                if self.problem == 1:
                    self.controller.show_frame(google_meet_issue_simple)
                elif self.problem == 2:
                    self.controller.show_frame(google_meet_issue_advanced)
        self.problem = 0

    def set_var(self, var):
        self.problem = var

class canvas(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        Label(self, text ="Canvas Troubleshooting", font=("Courier", 24, "bold")).grid(row = 0, column = 0, columnspan = 2)
        Label(self, text ="What are you having trouble with?", font=("Helvetica", 14)).grid(row = 1, column = 0, columnspan = 2)

        Button(self, text ="Accessing Canvas", command = lambda : [self.set_var(1), self.loop()]).grid(row = 2, column = 0, sticky = "e")
        Button(self, text ="Other", command = lambda : [self.set_var(2), self.loop()]).grid(row = 2, column = 1, sticky = "w")

        Button(self, text ="Home", command = lambda : controller.show_frame(main_page)).grid(row = 5, column = 0, sticky = "e")
        Button(self, text ="Exit", command = lambda : exit()).grid(row = 5, column = 1, sticky = "w")

    def loop(self):
        if self.problem != 0:
            is_connected = connected()

            if is_connected == False:
                self.controller.show_frame(no_connection)
            else:
                if self.problem == 1:
                    url = "https://status.instructure.com/"
                    page = urlopen(url)
                    html = page.read().decode("utf-8")

                    if "All Systems Operational" in html:
                        self.controller.show_frame(canvas_issue_simple_yes)
                    else:
                        self.controller.show_frame(canvas_issue_simple_no)

                elif self.problem == 2:
                    self.controller.show_frame(canvas_issue_advanced)

    def set_var(self, var):
        self.problem = var

class no_connection(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text ="No connection", font=("Courier", 24, "bold")).grid(row = 0, column = 0,
        columnspan = 2, pady = 1)
        Label(self, text ="According to this programs tests, you are not connected to the internet.",
        font=("Helvetica", 14)).grid(row = 1, column = 0, columnspan = 2, pady = 1)
        Label(self, text ="Please connect your device to the internet and that hopefully shall fix your problem.",
        font=("Helvetica", 14)).grid(row = 2, column = 0, columnspan = 2, pady = 1)

        Button(self, text ="Home", command = lambda : controller.show_frame(main_page)).grid(row = 3, column = 0, sticky = "e")
        Button(self, text ="Exit", command = lambda : exit()).grid(row = 3, column = 1, sticky = "w")

class google_meet_issue_simple(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text ="Google Meet Troubleshooting", font=("Courier", 24,
        "bold")).grid(row = 0, column = 0, columnspan = 2)

        Label(self, text ="Try visiting ", font=("Helvetica", 14)).grid(row = 1, column = 0, columnspan = 1, sticky = "e")
        link1 = Label(self, text="Google's troubleshooting page.", fg="blue", cursor="hand2")
        link1.grid(row = 1, column = 1, columnspan = 1, sticky = "w")
        link1.bind("<Button-1>", lambda e: browse("https://support.google.com/meet/answer/7380413?hl=en&ref_topic=7290455"))
        Label(self, text ="If trying methods found here don't fix your issue, there may be other issues going on.",
        font=("Helvetica", 14)).grid(row = 2, column = 0, columnspan = 2)
        Label(self, text ="Try running diagnostics on your computer, and if all else fails visit",
        font=("Helvetica", 14)).grid(row = 3, column = 0, columnspan = 2)
        link2 = Label(self, text="Google meet's forum page.", fg="blue", cursor="hand2")
        link2.grid(row = 4, column = 0, columnspan = 1, sticky = "e")
        link2.bind("<Button-1>", lambda e: browse("https://support.google.com/meet/thread/new?hl=en"))
        Label(self, text =" to ask a question in the forms.", font=("Helvetica", 14)).grid(row = 4, column = 1, columnspan = 1,
        sticky = "w")

        Button(self, text ="Home", command = lambda : controller.show_frame(main_page)).grid(row = 5, column = 0, sticky = "e")
        Button(self, text ="Exit", command = lambda : exit()).grid(row = 5, column = 1, sticky = "w")

class google_meet_issue_advanced(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text ="Google Meet Troubleshooting", font=("Courier", 24,
        "bold")).grid(row = 0, column = 0, columnspan = 2)
        link1 = Label(self, text="Visi Google meet's forum page", fg="blue", cursor="hand2")
        link1.grid(row = 1, column = 0, columnspan = 1, sticky = "e")
        link1.bind("<Button-1>", lambda e: browse("https://support.google.com/meet/search?q="))
        Label(self, text =" and search for your issue. Otherwise",
        font=("Helvetica", 14)).grid(row = 1, column = 1, columnspan = 1, sticky = "w")
        Label(self, text ="this may not be an issue with google meet. Try running diagnostics on your computer.",
        font=("Helvetica", 14)).grid(row = 2, column = 0, columnspan = 2)
        Label(self, text ="If all else fails than I would suggest asking a question on",
        font=("Helvetica", 14)).grid(row = 3, column = 0, columnspan = 1, sticky = "e")
        link2 = Label(self, text="Google meet's forum page.", fg="blue", cursor="hand2")
        link2.grid(row = 3, column = 1, columnspan = 1, sticky = "w")
        link2.bind("<Button-1>", lambda e: browse("https://support.google.com/meet/thread/new?hl=en"))

        Button(self, text ="Home", command = lambda : controller.show_frame(main_page)).grid(row = 5, column = 0, sticky = "e")
        Button(self, text ="Exit", command = lambda : exit()).grid(row = 5, column = 1, sticky = "w")

class canvas_issue_simple_yes(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text ="Canvas Troubleshooting", font=("Courier", 24, "bold")).grid(row = 0, column = 0, columnspan = 2)
        Label(self, text ="Instructure is up. Canvas may be running slow and/or the counties servers are overloaded.",
        font=("Helvetica", 14)).grid(row = 1, column = 0, columnspan = 2)
        Label(self, text ="Please be paitent. Otherwise, please make sure that you're going to hcpss.me and using your",
        font=("Helvetica", 14)).grid(row = 2, column = 0, columnspan = 2)
        Label(self, text ="school username and password to login.",
        font=("Helvetica", 14)).grid(row = 3, column = 0, columnspan = 2)

        Button(self, text ="Home", command = lambda : controller.show_frame(main_page)).grid(row = 5, column = 0, sticky = "e")
        Button(self, text ="Exit", command = lambda : exit()).grid(row = 5, column = 1, sticky = "w")

class canvas_issue_simple_no(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text ="Canvas Troubleshooting", font=("Courier", 24, "bold")).grid(row = 0, column = 0, columnspan = 2)
        Label(self, text ="Canvas is down. Please be paitent.", font=("Helvetica", 14)).grid(row = 1,
        column = 0, columnspan = 2)

        Button(self, text ="Home", command = lambda : controller.show_frame(main_page)).grid(row = 5, column = 0, sticky = "e")
        Button(self, text ="Exit", command = lambda : exit()).grid(row = 5, column = 1, sticky = "w")

class canvas_issue_advanced(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        Label(self, text ="Canvas Troubleshooting", font=("Courier", 24, "bold")).grid(row = 0, column = 0, columnspan = 2)
        link1 = Label(self, text="Visit Canvas's forum", fg="blue", cursor="hand2")
        link1.grid(row = 1, column = 0, columnspan = 1, sticky = "e")
        link1.bind("<Button-1>", lambda e: browse("https://community.canvaslms.com/t5/forums/searchpage/tab/message?q="))
        Label(self, text =" and search for your issue. Otherwise, visit ",
        font=("Helvetica", 14)).grid(row = 1, column = 1, columnspan = 1, sticky = "w")
        link1 = Label(self, text="Canvas's forum", fg="blue", cursor="hand2")
        link1.grid(row = 2, column = 0, columnspan = 1, sticky = "e")
        link1.bind("<Button-1>", lambda e: browse("https://community.canvaslms.com/t5/forums/postpage/"))
        Label(self, text =" and create a post.",
        font=("Helvetica", 14)).grid(row = 2, column = 1, columnspan = 1, sticky = "w")

        Button(self, text ="Home", command = lambda : controller.show_frame(main_page)).grid(row = 5, column = 0, sticky = "e")
        Button(self, text ="Exit", command = lambda : exit()).grid(row = 5, column = 1, sticky = "w")

if __name__ == "__main__":
    app = main()
    app.mainloop()
