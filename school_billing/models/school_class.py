from odoo import fields, models


class SchoolClass(models.Model):
    _name = "school.class"
    _description = "School Class"
    _order = "name"

    name = fields.Char(
        string="Class",
        required=True,
    )

    academic_year_id = fields.Many2one(
        comodel_name="school.academic.year",
        string="Academic Year",
        required=True,
    )

    standard_monthly_fee = fields.Monetary(
        string="Standard Monthly Fee",
    )

    registration_fee = fields.Monetary(
        string="Registration Fee",
    )

    currency_id = fields.Many2one(
        comodel_name="res.currency",
        string="Currency",
        required=True,
        default=lambda self: self.env.company.currency_id,
    )

    active = fields.Boolean(
        string="Active",
        default=True,
    )