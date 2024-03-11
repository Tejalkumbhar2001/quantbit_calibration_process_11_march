// Copyright (c) 2024, tejal kumbhar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Equipment Maintanance Schedule', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('Equipment Maintanance Schedule', {
	equipment_id: function(frm) {
		frm.refresh_field('items');
		frm.call({
			method:'append_equi_in_items',
			doc:frm.doc
		})
	}
});