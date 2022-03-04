from odoo import fields, models, api
from datetime import datetime, date


class ScheduleLearn(models.Model):
    _name = 'schedule.learn'
    _description = 'Lịch trình học'

    name = fields.Char('Tên', required=True)
    code_schedule = fields.Char('Mã', required=True)
    date_learn = fields.Date('Ngày', required=True)
    repeat_weekday = fields.Selection([
        ('mon', 'Thứ 2'),
        ('tue', 'Thứ 3'),
        ('wed', 'Thứ 4'),
        ('thu', 'Thứ 5'),
        ('fri', 'Thứ 6'),
        ('sat', 'Thứ 7'),
        ('sun', 'Chủ nhật'),
    ], string='Ngày trong tuần', readonly=False)
    lesson = fields.Selection([
        ('mor', 'Buổi sáng'),
        ('after', 'Buổi chiều'),
        ('night', 'Buổi tối'),
    ], 'Ca học', required=True)
    classroom_id = fields.Many2one('classroom', 'Phòng học')
    #Giảng viên Lecturers
    employee_id = fields.Many2one('hr.employee', 'Giảng viên')
    #trợ giảng
    tutor_ids = fields.Many2many('hr.employee', string='Trợ giảng')
    manage_class_id = fields.Many2one('manage.class', string='Quản lý lớp')

    def onchange_date(self):
            r = self.env['schedule.learn'].search([('date_learn', '=', self.date_learn)])
            print(r)
            return True
        #     if a:
        #         b = datetime.strftime(a, '%A')
        #         res = {'hari': b}
        #     return {'value': res}
        # return True
