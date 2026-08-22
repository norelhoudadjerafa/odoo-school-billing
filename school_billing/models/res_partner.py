from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_student = fields.Boolean(
        string="Student",
        default=False,
    )

    is_parent = fields.Boolean(
        string="Parent",
        default=False,
    )

    billing_parent_id = fields.Many2one(
        comodel_name="res.partner",
        string="Billing Parent",
        domain=[("is_parent", "=", True)],
        ondelete="set null",
    )