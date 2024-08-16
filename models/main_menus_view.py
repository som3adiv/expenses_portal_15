from odoo import http
from odoo.http import request
from datetime import date

class MenuController(http.Controller):
    @http.route('/home', type="http", auth='public', website=True)
    def home_menu_submit(self, **kwargs):
        # Fetch the user object
        user = request.env.user
        user_name = user.name  # Retrieve the user's name
        user_email = user.email  # Retrieve the user's email
        user_image = user.image_1920  # Retrieve the user's image

        # Initialize the total amount variables
        food_total = 0
        shopping_total = 0
        housing_total = 0
        transportation_total = 0
        vehicle_total = 0
        grocery_total = 0
        entertainment_total = 0

        # Get today's date
        today_date = date.today()

        # Fetch all expense records
        get_expenses_details = request.env["hr.expense"].sudo().search([])

        # Calculate total amount for expenses related to the current user for today
        for expense in get_expenses_details:
            # if expense.date == today_date:
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

        # Pass data to the template
        return request.render('expenses_portal_15.home_menu_page', {
            'user_name': user_name,
            'user_email': user_email,
            'user_image': user_image,
            'food_total': food_total,
            'shopping_total': shopping_total,
            'housing_total': housing_total,
            'transportation_total': transportation_total,
            'vehicle_total': vehicle_total,
            'grocery_total': grocery_total,
            'entertainment_total': entertainment_total,
            'today_date': today_date
        })
