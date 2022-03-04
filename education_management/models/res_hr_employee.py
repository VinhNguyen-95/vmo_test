from odoo import fields, models, api


class Employee(models.Model):
    _inherit = 'hr.employee'
    _description = 'custom bảng hr employee'

    worked_time = fields.Char('Thâm niên')
    code = fields.Char('Mã nhân viên')
    job_position = fields.Char('Cấp bậc')
    #work_location
    job_title = fields.Char('Chức danh công việc')
    leave_manager_id = fields.Char('Time Off Approver')

    # form
    join_date = fields.Date('Ngày tham gia')
    contract_type = fields.Char('Loại hợp đồng')
    # department_id Bộ phận
    # parent_id  Người quản lý
    # job_id vị trí làm việc
    # birthday = fields ngày sinh
    home_town = fields.Char('Quê quán')
    # place_of_birth nơi sinh
    household = fields.Char('Hộ khẩu thường trú')
    staying = fields.Char('Tạm trú')
    marital_status = fields.Char('Tình trạng hôn nhân')
    study_university = fields.Char('Trường đào tạo')
    x_study_field = fields.Char('Chuyên ngành')
    certificate_level = fields.Selection([
        ('1', 'Chưa tốt nghiệp'), ('2', 'Không'), ('3', 'Cử nhân'),
        ('4', 'Thạc sỹ'), ('5', 'Trung cấp'), ('6', 'Cao đẳng'),
        ('7', 'Đại học'), ('8', 'Sinh viên'), ('9', 'Cao học'),
    ])
    graduation_year = fields.Date('Năm tốt nghiệp')
    other_certificate = fields.Char('Chứng chỉ khác')
    # identification_id = fields.Integer('ID(CMTND/CCCD)')
    id_date = fields.Date('Ngày cấp')
    id_place = fields.Char('Nơi cấp')
    old_id = fields.Integer('Số ID cũ')
    tex_code = fields.Integer('Mã số thuế')
    bank_name = fields.Char('Tên ngân hàng')
    bank_number = fields.Integer('Số tài khoản ngân hàng')
    bank_branch = fields.Char('Chi nhánh')
    old_companies = fields.Char('Công ty cũ')


