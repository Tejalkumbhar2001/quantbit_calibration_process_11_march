# Copyright (c) 2024, tejal kumbhar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MaintenanceRequestNotification(Document):
	
	def on_submit(self):
		self.create_maintanance_orders()


	@frappe.whitelist()
	def create_maintanance_orders(self):
		doc = frappe.new_doc("Equipment Maintenance Order")
		doc.company =self.company
		doc.order_from_department = self.department_name
		doc.orderer_name = self.requested_by	
		doc.date =self.date
		doc.equipment_plant = self.plant
		doc.status= "Draft"
		doc.maintanance_order_type=self.maintanance_type
		doc.equipment_id = self.equipment_id
		doc.equipment_name = self.equipment_name
		doc.equipment_location =self.location
		doc.valid_to =self.valid_to
		doc.valid_from = self.valid_from
		doc.equipment_category = self.equipment_category
		doc.equipment_description = self.discription
		doc.order_type=self.request_type 
		if self.request_type == "Calibration" and self.equipment_id:
			for i in self.get('notification_calibration_task_list', filters = {"check":1}):
				doc.append('maintanance_task_list',{
					'maintenance_task':i.parameter,
					'maintenance_type':self.request_type,
					'maintenance_status':"Planned",
					'description':i.parameter_details,
					'minimum_value':i.minimum,
					'maximum_value':i.maximum,
					'standard_value':i.standard_value,
				})

		doc.maintanance_notification = self.name
		doc.insert()
		doc.save()
		

	@frappe.whitelist()
	def fetch_calibration_task_list(self):
		if self.request_type == "Calibration" and self.equipment_id:
			doc_names = frappe.get_all("Calibration Task List", filters={'parent': self.equipment_id},
										fields=["parameter", "parameter_details", "minimum", "maximum", "standard_value", "description"])

			if doc_names:
				for doc_name in doc_names:
					self.append('notification_calibration_task_list', {    
							"parameter": doc_name.parameter,
							"parameter_details": doc_name.parameter_details,
							"minimum": doc_name.minimum,
							"maximum": doc_name.maximum,
							"standard_value": doc_name.standard_value,
							"description": doc_name.description,
						})
		
		
	# after check all button select all employee
	@frappe.whitelist()
	def checkall(self):
		children = self.get('notification_calibration_task_list')
		if not children:
			return
		all_selected = all([child.check for child in children])  
		value = 0 if all_selected else 1 
		for child in children:
			child.check = value