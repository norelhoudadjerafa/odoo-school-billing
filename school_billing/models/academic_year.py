from odoo import fields, models


class SchoolAcademicYear(models.Model):
    _name = "school.academic.year"
    _description = "Academic Year"

    name = fields.Char(
        string="Academic Year",
        required=True,
    )

    date_start = fields.Date(
        string="Start Date",
        required=True,
    )

    date_end = fields.Date(
        string="End Date",
        required=True,
    )

    active = fields.Boolean(
        string="Active",
        default=True,
    )