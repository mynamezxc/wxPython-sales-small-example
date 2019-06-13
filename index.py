# Templates
from templates.order import *
from templates.saler import *
from templates.product import *
from templates.unit import *
from templates.customer import *


# Frame
from templates.navigations.default import *


# Inventories
from models.inventories.order import *
from models.inventories.customer import *
from models.inventories.saler import *
from models.inventories.product import *
from models.inventories.order_line import *
from models.inventories.unit import *


import wx
import os.path

class Mainer():
    
    def __init__(self):
        self.app = wx.App()
        width = 860
        height = 750
        self.frame = Navigation(parent = None, width=width, height=height)
        self.panel = OrderPanel(self.frame)
    
    def openCustomerPanel(self):
        width = 850
        height = 785
        self.frame = Navigation(parent = None, width=width, height=height)
        self.panel = CustomerPanel(self.frame)
        customerInv = CustomerInventory()
        customers = customerInv.getAll()
        row = 0
        for customer in customers:
            self.panel.m_customer_list.AppendRows(numRows=1)
            self.panel.m_customer_list.SetCellValue(row, 0, str(customer.id))
            self.panel.m_customer_list.SetCellValue(row, 1, str(customer.name))
            self.panel.m_customer_list.SetCellValue(row, 2, str(customer.address))
            self.panel.m_customer_list.SetCellValue(row, 3, str(customer.phone))
            self.panel.m_customer_list.SetCellValue(row, 4, str(customer.email))
            row += 1
            self.panel.m_customer_name_list.Append(str(customer.id) + " " + str(customer.name))
        
    def openSalerPanel(self):
        width = 850
        height = 785
        self.frame = Navigation(parent = None, width=width, height=height)
        self.panel = SalerPanel(self.frame)
        SalerInv = SalerInventory()
        salers = SalerInv.getAll()
        row = 0
        for saler in salers:
            self.panel.m_saler_list.AppendRows(numRows=1)
            self.panel.m_saler_list.SetCellValue(row, 0, str(saler.id))
            self.panel.m_saler_list.SetCellValue(row, 1, str(saler.name))
            self.panel.m_saler_list.SetCellValue(row, 2, str(saler.address))
            self.panel.m_saler_list.SetCellValue(row, 3, str(saler.phone))
            self.panel.m_saler_list.SetCellValue(row, 4, str(saler.identity_num))
            self.panel.m_saler_list.SetCellValue(row, 5, "True" if saler.status == 1 else "False")
            row += 1
            self.panel.m_saler_name_list.Append(str(saler.id) + " " + str(saler.name))
        
    def show(self):
        self.frame.Show()
        self.app.MainLoop()


if __name__ == "__main__":
    mainer = Mainer()
    mainer.openSalerPanel()
    mainer.show()
    # Query Database
    
    # orderInv = CustomerInventory()
    # orders = orderInv.getAll()
    
    # orderLineInv = OrderLineInventory()
    # condition = ["order_id", "=", str(orders[0].id)]
    # orderLines = orderLineInv.getWhere(condition)
    # print(orderLines[0].sub_total)

# if user:
    # panel.m_input_name.SetValue(user[1])
    # panel.m_input_address.SetValue(user[3])
    # panel.m_input_email.SetValue(user[4])
    # panel.m_input_code.SetValue(user[2])
# Query Database