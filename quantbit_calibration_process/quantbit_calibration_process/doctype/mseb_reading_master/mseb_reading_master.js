// Copyright (c) 2024, tejal kumbhar and contributors
// For license information, please see license.txt

frappe.ui.form.on('MSEB Reading Master', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('MSEB Reading Master', {
	validate: function(frm) {
		frm.call({
			method:'getmseb_reading_values',
			doc:frm.doc
		})
	}
});


// frappe.ui.form.on('MSEB Reading Master', {
// 	kvah: function(frm) {
// 		frm.call({
// 			method:'getmseb_reading_values',
// 			doc:frm.doc
// 		})
// 	}
// });

// frappe.ui.form.on('MSEB Reading Master', {
// 	md_kva2: function(frm) {
// 		frm.call({
// 			method:'getmseb_reading_values',
// 			doc:frm.doc
// 		})
// 	}
// });

// frappe.ui.form.on('MSEB Reading Master', {
// 	kvarh_lead: function(frm) {
// 		frm.call({
// 			method:'getmseb_reading_values',
// 			doc:frm.doc
// 		})
// 	}
// });

// frappe.ui.form.on('MSEB Reading Master', {
// 	furnace_kwh: function(frm) {
// 		frm.call({
// 			method:'getmseb_reading_values',
// 			doc:frm.doc
// 		})
// 	}
// });

// frappe.ui.form.on('MSEB Reading Master', {
// 	liquid_metal_kg: function(frm) {
// 		frm.call({
// 			method:'getmseb_reading_values',
// 			doc:frm.doc
// 		})
// 	}
// });
