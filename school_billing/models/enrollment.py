from odoo import api, fields, models


class SchoolEnrollment(models.Model):
    _name = "school.enrollment"
    _description = "School Enrollment"

    student_id = fields.Many2one(
        comodel_name="res.partner",
        string="Student",
        required=True,
        domain=[("is_student", "=", True)],
    )

    academic_year_id = fields.Many2one(
        comodel_name="school.academic.year",
        string="Academic Year",
        required=True,
    )

    class_id = fields.Many2one(
    comodel_name="school.class",
    string="Class",
    required=True,
    )

    registration_date = fields.Date(
        string="Registration Date",
        default=fields.Date.context_today,
        required=True,
    )

    registration_fee = fields.Monetary(
        string="Registration Fee",
    )

    standard_monthly_fee = fields.Monetary(
        string="Standard Monthly Fee",
    )

    student_monthly_fee = fields.Monetary(
        string="Student Monthly Fee",
    )

    currency_id = fields.Many2one(
        comodel_name="res.currency",
        string="Currency",
        required=True,
        default=lambda self: self.env.company.currency_id,
    )

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("cancelled", "Cancelled"),
        ],
        string="Status",
        default="draft",
        required=True,
    )
    @api.onchange("class_id")
    def _onchange_class_id(self):
        if self.class_id:
            self.registration_fee = self.class_id.registration_fee
            self.standard_monthly_fee = self.class_id.standard_monthly_fee
            self.student_monthly_fee = self.class_id.standard_monthly_fee
        else:
            self.registration_fee = 0.0
            self.standard_monthly_fee = 0.0
            self.student_monthly_fee = 0.0