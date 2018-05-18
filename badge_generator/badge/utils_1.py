from io import BytesIO

from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render

import qrcode
from xhtml2pdf import pisa

import pdfkit
import os

from .models import Employee


def generate_qr_code(self, Employee):

    #create qr code instance
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4,
    )

    #Add data to store
    qr.add_data(Employee.name)
    qr.add_data(Employee.id_no)
    qr.add_data(Employee.position)

    #create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    return img


def render_to_pdf(template_name, data):
    template = get_template(template_name)
    html = template.render(data)

    result = BytesIO()
    pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    response = HttpResponse(result.getvalue(), content_type='application/pdf')

    return response
        
    
def download_pdf(template_name, data):
    response = render_to_pdf(template_name, data)
    filename = data["employee_name"]
    response['Content-Disposition'] = 'attachment; filename={}.pdf'.format(filename)
    return response
'''   
def convert_hmtl_to_pdf():
    #context = Context({"data": "data"})

    context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }

    options = {
        'quiet': ''
    }
    
    #template = get_template(template_name)
    template = get_template('badge_back.html')

    #render template with the context data
    html = template.render(context)
    pdfkit.from_string(html, 'out.pdf', options=options)
    
    file = open('out.pdf')

    #generate response as pdf response
    response = HttpResponse(file.read(), content_type='application/pdf')

    filename = "y"

    response['Content-Disposition'] = 'attachment; filename={}.pdf'.format(filename)

    file.close()

    os.remove('out.pdf')

    return response
    '''
