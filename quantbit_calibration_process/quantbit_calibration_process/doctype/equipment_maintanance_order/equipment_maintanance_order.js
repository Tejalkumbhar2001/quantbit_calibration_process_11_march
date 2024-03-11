// Copyright (c) 2024, tejal kumbhar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Equipment Maintanance Order', {
	// refresh: function(frm) {

	// }
});



frappe.ui.form.on('Equipment Maintanance Order', {
    refresh: function(frm) {
        frm.add_custom_button(__('Equipment Maintanance Order'), function() {
            frappe.set_route('Form', 'Equipment Maintanance Order');
        }, __('Go To Doctype'));

		frm.add_custom_button(__('Equipment Maintanance Schedule'), function() {
            frappe.set_route('Form', 'Equipment Maintanance Schedule');
        }, __('Go To Doctype'));
		// frm.add_custom_button(__('Inspection Order Requests'), function() {
        //     frappe.set_route('Form', 'Inspection Order Requests');
        // }, __('Go To Doctype'));
    }
});

frappe.ui.form.on('Equipment Maintanance Order', {
    refresh: function(frm) {
        frm.add_custom_button(__('Material Request'), function() {
            frappe.set_route('Form', 'Material Request');
        }, __('Create'));
    }
});

frappe.ui.form.on('Required Item and Details', {
	source_warehouse: function(frm) {
		frm.call({
			method:'available_qty',
			doc:frm.doc
		})
	}
});