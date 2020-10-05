from celery import task
import weasyprint
from io import BytesIO
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order


@task
def payment_completed(order_id):
    """ task to send email to customer once
    order successfully created"""

    order = Order.objects.get(id=order_id)

    # lets create the invoice email
    subject = f'TRAPSOUL - GL Invoice no. {order_id}'
    message = 'Plese, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject, message, 'admin@online.com', [order.email])

    # lets generate the PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    # attach the PDF file
    email.attach(f'order_{order.id}.pdf',
                 out.getvalue(),
                 'application/pdf')

    # send email
    email.send()
