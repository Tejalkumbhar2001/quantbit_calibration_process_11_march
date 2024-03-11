// Copyright (c) 2024, tejal kumbhar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Maintenance Request-Notification', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Maintenance Request-Notification', {
	equipment_id: function(frm) {
		frm.clear_table("notification_calibration_task_list");
		frm.refresh_field('notification_calibration_task_list');
		frm.call({
			method:'fetch_calibration_task_list',
			doc:frm.doc
		})
	}
});

// frappe.ui.form.on('Maintenance Request-Notification', {
// 	setup: function(frm) {
// 		frm.call({
// 			method:'fetch_calibration_task_list',
// 			doc:frm.doc
// 		})
// 	}
// });


frappe.ui.form.on('Maintenance Request-Notification', {
	select_all: function(frm) {
		frm.call({
			method:'checkall',
			doc:frm.doc
		})
	}
});



//  filter warehouse based on company
frappe.ui.form.on("Maintenance Request-Notification", {
	setup: function(frm) {
			frm.set_query("equipment_id", function() { // Replace with the name of the link field
				if(frm.doc.department_name){
					return {
						filters: [
							["Equipment Master", "company", '=', frm.doc.company],
							["Equipment Master", "department", '=', frm.doc.department_name]
							
						]
					};
				}
			});

		}
})