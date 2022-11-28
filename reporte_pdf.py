from fpdf import FPDF
import os


class PDF(FPDF):
    def lines(self):
        self.rect(5.0, 5.0, 287.0, 200.0)

    def set_marks(self):
        self.image(name=i_name, x=6, y=6, w=1586/80, h=1920/80)
        self.image(name=i_name, x=271, y=6,
                   w=1586/80, h=1920/80)
        self.image(name=i_name, x=6, y=180, w=1586/80, h=1920/80)
        self.image(name=i_name, x=271, y=180,
                   w=1586/80, h=1920/80)

    def set_image(self, fig, coor1, coor2, widht, height):
        self.image(name=fig, x=coor1, y=coor2, w=widht, h=height)

    def titles(self, text):
        self.set_font('Arial', 'B', 20)
        self.set_text_color(220, 50, 50)
        self.cell(w=275.0, h=30.0, align='C', txt=text, border=20)

    def texts(self, txt):
        self.set_xy(30, 140)
        self.set_text_color(128, 0, 128)
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, txt)


# Empezamos a escribir el pdf
i_name = os.path.basename('pizza.png')
pdf = PDF(orientation='L')  # Lo quiero poner horizontal.
pdf.add_page()
pdf.lines()
pdf.titles('Maven Pizzas')
pdf.set_marks()
pdf.set_image('ordering_day.png', 30, 30, 120, 100)
pdf.set_image('revenues_per_week.png', 150, 30, 120, 86)
pdf.set_image('comida_cena.png', 60, 130, 100, 65)
pdf.set_image('most_used_ingredients.png', 170, 120, 90, 80)
pdf.add_page()
pdf.lines()
pdf.set_marks()
pdf.set_image('ordering_month.png', 30, 40, 120, 100)
pdf.set_image('pedidos_pizzas.png', 150, 40, 120, 100)
pdf.titles('Maven Pizzas')
pdf.set_author('Nicolas Villagran Prieto')
texto = 'We can appreciate in the first graphic how people mostly visit us during weekends. We could get daily clients if we threw marketing campaigns '\
        + 'to gain their attention (such as offering a worker-menu). It is also important to remark that people tend to visit us during lunch. '\
        + 'Orders by month seem to be pretty similar, the discrepancies may be due to random events. '\
        + 'The most used ingredients represent the 71% out of total, which implies that these ingredients must be always present.'
pdf.texts(texto)
pdf.output('reporte_ejecutivo.pdf', 'F')
