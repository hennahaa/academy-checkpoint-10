def kissaweb_subscription(request):

    request_json = request.get_json()
    
    if request.args and 'nimi' in request.args:
        name = int(request.args.get('nimi'))
    elif request_json and 'length' in request_json:
        name = int(request_json['nimi'])
    else:
         name = "Juukeli"

    return f"Thank you for subscribing to cat facts, {name}!"