from io import BytesIO

from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from badge_generator import settings

import qrcode
from weasyprint import HTML, CSS

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
    
    
def download_pdf(data, request):
    response = render_to_pdf(data, request)
    filename = data["employee_name"]
    response['Content-Disposition'] = 'attachment; filename={}.pdf'.format(filename)
    return response

def render_to_pdf(data, request):
    template = get_template('badge.html')
    html = template.render(data)
    pdf_file = HTML(string=html,  base_url=request.build_absolute_uri()).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    return response


