from flask import Blueprint, render_template, request, redirect, url_for, flash
from jade_ims.models import db, Stock, Product, Supplier

stock = Blueprint('stock', __name__)


@stock.route('/stock')
def list_stock():
    product_data = Product.query.all()
    data = []
    for i in product_data:
        data.append(
            {
                "ID": i.ID,
                "Name": i.Name,
                "Price": i.Price,
                "Supplier_Name": Supplier.query.get(i.Supplier_ID).Name,
                "Quantity": Stock.query.get(i.ID).Quantity,
                "Remark": i.Remark
            }
        )
    return render_template('stock/stock.html',
                           title="库存信息",
                           data=data)


@stock.route('/stock/add', methods=['POST'])
def add_product():
    form = request.form
    print(form)
    if request.method == 'POST':
        product = Product(
            form['product_name'],
            float(form['product_price']),
            int(form['product_supplier']),
            form['product_remark']
        )
        try:
            db.session.add(product)
            db.session.commit()
            flash('商品添加成功!', 'success')
        except:
            db.session.rollback()
            flash('输入不合法,请重新输入!', 'danger')
        stock = Stock(
            Product.query.filter_by(Name=form['product_name']).first().ID,
            0,
            ''
        )
        db.session.add(stock)
        db.session.commit()
    return redirect(url_for('stock.list_stock'))


@stock.route('/stock/del')
def del_route():
    pass
