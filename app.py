from flask import Flask
from view import *

app = Flask(__name__)

app.add_url_rule('/', view_func=start_page)
app.add_url_rule('/about', view_func=about)

app.add_url_rule('/cart', view_func=cart)
app.add_url_rule('/cart/order', view_func=cart_order)
app.add_url_rule('/cart/add', view_func=cart_add)

app.add_url_rule('/user', view_func=user)
app.add_url_rule('/user/register', view_func=user_register)
app.add_url_rule('/user/sign_in', view_func=user_sign_in)
app.add_url_rule('/user/logout', view_func=user_logout)
app.add_url_rule('/user/restore', view_func=user_restore)
app.add_url_rule('/user/history', view_func=user_orders_history)
app.add_url_rule('/user/history/<order_id>', view_func=user_order)
app.add_url_rule('/user/addresses', view_func=user_address_list)
app.add_url_rule('/user/addresses/<address_id>', view_func=user_address)

app.add_url_rule('/menu', view_func=menu)
app.add_url_rule('/menu/categories', view_func=categories)
app.add_url_rule('/menu/categories/<cat_id>', view_func=category_dishes)
app.add_url_rule('/menu/categories/<cat_id>/<dish_id>', view_func=dish)
app.add_url_rule('/menu/categories/<cat_id>?order_by=ccal/price/rate/name', view_func=category_sort)
app.add_url_rule('/menu/all_dishes', view_func=dishes)


app.add_url_rule('/menu/search', view_func=search)
app.add_url_rule('/menu/all_dishes?order_by_var=ccal/price/rate/dish_name&order=ASC/DESC', view_func=dish_sort)

app.add_url_rule('/admin/dishes', view_func=admin_dishes)
app.add_url_rule('/admin/dishes/<dish_id>', view_func=admin_dish)
app.add_url_rule('/admin/orders', view_func=admin_orders)
app.add_url_rule('/admin/orders/<order_id>', view_func=admin_order)
app.add_url_rule('/admin/orders?status={new/in_progress}', view_func=admin_sort_order_status)
app.add_url_rule('/admin/orders/<id>/status', view_func=admin_set_order_status)
app.add_url_rule('/admin/categories', view_func=admin_show_categories)
app.add_url_rule('/admin/categories/<cat_id>', view_func=admin_category_edit)
app.add_url_rule('/admin/search', view_func=admin_search)

if __name__ == '__main__':
    app.run(debug=True)
