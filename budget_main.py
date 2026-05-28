import kivy

class Transactions():
    
    def __init__(self):
        self.transactionDate = date
        
    def addNew():
        self.postedDate = null
        self.amount = float(amount)
        self.debit = True
        
class Ledger():
    
    def __init__(self):



class budgetApp(App):
    
    def build(self):
        
        self.layout = BoxLayout(orientation = 'vertical', padding = 10, spacing = 10)
        
        self.transactionBtn = Button(text = 'Transactions', background_color = (0, .7, 1, 1)
        self.transactionBtn.bind(on_press = Transactions.addNew())
        self.layout.add_widget(self.transactionBtn)
        
        self.ledgerBtn = Button(text = 'Ledger', background_color = (0, .7, 1, 1)
        self.ledgerBtn.bind(on_press = Ledger())
        self.layout.add_widget(self.ledgerBtn)

        self.displayBtn = Button(text = 'Display', background_color = (0, .7, 1, 1)
        self.displayBtn.bind(on_press = Display())
        self.layout.add_widget(self.displayBtn)
