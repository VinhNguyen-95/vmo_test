from odoo import fields, models, api


class Classroom(models.Model):
    # Todo tên model nên đặt có 2 từ trở lên vd: xxx.yyy
    _name = 'classroom'
    _description = 'Phòng học'

    name = fields.Char('Tên phòng', required=True)
    location_id = fields.Many2one('location.included', 'Địa điểm')
    #lịch học
    schedule_learn_ids = fields.One2many('schedule.learn', 'classroom_id')
    manage_class_ids = fields.One2many('manage.class', 'classroom_id')

