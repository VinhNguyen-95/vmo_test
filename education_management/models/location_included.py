from odoo import fields, models, api


class LocationIncluded(models.Model):
    _name = 'location.included'
    _description = 'Địa điểm'

    name = fields.Char('Tên địa điểm', required=True)
    code_location = fields.Char('Mã địa điểm', required=True)
    classroom_ids = fields.One2many('classroom', 'location_id')
    manage_class_ids = fields.One2many('manage.class', 'location_id')




