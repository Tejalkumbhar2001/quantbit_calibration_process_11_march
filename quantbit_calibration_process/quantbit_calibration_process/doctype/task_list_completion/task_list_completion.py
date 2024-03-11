# Copyright (c) 2024, tejal kumbhar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TaskListCompletion(Document):
	
	def on_submit(self):
		self.changes_status_submit()

	def on_update(self):
		self.changes_status_submit()

	@frappe.whitelist()
	def changes_status_submit(self):
		
		if self.completion_status:
			for i in self.get("task_completion_details"):
				name = frappe.get_value("Maintanance Task List",
										filters={"parent": self.maintenance_order, "maintenance_task": i.maintenance_task, "description": i.description, "assign_to": self.assign_to},
										fieldname=["name"])

				if name:                                                                      
					if self.completion_status == "Fully Completed" and self.equipment_status:
						frappe.db.set_value('Maintanance Task List', name, 'maintenance_status', 'Completed')
						frappe.db.set_value('Maintanance Task List', name, 'last_completion_date', self.task_completion_date)
						frappe.db.set_value('Maintanance Task List', name, 'equipment_status', self.equipment_status)
					else:
						frappe.db.set_value('Maintanance Task List', name, 'maintenance_status', 'Open')

			doc = frappe.get_doc('Equipment Maintenance Order', self.maintenance_order)
			all_tasks_completed = all(task.maintenance_status == "Completed" for task in doc.get('maintanance_task_list'))

			if all_tasks_completed:
				frappe.db.set_value('Equipment Maintenance Order', self.maintenance_order, 'status', 'Completed')

			else:
				frappe.db.set_value('Equipment Maintenance Order', self.maintenance_order, 'status', 'Open')

	# def on_update(self):
	# 	self.changes_status_submit()

	# @frappe.whitelist()
	# def changes_status_submit(self):
	# 	try:
	# 		frappe.msgprint("Entering changes_status_submit")
	# 		if self.completion_status == "Fully Completed":
	# 			for i in self.get("task_completion_details"):
	# 				name = frappe.get_value("Maintanance Task List",
	# 										filters={"parent": self.maintenance_order, "maintenance_task": i.maintenance_task, "description": i.description, "assign_to": self.assign_to},
	# 										fieldname=["name"])
	# 				frappe.msgprint("Name: {}".format(name))
	# 				if name:
	# 					frappe.db.set_value('Maintanance Task List', name, 'maintenance_status', 'Completed')

	# 			doc = frappe.get_doc('Equipment Maintanance Order', self.maintenance_order)
	# 			all_tasks_completed = all(task.maintenance_status == "Completed" for task in doc.get('maintanance_task_list'))

	# 			if all_tasks_completed:
	# 				frappe.db.set_value('Equipment Maintanance Order', self.maintenance_order, 'status', 'Completed')
	# 			else:
	# 				frappe.db.set_value('Equipment Maintanance Order', self.maintenance_order, 'status', 'Open')

	# 		frappe.msgprint("Exiting changes_status_submit")
	# 	except Exception as e:
	# 		frappe.msgprint("Error in changes_status_submit: {}".format(str(e)))
	# 		frappe.log_error("Error in changes_status_submit", title="Script Error")

