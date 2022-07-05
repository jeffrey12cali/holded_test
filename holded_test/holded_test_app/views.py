from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests
import json

from xlsxwriter.workbook import Workbook

# Create your views here.

def test_view(request):
    url = 'https://api.holded.com/api/invoicing/v1/documents/salesorder'
    headers = {'key': settings.HOLDED_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:         # SUCCESS
        result = response.json()

        # Declaring response
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = "attachment; filename=salesorders.xlsx"

        # Writing data to xlsx file
        book = Workbook(response, {'in_memory': True})
        sheet = book.add_worksheet('salesorders')       
        sheet.write(0, 0, 'DeliveryID')
        sheet.write(0, 1, 'Adress/Code')
        sheet.write(0, 2, 'Adress/Name')
        sheet.write(0, 3, 'LineNumber')
        sheet.write(0, 4, 'Sku')
        sheet.write(0, 5, 'ExpectedQuantity')

        line = 1
        for i in range(len(result)):
            
            # Get client data
            client_id = result[i]['contact']
            url = 'https://api.holded.com/api/invoicing/v1/contacts/' + client_id
            contact_response = requests.get(url, headers=headers)
            client_code = ''
            if contact_response.status_code == 200:
                contact_data = contact_response.json()
                if len(contact_data['customFields']) > 0:
                    for field_obj in contact_data['customFields']:
                        if field_obj['field'] == 'Código Cliente':
                            client_code = field_obj['value']

            # Write a in a line for each product in the ordersale of this client
            for j in range(len(result[i]['products'])):
                sheet.write(line, 0, result[i]['docNumber'])
                sheet.write(line, 1, client_code)
                sheet.write(line, 2, result[i]['contactName'])
                sheet.write(line, 3, j+1)
                sheet.write(line, 4, result[i]['products'][j]['name'])
                sheet.write(line, 5, result[i]['products'][j]['units'])
                line += 1

        book.close()

        response['message'] = 'Data succesfully retrieved'
    else:
        if response.status_code == 404:     # NOT FOUND
            response['message'] = "URL does not exist"
        else:                               # OTHER ERRORS
            response['message'] = "An error was produced"
    return response
    #return HttpResponse(result[1]['products'])