import logging
import re

from odoo import api, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)
regx = "^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4,8}$"


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.onchange('phone')
    def on_change_phone(self):
        if self.phone != '' and self.phone:
            phone = self.phone
            if bool(re.search(regx, phone)):
                phone = phone.replace("(", "")
                phone = phone.replace(")", "")
                phone = phone.replace(" ", "")
                phone = phone.replace("-", "")
                phone = phone.replace("+", "")
                if not phone[1:].isdigit():
                    raise ValidationError('Phone Number is wrongly formatted!!!')
                else:
                    if len(phone) == 10:
                        self.phone = f'+1{phone}'
                    else:
                        self.phone = f'+52{phone}'

            else:
                raise ValidationError('Phone Number is wrongly formatted!!!')

    @api.onchange('mobile')
    def on_change_mobile(self):

        if self.mobile != '' and self.mobile:
            phone = self.mobile
            if bool(re.search(regx, phone)):
                phone = phone.replace("(", "")
                phone = phone.replace(")", "")
                phone = phone.replace(" ", "")
                phone = phone.replace("-", "")
                if not phone[1:].isdigit():
                    raise ValidationError('Phone Number is wrongly formatted!!!')
                else:
                    if len(phone) == 10:
                        self.mobile = f'+1{phone}'
                    else:
                        self.mobile = f'+52{phone}'

            else:
                raise ValidationError('Phone Number is wrongly formatted!!!')

    @api.model
    def create(self, vals_list):
        if 'phone' in vals_list:
            if vals_list['phone'] != '' and vals_list['phone']:
                phone = vals_list['phone']
                if bool(re.search(regx, phone)):
                    phone = phone.replace("(", "")
                    phone = phone.replace(")", "")
                    phone = phone.replace(" ", "")
                    phone = phone.replace("-", "")
                    if not phone[1:].isdigit():
                        raise ValidationError('Phone Number is wrongly formatted!!!')
                    else:
                        if len(phone) == 10:
                            self.phone = f'+1{phone}'
                        else:
                            self.phone = f'+52{phone}'

                else:
                    raise ValidationError('Phone Number is wrongly formatted!!!')
        if 'mobile' in vals_list:
            if vals_list['mobile'] != '' and vals_list['mobile']:
                phone = vals_list['mobile']
                if bool(re.search(regx, phone)):
                    phone = phone.replace("(", "")
                    phone = phone.replace(")", "")
                    phone = phone.replace(" ", "")
                    phone = phone.replace("-", "")
                    if not phone[1:].isdigit():
                        raise ValidationError('Phone Number is wrongly formatted!!!')
                    else:
                        if len(phone) == 10:
                            self.mobile = f'+1{phone}'
                        else:
                            self.mobile = f'+52{phone}'

                else:
                    raise ValidationError('Phone Number is wrongly formatted!!!')
        return super(ResPartner, self).create(vals_list)

    # def write(self, vals_list):
    #     if 'phone' in vals_list:
    #         if vals_list['phone'] != '' and vals_list['phone']:
    #             phone = vals_list['phone']
    #             if bool(re.search(regx, phone)):
    #                 phone = phone.replace("(", "")
    #                 phone = phone.replace(")", "")
    #                 phone = phone.replace(" ", "")
    #                 phone = phone.replace("-", "")
    #                 if not phone[1:].isdigit():
    #                     raise ValidationError('Phone Number is wrongly formatted!!!')
    #                 else:
    #                     self.phone = phone
    #             else:
    #                 raise ValidationError('Phone Number is wrongly formatted!!!')
    #     if 'mobile' in vals_list:
    #         if vals_list['mobile'] != '' and vals_list['mobile']:
    #             phone = vals_list['mobile']
    #             if bool(re.search(regx, phone)):
    #                 phone = phone.replace("(", "")
    #                 phone = phone.replace(")", "")
    #                 phone = phone.replace(" ", "")
    #                 phone = phone.replace("-", "")
    #                 if not phone[1:].isdigit():
    #                     raise ValidationError('Phone Number is wrongly formatted!!!')
    #                 else:
    #                     self.mobile = phone if phone[0] == '+' else f'+{phone}'
    #             else:
    #                 raise ValidationError('Phone Number is wrongly formatted!!!')
    #     return super(ResPartner, self).write(vals_list)
