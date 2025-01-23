# Copyright (c) 2025, RP and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Driver(Document):
    def onload(self):
        self.full_name = self.first_name + " " + self.last_name  