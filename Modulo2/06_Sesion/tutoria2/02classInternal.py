class AccountBank:      # CLASE EXTERNA
    def __init__(self, titular, balanceStart):
        self.titular = titular
        self.balanceStart = balanceStart
    
    class Transaction:  # CLASE INTERNA
        def __init__(self, account, amount, type):
            self.account = account
            self.amount = amount
            self.type = type
        
        def executeTransaction(self):
            if self.type == 'deposito':
                self.account.balanceStart += self.amount
            elif self.type == 'retiro' and self.account.balanceStart >= self.amount:
                self.account.balanceStart -= self.amount
            else:
                print('Fondos insuficientes para la transacción')
            print(f'Saldo actual: ${self.account.balanceStart}')

account = AccountBank('Juan', 1000)
deposit = account.Transaction(account, 500, 'deposito')
deposit.executeTransaction()

withdrawal = account.Transaction(account, 600, 'retiro')
withdrawal.executeTransaction()
            