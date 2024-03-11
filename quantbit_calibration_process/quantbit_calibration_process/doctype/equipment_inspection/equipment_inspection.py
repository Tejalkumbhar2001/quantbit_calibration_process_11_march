# Copyright (c) 2024, tejal kumbhar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class EquipmentInspection(Document):

	def on_submit(self):
		self.changes_status_submit()
		self.changes_equistatus_submit()

	@frappe.whitelist()
	def changes_status_submit(self):
	
		name = frappe.get_value("Equipment Maintanance Order", 
							filters={"name": self.maintanance_order},
							fieldname=["name"])
		if(self.completion_status == "Fully Completed"):
			frappe.msgprint("Completed")
			frappe.db.set_value('Equipment Maintanance Order', name, 'status', "Completed")
		else:
			frappe.msgprint("Open")
			frappe.db.set_value('Equipment Maintanance Order', name, 'status', "Open")

		

	@frappe.whitelist()
	def changes_equistatus_submit(self):
	
		name = frappe.get_value("Equipment Maintanance Order", 
							filters={"name": self.maintanance_order},
							fieldname=["name"])
		if(self.equipment_status):
			frappe.db.set_value('Equipment Maintanance Order', name, 'equipment_status', self.equipment_status)

		

	