# Copyright (c) 2024, tejal kumbhar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class EquipmentMaintananceOrder(Document):
	# pass


	@frappe.whitelist()
	def get_events(start, end, filters=None):
		"""Returns events for Gantt / Calendar view rendering.

		:param start: Start date-time.
		:param end: End date-time.
		:param filters: Filters (JSON).
		"""
		from frappe.desk.calendar import get_event_conditions

		conditions = get_event_conditions("Equipment Maintanance Order", filters)

		data = frappe.db.sql(
			"""
			select
				distinct `tabEquipment Maintanance Order`.name, `tabEquipment Maintanance Order`.equipment_name,
				`tabEquipment Maintanance Order`.status, `tabEquipment Maintanance Order`.maintanance_date
			from
				`tabEquipment Maintanance Order`
			where (ifnull(`tabEquipment Maintanance Order`.maintanance_date, '0000-00-00')!= '0000-00-00') \
				and (`tabEquipment Maintanance Order`.maintanance_date between %(start)s and %(end)s)
				{conditions}
			""".format(
				conditions=conditions
			),
			{"start": start, "end": end},
			as_dict=True,
			update={"allDay": 0},
		)
		return data


	@frappe.whitelist()
	def available_qty(self):
		for row in self.get("items"):
			if row.source_warehouse and row.item_code:
				doc_name = frappe.get_value('Bin',{'item_code':row.item_code,'warehouse': row.source_warehouse}, "actual_qty")
				row.available_quantity = doc_name



	def on_submit(self):
		self.create_task_completion()
		# self.change_after_completion()

	@frappe.whitelist()
	def create_task_completion(self):
		for i in self.get("maintanance_task_list"):
			doc = frappe.new_doc("Task List Completion")
			doc.company =self.company
			doc.order_type = self.order_type
			doc.maintanance_order_type = self.maintanance_order_type	
			doc.date =self.date
			doc.equipment_category = self.equipment_category
			doc.equipment_id= self.equipment_id
			doc.equipment_brand=self.equipment_brand
			doc.equipment_name = self.equipment_name
			doc.plant = self.equipment_plant
			doc.location =self.equipment_location
			doc.order_by_department = self.order_from_department
			# doc.maintanance_scheduled_date = self.maintanance_date

			doc.assign_to = i.assign_to
			doc.assign_to_name = i.assign_to_name
			doc.append('task_completion_details', {	
						"maintenance_task": i.maintenance_task,
						"description": i.description,
					})

			
			doc.maintenance_order= self.name
			doc.insert()
			doc.save()


	# @frappe.whitelist()
	# def change_after_completion(self):
	# 	for i in self.get("maintanance_task_list"):
	# 		if i.maintenance_status =="Completed"
	# 			frappe.db.set_value('Equipment Maintanance Order', name, 'status', "Completed")


	# @frappe.whitelist()
	# def change_after_completion(self):
	# 	if self.docstatus == 0:  # Check if the document is newly created
	# 		self.status = "Submitted"

	# 	all_tasks_completed = all(task.maintenance_status == "Completed" for task in self.maintanance_task_list)
		
	# 	if all_tasks_completed:
	# 		self.status = "Completed"
	# 	else:
	# 		self.status = "Open"

	# 	self.save()



	# if(self.completion_status == "Fully Completed"):
	# 		frappe.msgprint("Completed")
	# 		frappe.db.set_value('Equipment Maintanance Order', name, 'status', "Completed")
	# 	else:
	# 		frappe.msgprint("Open")
	# 		frappe.db.set_value('Equipment Maintanance Order', name, 'status', "Open")

