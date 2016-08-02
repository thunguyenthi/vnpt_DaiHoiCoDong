from openerp import models, fields, api
from openerp import re
 class demovppt(models.Model):
     _name = 'demovppt.demovppt'

     name = fields.Char(string = 'Tên')
     ma_co_dong = fields.Char(string='Mã Cổ Đông')
     email = fields.Char(string = 'Email')
     phone = fields.Char(string  = 'SDT')
     dia_chi = fields.Char(string='Địa Chỉ')
     gender = fields.selection([('m' ,'Nam') ,('f','Nữ')], string = "Gender")
     is_active = fields.Boolean(string = 'Active')
     birth_date = fields.Date(string = "Birth Date")
     so_co_dong = fields.Integer('Số cổ đông')
     
     @api.one
     @api.constrains('email')
     def check_email(self):
          EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
          if len(self.email) > 7:
             if re.match(EMAIL_REGEX, emailkey) is not None:
                return False
             return True
          else:
             return True

    _sql_constraints = [
        ('unique_emial', 'unique (email)', _('The email is exist you not use this email !')),
    ]

          