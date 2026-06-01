# from . import models

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     def action_create_invoice_custom(self):
#         customer = self.partner_id
#         product = self.env['product.product'].search([], limit=1)

#         invoice = self.env['account.move'].create({
#             'move_type': 'out_invoice',
#             'partner_id': customer.id,
#             'invoice_line_ids': [(0, 0, {
#                 'product_id': product.id,
#                 'quantity': 1,
#                 'price_unit': 100,
#             })]
#         })

#         return {
#             'type': 'ir.actions.act_window',
#             'name': 'Invoice',
#             'res_model': 'account.move',
#             'view_mode': 'form',
#             'res_id': invoice.id,
#         }




# from . import models

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'