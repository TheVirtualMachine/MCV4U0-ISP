import tkinter as tk

from sympy import *
from sympy.abc import x, e

from PIL import Image
from PIL import ImageTk

FORMULA_FILE_NAME = "Formula"
FORMULA_PDF_FILE = FORMULA_FILE_NAME + ".pdf"
FORMULA_PNG_FILE = FORMULA_FILE_NAME + ".png"

# Render a LaTeX string to a PDF and return it.
def renderLatexString(expression):
	preamble = "\\documentclass[12pt]{article} \\usepackage[active,tightpage]{preview} \\PreviewEnvironment{math} \\PreviewBorder=3pt \\begin{document}"

	string = "\\begin{math} \\displaystyle " + expression + " \\end{math}"
	preview(string, output="png", viewer="file", filename=FORMULA_PNG_FILE, euler=False, preamble=preamble)
	#preview(string, output="pdf", viewer="file", filename=FORMULA_PDF_FILE, euler=False, preamble=preamble)

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.formula = tk.Text(self, height=10)
		self.formula.pack(side="top")

		self.renderButton = tk.Button(self, text="Render")
		self.renderButton["command"] = self.renderFormula
		self.renderButton.pack(side="top")

		renderLatexString("e^x")
		self.formulaImage = ImageTk.PhotoImage(Image.open(FORMULA_PNG_FILE))
		self.renderedFormula = tk.Label(self, image=self.formulaImage)
		self.renderedFormula.pack(side="top")

		self.quitButton = tk.Button(self, text="Quit", command=root.destroy)
		self.quitButton.pack(side="top")

	def renderFormula(self):
		renderLatexString(self.formula.get("1.0", "end"))
		self.formulaImage = ImageTk.PhotoImage(Image.open(FORMULA_PNG_FILE))
		self.renderedFormula.configure(image=self.formulaImage)

root = tk.Tk()
root.title("MCV4U0 ISP")
root.geometry("500x500")

app = Application(master=root)

app.mainloop()
