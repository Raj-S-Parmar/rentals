// Copyright (c) 2025, RP and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue by MAke"] = {
	filters: [
		{
			"fieldname": "my_filter",
			"label": __("My Filter"),
			"fieldtype": "Link",
			"options": "Vehicle"
		},
	],
};
