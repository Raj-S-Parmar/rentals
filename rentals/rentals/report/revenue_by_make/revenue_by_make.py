# Copyright (c) 2025, RP and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
 
 
	print("---"*20)
	print(filters)
 
	columns = columns = [{
		"fieldname": "model",
		"label": "model",
		"fieldtype": "Data"
	},{
		"fieldname": "total",
		"label": "Total",
		"fieldtype": "Currency",
		"options": "TZS"
		}  ,   
    ]
	
 
	data = frappe.get_all(
    "Ride Booking", 
    fields=["SUM(total) AS total","vehicle.model"],
    filters={"docstatus":1}, group_by="model"
    )
 
 
	chart = {
		"data": {
			"labels": [x.model for x in data],
			"datasets":[
				{
					"values": [x.total for x in data]
				}
			],
		},
		"type": "pie",
	}

	return columns, data, "Message summary", chart


