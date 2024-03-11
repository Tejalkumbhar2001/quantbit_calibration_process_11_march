// Copyright (c) 2024, tejal kumbhar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Inspection Order Requests', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('Inspection Order Requests', {
	to_date: function(frm) {
		frm.clear_table("order_request_details");
		frm.refresh_field('order_request_details');
		frm.call({
			method:'get_order_requests',
			doc:frm.doc
		})
	}
});

frappe.ui.form.on('Inspection Order Requests', {
	from_date: function(frm) {
		frm.clear_table("order_request_details");
		frm.refresh_field('order_request_details');
		frm.call({
			method:'get_order_requests',
			doc:frm.doc
		})
	}
});


// frappe.ui.form.on('Order Request Details', {
//     go_to: function(frm, cdt, cdn) {
//         var child = locals[cdt][cdn];

//         var testFormMapping = {
//             "Equipment Inspection": "Equipment Inspection"
//         };

//         var selectedTest = child.test;

//         if (testFormMapping[selectedTest]) {
//             frappe.set_route("Form", testFormMapping[selectedTest]);
//         }
//     }
// });


