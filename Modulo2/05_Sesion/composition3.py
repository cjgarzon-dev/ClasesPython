class Billing:
    def __init__(self):
        self.steps = []
    
    def addStep(self, step):
        self.steps.append(step)
        
    def processBilling(self, amount, rebate=0):
        print('Procesar factura:')
        for step in self.steps:
            if isinstance(step, CalculateTax):    # Valida que el objeto que estoy validando provenga del método que le estoy preguntando
                tax = step.execute(amount)
                print(f'Impuesto calculado: ${tax:.2f}')
                amount += tax
            elif isinstance(step, ApplyRebate):
                amount = step.execute(amount, rebate)
                print(f'Descuento aplicado: ${amount:.2f}')
            elif isinstance(step, GenerateBill):
                print(step.execute(amount))

class CalculateTax:
    def execute(self, amount):
        return amount*0.19

class ApplyRebate:
    def execute(self, amount, rebate):
        return amount - (amount*rebate / 100)

class GenerateBill:
    def execute(self, amount):
        return f'Recibo generado por ${amount:.2f}'

billing = Billing()

tax = CalculateTax()
rebate = ApplyRebate()
bill = GenerateBill

billing.addStep(tax)
billing.addStep(rebate)
billing.addStep(rebate)
billing.addStep(bill)

billing.processBilling(500,rebate=10)
