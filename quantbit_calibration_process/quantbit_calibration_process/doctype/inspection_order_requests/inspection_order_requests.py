# Copyright (c) 2024, tejal kumbhar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class InspectionOrderRequests(Document):

	@frappe.whitelist()
	def get_order_requests(self):
		if self.from_date and self.to_date:
			doc = frappe.get_all("Equipment Maintanance Order", 
							filters={"maintanance_date": ["between", [self.from_date, self.to_date]],"order_status": ["in",["Placed","Open"]],
									},
							fields=["name","maintanance_date","equipment_id","equipment_name","maintanance_order_type","valid_from",
									"valid_to","orderer_name","order_status","equipment_maintanance_schedule","equipment_plant","equipment_location"],)
			if(doc):
				for d in doc:
					self.append('order_request_details', {
												"order_type":d.maintanance_order_type,
												"equipment_id":d.equipment_id,
												"equipment_name":d.equipment_name,
												"maint_scheduled_date":d.maintanance_date,
												"order_status":d.order_status,
												"valid_from":d.valid_from,
												"valid_to":d.valid_to,
												"equipment_maintanance_schedule":d.equipment_maintanance_schedule ,
												"equipment_plant":d.equipment_plant,
												"equipment_location":d.equipment_location,})
					
					# "equipment_id":self.equipment_id,"equipment_name":self.equipment_name