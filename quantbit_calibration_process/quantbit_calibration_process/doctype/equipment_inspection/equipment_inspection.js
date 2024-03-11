// Copyright (c) 2024, tejal kumbhar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Equipment Inspection', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on("Equipment Inspection", {
	setup: function(frm) {
			frm.set_query("maintanance_order", function() { 
					return {
						filters: [
							["Equipment Maintanance Order", "company", '=', frm.doc.company],
							["Equipment Maintanance Order", "equipment_id", '=', frm.doc.equipment_id],
							["Equipment Maintanance Order", "status", 'in', ["Placed","Open"]],

						]
					};
			
			});

		}
});



frappe.ui.form.on('Equipment Inspection', {
    refresh: function(frm) {
        frm.add_custom_button(__('Equipment Maintanance Order'), function() {
            frappe.set_route('Form', 'Equipment Maintanance Order');
        }, __('Go To Doctype'));

		frm.add_custom_button(__('Equipment Maintanance Schedule'), function() {
            frappe.set_route('Form', 'Equipment Maintanance Schedule');
        }, __('Go To Doctype'));
    }
});