from odoo import fields, models, api


class Subjects(models.Model):
    # Todo tên file python nên đặt theo tên model chính để dễ tìm, TH này nên đặt tên file là subjects_management
    _name = 'subjects.management'
    _description = 'Quản lý môn học'

    name = fields.Char('Tên môn học', required=True)
    code_subjects = fields.Char('Mã môn học', required=True)
    description_subjects = fields.Text('Mô tả môn học')
    number_lessons = fields.Integer('Số buổi môn học', required=True)
    manage_class_ids = fields.One2many('manage.class', 'subjects_id')

