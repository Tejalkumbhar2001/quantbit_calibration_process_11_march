# Copyright (c) 2024, tejal kumbhar and contributors
# For license information, please see license.txt

import json
import frappe
from frappe.model.document import Document

class MSEBReadingMaster(Document):

	
	@frappe.whitelist()
	def getmseb_reading_values(self):
		kwh =0
		kvah=0
		last_mseb_reading = frappe.get_all('MSEB Reading Master',
											filters = {"docstatus":1},
											fields=["name", "kwh", "kvah", "kvarh_lag", "kvarh_lead", "furnace_kwh"], 
											order_by="creation DESC", limit=1)
		
		for d in last_mseb_reading:
			self.kwh_units = (self.kwh-d.kwh)*10
			self.kvah_units =(self.kvah-d.kvah)*10
			self.power_factor=self.kwh_units/self.kvah_units
			self.kvarh_lag_units =(self.kvarh_lag-d.kvarh_lag)*10
			self.kvarh_lead_units =(self.kvarh_lead-d.kvarh_lead)*10
			self.furnace_units =(self.furnace_kwh-d.furnace_kwh)
			self.amount = self.kvah_units * 9.963
			self.auxunits = self.kvah_units -self.furnace_units
			self.good_metalkg = self.liquid_metal_kg-((self.liquid_metal_kg)*32/100)
			self.fce_unitsmt=(self.furnace_units/self.liquid_metal_kg)*1000
			self.aux_unitsmt = (self.auxunits/self.liquid_metal_kg)*1000

			