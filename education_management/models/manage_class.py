from odoo import fields, models, api


class ManageClass(models.Model):
    _name = 'manage.class'
    _description = 'Quản lý lớp học'

    #Thông tin lịch học
    name = fields.Char('Tên lớp')
    code_class = fields.Char("Mã")
    subjects_id = fields.Many2one('subjects.management', 'Môn học')
    number_lessons = fields.Integer(related='subjects_id.number_lessons', string='Số buổi học')
    opening_day = fields.Date('Ngày khai gảng')
    end_date = fields.Date('Ngày kết thúc')
    lesson = fields.Selection([
        ('mor', 'Buổi sáng'),
        ('after', 'Buổi chiều'),
        ('night', 'Buổi tối'),
    ], 'Ca học', required=True)
    repeat_weekday = fields.Selection([
        ('mon', 'Thứ 2'),
        ('tue', 'Thứ 3'),
        ('wed', 'Thứ 4'),
        ('thu', 'Thứ 5'),
        ('fri', 'Thứ 6'),
        ('sat', 'Thứ 7'),
        ('sun', 'Chủ nhật'),
    ], string='Thứ trong tuần', readonly=False)

    #Thông tin lớp học
    location_id = fields.Many2one('location.included', 'Địa điểm')
    classroom_id = fields.Many2one('classroom', 'Phòng học')
    employee_id = fields.Many2one('hr.employee', 'Giảng viên')
    tutor_id = fields.Many2one('hr.employee', 'Trợ giảng')
    note = fields.Text('Ghi chú')

    state = fields.Selection([
        ('s1', 'Dự thảo'),
        ('s2', 'Chuẩn bị khai giảng'),
        ('s3', 'Đang học'),
        ('s4', 'Đã tốt nghiệp'),
        ('s5', 'Hủy'),
    ], string='Trạng thái lớp', default='s1')
    #Thông tin lịch học
    schedule_learn_ids = fields.One2many('schedule.learn', 'manage_class_id')
    #Thông tin học viên
    student_list_ids = fields.Many2many('res.partner')

