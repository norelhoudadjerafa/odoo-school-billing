from odoo import api, fields, models
from odoo.exceptions import ValidationError


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
    # 2. Contraintes SQL
    _name_unique = models.Constraint(
    "UNIQUE(name)",
    "The academic year must be unique.",
    )

    # 3. Contraintes métier Python
    @api.constrains("date_start", "date_end")
    def _check_dates(self):
        for record in self:
            if record.date_start and record.date_end:
                if record.date_end < record.date_start:
                    raise ValidationError(
                        "The end date must be after the start date."
                    )