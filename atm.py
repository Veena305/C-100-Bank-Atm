class Atm(object):
    def __init__ (self, atm_card_number, pin_number):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number

    def cashwithdrawl (self):
        print("Cash Withdrawl")

    def balanceenquiry (self):
        print("Balance Enquiry")

SBI = Atm("123456", "97572")

print(SBI.cashwithdrawl())
print(SBI.balanceenquiry())
print(SBI.atm_card_number)
print(SBI.pin_number)