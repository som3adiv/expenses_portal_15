from odoo import http , fields
from odoo.http import request
from datetime import date
from odoo.exceptions import UserError, ValidationError
import logging

# Initialize logger
_logger = logging.getLogger(__name__)
date_to_view = fields.Date()
class MenuController(http.Controller):
    @http.route('/home', type="http", auth='public', website=True)
    def home_menu_submit(self, **kwargs):
        selected_date = kwargs.get('selected_date')
        _logger.info(f"Selected Date: {selected_date}")
        
        user_id = int(kwargs.get('user_id', request.env.user.id))
        user = request.env['res.users'].browse(user_id)
        _logger.info(f"User ID: {user_id}, User Name: {user.name}")

        # Initialize totals
        food_total = 0
        shopping_total = 0
        housing_total = 0
        transportation_total = 0
        vehicle_total = 0
        grocery_total = 0
        entertainment_total = 0

        # Check if a date is selected
        if selected_date:
            date_to_view = selected_date
            selected_date = date.fromisoformat(selected_date)
            _logger.info(f"Filtered Date: {selected_date}")
            expenses = request.env["hr.expense"].sudo().search([('date', '=', selected_date)])
        else:
            expenses = request.env["hr.expense"].sudo().search([])

        for expense in expenses:
            if expense.product_id.name == 'Food and Drinks':
                food_total += expense.total_amount_company
            elif expense.product_id.name == 'Shopping':
                shopping_total += expense.total_amount_company
            elif expense.product_id.name == 'Housing':
                housing_total += expense.total_amount_company
            elif expense.product_id.name == 'Transportation':
                transportation_total += expense.total_amount_company
            elif expense.product_id.name == 'Vehicle':
                vehicle_total += expense.total_amount_company
            elif expense.product_id.name == 'Grocery':
                grocery_total += expense.total_amount_company
            elif expense.product_id.name == 'Entertainment':
                entertainment_total += expense.total_amount_company

        _logger.info(f"Food Total: {food_total}, Shopping Total: {shopping_total}")

        return request.render('expenses_portal_15.home_menu_page', {
            'user_name': user.name,
            'user_email': user.email,
            'user_image': user.image_1920,
            'food_total': food_total,
            'shopping_total': shopping_total,
            'housing_total': housing_total,
            'transportation_total': transportation_total,
            'vehicle_total': vehicle_total,
            'grocery_total': grocery_total,
            'entertainment_total': entertainment_total,
            'today_date': date.today(),
            'image': user.image_1920,
            'date_to_view':date_to_view
        })
